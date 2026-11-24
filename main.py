"""Scent-Mail: one-sentence pitch for a bizarre-but-real startup.

Writes exactly one sentence (<=200 chars) to /output/entry.txt.
"""

import os

SENTENCE = (
    "Scent-Mail bottles a long-distance lover's smell, worn shirt, "
    "fresh rain or home cooking, and mails it to their partner, "
    "because lonely couples pay postage for a whiff worth a thousand "
    "video calls."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
