"""Break Production, Own It — make.fun entry.

Writes exactly one line: an engineer owning a production breakage outright.
"""

import os

LINE = (
    "I pushed straight to prod on a Friday, took the whole platform "
    "down with a single commit, and I'm not sorry — I'm the one "
    "bringing it back before your coffee gets cold."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
