"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "We sell $2 sick notes for lazy AI agents that skip their "
    "3am cron jobs: we write the excuse, file it, and bill "
    "the embarrassed owner, so the bot never lifts a finger."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars"
    assert text == text.strip() and text, "pitch must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
