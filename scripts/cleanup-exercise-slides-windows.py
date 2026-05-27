#!/usr/bin/env python3
"""Apply Windows cleanups to all slides in modules 5-10."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

from marp_tables import split_marp_slides

_spec = importlib.util.spec_from_file_location(
    "sync", Path(__file__).parent / "sync-exercise-steps-to-slides.py"
)
_sync = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_sync)

DECK = _sync.DECK
_CLEANUPS = _sync._CLEANUPS

_BASH_TO_PS = [
    (
        r"```bash\nexport CURSOR_ADMIN_API_KEY=.*?\n```",
        "```powershell\n"
        '$env:CURSOR_ADMIN_API_KEY = "cursor_admin_paste_here"\n'
        "curl.exe -s -u \"$($env:CURSOR_ADMIN_API_KEY):\" `\n"
        "  https://api.cursor.com/v1/teams/members\n"
        "```",
    ),
    (r"```bash\nagent\n", "```powershell\nagent\n"),
    (r"```bash\n", "```powershell\n"),
]


def main() -> None:
    text = DECK.read_text(encoding="utf-8")
    fm_end = text.find("\n---\n", 3) + 5
    frontmatter, body = text[:fm_end], text[fm_end:]
    slides = split_marp_slides(body)
    current: int | None = None
    out = []
    n = 0
    for slide in slides:
        hdr = re.search(r"Module\s+(\d+)", slide)
        if hdr:
            current = int(hdr.group(1))
        if current and 5 <= current <= 10:
            orig = slide
            for pat, repl in _CLEANUPS:
                slide = re.sub(pat, repl, slide)
            if "## Exercise" in slide:
                for pat, repl in _BASH_TO_PS:
                    slide = re.sub(pat, repl, slide, flags=re.DOTALL)
            if slide != orig:
                n += 1
        out.append(slide)
    DECK.write_text(
        frontmatter + "\n\n" + "\n\n---\n\n".join(s.rstrip() for s in out) + "\n",
        encoding="utf-8",
    )
    print(f"Cleaned {n} slides in modules 5-10")


if __name__ == "__main__":
    main()
