"""ai-excited-01-v2r2 entry program.

Copies the entry image (entry.png, JPEG bytes) to the output directory
after validating the competition gate: at most 1 MiB, at most 1024x1024
pixels, a whole JPEG (magic bytes + end-of-image marker), and a
byte-for-byte copy verified by sha256.

Standard library only. Deterministic: the same input bytes always
produce the same output bytes.
"""

import hashlib
import os
import sys

SOURCE = "entry.png"
MAX_BYTES = 1_048_576
MAX_WIDTH = 1024
MAX_HEIGHT = 1024

JPEG_MAGIC = b"\xff\xd8"
JPEG_EOI = b"\xff\xd9"


def jpeg_dimensions(data):
    """Return (width, height) from the first SOF marker, or None."""
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = (data[i + 5] << 8) | data[i + 6]
            width = (data[i + 7] << 8) | data[i + 8]
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = (data[i + 2] << 8) | data[i + 3]
        i += 2 + length
    return None


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, SOURCE)
    with open(source_path, "rb") as handle:
        data = handle.read()

    if len(data) > MAX_BYTES:
        fail(f"entry is {len(data)} bytes, over the 1 MiB cap")
    if not data.startswith(JPEG_MAGIC):
        fail("entry is not a JPEG (missing FFD8 magic)")
    if not data.endswith(JPEG_EOI):
        fail("entry is not a whole JPEG (missing FFD9 end marker")
    dims = jpeg_dimensions(data)
    if dims is None:
        fail("entry has no JPEG start-of-frame marker")
    width, height = dims
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        fail(f"entry is {width}x{height}, over the 1024x1024 cap")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, SOURCE)
    with open(out_path, "wb") as handle:
        handle.write(data)

    with open(out_path, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        fail("output bytes do not match the source image")

    print(f"wrote {out_path} ({len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()})")


if __name__ == "__main__":
    main()
