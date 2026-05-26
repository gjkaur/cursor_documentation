#!/usr/bin/env python3
"""Add lab guide links to lesson lead slides in module-*-marp.md."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SLIDES = REPO / "slides"

spec = importlib.util.spec_from_file_location(
    "gse", REPO / "scripts" / "generate-slide-exercises.py"
)
gse = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(gse)

EXERCISE_META = gse.EXERCISE_META
slugify = gse.slugify

LAB_LINE = (
    '**Lab guide:** [`Exercise {m}.{n}](../slide-exercises/module-{m:02d}/'
    "exercise-{m}.{n}-{slug}.md)"
)


def inject_module(module_num: int) -> int:
    path = SLIDES / f"module-{module_num:02d}-marp.md"
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8")
    original = text
    count = 0

    for (m, n), meta in EXERCISE_META.items():
        if m != module_num:
            continue
        slug = slugify(meta["title"])
        link = LAB_LINE.format(m=m, n=n, slug=slug)
        if link in text:
            continue
        pattern = (
            rf"(<!-- _class: lead -->\s*\n\s*\n# Lesson {m}\.{n}\s*\n\s*\n"
            rf"## [^\n]+\s*\n\s*\n\*[^\n]+\*)"
        )
        replacement = rf"\1\n\n{link}"
        new_text, n_repl = re.subn(pattern, replacement, text, count=1)
        if n_repl:
            text = new_text
            count += 1

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"Updated {path.name}: {count} lab link(s)")
    return count


def main() -> int:
    total = sum(inject_module(n) for n in range(2, 11))
    print(f"Done. Injected {total} lab guide link(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
