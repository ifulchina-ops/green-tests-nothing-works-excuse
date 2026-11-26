#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes the entry -- one original excuse, under 140 characters -- to
``<output-dir>/entry.txt``. The grader runs this file as
``python3 -P -s /bot/main.py`` with no network; the output directory
comes from ``MAKEFUN_OUTPUT_DIR`` (``/output`` in the grader).
"""

import os
import sys

EXCUSE = (
    "All 214 tests pass \u2014 they just test the version of the app "
    "I described in the prompt, not the one I shipped."
)

MAX_CHARS = 140


def validate(line: str) -> str:
    """Return the line if it is a valid entry, else raise ValueError."""
    if not line:
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, over {MAX_CHARS}")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    return line


def main() -> int:
    try:
        line = validate(EXCUSE.strip())
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        print("entry.txt round-trip mismatch", file=sys.stderr)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
