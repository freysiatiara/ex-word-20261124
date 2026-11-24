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


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
