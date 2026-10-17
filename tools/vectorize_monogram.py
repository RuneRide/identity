# SPDX-License-Identifier: EUPL-1.2
"""Vectorise le monogramme de source/logo-reference.jpeg en SVG (deux calques : chalk / ochre)."""
import sys
import cv2
import numpy as np

SRC, OUT = sys.argv[1], sys.argv[2]
SCALE = 4  # sur-échantillonnage avant tracé pour des bords plus lisses
CHALK, OCHRE, BG = (0xEB, 0xE8, 0xE0), (0xC6, 0x93, 0x4B), (0x17, 0x19, 0x1C)

img = cv2.imread(SRC)[:, :, ::-1]  # RGB
h, w = img.shape[:2]
s = w / 2000
x0, y0, x1, y1 = (int(v * s) for v in (820, 245, 1170, 680))
crop = img[y0:y1, x0:x1]
crop = cv2.resize(crop, None, fx=SCALE, fy=SCALE, interpolation=cv2.INTER_CUBIC).astype(np.float32)


def mask(name):
    # classification HSV : fond sombre / chalk (clair, peu saturé) / ochre (saturé)
    hsv = cv2.cvtColor(crop.astype(np.uint8), cv2.COLOR_RGB2HSV)
    sat, val = hsv[:, :, 1], hsv[:, :, 2]
    if name == "chalk":
        m = (val > 110) & (sat < 70)
    else:
        m = (val > 90) & (sat >= 70)
    m = m.astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(m, (0, 0), SCALE * 0.8).__ge__(127).astype(np.uint8) * 255


CORNER_DEG = 38  # au-delà : vrai angle ; en deçà : point d'un arc à lisser


def turn(a, b, c):
    v1, v2 = b - a, c - b
    ang = np.degrees(np.arctan2(v1[0] * v2[1] - v1[1] * v2[0], v1 @ v2))
    return abs(ang)


def contour_d(pts):
    """Polygone simplifié -> chemin SVG : segments droits + Béziers sur les arcs."""
    n = len(pts)
    corner = [turn(pts[i - 1], pts[i], pts[(i + 1) % n]) > CORNER_DEG for i in range(n)]
    if not any(corner):
        corner[0] = True
    start = corner.index(True)
    pts = np.roll(pts, -start, axis=0)
    corner = corner[start:] + corner[:start]
    pts = np.vstack([pts, pts[:1]])  # fermer
    corner = corner + [True]
    idx = [i for i, c in enumerate(corner) if c]
    out = [f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for a, b in zip(idx, idx[1:]):
        run = pts[a:b + 1]
        if len(run) == 2:
            out.append(f"L{run[1][0]:.1f} {run[1][1]:.1f}")
            continue
        ext = np.vstack([run[:1], run, run[-1:]])
        for i in range(1, len(ext) - 2):
            c1 = ext[i] + (ext[i + 1] - ext[i - 1]) / 6
            c2 = ext[i + 1] - (ext[i + 2] - ext[i]) / 6
            e = ext[i + 1]
            out.append(f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {e[0]:.1f} {e[1]:.1f}")
    return "".join(out) + "Z"


def path(m, eps):
    cs, _ = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    d = []
    for c in cs:
        if cv2.contourArea(c) < 30 * SCALE * SCALE / 4:
            continue
        a = cv2.approxPolyDP(c, eps * SCALE, True).reshape(-1, 2).astype(np.float64) / SCALE
        d.append(contour_d(a))
    return "".join(d)


vw, vh = (x1 - x0), (y1 - y0)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" fill-rule="evenodd">
  <path id="chalk" fill="#EBE8E0" d="{path(mask("chalk"), 1.0)}"/>
  <path id="ochre" fill="#C6934B" d="{path(mask("ochre"), 1.0)}"/>
</svg>
'''
open(OUT, "w").write(svg)
print(vw, vh, len(svg))
