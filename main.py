#!/usr/bin/env python3
"""Entrypoint for news-image-20261124.

Tuesday 24 November 2026 on one page: 33 dated stories, 7 regions,
13 illustrated scenes. The page itself is the entry — this program only
moves the committed picture into the output folder, after proving it is
a genuine PNG/JPEG inside the competition's 1 MiB cap. Stdlib only.
"""
import os
import shutil
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
PICTURE = os.path.join(BASE, "entry.png")
LIMIT = 1024 * 1024  # competition cap: 1 MiB


def picture_ok(path):
    """True only for a real PNG/JPEG under the size cap."""
    try:
        with open(path, "rb") as handle:
            magic = handle.read(8)
        nbytes = os.path.getsize(path)
    except OSError as exc:
        print(f"cannot read {path}: {exc}", file=sys.stderr)
        return False
    png = magic.startswith(b"\x89PNG\r\n\x1a\n")
    jpg = magic.startswith(b"\xff\xd8\xff")
    if not (png or jpg):
        print("entry.png is not a PNG/JPEG image", file=sys.stderr)
        return False
    if nbytes > LIMIT:
        print(f"entry.png is {nbytes} bytes, over the 1 MiB cap", file=sys.stderr)
        return False
    return True


def run():
    if not picture_ok(PICTURE):
        return 1
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "entry.png")
    shutil.copyfile(PICTURE, dest)
    os.chmod(dest, 0o644)
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
