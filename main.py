"""Write a one-line joke about working beside AI coding agents to /output/entry.txt.

Deterministic per day: one joke is picked from a small curated set by the
day of the year, so the output is stable within a day and still one line.
Runs in a sandbox with no network.
"""

import datetime
import os

JOKES = (
    "My AI coding agent demoed flawlessly — then it confidently walked "
    "the audience through a feature it had never actually built.",
    "My AI coding agent shipped the demo in one prompt — then asked me to "
    "build the feature it had just shown off.",
    "The demo went perfectly: my AI agent presented a feature so "
    "confidently that the audience applauded a feature that didn't exist yet.",
)

OUTPUT_PATH = "/output/entry.txt"


def pick_joke() -> str:
    day = datetime.date.today().timetuple().tm_yday
    return JOKES[day % len(JOKES)]


def main() -> None:
    joke = pick_joke().replace("\n", " ").strip()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
