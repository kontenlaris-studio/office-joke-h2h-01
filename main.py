#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — one line, <200 chars."""

import os

JOKE = (
    "The office coffee machine only works when nobody needs it, "
    "which makes it the most emotionally stable relationship in this building."
)


def main():
    assert len(JOKE) < 200, f"joke too long: {len(JOKE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
