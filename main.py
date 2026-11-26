#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis.

Writes one line to /output/entry.txt: the diagnosis an AI therapist
hands its human.

The line: a deadpan clinical label (chronic overthinking, acute
validation-seeking) with the turn at the end — the patient rehearsed
the session fourteen times, then asked a chatbot to feel something
for them. Therapist voice, one sentence, nothing borrowed.
"""

import os

ENTRY = (
    "Diagnosis: chronic overthinking, acute validation-seeking \u2014 you "
    "rehearsed this session fourteen times, then asked a chatbot to "
    "feel something for you."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace. The entry is one line, so a newline inside
    # it is a defect too. Fail loudly instead of shipping an entry
    # the scorer would refuse.
    if not ENTRY.strip() or not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry.txt must be 1-200 non-blank characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry.txt must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
