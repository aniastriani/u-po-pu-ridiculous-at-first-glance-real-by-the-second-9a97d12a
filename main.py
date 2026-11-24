"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (max 200 chars) pitching a bizarre startup idea
that sounds absurd but would actually sell, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library, deterministic.

The pitch works the brief's turn: bathtub rental sounds like a joke,
then the second look lands — idle tubs are an unused asset in every
city, and the buyers (remote workers) already pay for stranger
wellness rituals, from saunas to float tanks.
"""

import os

SENTENCE = (
    "We rent strangers' spare bathtubs by the hour to remote workers "
    "who think best while soaking, because every city has thousands "
    "of idle tubs and one very stressed laptop class."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
