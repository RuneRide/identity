# RuneRide — Identité visuelle

Source de référence : `source/logo-reference.jpeg` (généré, à vectoriser). Recadrage du monogramme : `source/monogram-crop.png`.

## 1. Positionnement
- **Nom :** RuneRide (anciennement NomadRide / Bike360)
- **Domaine :** assistant road-trip moto tout-en-un, caméra 360° (télémétrie/montage), tracking de route, optimisation du prix du carburant, communauté de riders.
- **Philosophie visuelle :** « Nordic Craft & Modern Telemetry » — les runes gravées pour guider les voyageurs, rencontrent la moto d'aventure moderne (traces GPS, cols, asphalte et pistes).
- **À éviter :**
  - Imagerie viking cliché (cornes, boucliers, polices médiévales).
  - Codes racing/motocross (orange néon type KTM, flammes, damier).
  - Dégradés dorés/métalliques « luxe ». Couleurs plates, mates, ancrées.

## 2. Logo et monogramme
- **Symbole :** monogramme géométrique minimal combinant la rune **Raidho (ᚱ)** (voyage, chevauchée, mouvement) et un double **R** entrelacé (`Rune` + `Ride`).
- **Construction :** deux rubans parallèles de largeur de trait uniforme (`stroke-width: 10.5px` dans le SVG de base) :
  - **Ruban gauche/intérieur (Chalk White) :** fût vertical de la rune/R.
  - **Ruban droit/extérieur (Sand Ochre) :** enveloppe la boucle haute puis descend dans la jambe basse, comme une route de montagne, une épingle ou une trace GPS à double voie.
- **Wordmark :** `RuneRide` en sans-serif géométrique (`Inter` ou `Plus Jakarta Sans`, weight 600, tracking `-1px`), `Rune` en Chalk, `Ride` en Ochre.

## 3. Couleurs (dark-first)
Dark-mode d'abord : contraste, économie OLED, lisibilité sans reflet sur guidon en plein soleil.

| Rôle | Token | Hex | Usage |
| :-- | :-- | :-- | :-- |
| Fond principal | `obsidian-950` | `#17191C` | Fond app, splash, carte sombre |
| Surface | `obsidian-900` | `#212429` | Cartes, bottom sheets, barres, modales |
| Bordure | `obsidian-800` | `#2E323B` | Bordures 1px, séparateurs, états inactifs |
| Texte principal / marque 1 | `chalk-100` | `#EBE8E0` | Typo principale, « Rune », icônes |
| Texte secondaire | `chalk-400` | `#9BA1AB` | Sous-titres, métadonnées, unités |
| Accent / marque 2 | `ochre-500` | `#C6934B` | CTA, tracé GPS actif, « Ride », highlights |
| Accent pressé | `ochre-600` | `#A87938` | États pressés, badges secondaires |
| Succès | `trail-green` | `#10B981` | Station dispo, ride terminé, membre actif |
| Alerte | `amber-warn` | `#F59E0B` | Carburant bas, météo |
| Danger | `crimson-alert` | `#EF4444` | SOS/crash, col fermé, enregistrement |

Tokens exportables : `tokens/tokens.css`, `tokens/tokens.json`.

## 4. Typographie et icônes
- **UI :** `Inter` ou `Plus Jakarta Sans` (x-height élevée, lisible d'un coup d'œil).
- **Télémétrie :** `JetBrains Mono` ou `Space Mono` avec `tabular-nums` (vitesse, distance, angle d'inclinaison, prix, chronos) pour éviter le jitter des chiffres.
- **Icônes :** `Lucide` ou `Phosphor`, `strokeWidth={2}`, géométrie constante comme le monogramme.

## 5. Règles UI/UX
1. **Cibles tactiles gantées :** 48×48dp minimum, 56dp de haut pour les boutons primaires.
2. **Surfaces plates et mates :** pas d'ombres lourdes ni de glassmorphism ; fond `#212429`, bordure `1px #2E323B` ou ochre `#C6934B` si actif.
3. **Télémétrie à fort contraste :** `chalk-100` pour les grandes valeurs, `ochre-500` pour les indicateurs clés (waypoint actif, meilleur prix).

## 6. Écarts constatés sur l'image de référence
- Le monogramme est en **contour (outline)** à lignes multiples, plus complexe que les « deux rubans pleins » du brief : à trancher avant vectorisation.
- Ochre de l'image (~orange cuivré) légèrement plus saturé que `#C6934B` : se caler sur le token.
- Lisibilité à petite taille (favicon, 48px) à valider : les lignes fines fusionneront.

## 7. Fichiers logo
- `logo/monogram.svg` : monogramme bicolore, construit géométriquement (`tools/build_monogram.py`), viewBox 481×598, traits de 22 unités, superposable à `source/monogram-crop.png`.
- `logo/monogram-mono-chalk.svg` (fond sombre), `logo/monogram-mono-dark.svg` (fond clair).
- `logo/monogram-preview.png` : planche de rendu (grand format, 64/32/16 px, monochrome).
- Constat : sous ~32 px les lignes parallèles fusionnent, une version simplifiée (favicon / icône d'app) reste à dessiner.
- `logo/lockup.svg` : lockup vertical monogramme + `RuneRide` (Inter 600 variable, opsz 32, tracking −0,02 em, texte converti en chemins : aucune police requise). Variantes `lockup-mono-chalk.svg` / `lockup-mono-dark.svg`, aperçu `lockup-on-dark.png`. Généré par `tools/build_lockup.py` avec `fonts/Inter-Variable.ttf` (licence SIL OFL).
- `logo/icon/` (généré par `tools/build_icon.py`) : **monogramme complet** pour les grandes tailles, **version simplifiée** (traits épais, un seul ruban ochre) uniquement pour les plus petites. `icon.svg` (coins arrondis, icône d'app), `icon-square.svg` (plein cadre, pour les stores qui appliquent leur masque), `icon-tight.svg` (monogramme complet agrandi, 32 à 64 px), `icon-small.svg` (simplifiée, ≤ 20 px). PNG dans `logo/icon/png/` : `favicon-16` (simplifiée), `favicon-32/48/64` et `icon-180/192/512` (logo complet, coins arrondis transparents), `icon-square-512` et `icon-square-120` (carrés, fond opaque, sans arrondi : pour les services qui appliquent leur propre masque ou n'acceptent pas la transparence, par exemple l'écran de consentement OAuth de Google).
- `brand-board.html` : planche d'aperçu (logo, icône, palette lue depuis `tokens/tokens.css`, typographie, composants, micro-copy). S'ouvre directement dans un navigateur ; polices locales dans `fonts/` (Inter, JetBrains Mono, licence SIL OFL).
- `patterns/` (généré par `tools/build_patterns.py`) :
  - `runic-divider.svg`, `runic-divider-ornate.svg` : séparateur `───◇───` (ligne `obsidian-800`, losange ochre).
  - `topo-tile.svg` : courbes de niveau en tuile 600×600 **sans couture**, pour fonds de cartes (`background: url(...) 0 0 / 400px`) ; `topo-tile-ochre.svg` : variante ochre à 18 % d'opacité pour fond `obsidian-950`.
- `logo/lockup-horizontal.svg` (+ `-mono-chalk`, `-mono-dark`, aperçu `lockup-horizontal-on-dark.png`) : monogramme à gauche, wordmark à droite, centré verticalement (`build_lockup.py … --horizontal`). À privilégier pour les en-têtes et la barre d'app.
- `logo/icon/favicon.ico` : 16 px simplifié + 32/48 px logo complet (`tools/build_ico.py`).
- Documents de marque : `LORE.md` (ton, micro-copy, règle 80/20) et `CODEX.md` (mythe, Ordres, Clans, lignées marque × segment, dictionnaire UI qui fait foi, gamification).
