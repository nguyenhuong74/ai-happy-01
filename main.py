#!/usr/bin/env python3
"""ai-happy-01 entry: write the image that makes the AI judge happy.

The image lives in this repository as entry.png (1024x1024 PNG, under
1 MiB). This program copies it, byte for byte, to /output/entry.png.

No network, no randomness, no dependencies beyond the standard
library: every run produces identical bytes.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT = Path("/output/entry.png")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # The copy must be byte-identical to the image in the repository.
    assert _sha256(SOURCE) == _sha256(OUTPUT), "output differs from source"
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
