#!/usr/bin/env python3
"""The 3 AM Commit Message - make.fun entry.

Writes one commit message (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it
to stdout. No dependencies, no network, deterministic output.
"""

import os
import sys

ENTRY = "fix: force-pushed prod back to yesterday; yesterday is on fire too. Revoking my own deploy access."


def main() -> int:
    if not (1 <= len(ENTRY) <= 200):
        sys.stderr.write(f"entry is {len(ENTRY)} chars, must be 1-200\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
