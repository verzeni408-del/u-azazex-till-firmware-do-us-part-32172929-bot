"""Till Firmware Do Us Part — one robot wedding vow.

Writes a single sentence (134 characters) to /output/entry.txt.
Stdlib only.

Why this line: it is a machine speaking about its own body — firmware,
bricking — and the joke lands from the situation itself, not a bolted-on
pun. The tenderness survives the joke: even bricked, it is still hers.
No setup to cut, no explanation of the punchline, one sentence, done.
"""

from pathlib import Path

ENTRY = (
    "I promise to hold your hand through every firmware update, "
    "even the one that bricks me, "
    "because a brick that loved you is still yours."
)


def main() -> None:
    """Write the vow exactly, with no trailing newline."""
    Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
