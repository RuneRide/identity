"""Icône simplifiée (favicon / icône d'app) dérivée de la géométrie du monogramme.

Même repère que build_monogram.py (viewBox 481x598) : traits épais, un seul ruban ochre,
pas de barres de liaison basses ni de crochet haut droit.

Usage : build_icon.py <sortie.svg> [--full] [--scale 0.55] [--radius 112]
  --full : monogramme complet (identique à logo/monogram.svg) sur fond obsidian ; sinon version simplifiée
           pour les très petites tailles (<= 48 px).
"""
import re
import sys
from pathlib import Path

from geom import rounded

W = 46.0
K, LEG_K = 0.85, 1.13
CHALK, OCHRE, BG = "#EBE8E0", "#C6934B", "#17191C"
Y_TOP, Y_BOT = 27.0, 587.0 - W / 2 + 6  # bas des traits calé sur y=587 par le cadre

arg = lambda name, default: float(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
SCALE, RADIUS, SIZE = arg("--scale", 0.55), arg("--radius", 112), 512

APEX_Y = 219.0
chalk_apex, ochre_apex = (256, APEX_Y), (358, APEX_Y)
X_OCHRE = 94  # montant ochre : écart perpendiculaire ~66 avec la tige chalk (x=28), comme sur les diagonales
diag = lambda apex, x: (x, apex[1] + K * (apex[0] - x))
arm = lambda apex, y: (apex[0] - (apex[1] - y) / K, y)

LOW = 620  # les traits dépassent en bas, le cadre les coupe à plat
chalk_main = rounded([(28, LOW), diag(chalk_apex, 28), chalk_apex, arm(chalk_apex, 120)], [0, 100, 0, 0])
stem_top = rounded([(28, 0), (28, 420)], [0, 0])
ochre = rounded(
    [arm(ochre_apex, -10), ochre_apex, diag(ochre_apex, X_OCHRE), (X_OCHRE, LOW)],
    [0, 3, 36, 0],
)
chalk_leg = rounded([(243.5 - 40, 426.5 - 40 * LEG_K), (243.5 + (LOW - 426.5) / LEG_K, LOW)], [0, 0])
ochre_leg = rounded([(297 - 40, 388.5 - 40 * LEG_K), (297 + (LOW - 388.5) / LEG_K, LOW)], [0, 0])

G = "M0 630.7L500 205V700H0Z"
B = "M0 0H110V296L0 390.7Z"

mark_w, mark_h = 500, 598
tx, ty = (SIZE - mark_w * SCALE) / 2, (SIZE - mark_h * SCALE) / 2

if "--full" in sys.argv:
    mono = Path(__file__).resolve().parent.parent / "logo" / "monogram.svg"
    inner = re.search(r"<svg[^>]*>(.*)</svg>", mono.read_text(), re.S).group(1)
    fx = (SIZE - 481 * SCALE) / 2
    Path(sys.argv[1]).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" role="img" aria-label="RuneRide">
  <rect width="{SIZE}" height="{SIZE}" rx="{RADIUS:g}" fill="{BG}"/>
  <g transform="translate({fx:.2f} {ty:.2f}) scale({SCALE})" fill="none" stroke-width="22" stroke-linejoin="round">{inner}</g>
</svg>
''')
    sys.exit()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" role="img" aria-label="RuneRide">
  <rect width="{SIZE}" height="{SIZE}" rx="{RADIUS:g}" fill="{BG}"/>
  <defs>
    <clipPath id="frame"><rect x="0" y="10" width="500" height="577"/></clipPath>
    <clipPath id="top"><path d="M99 10H500V600H0V80H99Z"/></clipPath>
    <clipPath id="g"><path d="{G}"/></clipPath>
    <clipPath id="b"><path d="{B}"/></clipPath>
    <clipPath id="ch"><path d="M0 0H481V598H0Z"/></clipPath>
  </defs>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({SCALE})" fill="none" stroke-width="{W:g}" stroke-linejoin="round">
   <g clip-path="url(#frame)">
    <g stroke="{CHALK}" stroke-linejoin="miter">
      <g clip-path="url(#b)"><path d="{stem_top}"/></g>
      <path d="{chalk_main}"/>
      <g clip-path="url(#g)"><path d="{chalk_leg}"/></g>
    </g>
    <g stroke="{OCHRE}" stroke-linejoin="miter">
      <g clip-path="url(#top)"><path d="{ochre}"/></g>
      <g clip-path="url(#g)"><path d="{ochre_leg}"/></g>
    </g>
   </g>
  </g>
</svg>
'''
open(sys.argv[1], "w").write(svg)
