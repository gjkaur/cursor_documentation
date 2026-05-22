#!/usr/bin/env python3
"""Build a single Marp deck combining all training modules with course intro slides."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from marp_tables import split_marp_slides

MODULES = [
    (1, "Mental Models for AI-Assisted Development", "Day 1", "Foundations", "~60 min"),
    (2, "Cursor Editor Essentials", "Day 1", "Hands-On", "~90 min"),
    (3, "Agent Modes and Tools", "Day 1", "Hands-On + Concept", "~60 min"),
    (4, "Customizing Cursor for Your Team", "Day 1", "Hands-On + Walkthrough", "~60 min"),
    (5, "Cursor CLI and Local Automation", "Day 1", "Hands-On", "~60 min"),
    (6, "Cloud Agents in the UI", "Day 2", "Hands-On + Demonstration", "~90 min"),
    (7, "Cursor API Foundations", "Day 2", "Concept + Hands-On", "~60 min"),
    (8, "Cloud Agents API and Webhooks", "Day 2", "Hands-On", "~60 min"),
    (9, "Admin and Analytics APIs", "Day 2", "Hands-On + Demonstrations", "~75 min"),
    (10, "AI Code Tracking and Reporting", "Day 2", "Hands-On + Take-Home", "~20 min"),
]

FRONTMATTER = """---
marp: true
theme: flat-gaia
paginate: true
header: 'Cursor Training Program — Complete Course'
footer: 'Springpeople · Cursor Training'
---"""


def _strip_frontmatter(markdown: str) -> str:
    text = markdown.lstrip("\ufeff")
    if not text.startswith("---"):
        return text
    end = text.find("\n---\n", 3)
    if end == -1:
        return text
    return text[end + 5 :]


def _is_up_next_slide(slide_md: str) -> bool:
    return bool(re.search(r"^#\s+Up Next:\s+Module\s+\d+", slide_md.strip(), re.MULTILINE))


def _module_slides(slides_dir: Path, module_num: int, *, skip_up_next: bool = True) -> list[str]:
    path = slides_dir / f"module-{module_num:02d}-marp.md"
    if not path.exists():
        raise FileNotFoundError(path)
    body = _strip_frontmatter(path.read_text(encoding="utf-8"))
    slides = split_marp_slides(body)
    if skip_up_next and module_num < 10:
        slides = [slide for slide in slides if not _is_up_next_slide(slide)]
    return slides


def _intro_slides() -> list[str]:
    day1_rows = "\n".join(
        f"| **{num}** | {title} | {focus} | {duration} |"
        for num, title, day, focus, duration in MODULES
        if day == "Day 1"
    )
    day2_rows = "\n".join(
        f"| **{num}** | {title} | {focus} | {duration} |"
        for num, title, day, focus, duration in MODULES
        if day == "Day 2"
    )
    overview_rows = "\n".join(
        f"| **{num}** | {title} | {day} | {duration} |" for num, title, day, _, duration in MODULES
    )

    title_slide = """<!-- _class: lead -->

# Cursor Training Program

## AI-Assisted Development with Cursor

Springpeople · 2-day instructor-led course · Modules 1–10
"""

    agenda_slide = f"""## Course Agenda

| Module | Title | Day | Duration |
|--------|-------|-----|----------|
{overview_rows}

**Total:** ~11.5 hours across 2 days (hands-on labs + demonstrations)
"""

    day1_slide = f"""## Day 1 — Foundations & Editor Workflows

| Module | Title | Focus | Duration |
|--------|-------|-------|----------|
{day1_rows}

Concept blocks, hands-on exercises, team customization, and CLI automation.
"""

    day2_slide = f"""## Day 2 — Cloud Agents, APIs & Analytics

| Module | Title | Focus | Duration |
|--------|-------|-------|----------|
{day2_rows}

Cloud agents, programmatic APIs, admin analytics, and AI code tracking.
"""

    return [title_slide, agenda_slide, day1_slide, day2_slide]


def _day_break_slide(day: str, subtitle: str) -> str:
    return f"""<!-- _class: lead -->
<!-- _footer: 'Cursor Training Program · {day}' -->

# {day}

## {subtitle}

Cursor Training Program · Complete Course
"""


def build_course_markdown(slides_dir: Path) -> str:
    parts = list(_intro_slides())
    previous_day: str | None = None

    for num, title, day, focus, duration in MODULES:
        if day != previous_day:
            if day == "Day 2":
                parts.append(
                    _day_break_slide(
                        "Day 2",
                        "Cloud Agents, APIs & Analytics",
                    )
                )
            previous_day = day

        module_slides = _module_slides(slides_dir, num)
        if not module_slides:
            continue

        header = f"Module {num} — {title}"
        footer = f"Cursor Training Program · {day}"
        module_slides[0] = (
            f"<!-- _header: '{header}' -->\n"
            f"<!-- _footer: '{footer}' -->\n\n"
            f"{module_slides[0].lstrip()}"
        )
        parts.extend(module_slides)

    return FRONTMATTER.rstrip() + "\n\n---\n\n" + "\n\n---\n\n".join(
        part.strip("\n") for part in parts if part.strip()
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("slides/course-complete-marp.md"),
        help="Output path for the combined Marp markdown",
    )
    parser.add_argument(
        "--slides-dir",
        type=Path,
        default=Path("slides"),
        help="Directory containing module-*-marp.md sources",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    slides_dir = args.slides_dir if args.slides_dir.is_absolute() else repo_root / args.slides_dir
    output = args.output if args.output.is_absolute() else repo_root / args.output

    markdown = build_course_markdown(slides_dir)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")

    slide_count = len(split_marp_slides(markdown))
    print(f"Wrote {output}")
    print(f"Slides: {slide_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
