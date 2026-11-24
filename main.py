#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes the chosen entry sentence to /output/entry.txt (creating /output
if needed). The sentence explains the modern internet to a time traveler
from 1800 using only things a person of that year already knows: a
library, a post office, a road, a breath.
"""

import os

ENTRY = (
    "It is a library with no walls and a post office with no roads, "
    "where any man may ask any question and hear the whole world "
    "answer in a single breath."
)


def output_dir() -> str:
    """Where entry.txt goes: the grader's MAKEFUN_OUTPUT_DIR first,
    then an argv directory, then /output (the gate's documented path)."""
    if env_dir := os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return env_dir
    import sys

    if len(sys.argv) > 1:
        return sys.argv[1]
    return "/output"


def main() -> None:
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    # Guard: the gate only accepts 1-200 chars, one line, non-whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
