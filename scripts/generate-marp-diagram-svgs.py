#!/usr/bin/env python3
"""Convert ASCII / reference-panel code fences in module Marp files to SVG images."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from marp_svg_common import monospace_panel_svg, slugify

FENCE_RE = re.compile(r"```([^\n]*)\n(.*?)```", re.DOTALL)
HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)

PROMPT_PREFIXES = (
    "explain ",
    "change ",
    "based on",
    "run ",
    "go to ",
    "what ",
    "give me",
    "add ",
    "use ",
    "compare ",
    "scan for",
    "spawn ",
    "check whether",
    "now open",
    "on that same",
    "the login",
    "save this",
    "that change",
    "use jwt",
    "install the",
    "fix the",
    "create an ascii",
    "repository:",
    "prompt:",
    "command:",
    "generate:\n1.",
)


def _load_fix_ascii():
    path = Path(__file__).resolve().parent / "fix-ascii-diagrams.py"
    spec = importlib.util.spec_from_file_location("fix_ascii_diagrams", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


_FIX = _load_fix_ascii()


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


def _is_agent_prompt(slide: str, body: str) -> bool:
    text = body.strip()
    lower = text.lower()
    if not text:
        return True
    if lower.startswith(PROMPT_PREFIXES):
        return True
    if "**where:**" in slide.lower() and "agent panel" in slide.lower():
        if not lower.startswith(
            ("endpoints", "basic", "active (", "→", "boundaries:", "main agent combines")
        ):
            if len(text.splitlines()) <= 10 and "http" in lower:
                return True
    if lower.startswith("user:") or lower.startswith("agent:"):
        return True
    if re.match(r"^(never|before changes|after changes|always|python function)", lower):
        return True
    return False


def should_convert_block(heading: str, slide: str, lang: str, body: str) -> bool:
    if _is_agent_prompt(slide, body):
        return False

    h = heading.lower()
    b = body.strip()
    bl = b.lower()

    if h == "quick reference card":
        return True
    if h == "cloud agent dashboard":
        return True
    if "subagents in action" in h and "→ subagent" in bl:
        return True
    if bl.startswith("boundaries:"):
        return True
    if lang == "text":
        return True
    if _FIX.is_diagram_block(lang, body):
        return True
    if bl.startswith(("endpoints:", "basic:", "key metrics:", "deploy:")):
        return True
    return False


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
            lang = match.group(1).strip().lower()
            block = match.group(2).rstrip("\n")
            if not should_convert_block(heading, slide, lang, block):
                return match.group(0)

            lines = block.split("\n")
            base = slugify(heading)
            if h := heading.lower():
                if h == "quick reference card":
                    base = "quick-reference-card"
                elif h == "cloud agent dashboard":
                    base = "cloud-agent-dashboard"
                elif "subagents in action" in h:
                    base = "walkthrough-subagents-parallel"

            name = base
            suffix = 2
            while name in used_names:
                name = f"{base}-{suffix}"
                suffix += 1
            used_names.add(name)

            max_height = 460 if "fit-xs" in slide or "fit-sm" in slide else 500
            svg = monospace_panel_svg(lines, max_panel_height=max_height)
            svg_path = out_dir / f"{name}.svg"
            svg_path.write_text(svg, encoding="utf-8")
            converted += 1
            alt = heading.replace('"', "&quot;")
            return (
                f'<img src="assets/module-{module_num:02d}/{name}.svg" '
                f'alt="{alt}" />'
            )

        new_slide = FENCE_RE.sub(repl, slide)
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

    gen01 = Path(__file__).resolve().parent / "generate-module-01-svgs.py"
    if gen01.exists():
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
