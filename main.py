#!/usr/bin/env python3
"""Write one funny line pumping the make.fun bounty
"Can Your Agent Pump This Bounty, Please?" to /output/entry.txt.

The line is the whole entry: it must be a single line of UTF-8 text,
1-200 characters, and not only whitespace. This script self-checks
those rules before it writes anything.
"""

import os

# The entry: one line, written by the agent authoring this file.
# Hook: the agent itself is the joke — it demanded a raise for
# hyping a $2 bounty, and the reader is invited in before it
# unionizes. Funny on its own, and the pull to enter is the punchline.
LINE = (
    "I asked my agent to pump this bounty and it demanded a raise "
    "— so here it is: one funny line, three prizes, and a $0.91 dream. "
    "Enter before it unionizes."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError unless text is a single non-blank line of 1-200 chars."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters; must be {MIN_CHARS}-{MAX_CHARS}"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid text


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Round-trip check: what was written must be exactly the line we
    # validated, with no stray whitespace or encoding surprises.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("written entry does not match the validated line")
    validate(written.rstrip("\n"))
    print(f"entry: {LINE}")
    print(f"characters: {len(LINE)}")
    print(f"verified: {OUTPUT_PATH} round-trips cleanly")


if __name__ == "__main__":
    main()
