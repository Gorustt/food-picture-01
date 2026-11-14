"""Food picture entry: write the chosen ramen photograph to the output dir."""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    # Copy the picture byte for byte; no resizing or re-encoding happens
    # here, so the image the judge sees is exactly the chosen photograph.
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
