# Licences, copyright et usage de l'IA

## Copyright

© 2026 Philippe Vienne et contributeurs de RuneRide.

## Licences

Ce dépôt applique deux licences, selon la nature des fichiers (textes complets dans `LICENSES/`) :

| Licence | Périmètre |
| :-- | :-- |
| **EUPL-1.2** (`SPDX : EUPL-1.2`) | Le **code** : `tools/` (scripts de génération), `tokens/` (CSS et JSON), `brand-board.html` |
| **CC BY-SA 4.0** (`SPDX : CC-BY-SA-4.0`) | **Tout le reste** : logos, icônes, motifs, images, textes (`BRAND.md`, `LORE.md`, `CODEX.md`, `README.md`), dossier `github/` |
| **SIL OFL 1.1** (licence d'origine) | Polices tierces de `fonts/` (Inter, JetBrains Mono), non relicenciées, voir `fonts/README.md` |

Les fichiers générés par les scripts (SVG, PNG, `.ico`) sont des œuvres graphiques : ils relèvent de CC BY-SA 4.0, pas de l'EUPL.

## Usage de l'intelligence artificielle

Ce projet a été réalisé avec des outils d'IA, sous la direction et la relecture de l'auteur :

- **Image de référence du logo** (`source/logo-reference.jpeg`) : générée avec **Google Gemini** à partir d'un brief de l'auteur. Le monogramme et les lockups SVG en sont une **reconstruction géométrique** faite par script, alignée sur cette image.
- **Code, SVG, icônes, motifs, tokens, brand board** : écrits et générés avec l'assistance de **Claude** (Anthropic), via Claude Code. Les commits concernés portent le trailer `Co-authored-by: Claude <noreply@anthropic.com>`.
- **Textes** (`BRAND.md`, `LORE.md`, `CODEX.md`) : les briefs de marque et de lore sont fournis par l'auteur ; la mise en forme, la traduction, la structuration et les corrections ont été faites avec Claude.

Conséquences à connaître :

- Le **statut au regard du droit d'auteur** d'éléments produits par une IA est incertain et varie selon les pays. Les licences ci-dessus s'appliquent **dans la mesure des droits détenus** par l'auteur ; aucune exclusivité n'est revendiquée sur des éléments qui ne seraient pas protégeables.
- Tout est fourni **sans garantie**, y compris quant à l'absence d'antériorité ou de ressemblance avec d'autres œuvres. Une vérification (marque, dessin et modèle) est recommandée avant un usage commercial du logo.
- Les licences libres ne confèrent pas de droits sur le **nom « RuneRide »** en tant que marque, ni ne remplacent un dépôt éventuel.

## Marques de tiers

`CODEX.md` cite des marques et modèles de motos (BMW, Ducati, Harley-Davidson, KTM, Royal Enfield, Triumph, Yamaha, Honda, Kawasaki, Suzuki, Aprilia, Husqvarna, Indian, etc.) à titre purement **descriptif et humoristique**. Ces marques appartiennent à leurs titulaires ; RuneRide n'est ni affilié à eux ni approuvé par eux.

## English summary

Code (`tools/`, `tokens/`, `brand-board.html`): **EUPL-1.2**. Everything else (logos, icons, patterns, texts): **CC BY-SA 4.0**. Third-party fonts keep their **SIL OFL 1.1** licence. The logo reference image was generated with Google Gemini; code, SVG artwork and text structuring were produced with Claude (Anthropic) under the author's direction. Copyright status of AI-generated material is uncertain and varies by jurisdiction; licences apply to the extent of rights held, with no warranty. Motorcycle brand names in `CODEX.md` are used descriptively and humorously; no affiliation or endorsement.
