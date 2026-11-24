#!/usr/bin/env python3
"""Write the make.fun entry for One Word, One Username, One Reward.

The entry is the entrant's own make.fun username, one word and nothing else.
"""

import os

ENTRY = "siganteng"
OUTPUT_PATH = "/output/entry.txt"


def write_entry(text):
    """Write the entry text to the output path, creating its directory."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
