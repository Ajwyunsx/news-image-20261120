#!/usr/bin/env python3
"""make.fun entry point — news-image-20261120.

Deterministic publisher: copies the committed entry.png to /output/entry.png,
creating /output if it does not exist. Python 3 standard library only — no
network access, no rendering, no randomness.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUT_PATH)
    print("wrote %s (%d bytes)" % (OUT_PATH, os.path.getsize(OUT_PATH)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
