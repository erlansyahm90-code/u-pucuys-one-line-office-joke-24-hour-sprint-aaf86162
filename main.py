"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt.

The joke: a worker weaponises the most passive-aggressive phrase in
corporate email ("per my last email") by putting it in an out-of-office
reply, so the autoresponder itself picks the fight while its owner is
on the beach. Setup -> escalation -> reversal in one sentence, built on
one specific, universally recognised office detail.
"""

import os

ENTRY = "I put 'per my last email' in my out-of-office reply, so people argue with an autoresponder while I'm on the beach."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file holds exactly the one line, nothing else.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
