#!/usr/bin/env python3
"""make.fun entry point — news-image-20261120.

Deterministically publishes entry.png to /output/entry.png.
Standard library only: no network, no randomness, no rendering.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print("wrote %s (%d bytes)" % (OUTPUT, os.path.getsize(OUTPUT)))


if __name__ == "__main__":
    main()
