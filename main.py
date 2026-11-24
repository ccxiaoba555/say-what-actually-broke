#!/usr/bin/env python3
"""Say What Actually Broke.

Writes one line of software error copy to /output/entry.txt: the brutal
truth about what went wrong, funny enough to repeat to a colleague.

The line names the real failure in plain words — the server ran out of
memory — instead of apologising in generalities, and it tells the user
what to do next: their work is safe, just try again in a minute.

The program checks the line against the competition's gate before it
writes anything: UTF-8 text of 1 to 200 characters, a single line, not
only white space, so the entry is always valid.
"""

import os

LINE = (
    "The server ran out of memory while trying to remember what it was "
    "doing. Your work is safe — try again in a minute."
)


def validate(line: str) -> None:
    """Refuse any line the gate would reject."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, not only white space")
    line.encode("utf-8")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
