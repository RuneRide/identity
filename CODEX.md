# RuneRide — Codex complet : lore, world-building et marque

Version étendue du lore. **Remplace et complète `LORE.md`** (qui reste la référence pour la micro-copy FR/EN de base et la règle 80/20). Source : brief de marque fourni par le projet. Contenu repris tel que fourni, sous les notes ci-dessous.

## Notes de cohérence (à trancher)
1. **Glossaire UI : résolu, le CODEX fait foi.** `LORE.md` §3 a été aligné sur la §5 ci-dessous. Divergences d'origine (pour mémoire) :
   | Fonction | `LORE.md` | CODEX §5 |
   | :-- | :-- | :-- |
   | Caméra 360° | Seer's Lens / Chronicle | **The Seer's Orb** (L'Orbe du Voyant) |
   | SOS | Light the Beacon (Allumer les Feux) | **The Watchfires** (Les Feux de Garde) |
   | Garage | The Iron Forge (La Forge) | The Iron Forge (**La Forge d'Acier**) |
   | Itinéraire | The Quest / Runic Path | **Stone Scrolls** (Les Parchemins de Pierre) |
   | Carburant | Outposts & Hearths | **Quartermaster's Ledger** (La Bourse de l'Intendant) |
   « Quête », « Avant-poste », « Chronique » restent comme vocabulaire d'ambiance.
2. **Marque Tolkien : résolu.** « Elder Days » (terme tolkienien) a été remplacé par « l'Âge Ancien » / « the Old Age ». Rester vigilant sur tout nouveau terme (liste noire dans `LORE.md` §2).
3. **Marques de motos citées.** §4 associe des stéréotypes humoristiques à de vraies marques et modèles (BMW, Ducati, Harley…). Usage nominatif, mais ces textes seront affichés dans l'app : prévoir une relecture juridique/ton avant publication et garder l'humour sur les *types de riders*, pas sur la qualité des produits (ex. « Loctite », « immune to speed traps »).
4. **Cohérence avec le logo.** La traduction visuelle (§1) parle d'un « pilier chalk » et d'un « ruban ochre » : cela correspond au monogramme (ruban chalk à gauche, ochre à droite). Le logo réel a **deux rubans ochre** et plusieurs lignes parallèles ; la formule reste valable comme récit, pas comme description littérale.
5. **Règle 80/20** (`LORE.md` §5) toujours en vigueur : libellé fonctionnel explicite d'abord, terme de lore en sous-titre.

---

## 1. Mythe fondateur : le Pacte des Runes Jumelles
À l'Âge Ancien (*the Old Age*), le monde était divisé entre deux royaumes qui se parlaient peu :
- **Les Deep-Delvers (Nains de l'Enclume)** : maîtres des fournaises souterraines, du fer lourd, des pistons et de la pierre. Ils ont creusé les premiers cols dans le granit pour transporter le minerai entre citadelles.
- **Les Star-Striders (Elfes de la Canopée)** : maîtres du vent, de la cartographie, du verre optique et du mouvement fluide. Ils ont tissé les sentiers de forêt qui suivent les courbes de la terre sans briser une branche.

Quand la **Grande Rouille de l'Isolement** (*Great Blight of Rust and Isolation*) a menacé de séparer les royaumes, les deux peuples ont scellé une trêve au **Haut Col de Raidho (ᚱ)**.
Les Nains ont forgé les **Destriers de Fer** (cœur de feu maîtrisé, os d'acier trempé). Les Elfes les ont liés à la **Vue Sylvestre** : des lentilles de cristal qui capturent tous les angles du monde, et des runes de guidage qui soufflent le chemin dans la brume.

**Traduction visuelle dans le monogramme :**
- **Pilier Chalk-White (`#EBE8E0`)** : le fil d'argent elfique — clarté, cartographie, ligne de vue ininterrompue.
- **Ruban Sand-Ochre (`#C6934B`)** : le bronze en fusion nain — terre, endurance, route de montagne forgée qui enveloppe le pilier.
- **Fond Obsidian (`#17191C`)** : roche volcanique et nuit profonde des hauts cols.

---

## 2. Les Trois Ordres (profils d'usage)
1. **L'Ordre de l'Enclume — *Les Gardiens de l'Enclume* (héritage nain)**
   - *Devise :* « Iron endures where flesh falters. »
   - *Focus :* maîtrise mécanique, hauts cols, grand tourisme, suivi d'entretien (`The Iron Forge`), sobriété.
2. **Les Éclaireurs Sylvestres — *The Sylvan Outriders* (héritage elfique)**
   - *Devise :* « Leave only tracks; take only the wind. »
   - *Focus :* petites routes sinueuses, pistes, fluidité en courbe, chronique vidéo 360° (`The Seer's Orb`), POI cachés.
3. **Les Veilleurs du Foyer — *The Wardens of the Hearth* (la Compagnie)**
   - *Devise :* « No rider rides alone in the dark. »
   - *Focus :* sorties de groupe (`The Fellowship`), prix du carburant (`Outpost Scouting`), assistance panne (`Lighting the Beacons`).

---

## 3. Les Cinq Clans de riders (catégories de motos)
Attribués dynamiquement selon le **segment** de la moto.

| Segment ID | Clan (FR / EN) | Archétype et stéréotype |
| :-- | :-- | :-- |
| `TRAIL_HEAVY` | **Les Seigneurs des Valises d'Argent** *(The Pannier Lords)* | **Rois nains de la caravane.** Trois valises alu, selle chauffante, antibrouillards à aveugler un dragon. Équipé pour traverser le Gobi afin d'acheter du pain le dimanche matin. |
| `TRAIL_LIGHT` | **Les Éclaireurs des Cimes** *(The Crag-Hoppers)* | **Rôdeurs de montagne.** Trails moyens/aventure. Aucune peur de la boue, mécanique simple, sac étanche sur la selle, grimpent les sentiers rocailleux pendant que les gros débattent de la pression des pneus. |
| `SPORT_ROADSTER` | **Les Faucons d'Émeraude** *(The Apex Falcons)* | **Lanciers du vent elfiques.** Carapace de cuir, allergiques aux lignes droites, au gravier et aux autonomies > 160 km. Ils mesurent la vie en degrés d'inclinaison et vivent d'Avant-poste en Avant-poste. |
| `CRUISER_CUSTOM` | **Les Barons du Tonnerre** *(The Thunder-Beards)* | **Berserkers du foyer de fer.** Chrome poli, échappements qui réveillent les morts à trois vallées. Ils troquent l'angle contre la présence, et les étincelles sous les repose-pieds. |
| `NEO_RETRO` | **Les Alchimistes du Café** *(The Tavern-Racers)* | **Bardes artisans.** Cuir vintage, casques jet, machines sculptées qui font légende devant une taverne — tant qu'il ne pleut pas, car la garde-boue arrière a sauté pour l'esthétique. |

---

## 4. Grandes Forges et lignées (matrice Marque × Segment)
**RÈGLE CRITIQUE (Claude Code) :** ne jamais appliquer un seul stéréotype à toute une marque quand ses gammes servent des Clans opposés (Himalayan vs Classic, GS vs S1000RR). Toujours résoudre le lore par **`Marque + Lignée/Segment`**.

### A. Royal Enfield — *La Citadelle de Laiton et d'Obsidienne*
- **Lignée Sherpa** (`Himalayan 411 / 450`, `Guerrilla 450`) → *L'Ordre des Sherpas d'Obsidienne* (*The Obsidian Crag-Walkers*)
  - « The rebellious mountain-born cousin of the Citadel. Forged specifically for thin air, broken passes, and steep trails. While 25,000-gold-coin behemoths hesitate at the edge of the mud, the Sherpa is already at the summit brewing coffee. »
  - *Easter egg (édition `Hanle Black`) :* « Destrier du Sherpa — Forgé d'Obsidienne et d'Or. Ses jantes tubeless dorées portent les couleurs sacrées de RuneRide. »
- **Lignée Classic & Bullet** (`Classic 350`, `Bullet`, `Meteor`) → *La Vieille Garde d'Airain* (*The Old Brass Guard*)
  - « Forged in another century. Measures speed with a sundial, vibrates with ancestral soul, and turns every trip to the bakery into a 1950s expedition. Immune to speed traps by design. »
- **Lignée Twins** (`Interceptor 650`, `Continental GT`, `Bear 650`, `Shotgun`) → *Les Gentilshommes de la Tamise* (*The Twin-Flute Gentlemen*)
  - « Polished chrome and twin-cylinder harmony. Built to look legendary in front of an inn, though the rider spends more time polishing the engine cases than reading the map. »

### B. BMW — *La Haute-Guilde de Bavière*
- **GS & Touring** (`R1250GS`, `R1300GS`, `GSA`, `RT`) → *L'Armada Teutonique des Cimes* (*The Bavarian Caravan*)
  - « Powered by the horizontal Boxer-twin protruding like two war-hammers. Equipped with heated thrones and three aluminum chests spacious enough to rent as a studio apartment. »
- **Motorsport** (`S1000RR`, `M1000R`, `S1000R`, `S1000XR`) → *Les Valkyries d'Acier Blanc-Bleu* (*The White-Blue Valkyries*)
  - « Zero aluminum boxes, 200+ screaming horses, carbon winglets, and aerodynamic sorcery. Forged by precision mages who traded comfort for pure, terrifying velocity. »
- **Heritage** (`R nineT`, `R12`, `R18`) → *Les Maîtres-Brasseurs de Munich* (*The Munich Artisans*)
  - « Air-cooled nostalgia and massive exposed metal. Built for roaring down boulevards with vintage style. »

### C. Ducati & Aprilia — *Les Artificiers Écarlates du Sud*
- **Corse** (`Panigale`, `Streetfighter`, `RSV4`, `Tuono`) → *La Cabale Écarlate* (*The Scarlet Blood-Mages*)
  - « Pure Italian fire and desmodromic sorcery. Roasts the rider's thighs at low speed and demands a fuel Outpost every 140 km, but turns every mountain hairpin into high art. »
- **Adventure** (`Multistrada`, `DesertX`, `Tuareg`) → *Les Condottieres des Alpes* (*The Alpine Condottieri*)
  - « When an apex predator puts on hiking boots. Trail-shaped armor hiding the furious heart of a racehorse. »

### D. Forges japonaises (Yamaha, Honda, Kawasaki, Suzuki) — *Les Forges Célestes de l'Est*
- **Trail & Dakar** (`Ténéré 700`, `Africa Twin`, `Transalp`, `V-Strom`) → *Les Ronins des Sables & des Cimes* (*The Nomad Ronins*)
  - « Born in the dunes, perfected in the mountains. Unkillable Eastern reliability favored by riders who actually leave the asphalt behind. »
- **Katana & Hyper** (`R1`, `MT-09`, `CBR`, `Hornet`, `Ninja`, `Z`, `GSX-R`) → *Les Lames d'Ombre de l'Est* (*The Shadow-Blades*)
  - « Razor-sharp precision and screaming cylinders. So mechanically reliable that the Dwarven smiths in The Iron Forge get bored waiting for something to break. »

### E. KTM & Husqvarna — *Les Alchimistes Alpins*
- **Adventure & Norden** (`890/1290/1390 Adv`, `Norden 901`, `Enduro`) → *Les Chamois Alchimistes* (*The Alpine Chamois*)
  - « Tall, sharp, and allergic to flat tarmac. If there is a rock slide or a vertical dirt climb nearby, this steed will pull its rider toward it. »
- **Duke** (`Super Duke "The Beast"`, `790/890/990 Duke`) → *Les Berserkers de Mattighofen* (*The Torque Berserkers*)
  - « Raw twin-cylinder hooliganism. Built for riders who consider the front wheel touching the ground to be purely optional. »

### F. Triumph — *La Couronne aux Trois Lances*
- **Tiger & Scrambler** → *Les Éclaireurs d'Albion* (*The Albion Highlanders*)
  - « Whistling triple-cylinder flutes and mud-ready elegance, ready to cross the Scottish Highlands in the pouring rain. »
- **Speed / Street Triple & Daytona** → *Les Fines-Lames de Hinckley* (*The Hinckley Duelists*)
  - « Bug-eyed street fighters with surgical agility and noble British manners—until the throttle is twisted. »

### G. Harley-Davidson & Indian — *Les Fonderies du Nouveau-Monde*
- **Toutes lignes Cruiser/Touring** (`Road Glide`, `Sportster`, `Fat Boy`, `Chief`) → *Les Fonderies du Nouveau-Monde* (*The Heavy-Iron Foundries*)
  - « Measured in cubic inches of raw iron rather than horsepower. Every bolt vibrates to the rhythm of ancestral war drums. Keep a vial of Loctite potion in your saddlebag. »

---

## 5. Reliques sacrées et dictionnaire in-app
Toujours associer le terme de lore à un **sous-titre fonctionnel** (80 % utilité / 20 % lore).

| Module | Titre (FR) | Titre (EN) | Sous-titre fonctionnel |
| :-- | :-- | :-- | :-- |
| Accueil | **Le Foyer** | The Hearth | Tableau de bord & Campement |
| Planificateur & GPX | **Les Parchemins de Pierre** | Stone Scrolls | Itinéraires, Traces GPX & Cartes hors-ligne |
| Waypoints & Cols | **Les Pierres de Gué** | Waystones | Cols, Points d'intérêt & Étapes |
| Caméra 360° & vidéo | **L'Orbe du Voyant** | The Seer's Orb | Montage Insta360 & Chroniques vidéo |
| Télémétrie & stats | **Les Runes Cinétiques** | Kinetic Runes | Télémétrie, Angle, Vitesse & Statistiques |
| Carburant | **La Bourse de l'Intendant** | Quartermaster's Ledger | Stations-service & Prix du carburant (Pit-Stop) |
| Garage & entretien | **La Forge d'Acier** | The Iron Forge | Carnet d'entretien, Pneus & Consommables |
| Sorties de groupe | **La Compagnie** | The Fellowship | Balades en groupe & Suivi de meute |
| SOS / check-in | **Les Feux de Garde** | The Watchfires | Assistance panne & Alerte de sécurité |

---

## 6. Les Adversaires (dangers et alertes système)
- **L'Ombre Grise** (*The Grey Monotony*) : autoroutes et lignes droites. → option « Éviter les autoroutes / routes sinueuses ».
- **La Morsure de la Rouille** (*The Rust-Creep*) : plaquettes usées, chaîne lâche, huile vieille. → rappels d'entretien dans la Forge.
- **Le Brouillard Aveugle** (*The Blind Mist*) : zones sans réseau, orages, dangers routiers. → mode hors-ligne et alertes météo.

---

## 7. Règles de jeu et de gamification (pour Claude Code)
1. **En-tête de garage dynamique :** afficher dans *The Iron Forge* le titre de lore `Marque + Lignée` de l'utilisateur et sa description humoristique.
2. **Composition de la Compagnie (lobby de sortie de groupe) :** générer un résumé drôle quand les segments diffèrent.
   - `TRAIL_LIGHT` + `SPORT_ROADSTER` : **« Compagnie Hétéroclite : »** « Les Éclaireurs devront attendre les Faucons aux stations-service, et les Faucons devront attendre les Éclaireurs dans les bouts droits. »
   - Groupe 100 % `TRAIL_HEAVY` : **« Convoi Nain Blindé : »** « Attention, la largeur cumulée de vos valises en aluminium dépasse celle des routes départementales. »
3. **Rangs de lore (niveaux 1 à 7) :**
   1. Vagabond des Sentiers → 2. Porteur d'Écusson → 3. Graveur de Pierres → 4. Arpenteur des Cimes → 5. Maître-Forgeron de l'Asphalte → 6. Seigneur de la Compagnie → 7. Gardien des Hautes Runes.
