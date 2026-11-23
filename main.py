"""Dad Joke Showdown entry.

Writes a single dad joke to /output/entry.txt. The joke is the whole entry.
"""

import os

JOKE = "I told my dad I was forming a band called 1023 MB. He just sighed, 'Son, you still haven't got a gig.'"


def main():
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(JOKE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
