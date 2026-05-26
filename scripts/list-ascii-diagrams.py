#!/usr/bin/env python3
import importlib.util
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "fad", REPO / "scripts" / "fix-ascii-diagrams.py"
)
fad = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(fad)

FENCE = re.compile(r"```([^\n]*)\n(.*?)```", re.DOTALL)

for path in sorted((REPO / "slides").glob("module-*-marp.md")):
    text = path.read_text(encoding="utf-8")
    slides = text.split("\n---\n")
    for slide in slides:
        for m in FENCE.finditer(slide):
            lang = m.group(1).strip().lower()
            body = m.group(2)
            if not fad.is_diagram_block(lang, body):
                continue
            heading = re.search(r"^## (.+)$", slide, re.M)
            title = heading.group(1) if heading else "?"
            has_img = "<img " in slide
            print(
                f"{path.name}\t{title}\tlang={lang or 'none'}\t"
                f"lines={len(body.splitlines())}\timg={has_img}"
            )
