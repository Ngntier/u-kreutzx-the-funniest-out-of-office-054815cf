#!/usr/bin/env python3
"""Write the funniest out-of-office auto-reply to /output/entry.txt.

Single line, no trailing newline, pure stdlib, deterministic.
"""
import os

LINE = (
    "I'm out until Monday. My inbox is run by my cat, who has deleted "
    "two meetings, approved his own promotion, and eaten the Wi-Fi password."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space, and a single line.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-140")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("line must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
