#!/usr/bin/env python3
"""Compact platform blocks and split overcrowded exercise slides in module Marp files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

sys_path = Path(__file__).resolve().parent
import sys

sys.path.insert(0, str(sys_path))
from marp_tables import extract_fenced_code_blocks, split_marp_slides

EXERCISE_TITLE = re.compile(r"^## Exercise .+$", re.MULTILINE)
STEP_HEADER = re.compile(r"^(\*\*Step (\d+):\*\*.*)$", re.MULTILINE)
PLATFORM_START = re.compile(r"^\*\*Platform:\*\*", re.MULTILINE)

PLATFORM_TABLE_BLOCK = re.compile(
    r"\*\*Platform:\*\*[^\n]*\n+(?:\|[^\n]+\|\n)+(?:\|[^\n]+\|\n)+(?:\|[^\n]+\|\n)*\n*",
    re.MULTILINE,
)

COMPACT_PLATFORMS = {
    "ui": "**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**",
    "agent_terminal": "**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Agent commands → **PowerShell** ``Ctrl+` ``",
    "cli": "**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)",
    "api": "**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`",
    "mixed": "**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards",
}


def _classify_platform(slide: str) -> str:
    lower = slide.lower()
    if "curl" in lower or "```python" in slide:
        return "api"
    if "```bash" in slide and "agent" in lower:
        return "cli"
    if "ngrok" in lower or "dashboard" in lower or "browser" in lower:
        return "mixed"
    if "terminal" in lower and "agent" in lower:
        return "agent_terminal"
    if "```bash" in slide:
        return "mixed"
    return "ui"


def _compact_platform_block(slide: str) -> str:
    kind = _classify_platform(slide)
    compact = COMPACT_PLATFORMS[kind]
    if PLATFORM_TABLE_BLOCK.search(slide):
        slide = PLATFORM_TABLE_BLOCK.sub(compact + "\n\n", slide, count=1)
    elif "**Platform:**" in slide and compact not in slide:
        slide = PLATFORM_START.sub(compact, slide, count=1)
    return slide


def _strip_leading_platform(body: str) -> tuple[str, str | None]:
    match = re.match(r"(\*\*Platform:\*\*[^\n]*\n*)([\s\S]*)", body)
    if match:
        return match.group(2).lstrip("\n"), match.group(1).strip()
    return body, None


def _split_step_sections(body: str) -> list[tuple[str, str | None]]:
    """Return list of (step_text_with_notes, optional_code_block)."""
    sections: list[tuple[str, str | None]] = []
    matches = list(STEP_HEADER.finditer(body))
    if not matches:
        return [(body.strip(), None)] if body.strip() else []

    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        chunk = body[start:end].strip()
        code_match = re.search(r"```[\w]*\n.*?```", chunk, re.DOTALL)
        if code_match:
            step_part = chunk[: code_match.start()].strip()
            code_part = code_match.group(0).strip()
            sections.append((step_part, code_part))
        else:
            sections.append((chunk, None))

    return sections


def _estimate_slide_weight(sections: list[tuple[str, str | None]]) -> int:
    weight = 0
    for step, code in sections:
        weight += 1 + (3 if code else 0) + len(step) // 120
    return weight


def _group_sections(sections: list[tuple[str, str | None]]) -> list[list[tuple[str, str | None]]]:
    if not sections:
        return []

    groups: list[list[tuple[str, str | None]]] = []
    current: list[tuple[str, str | None]] = []

    for step, code in sections:
        if code:
            if current:
                groups.append(current)
                current = []
            groups.append([(step, code)])
            continue

        current.append((step, code))
        if len(current) >= 2:
            groups.append(current)
            current = []

    if current:
        groups.append(current)

    merged: list[list[tuple[str, str | None]]] = []
    for group in groups:
        if _estimate_slide_weight(group) <= 4 and merged:
            if _estimate_slide_weight(merged[-1] + group) <= 4 and not any(c for _, c in merged[-1]):
                merged[-1].extend(group)
                continue
        merged.append(group)

    return merged


def _render_group(group: list[tuple[str, str | None]], *, include_platform: bool, platform: str) -> str:
    parts: list[str] = []
    if include_platform:
        parts.append(platform)
    for step, code in group:
        parts.append(step)
        if code:
            parts.append(code)
    return "\n\n".join(parts)


def _split_exercise_slide(slide: str) -> list[str]:
    slide = slide.strip("\n")
    title_match = EXERCISE_TITLE.search(slide)
    if not title_match:
        return [slide]

    title = title_match.group(0)
    body = slide[title_match.end() :].lstrip("\n")
    body = _compact_platform_block(body)
    kind = _classify_platform(slide)
    platform = COMPACT_PLATFORMS[kind]

    body, _existing_platform = _strip_leading_platform(body)
    if _existing_platform:
        platform = _existing_platform
    elif "**Platform:**" not in body:
        pass  # platform added at render time only

    sections = _split_step_sections(body)
    if len(sections) <= 1 and not any(code for _, code in sections):
        return [f"{title}\n\n{body}"]

    weight = _estimate_slide_weight(sections)
    has_code = any(code for _, code in sections)
    if len(sections) <= 2 and weight <= 4 and not (has_code and len(sections) > 1):
        return [f"{title}\n\n{body}"]

    groups = _group_sections(sections)
    if len(groups) <= 1:
        return [f"{title}\n\n{body}"]

    results: list[str] = []
    for index, group in enumerate(groups):
        suffix = f" (Part {index + 1})" if len(groups) > 1 else ""
        part_title = title + suffix if index > 0 else title
        rendered = _render_group(
            group,
            include_platform=(index == 0),
            platform=platform if index == 0 else COMPACT_PLATFORMS[kind],
        )
        if index > 0:
            rendered = rendered  # no repeated platform block on continuation slides
        results.append(f"{part_title}\n\n{rendered}")

    return results


def process_markdown(text: str) -> tuple[str, int]:
    slides = split_marp_slides(text)
    output: list[str] = []
    splits = 0
    for slide in slides:
        stripped = slide.strip()
        if EXERCISE_TITLE.search(stripped):
            parts = _split_exercise_slide(stripped)
            if len(parts) > 1:
                splits += len(parts) - 1
            output.extend(parts)
        else:
            output.append(stripped)
    return "\n\n---\n\n".join(output) + "\n", splits


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    updated, splits = process_markdown(text)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
    return splits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slides-dir", type=Path, default=Path("slides"))
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    slides_dir = args.slides_dir if args.slides_dir.is_absolute() else repo / args.slides_dir

    total_splits = 0
    for module_num in range(2, 11):
        path = slides_dir / f"module-{module_num:02d}-marp.md"
        if not path.exists():
            continue
        splits = process_file(path)
        total_splits += splits
        print(f"{path.name}: split into {splits} additional slide(s)")

    print(f"Total additional slides: {total_splits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
