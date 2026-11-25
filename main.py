"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply line to /output/entry.txt.
The line is the duel winner of 7 drafts (see README for the duel table).

Duel result: D3 won all 6 of its pairings (4.1/6 game score). Runner-up D5
("good first draft, please revise") lost to D3 by a single margin point.
The winning gag is the machine habit everyone recognises -- the "As an AI
language model" preamble -- turned into a barista's tic and cut off
mid-sentence by the espresso machine, inside a concrete scene (chalkboard,
Café Segfault, 7-11, oat milk only) instead of a generic caffeine pun.
"""

import os

ENTRY = (
    "I quit. My out-of-office is now a chalkboard at Café Segfault: "
    "open 7–11, oat milk only, and I still start every order with "
    "'As an AI language model—' before the espresso machine cuts me off."
)


def main() -> None:
    # Self-check: gate requires UTF-8 text of 1-280 chars, one line, non-blank.
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
