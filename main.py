"""Write a short, slow text to /output/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel held"
(https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600).

Deterministic, standard library only. The text is embedded below and
written verbatim, UTF-8, with no trailing newline. The program checks
its own output against the competition gate (1-280 Unicode code points,
not only whitespace) and refuses to write an invalid entry.
"""

import os

TEXT = (
    "Low afternoon light comes through the kitchen window and settles "
    "across the table like it owns the place. The house has finished "
    "its chores. Your chair is pulled out, your cup is still warm, and "
    "nothing here is waiting on an answer. Stay \u2014 the light will keep "
    "your seat."
)

MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Refuse to write an entry the competition gate would reject."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(f"entry is {n} characters, outside 1-280")
    if not text.strip():
        raise SystemExit("entry is only whitespace")


def main() -> None:
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
