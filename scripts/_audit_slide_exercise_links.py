#!/usr/bin/env python3
"""Audit slide-exercises for broken image paths, links, and missing local files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EX = ROOT / "slide-exercises"

issues: list[tuple[str, str, str]] = []

link_re = re.compile(r"\]\(([^)]+)\)")

for md in sorted(EX.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    rel_md = str(md.relative_to(ROOT))

    for m in re.finditer(r'src="([^"]+)"', text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "//")):
            continue
        p = (md.parent / target).resolve()
        if not p.exists():
            issues.append(("img", rel_md, target))

    for m in link_re.finditer(text):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        p = (md.parent / target.split("#")[0]).resolve()
        if not p.exists():
            issues.append(("link", rel_md, target))

    lower = text.lower()
    if "in this folder" in lower or "same directory as this doc" in lower:
        for fname in ("calculator.c", "test_calculator.c", "math_utils.c", "math_utils.h"):
            if fname not in text:
                continue
            if (md.parent / fname).exists():
                continue
            if "core-exercises/" in text:
                continue
            issues.append(("missing-local", rel_md, fname))

for kind, file, detail in issues:
    print(f"{kind}\t{file}\t{detail}")
print("---")
print(f"Total issues: {len(issues)}")
