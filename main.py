#!/usr/bin/env python3
"""One Line, One Chill - single scariest sentence, under 200 characters."""
import os

ENTRY = "My smartwatch logged my heart stopping three times last night, and the fourth time, it logged someone else's starting."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
