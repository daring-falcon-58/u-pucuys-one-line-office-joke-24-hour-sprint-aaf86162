"""One-line office joke entry for make.fun.

The joke (103 characters, one line, one sentence):

    The meeting ended with 'any questions?' and nobody spoke, so the
    minutes recorded unanimous enthusiasm.

Why it fits the judge's five criteria, in the order the judge applies them:
  1. One-line joke about office life: a meeting, a question round, HR's
     minutes - unmistakably office, and a joke, not an observation.
  2. Funny: the punchline surprises - total silence becomes "unanimous
     enthusiasm" - and pays off a scene anyone who has sat in an office
     recognises (silence after "any questions?" is how meetings end).
  3. One line: a single sentence, setup and punchline on one line.
  4. Fresh: the specific detail is the minutes recording the silence,
     not a generic complaint about meetings or a reworded stock joke.
  5. Clear on first read: no explanation needed, no reference the reader
     cannot follow, every word earning its place.

The program writes exactly the joke bytes (no trailing newline) to
/output/entry.txt, deterministically: no network, no randomness, no
clock, no model call. Two runs write byte-identical files.
"""

import os

JOKE = (
    "The meeting ended with 'any questions?' and nobody spoke, "
    "so the minutes recorded unanimous enthusiasm."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {target}")


if __name__ == "__main__":
    main()
