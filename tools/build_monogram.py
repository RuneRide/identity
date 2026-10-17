"""Construit le monogramme RuneRide en SVG géométrique (traits de largeur uniforme).

Repère : viewBox 481x598, aligné sur le recadrage de source/logo-reference.jpeg.
Usage : build_monogram.py <sortie.svg> [--outline-ref <png>]
"""
import math
import sys

from geom import rounded

W = 22.0                 # largeur de trait
K = 0.85                 # pente des diagonales (dy/dx)
LEG_K = 1.13             # pente des jambes du R
CHALK, OCHRE, BG = "#EBE8E0", "#C6934B", "#17191C"
Y_TOP, Y_BOT = 27.0, 576.0
APEX_Y = 219.0


def at_x(apex, x):
    """Point de la diagonale descendante vers la gauche depuis `apex`, à l'abscisse x."""
    return (x, apex[1] + K * (apex[0] - x))


def arm_up(apex, y):
    """Point de la diagonale montante vers la gauche depuis `apex`, à l'ordonnée y."""
    return (apex[0] - (apex[1] - y) / K, y)


chalk_apex, och1_apex, och2_apex = (256, APEX_Y), (342, APEX_Y), (432, APEX_Y)

# Ruban chalk principal : barre basse -> montant -> diagonale -> apex -> bras haut
chalk_main = rounded(
    [(77, Y_BOT), (28, Y_BOT), (28, at_x(chalk_apex, 28)[1]), chalk_apex, arm_up(chalk_apex, 100)],
    [0, 0, 100, 0, 0],
)

# Boucle ochre : bras interne -> apex -> diagonale -> montant -> barre basse -> montant -> apex -> bras -> barre haute
ochre_loop = rounded(
    [
        arm_up(och1_apex, 0), och1_apex,
        at_x(och1_apex, 88), (88, Y_BOT), (148, Y_BOT),
        at_x(och2_apex, 148), och2_apex,
        arm_up(och2_apex, Y_TOP), (99, Y_TOP),
    ],
    [0, 3, 44, 0, 0, 6, 3, 0, 0],
)

# Crochet chalk (haut gauche), coupé par la ligne de séparation B
bracket = rounded([(88, 340), (88, Y_TOP), (28, Y_TOP), (28, 420)], [0, 0, 0, 0])

# Jambes du R
LEG_DX = lambda y0, y1: (y1 - y0) / LEG_K
ochre_leg = rounded(
    [(290 - 40, 388.5 - 40 * LEG_K), (290 + LEG_DX(388.5, Y_BOT), Y_BOT), (380, Y_BOT)],
    [0, 0, 0],
)
chalk_leg = rounded(
    [
        (198.5 - 20, 464 - 20 * LEG_K), (198.5 + LEG_DX(464, Y_BOT), Y_BOT),
        (243.5 + LEG_DX(426.5, Y_BOT), Y_BOT), (243.5 - 20, 426.5 - 20 * LEG_K),
    ],
    [0, 0, 0, 0],
)

# Fragment ochre au centre (polygone plein, extrait du tracé de référence)
# Fragment ochre : son haut prolonge l'arête supérieure du bras chalk (qui s'arrête à son bord droit x=159)
BAR_X0, BAR_X1 = 137.0, 159.0
_edge = lambda x: chalk_apex[1] - K * (chalk_apex[0] - x) - (W / 2) * math.hypot(1, K) / 1
ochre_bar = f"M{BAR_X0} {_edge(BAR_X0):.2f}L{BAR_X1} {_edge(BAR_X1):.2f}V255L{BAR_X0} 274Z"

G = "M0 630.7L481 227V700H0Z"                 # ligne G : zone sous la séparation des jambes
B = "M0 0H110V296L0 390.7Z"                   # zone au-dessus de la ligne B (crochet)
CH = "M159 0H481V598H0V230H159Z"          # coupe verticale du bras chalk
LEGCUT = "M-116 0H481V598H413Z"               # biseau (pente des jambes) du bout de la barre ochre

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 481 598" fill="none" stroke-width="{W:g}" stroke-linejoin="round" aria-label="RuneRide">
  <defs>
    <clipPath id="frame"><path d="M99 16H481V598H0V80H99Z"/></clipPath>
    <clipPath id="g"><path d="{G}"/></clipPath>
    <clipPath id="b"><path d="{B}"/></clipPath>
    <clipPath id="ch"><path d="{CH}"/></clipPath>
    <clipPath id="legcut"><path d="{LEGCUT}"/></clipPath>
  </defs>
  <g id="chalk" stroke="{CHALK}" stroke-linejoin="miter">
    <path d="{bracket}" clip-path="url(#b)"/>
    <g clip-path="url(#ch)"><path d="{chalk_main}"/></g>
    <g clip-path="url(#g)"><path d="{chalk_leg}"/></g>
  </g>
  <g id="ochre" stroke="{OCHRE}" stroke-linejoin="miter">
    <g clip-path="url(#frame)"><path d="{ochre_loop}"/></g>
    <path d="{ochre_bar}" fill="{OCHRE}" stroke="none"/>
    <g clip-path="url(#g)"><g clip-path="url(#legcut)"><path d="{ochre_leg}" stroke-linejoin="round"/></g></g>
  </g>
</svg>
'''
open(sys.argv[1], "w").write(svg)
