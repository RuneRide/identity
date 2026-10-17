# RuneRide : identité visuelle

Dossier de travail de la marque (hors dépôts applicatifs).

| Fichier / dossier | Contenu |
| :-- | :-- |
| `BRAND.md` | Charte : positionnement, logo, couleurs, typographie, règles UI, liste des fichiers |
| `LORE.md` | Ton de voix, micro-copy FR/EN, règle 80 % utilité / 20 % lore |
| `CODEX.md` | Mythe fondateur, Ordres, Clans, lignées marque × segment, dictionnaire UI (fait foi) |
| `brand-board.html` | Planche d'aperçu, à ouvrir dans un navigateur |
| `tokens/` | `tokens.css` et `tokens.json` (couleurs, polices, tailles) |
| `logo/` | Monogramme, lockups vertical et horizontal, icônes (`icon/`), PNG et `favicon.ico` |
| `patterns/` | Séparateurs runiques et tuiles de courbes de niveau |
| `fonts/` | Inter et JetBrains Mono (variables, OFL) |
| `source/` | Image de référence d'origine et recadrage du monogramme |
| `tools/` | Scripts de génération (voir ci-dessous) |

## Régénérer les fichiers

Dépendances : Python 3 avec `fonttools`, `Pillow` (et `opencv-python`, `numpy` pour `build_patterns.py` et `vectorize_monogram.py`), Google Chrome pour les rendus PNG.

```sh
python3 tools/build_monogram.py logo/monogram.svg
python3 tools/build_lockup.py fonts/Inter-Variable.ttf logo/monogram.svg logo/lockup.svg
python3 tools/build_lockup.py fonts/Inter-Variable.ttf logo/monogram.svg logo/lockup-horizontal.svg --horizontal
python3 tools/build_icon.py logo/icon/icon.svg --full --scale 0.62            # icône complète, coins arrondis
python3 tools/build_icon.py logo/icon/icon-small.svg --scale 0.74 --radius 96 # simplifiée, <= 20 px
python3 tools/build_patterns.py patterns
python3 tools/build_ico.py logo/icon/png logo/icon/favicon.ico
```

Les variantes monochromes sont obtenues en remplaçant les couleurs des SVG (`#EBE8E0` pour fond sombre, `#17191C` pour fond clair). Les PNG sont rendus avec Chrome headless à partir des SVG.

Règle d'icône : logo complet à partir de 32 px, version simplifiée uniquement pour 20 px et moins.
