"""Write a one-line joke about working beside AI coding agents to /output/entry.txt.

Deterministic: the joke is a fixed string; the program only writes it out.
Runs in a sandbox with no network.
"""

import os

JOKE = (
    "My AI coding agent demoed flawlessly — then it confidently walked "
    "the audience through a feature it had never actually built."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
