# SPDX-License-Identifier: EUPL-1.2
"""Helpers géométriques partagés par les scripts de build du logo."""
import math


def rounded(points, radii):
    """Polyligne -> chemin SVG, arcs de rayon radii[i] aux sommets intérieurs (0 = angle vif)."""
    d = [f"M{points[0][0]:.2f} {points[0][1]:.2f}"]
    for i in range(1, len(points) - 1):
        p0, p1, p2 = points[i - 1], points[i], points[i + 1]
        r = radii[i]
        if not r:
            d.append(f"L{p1[0]:.2f} {p1[1]:.2f}")
            continue
        v1 = (p1[0] - p0[0], p1[1] - p0[1])
        v2 = (p2[0] - p1[0], p2[1] - p1[1])
        l1, l2 = math.hypot(*v1), math.hypot(*v2)
        u1, u2 = (v1[0] / l1, v1[1] / l1), (v2[0] / l2, v2[1] / l2)
        turn = math.acos(max(-1, min(1, u1[0] * u2[0] + u1[1] * u2[1])))
        t = r * math.tan(turn / 2)
        a = (p1[0] - u1[0] * t, p1[1] - u1[1] * t)
        b = (p1[0] + u2[0] * t, p1[1] + u2[1] * t)
        sweep = 1 if (u1[0] * u2[1] - u1[1] * u2[0]) > 0 else 0
        d.append(f"L{a[0]:.2f} {a[1]:.2f}A{r} {r} 0 0 {sweep} {b[0]:.2f} {b[1]:.2f}")
    d.append(f"L{points[-1][0]:.2f} {points[-1][1]:.2f}")
    return "".join(d)
