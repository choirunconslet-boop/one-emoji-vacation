"""One Emoji, One Dream Vacation.

Writes exactly one emoji -- a desert island -- to /output/entry.txt.
The desert island is the dream-vacation postcard in a single glyph:
turquoise water, a palm, white sand, nowhere else to be.
"""

import os

EMOJI = "\U0001F3DD"  # U+1F3DD DESERT ISLAND (emoji presentation by default)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one emoji, no trailing newline, no extra text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Robustness: read back and fail loudly rather than submit a bad file.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EMOJI:
        raise SystemExit(f"verification failed: entry.txt is {written!r}, expected {EMOJI!r}")


if __name__ == "__main__":
    main()
