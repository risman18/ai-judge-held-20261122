"""Write a short, slow text to /output/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel held"
(https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600).

Deterministic, standard library only. The text is embedded below and
written verbatim, UTF-8, with no trailing newline.
"""

import os

TEXT = (
    "Low afternoon light comes through the kitchen window and settles "
    "across the table like it owns the place. The house has finished "
    "its chores. Your chair is pulled out, your cup is still warm, and "
    "nothing here is waiting on an answer. Stay \u2014 the light will keep "
    "your seat."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
