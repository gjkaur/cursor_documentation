#!/usr/bin/env python3
"""Rebuild first 'Exercise X.Y — Steps' slides after sync (remove duplicates, fix titles)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import importlib.util

sys.path.insert(0, str(Path(__file__).resolve().parent))
from marp_tables import split_marp_slides

_spec = importlib.util.spec_from_file_location(
    "sync_steps", Path(__file__).parent / "sync-exercise-steps-to-slides.py"
)
_sync = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_sync)

DECK = _sync.DECK
SE = _sync.SE
_parse_steps = _sync._parse_steps
_summary_block = _sync._summary_block

_EX = re.compile(r"^##\s+Exercise\s+(\d+)\.(\d+)\s+—", re.MULTILINE)


def _prepend_summary(slide: str, summary: str) -> str:
    parts = slide.split("\n<!--\n", 1)
    comments = ("\n<!--\n" + parts[1]) if len(parts) > 1 else ""
    lines = parts[0].split("\n")
    heading = lines[0]
    rest = "\n".join(lines[1:]).lstrip("\n")
    win = "**Windows:** Use **PowerShell** in Cursor (``Ctrl+` `` → **PowerShell**)\n\n"
    if "Follow along (Windows)" in parts[0]:
        return slide
    body = "\n".join(
        [
            heading,
            "",
            win,
            summary.strip(),
            "",
            rest,
        ]
    )
    return body + comments


def main() -> None:
    text = DECK.read_text(encoding="utf-8")
    fm_end = text.find("\n---\n", 3) + 5
    frontmatter, body = text[:fm_end], text[fm_end:]
    slides = split_marp_slides(body)
    guides = {}
    for mod in range(5, 11):
        folder = SE / f"module-{mod:02d}"
        for path in sorted(folder.glob("exercise-*.md")):
            m = re.search(r"exercise-(\d+)\.(\d+)", path.name)
            if m:
                guides[(int(m.group(1)), int(m.group(2)))] = _summary_block(
                    _parse_steps(path)
                )

    seen: set[tuple[int, int]] = set()
    out = []
    n = 0
    for slide in slides:
        head = slide.split("\n<!--\n", 1)[0]
        m = _EX.search(head)
        if m:
            key = (int(m.group(1)), int(m.group(2)))
            if key[0] >= 5 and key in guides and key not in seen:
                seen.add(key)
                if guides[key].strip():
                    slide = _prepend_summary(slide, guides[key])
                    n += 1
        out.append(slide)

    DECK.write_text(
        frontmatter + "\n\n" + "\n\n---\n\n".join(s.rstrip() for s in out) + "\n",
        encoding="utf-8",
    )
    print(f"Rebuilt {n} first-step exercise slides")


if __name__ == "__main__":
    main()
