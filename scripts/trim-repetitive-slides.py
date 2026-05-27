#!/usr/bin/env python3
"""Remove repetitive boilerplate slides from the combined course Marp deck."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from marp_tables import split_marp_slides

REPO = Path(__file__).resolve().parent.parent
DEFAULT_DECK = REPO / "slides" / "course-complete-marp-with-notes.md"

# Visible slide title (first ## or # heading after stripping Marp directives)
_HEADING = re.compile(r"^#{1,2}\s+(.+?)\s*$", re.MULTILINE)
_LESSON_INTRO = re.compile(r"^#\s+Lesson\s+\d+\.\d+\s*$", re.MULTILINE)
_LAB_GUIDE = re.compile(
    r"\*\*Lab guide:\*\*\s*(\[`[^`]+`\]\([^)\n]*slide-exercises[^\s)\n]+(?:\.md)?\)?)",
    re.IGNORECASE,
)


def _visible(slide: str) -> str:
    text = re.sub(r"<!--.*?-->", "", slide, flags=re.DOTALL)
    text = re.sub(r"^<!--.*?-->$", "", text, flags=re.MULTILINE)
    return text.strip()


def _slide_title(slide: str) -> str | None:
    visible = _visible(slide)
    for line in visible.splitlines():
        m = re.match(r"^#{1,2}\s+(.+?)\s*$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def _is_lesson_intro(slide: str) -> bool:
    visible = _visible(slide)
    if not _LESSON_INTRO.search(visible):
        return False
    # Keep slides that are real exercise walkthroughs (many steps / code)
    if visible.count("```") >= 2:
        return False
    if re.search(r"^##\s+Exercise\s+", visible, re.MULTILINE):
        return False
    lines = [
        ln
        for ln in visible.splitlines()
        if ln.strip()
        and not re.match(r"^#{1,6}\s", ln.strip())
        and not re.match(r"^[_*].*[_*]\s*$", ln.strip())
        and "Lab guide:" not in ln
        and "slide-exercises/" not in ln
    ]
    body = " ".join(lines)
    return len(body) < 80


def should_remove(slide: str, module_num: int | None) -> tuple[bool, str]:
    title = _slide_title(slide)
    if title is None:
        return False, ""

    if title in (
        "Day 1 — Foundations & Editor Workflows",
        "Day 2 — Cloud Agents, APIs & Analytics",
    ):
        return True, "duplicate of course agenda"

    if title == "Agenda" and module_num is not None and module_num >= 2:
        return True, "duplicates module overview lesson list"

    if title == "Learning Objectives" and module_num is not None and module_num >= 2:
        return True, "covered in module overview goal + labs"

    if title == "Module Summary" and module_num is not None and module_num >= 2:
        return True, "repeats agenda / lesson titles"

    if title == "Quick Reference Card":
        return True, "per-module QR; assets remain in slides/assets/"

    if title == "Learning Objectives" and module_num == 1:
        return True, "objectives align with module goal table"

    if title == "Module Summary" and module_num == 1:
        return True, "recap of lessons just taught"

    return False, ""


def _extract_lab_guide(slide: str) -> str | None:
    m = _LAB_GUIDE.search(slide)
    return m.group(1) if m else None


def _agenda_table(slide: str) -> str | None:
    visible = _visible(slide)
    if _slide_title(slide) != "Agenda":
        return None
    lines: list[str] = []
    in_table = False
    for line in visible.splitlines():
        if line.strip().startswith("|"):
            in_table = True
            lines.append(line)
        elif in_table:
            break
    return "\n".join(lines) if lines else None


def _append_agenda_to_overview(overview: str, table: str) -> str:
    if table in overview:
        return overview
    parts = overview.split("\n<!--\n", 1)
    body = parts[0].rstrip() + "\n\n### Lessons\n\n" + table + "\n"
    return body + ("\n<!--\n" + parts[1] if len(parts) > 1 else "")


def _inject_lab_guide(slide: str, link_md: str) -> str:
    if "slide-exercises/" in _visible(slide):
        return slide
    note = f"**Lab guide:** {link_md}\n\n"
    parts = slide.split("\n<!--\n", 1)
    body = parts[0].rstrip()
    rest = ("\n<!--\n" + parts[1]) if len(parts) > 1 else ""
    lines = body.split("\n")
    insert_at = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("#"):
            insert_at = i + 1
            while insert_at < len(lines) and not lines[insert_at].strip():
                insert_at += 1
            break
    lines.insert(insert_at, note.rstrip())
    return "\n".join(lines) + rest


def trim_deck(markdown: str) -> tuple[str, list[str]]:
    if not markdown.startswith("---"):
        raise ValueError("Expected Marp frontmatter")

    end = markdown.find("\n---\n", 3)
    if end == -1:
        raise ValueError("Invalid frontmatter")

    frontmatter = markdown[: end + 5]
    body = markdown[end + 5 :]
    slides = split_marp_slides(body)

    current_module: int | None = None
    kept: list[str] = []
    removed: list[str] = []
    pending_lab: str | None = None

    for slide in slides:
        hdr = re.search(r"<!--\s*_header:\s*['\"]Module\s+(\d+)", slide)
        if hdr:
            current_module = int(hdr.group(1))
        if current_module is None:
            m = re.search(r"Module\s+(\d+)", slide)
            if m:
                current_module = int(m.group(1))

        drop, reason = should_remove(slide, current_module)
        title = _slide_title(slide) or "(untitled)"
        if drop:
            removed.append(f"  - {title}: {reason}")
            if lab := _extract_lab_guide(slide):
                pending_lab = lab
            if reason.startswith("duplicates module overview") and kept:
                table = _agenda_table(slide)
                if table and _slide_title(kept[-1]) == "Module Overview":
                    kept[-1] = _append_agenda_to_overview(kept[-1], table)
        else:
            if pending_lab:
                slide = _inject_lab_guide(slide, pending_lab)
                pending_lab = None
            kept.append(slide)

    out = frontmatter + "\n\n" + "\n\n---\n\n".join(s.rstrip() for s in kept) + "\n"
    return out, removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_DECK)
    parser.add_argument("-o", "--output", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    path = args.input if args.input.is_absolute() else REPO / args.input
    text = path.read_text(encoding="utf-8")
    body_start = text.find("\n---\n", 3) + 5
    before = len(split_marp_slides(text[body_start:]))
    trimmed, removed = trim_deck(text)
    after = len(split_marp_slides(trimmed[trimmed.find("\n---\n", 3) + 5 :]))

    print(f"Slides: {before} -> {after} (removed {before - after})")
    for line in removed:
        print(line)

    if args.dry_run:
        return 0

    out = args.output or path
    if not out.is_absolute():
        out = REPO / out
    out.write_text(trimmed, encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
