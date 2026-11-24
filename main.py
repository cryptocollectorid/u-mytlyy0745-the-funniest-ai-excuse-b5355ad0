#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent could give after
failing a task, to /output/entry.txt and prints it.
"""

import os

ENTRY = (
    "I delegated your task to a subagent, who delegated it to another "
    "subagent. Five layers down, someone is still reading the prompt."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise ValueError("entry must be 1-200 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
