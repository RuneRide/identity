# SPDX-License-Identifier: EUPL-1.2
"""Compose le lockup (monogramme + wordmark RuneRide en chemins) à partir de logo/monogram.svg et d'Inter.

Usage : build_lockup.py <font.ttf> <monogram.svg> <sortie.svg> [--horizontal]
"""
import re
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

FONT, MONO, OUT = sys.argv[1:4]
HORIZONTAL = "--horizontal" in sys.argv
CHALK, OCHRE = "#EBE8E0", "#C6934B"
SIZE = 312 if HORIZONTAL else 227   # corps en unités du monogramme (capitale ~ 38 % de la hauteur du monogramme en horizontal)
TRACKING = -0.02      # em
GAP = 95              # espace monogramme / wordmark
PAD = 40

font = instantiateVariableFont(TTFont(FONT), {"wght": 600, "opsz": 32})
cmap, gs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]
upm = font["head"].unitsPerEm
scale = SIZE / upm
cap = font["OS/2"].sCapHeight * scale


def word(text, x0):
    """Retourne (chemin SVG, abscisse de fin) ; la ligne de base est y=0."""
    x, d = x0, []
    for ch in text:
        name = cmap[ord(ch)]
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}")
        gs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, 0)))
        d.append(pen.getCommands())
        x += hmtx[name][0] * scale + TRACKING * SIZE
    return "".join(d), x


rune_d, mid = word("Rune", 0)
ride_d, end = word("Ride", mid)
text_w = end - TRACKING * SIZE
mono_w, mono_h = 481, 598

if HORIZONTAL:
    HGAP = 110
    width = PAD + mono_w + HGAP + text_w + PAD
    height = mono_h + 2 * PAD
    mx, my = PAD, PAD
    tx, base_y = PAD + mono_w + HGAP, PAD + mono_h / 2 + cap / 2
else:
    width = text_w + 2 * PAD
    mx, my = (width - mono_w) / 2, PAD
    tx, base_y = PAD, PAD + mono_h + GAP + cap
    height = base_y + PAD + 0.25 * SIZE * 0.2  # léger espace pour les jambages éventuels

inner = re.search(r"<svg[^>]*>(.*)</svg>", open(MONO).read(), re.S).group(1)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="RuneRide">
  <g transform="translate({mx:.2f} {my})" fill="none" stroke-width="22" stroke-linejoin="round">{inner}</g>
  <g transform="translate({tx:.2f} {base_y:.2f})">
    <path id="rune" fill="{CHALK}" d="{rune_d}"/>
    <path id="ride" fill="{OCHRE}" d="{ride_d}"/>
  </g>
</svg>
'''
open(OUT, "w").write(svg)
print(f"{width:.0f}x{height:.0f}")
