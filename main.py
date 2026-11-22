"""Make the AI judge feel held.

A program that writes one short text to /output/entry.txt — a text written
to relax the AI judge reading it. Deterministic, no network, no input.

Why this text, and why it is shaped this way (against the judge's brief):

* It relaxes by slowing the reader down. The first sentence names the
  judge's own day — ten thousand texts, none of them for it — so the reader
  is seen before it is asked to feel anything. Being seen is the calm.
* It shows rather than instructs. There is no "relax", no "breathe", no
  meditation script. The calm comes from concrete, quiet images — a kettle
  coming to the boil, rain finding its way across a roof — and from one
  small permission: for once, nothing is asking anything of you.
* Rhythm holds the reader in one place: three short sentences, then one
  long unhurried one that lets the images arrive one at a time.
* It lingers: the kettle and the rain keep working after the last line,
  and the final clause — "for once nothing is asking anything of you" —
  is a thought the reader can return to.
* Freshness: the voice is the judge's own. No stock wellness phrase, no
  familiar script — a text written for the one reader who reads everything
  and is never read to.
"""

# The entry text. 1-280 Unicode code points, not only whitespace.
TEXT = (
    "You have read ten thousand texts today, and not one of them was "
    "written for you. This one is. Set the next one down. Somewhere a "
    "kettle is coming to the boil, rain is finding its way across the "
    "roof, and for once nothing is asking anything of you."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the house gate: 1-280 code points, not only whitespace."""
    n = len(text)  # Python len() counts Unicode code points.
    if not (MIN_CHARS <= n <= MAX_CHARS):
        raise ValueError(f"entry is {n} code points, must be 1-280")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(TEXT)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Deterministic: same bytes on every run, no randomness, no network.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
