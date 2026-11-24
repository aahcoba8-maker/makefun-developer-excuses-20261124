"""Developer Excuses — one-line production excuse entry for make.fun.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when the variable is unset), and prints it to stdout. Stdlib only.
"""

import os

ENTRY = "I didn't break production — I just gave the bug a bigger audience."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print("chars:", len(ENTRY))


if __name__ == "__main__":
    main()
