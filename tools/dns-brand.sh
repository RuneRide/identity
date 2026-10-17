#!/usr/bin/env bash
# SPDX-License-Identifier: EUPL-1.2
#
# Configure le DNS de runeride.fr (cPanel, o2switch) pour brand.runeride.fr sur GitHub Pages,
# et ajoute les TXT de vérification de domaine GitHub.
#
# Le jeton cPanel est lu dans AWS Secrets Manager (runeride/cpanel, eu-north-1) à l'intérieur du script :
# il n'est jamais affiché, ni écrit sur disque, ni passé en argument visible.
#
# Usage :
#   tools/dns-brand.sh                         # simulation : liste les enregistrements existants et le plan
#   tools/dns-brand.sh --apply                 # crée le CNAME brand -> runeride.github.io
#   tools/dns-brand.sh --apply \
#       '_github-pages-challenge-RuneRide=CODE_PAGES' \
#       '_github-challenge-RuneRide-org=CODE_ORG'   # ajoute aussi les TXT (codes donnés par GitHub)
#
# Prérequis : aws (profil avec accès à Secrets Manager), curl, jq.
set -euo pipefail

SECRET_ID="runeride/cpanel"; REGION="eu-north-1"; DOMAIN="runeride.fr"
CNAME_NAME="brand"; CNAME_TARGET="runeride.github.io."

APPLY=0
if [[ "${1:-}" == "--apply" ]]; then APPLY=1; shift; fi
TXT_ARGS=("$@")

secret=$(aws secretsmanager get-secret-value --region "$REGION" --secret-id "$SECRET_ID" --query SecretString --output text)
pick() { jq -r --arg keys "$1" '[ ($keys | split(",")[]) as $k | .[$k]? | select(. != null and . != "") ] | first // empty' <<<"$secret"; }

host=$(pick host,hostname,server,url,cpanel_host)
user=$(pick user,username,login,cpanel_user)
token=$(pick token,api_token,apitoken,key,secret)
host=${host#*://}; host=${host%%/*}; host=${host%%:*}

if [[ -z "$host" || -z "$user" || -z "$token" ]]; then
  echo "Secret inattendu : il faut un hôte, un utilisateur et un jeton. Clés présentes :" >&2
  jq -r 'if type=="object" then keys | join(", ") else "(pas un objet JSON)" end' <<<"$secret" >&2
  exit 1
fi

# ZoneEdit n'existe qu'en API v2 de cPanel : $1 = fonction, puis des paires clé=valeur (encodées par curl)
api2() {
  local fn="$1"; shift
  local args=(--data-urlencode "cpanel_jsonapi_apiversion=2" --data-urlencode "cpanel_jsonapi_module=ZoneEdit" --data-urlencode "cpanel_jsonapi_func=$fn")
  for kv in "$@"; do args+=(--data-urlencode "$kv"); done
  curl -fsS --get -H "Authorization: cpanel ${user}:${token}" "https://${host}:2083/json-api/cpanel" "${args[@]}"
}

# Arrêt net si la réponse n'est pas exploitable (jamais de « liste vide » trompeuse)
require_ok() {
  if ! jq -e '.cpanelresult.data' >/dev/null 2>&1 <<<"$1"; then
    echo "Réponse cPanel inattendue :" >&2
    jq -r '.cpanelresult.error // .error // "(pas de message)"' <<<"$1" 2>/dev/null >&2 || echo "$1" | head -c 300 >&2
    exit 1
  fi
}

zone=$(api2 fetchzone_records "domain=$DOMAIN" "customonly=1")
require_ok "$zone"
echo "== Enregistrements personnalisés existants pour $DOMAIN (brand et vérifications GitHub) =="
jq -r '.cpanelresult.data[]? | select((.name // "") | test("^(brand|_github)")) | [.type, .name, (.cname // .txtdata // .address // "")] | @tsv' <<<"$zone" || true
echo "($(jq '.cpanelresult.data | length' <<<"$zone") enregistrements personnalisés au total)"

# Retourne la valeur d'un enregistrement existant (nom relatif) ou vide
existing() { jq -r --arg n "$1.$DOMAIN." --arg t "$2" '.cpanelresult.data[]? | select(.type==$t and .name==$n) | (.cname // .txtdata // "")' <<<"$zone" | head -1; }

add_record() { # type, nom relatif, valeur
  local type="$1" name="$2" value="$3" cur res
  cur=$(existing "$name" "$type")
  if [[ -n "$cur" ]]; then
    if [[ "$cur" == "$value" || "$cur" == "${value%.}" ]]; then echo "= $type $name : déjà présent, rien à faire"; return; fi
    echo "! $type $name existe déjà avec une autre valeur ($cur) : non modifié" >&2; return
  fi
  echo "+ $type $name -> $value"
  [[ $APPLY -eq 1 ]] || return 0
  if [[ "$type" == "CNAME" ]]; then
    res=$(api2 add_zone_record "domain=$DOMAIN" "name=$name" "type=CNAME" "cname=$value" "ttl=300")
  else
    res=$(api2 add_zone_record "domain=$DOMAIN" "name=$name" "type=TXT" "txtdata=$value" "ttl=300")
  fi
  require_ok "$res"
  jq -r '.cpanelresult.data[0].result | "  statut=\(.status) \(.statusmsg // "")"' <<<"$res"
  [[ "$(jq -r '.cpanelresult.data[0].result.status' <<<"$res")" == "1" ]] || { echo "  échec de l'ajout" >&2; exit 1; }
}

echo "== Plan $( [[ $APPLY -eq 1 ]] && echo '(appliqué)' || echo '(simulation, ajouter --apply pour écrire)' ) =="
add_record CNAME "$CNAME_NAME" "$CNAME_TARGET"
for kv in "${TXT_ARGS[@]}"; do add_record TXT "${kv%%=*}" "${kv#*=}"; done

if [[ $APPLY -eq 1 ]]; then
  echo "== Vérification DNS (la propagation peut prendre quelques minutes) =="
  dig +short CNAME "$CNAME_NAME.$DOMAIN" || true
  cat <<'EOF'
Ensuite, quand le CNAME répond (runeride.github.io.) :
  gh api -X PUT repos/RuneRide/identity/pages -F https_enforced=true
Puis, dans GitHub : Settings de l'organisation > Verified and approved domains > Add a domain (runeride.fr),
et Settings > Pages > Add a domain, avec les codes TXT ci-dessus.
EOF
fi
