#!/usr/bin/env python3
"""Tag dense Marp slides with fit-* classes so the theme can shrink body text only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from marp_tables import extract_fenced_code_blocks, extract_markdown_tables, split_marp_slides

FIT_CLASSES = ("fit-xs", "fit-sm", "fit-md")
CLASS_RE = re.compile(r"<!--\s*_class:\s*([^>]+?)\s*-->")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)|<img\b", re.I)

# Thresholds tuned for 32px default body — tag slides before they overflow.
THRESHOLD_MD = 72
THRESHOLD_SM = 98
THRESHOLD_XS = 124


def _strip_directives(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return text


def score_slide(slide: str) -> int:
    """Heuristic overflow score — higher means more likely to clip at default fonts."""
    body = _strip_directives(slide)
    score = 0

    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# "):
            score += 14
        elif stripped.startswith("## "):
            score += 11
        elif stripped.startswith("### "):
            score += 8
        elif stripped.startswith("|"):
            continue
        elif stripped.startswith(">"):
            score += 16
        elif stripped.startswith("- ") or stripped.startswith("* "):
            score += 9
        elif re.match(r"^\d+\.\s", stripped):
            score += 9
        elif stripped.startswith("```"):
            continue
        else:
            score += max(6, len(stripped) // 45)

    for table in extract_markdown_tables(slide):
        for row in table:
            score += 11
            score += sum(max(1, len(cell) // 35) for cell in row)

    for block in extract_fenced_code_blocks(slide):
        lines = [ln for ln in block.splitlines() if ln.strip()]
        score += len(lines) * 9
        score += len(block) // 55

    image_count = len(IMG_RE.findall(slide))
    score += image_count * 72
    if image_count and score > 40:
        score += 24

    return score


def fit_class_for_score(score: int) -> str | None:
    if score >= THRESHOLD_XS:
        return "fit-xs"
    if score >= THRESHOLD_SM:
        return "fit-sm"
    if score >= THRESHOLD_MD:
        return "fit-md"
    return None


def _clean_class_list(class_str: str) -> list[str]:
    return [part for part in class_str.split() if part and part not in FIT_CLASSES]


def apply_fit_class(slide: str, fit: str | None) -> str:
    match = CLASS_RE.search(slide)
    if match:
        classes = _clean_class_list(match.group(1).strip())
        if fit:
            classes.append(fit)
        replacement = f"<!-- _class: {' '.join(classes)} -->" if classes else ""
        if replacement:
            return CLASS_RE.sub(replacement, slide, count=1)
        return CLASS_RE.sub("", slide, count=1).lstrip("\n")

    if not fit:
        return slide
    directive = f"<!-- _class: {fit} -->\n\n"
    return directive + slide.lstrip("\n")


def process_markdown(markdown: str) -> tuple[str, list[tuple[int, int, str | None]]]:
    slides = split_marp_slides(markdown)
    report: list[tuple[int, int, str | None]] = []
    updated_slides: list[str] = []

    for index, slide in enumerate(slides, start=1):
        score = score_slide(slide)
        fit = fit_class_for_score(score)
        report.append((index, score, fit))
        updated_slides.append(apply_fit_class(slide, fit))

    combined = "\n\n---\n\n".join(updated_slides) + "\n"
    if markdown.startswith("---"):
        end = markdown.find("\n---\n", 3)
        if end != -1:
            combined = markdown[: end + 5] + combined

    return combined, report


def process_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    updated, report = process_markdown(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
    return sum(1 for _, _, fit in report if fit)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Marp markdown files (default: all module-*-marp.md under slides/)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print scores without writing files")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    paths = args.paths or sorted((repo / "slides").glob("module-*-marp.md"))

    total_tagged = 0
    for path in paths:
        path = path if path.is_absolute() else repo / path
        if not path.exists():
            print(f"Missing {path}", file=sys.stderr)
            continue
        _, report = process_markdown(path.read_text(encoding="utf-8"))
        tagged = [(i, s, f) for i, s, f in report if f]
        total_tagged += len(tagged)
        print(f"{path.name}: {len(tagged)} dense slide(s)")
        if args.dry_run:
            for i, s, f in tagged[:15]:
                print(f"  slide {i}: score={s} -> {f}")
            if len(tagged) > 15:
                print(f"  ... and {len(tagged) - 15} more")
            continue
        count = process_file(path)
        print(f"  wrote {count} fit class tag(s)")

    if args.dry_run:
        print(f"Would tag {total_tagged} slide(s) total")
    else:
        print(f"Done. Tagged {total_tagged} slide(s) total.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
