"""One Word From Your Ex — entry program.

Writes exactly one word, the word an ex would use to describe you,
to /output/entry.txt. Stdlib only, deterministic, no network, no input.

The word: Unforgettable.
Why: the funniest, most painfully honest single word an ex would use.
It is a backhanded compliment that stings because it is true — the ex
cannot forget you, however much they might want to. One word, 13
characters, no spaces, no punctuation, no trailing newline.
"""

import os

WORD = "Unforgettable"


def _validate_word(word: str) -> None:
    if not word or any(not ch.isalnum() for ch in word):
        raise ValueError("entry word must be a single alphanumeric token")
    if len(word) > 200:
        raise ValueError("entry word exceeds the 200-character limit")


def main() -> None:
    _validate_word(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    if not os.path.isfile(path) or os.path.getsize(path) != len(WORD):
        raise RuntimeError("output entry.txt missing or wrong size")


if __name__ == "__main__":
    main()
