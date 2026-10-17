# SPDX-License-Identifier: EUPL-1.2
"""Génère les motifs lore : séparateurs runiques et courbes de niveau (tuile sans couture).

Usage : build_patterns.py <dossier_sortie>
"""
import sys
from pathlib import Path

import cv2
import numpy as np

OUT = Path(sys.argv[1])
LINE, OCHRE = "#2E323B", "#C6934B"

# --- Séparateurs runiques : ligne fine, losange ochre au centre -------------------------
def divider(width, ornate):
    cx, h = width / 2, 12
    gap = 14 if not ornate else 30
    d = 7  # demi-diagonale du losange
    parts = [
        f'<path d="M0 {h}H{cx - gap:g}M{cx + gap:g} {h}H{width}" stroke="{LINE}" stroke-width="1.5"/>',
        f'<path d="M{cx:g} {h - d}L{cx + d:g} {h}L{cx:g} {h + d}L{cx - d:g} {h}Z" fill="{OCHRE}"/>',
    ]
    if ornate:  # petits losanges latéraux + repères
        for s in (-1, 1):
            x = cx + s * 20
            parts.append(f'<path d="M{x:g} {h - 3}L{x + 3:g} {h}L{x:g} {h + 3}L{x - 3:g} {h}Z" fill="none" stroke="{OCHRE}" stroke-width="1.2"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {2 * h}" role="separator">'
            + "".join(parts) + "</svg>\n")

(OUT / "runic-divider.svg").write_text(divider(480, False))
(OUT / "runic-divider-ornate.svg").write_text(divider(480, True))

# --- Courbes de niveau : champ périodique -> contours -> tuile --------------------------
T, RES = 600, 600          # taille de tuile (unités SVG) et résolution du champ
rng = np.random.default_rng(7)
ys, xs = np.mgrid[0:3 * RES, 0:3 * RES] / RES * 2 * np.pi   # 3x3 tuiles
field = np.zeros_like(xs)
for _ in range(7):                                           # fréquences entières => périodique
    fx, fy = rng.integers(-3, 4, 2)
    if fx == fy == 0:
        continue
    field += rng.uniform(0.5, 1.0) / np.hypot(fx, fy) * np.sin(fx * xs + fy * ys + rng.uniform(0, 6.28))

lo, hi = np.percentile(field, [3, 97])
levels = np.linspace(lo, hi, 15)
paths, index_paths = [], []
for i, lv in enumerate(levels):
    m = (field > lv).astype(np.uint8) * 255
    cs, _ = cv2.findContours(m, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in cs:
        if len(c) < 40:
            continue
        a = cv2.approxPolyDP(c, 1.2, False).reshape(-1, 2) / RES * T - T  # recentre sur la tuile du milieu
        if a[:, 0].max() < -10 or a[:, 0].min() > T + 10 or a[:, 1].max() < -10 or a[:, 1].min() > T + 10:
            continue
        d = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in a)
        (index_paths if i % 5 == 2 else paths).append(d)

def topo(color, opacity=1.0):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {T} {T}" width="{T}" height="{T}" fill="none" '
            f'stroke-linejoin="round" stroke-linecap="round" opacity="{opacity}">'
            f'<path d="{"".join(paths)}" stroke="{color}" stroke-width="1.2"/>'
            f'<path d="{"".join(index_paths)}" stroke="{color}" stroke-width="2.2"/></svg>\n')

(OUT / "topo-tile.svg").write_text(topo(LINE))
(OUT / "topo-tile-ochre.svg").write_text(topo(OCHRE, 0.18))
print(len(paths), len(index_paths))
