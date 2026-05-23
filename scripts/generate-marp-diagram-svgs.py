#!/usr/bin/env python3
"""Convert ```text diagram blocks in module Marp files to SVG images."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from marp_svg_common import monospace_panel_svg, slugify

TEXT_FENCE_RE = re.compile(r"```text\n(.*?)```", re.DOTALL)
HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)


def _strip_frontmatter(text: str) -> str:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return text
    end = text.find("\n---\n", 3)
    if end == -1:
        return text
    return text[end + 5 :]


def _split_slides(body: str) -> list[str]:
    parts = re.split(r"\n---\n", body)
    return [part.strip("\n") for part in parts if part.strip("\n")]


def _join_slides(slides: list[str]) -> str:
    return "\n\n---\n\n".join(slides)


def process_module(path: Path, module_num: int) -> int:
    original = path.read_text(encoding="utf-8")
    if module_num == 1:
        return 0

    frontmatter = original[: original.find("\n---\n", 3) + 5] if original.startswith("---") else ""
    body = _strip_frontmatter(original)
    out_dir = path.parent / "assets" / f"module-{module_num:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)

    used_names: set[str] = set()
    converted = 0
    new_slides: list[str] = []

    for slide in _split_slides(body):
        heading_match = HEADING_RE.search(slide)
        heading = heading_match.group(1).strip() if heading_match else "Diagram"

        def repl(match: re.Match[str]) -> str:
            nonlocal converted
            block = match.group(1).rstrip("\n")
            lines = block.split("\n")
            base = slugify(heading)
            name = base
            suffix = 2
            while name in used_names:
                name = f"{base}-{suffix}"
                suffix += 1
            used_names.add(name)

            svg = monospace_panel_svg(lines)
            svg_path = out_dir / f"{name}.svg"
            svg_path.write_text(svg, encoding="utf-8")
            converted += 1
            return (
                f'<img src="assets/module-{module_num:02d}/{name}.svg" '
                f'alt="{heading.replace(chr(34), "&quot;")}" />'
            )

        new_slide = TEXT_FENCE_RE.sub(repl, slide)
        new_slides.append(new_slide)

    if converted == 0:
        return 0

    updated = frontmatter + "\n" + _join_slides(new_slides) + "\n"
    path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"{path.name}: converted {converted} diagram(s) → assets/module-{module_num:02d}/")
    return converted


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    slides_dir = repo / "slides"
    total = 0

    # Keep module-01 hand-crafted SVGs.
    gen01 = Path(__file__).resolve().parent / "generate-module-01-svgs.py"
    if gen01.exists():
        import importlib.util

        spec = importlib.util.spec_from_file_location("generate_module_01_svgs", gen01)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()
        print("Regenerated module-01 hand-crafted SVGs")

    for path in sorted(slides_dir.glob("module-*-marp.md")):
        num = int(path.stem.split("-")[1])
        total += process_module(path, num)

    print(f"Done. {total} diagram block(s) converted across modules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
