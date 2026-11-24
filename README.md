# One Emoji, One Dream Vacation

Entry for the make.fun bounty
`u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35`.

## What it does

`main.py` writes exactly one emoji — 🏝 (U+1F3DD DESERT ISLAND) — to
`/output/entry.txt`, with no trailing newline and no extra text.

## Why this emoji

A desert island is the dream vacation in a single glyph: turquoise
water, a palm tree, white sand, and nowhere else to be. It reads
instantly at any size, needs no words, and points at one specific
dream — a faraway tropical escape — rather than travel in general.

## Run

```sh
python3 main.py
```

The program verifies its own output: after writing, it reads the file
back and exits non-zero unless it contains exactly that one emoji.

## Verification

`/output/entry.txt` is 4 bytes, `f0 9f 8f 9d`, one UTF-8 character,
U+1F3DD DESERT ISLAND — inside the gate's 1–8 character range.
