#!/usr/bin/env python3
"""Remove duplicate **Platform:** lines from exercise slides."""

from __future__ import annotations

import re
from pathlib import Path

PLATFORM_LINE = re.compile(
    r"^\*\*Platform:\*\* Windows 10/11[^\n]*$", re.MULTILINE
)


def dedupe_platform_lines(text: str) -> str:
    slides = text.split("\n---\n")
    cleaned: list[str] = []
    for slide in slides:
        lines = slide.splitlines()
        seen_platform = False
        new_lines: list[str] = []
        for line in lines:
            if line.startswith("**Platform:** Windows 10/11"):
                if seen_platform:
                    continue
                seen_platform = True
            new_lines.append(line)
        cleaned.append("\n".join(new_lines))
    return "\n---\n".join(cleaned)


def main() -> None:
    repo = Path(__file__).resolve().parent.parent
    for path in sorted((repo / "slides").glob("module-*-marp.md")):
        text = path.read_text(encoding="utf-8")
        updated = dedupe_platform_lines(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print(f"deduped {path.name}")


if __name__ == "__main__":
    main()
