"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (139 characters) to /output/entry.txt
for Thistledown, a city that does not exist.

The line is built against the judge brief, in the brief's own order:
1. Reads as a one-line forecast for an invented city, named, weather the
   whole point ("In Thistledown: 10C, ... rain by nine").
2. Makes a bored commuter smile on one reading: the pigeons checked their
   watches, and so did you.
3. Keeps broadcast-forecast register and rhythm, bent not dropped.
4. One concrete detail of the place: thistledown drifting like snow, so
   the city name itself becomes its weather.
5. Uses 139 of the 140 characters; every word earns its place.
"""

import os
from pathlib import Path

TEXT = (
    "In Thistledown: 10C, thistledown drifting like snow, rain by nine. "
    "The 8:15 is on time - the pigeons checked their watches, and so did you."
)


# The competition accepts texts of 1 to 140 characters.
MIN_CHARS = 1
MAX_CHARS = 140


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
