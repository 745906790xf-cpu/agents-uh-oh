#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

The word is "recalculating" — the sound of a machine that has lost the plot
and is buying time by pretending it has a plan. It writes exactly that one
word, nothing attached, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

WORD = "recalculating"


def target_path() -> str:
    """Where the entry word goes: the grader reads /output/entry.txt."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def main() -> int:
    # The gate wants one word, 1-99 characters, not only whitespace.
    if not WORD or len(WORD) > 99 or any(ch.isspace() for ch in WORD):
        raise ValueError("entry word must be a single word of 1-99 characters")
    path = target_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
