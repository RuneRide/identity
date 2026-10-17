"""Assemble favicon.ico (entrées PNG) à partir de logo/icon/png.

Règle d'icône : 16 px simplifié, 32/48 px logo complet.
Usage : build_ico.py <dossier_png> <sortie.ico>
"""
import struct
import sys
from pathlib import Path

png_dir, out = Path(sys.argv[1]), Path(sys.argv[2])
sizes = (16, 32, 48)
blobs = [(s, (png_dir / f"favicon-{s}.png").read_bytes()) for s in sizes]

header = struct.pack("<HHH", 0, 1, len(blobs))
offset = 6 + 16 * len(blobs)
entries, data = b"", b""
for size, blob in blobs:
    entries += struct.pack("<BBBBHHII", size, size, 0, 0, 1, 32, len(blob), offset)
    data += blob
    offset += len(blob)
out.write_bytes(header + entries + data)
print(out, out.stat().st_size, "octets")
