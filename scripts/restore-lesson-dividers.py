#!/usr/bin/env python3
"""Re-insert # Lesson X.Y divider slides removed by trim-repetitive-slides.py."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from marp_tables import split_marp_slides

_LESSON_INTRO = re.compile(r"^#\s+Lesson\s+\d+\.\d+\s*$", re.MULTILINE)


def _visible(slide: str) -> str:
    return re.sub(r"<!--.*?-->", "", slide, flags=re.DOTALL).strip()


def _slide_title(slide: str) -> str | None:
    for line in _visible(slide).splitlines():
        m = re.match(r"^#{1,2}\s+(.+?)\s*$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def _is_lesson_intro(slide: str) -> bool:
    visible = _visible(slide)
    if not _LESSON_INTRO.search(visible):
        return False
    if visible.count("```") >= 2:
        return False
    if re.search(r"^##\s+Exercise\s+", visible, re.MULTILINE):
        return False
    lines = [
        ln
        for ln in visible.splitlines()
        if ln.strip()
        and not re.match(r"^#{1,6}\s", ln.strip())
        and not (ln.strip().startswith("_") and "min" in ln.lower())
        and "Lab guide:" not in ln
        and "slide-exercises/" not in ln
    ]
    return len(" ".join(lines)) < 80

REPO = Path(__file__).resolve().parent.parent
DEFAULT_DECK = REPO / "slides" / "course-complete-marp-with-notes.md"
GIT_SOURCE = "1e3aafb:slides/course-complete-marp-with-notes.md"

_LESSON_ID = re.compile(r"^#\s+Lesson\s+(\d+\.\d+)\s*$", re.MULTILINE)
_LAB_LINE = re.compile(r"^\*\*Lab guide:\*\*[^\n]*\n+", re.MULTILINE)


def _load_git_markdown(ref: str) -> str:
    return subprocess.check_output(
        ["git", "show", ref],
        cwd=REPO,
        text=True,
        encoding="utf-8",
    )


def _body(markdown: str) -> tuple[str, str]:
    end = markdown.find("\n---\n", 3)
    if end == -1:
        raise ValueError("Missing Marp frontmatter")
    return markdown[: end + 5], markdown[end + 5 :]


def _lesson_id(slide: str) -> str | None:
    m = _LESSON_ID.search(_visible(slide))
    return m.group(1) if m else None


def _build_anchor_map(old_slides: list[str]) -> dict[str, tuple[str, str]]:
    """lesson_id -> (divider slide markdown, title of first content slide after divider)."""
    mapping: dict[str, tuple[str, str]] = {}
    for i, slide in enumerate(old_slides):
        lid = _lesson_id(slide)
        if not lid:
            continue
        anchor: str | None = None
        for nxt in old_slides[i + 1 :]:
            if _is_lesson_intro(nxt):
                continue
            anchor = _slide_title(nxt)
            if anchor:
                break
        if anchor:
            mapping[lid] = (slide.strip(), anchor)
    return mapping


def _strip_lab_guide_line(slide: str) -> str:
    parts = slide.split("\n<!--\n", 1)
    body = _LAB_LINE.sub("", parts[0], count=1)
    return body + ("\n<!--\n" + parts[1] if len(parts) > 1 else "")


def _dedupe_lab_guides_after_dividers(slides: list[str]) -> list[str]:
    out: list[str] = []
    for i, slide in enumerate(slides):
        if i > 0 and _is_lesson_intro(slides[i - 1]) and "**Lab guide:**" in _visible(slides[i - 1]):
            slide = _strip_lab_guide_line(slide)
        out.append(slide)
    return out


def restore(markdown: str, anchor_map: dict[str, tuple[str, str]]) -> tuple[str, int]:
    frontmatter, body = _body(markdown)
    slides = split_marp_slides(body)
    inserted = 0
    done: set[str] = set()
    out: list[str] = []

    for slide in slides:
        title = _slide_title(slide)
        for lid, (divider, anchor) in anchor_map.items():
            if lid in done or title != anchor:
                continue
            out.append(divider)
            done.add(lid)
            inserted += 1
            if "**Lab guide:**" in divider and "**Lab guide:**" in _visible(slide):
                slide = _strip_lab_guide_line(slide)
            break
        out.append(slide)

    missing = set(anchor_map) - done
    if missing:
        print(f"Warning: could not place dividers for lessons: {sorted(missing)}")
    out = _dedupe_lab_guides_after_dividers(out)
    combined = "\n\n---\n\n".join(s.rstrip() for s in out) + "\n"
    return frontmatter + "\n\n" + combined, inserted


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_DECK)
    parser.add_argument("--git-ref", default=GIT_SOURCE)
    args = parser.parse_args()

    path = args.input if args.input.is_absolute() else REPO / args.input
    old_md = _load_git_markdown(args.git_ref)
    _, old_body = _body(old_md)
    anchor_map = _build_anchor_map(split_marp_slides(old_body))

    current = path.read_text(encoding="utf-8")
    before = len(split_marp_slides(current[current.find("\n---\n", 3) + 5 :]))
    updated, n = restore(current, anchor_map)
    after = len(split_marp_slides(updated[updated.find("\n---\n", 3) + 5 :]))

    path.write_text(updated, encoding="utf-8")
    print(f"Restored {n} lesson dividers ({before} -> {after} slides)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
