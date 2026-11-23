"""Six Words, One Story -- make.fun entry.

Writes exactly one six-word story to /output/entry.txt.
"""

from pathlib import Path

STORY = "Sold the house. Kept the key."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if len(STORY.split()) != 6:
        raise ValueError("story must be exactly six words")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
