#!/usr/bin/env python3
"""Normalize Marp frontmatter on all module slide decks to match module-01 settings."""

from __future__ import annotations

import re
import sys
from pathlib import Path

MODULES = [
    (1, "Mental Models for AI-Assisted Development"),
    (2, "Cursor Editor Essentials"),
    (3, "Agent Modes and Tools"),
    (4, "Customizing Cursor for Your Team"),
    (5, "Cursor CLI and Local Automation"),
    (6, "Cloud Agents in the UI"),
    (7, "Cursor API Foundations"),
    (8, "Cloud Agents API and Webhooks"),
    (9, "Admin and Analytics APIs"),
    (10, "AI Code Tracking and Reporting"),
]


def _strip_frontmatter(text: str) -> str:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return text
    end = text.find("\n---\n", 3)
    if end == -1:
        return text
    return text[end + 5 :]


def frontmatter(num: int, title: str) -> str:
    return (
        "---\n"
        "marp: true\n"
        "theme: flat-gaia\n"
        "paginate: true\n"
        f'header: "Module {num} — {title}"\n'
        "---\n"
    )


def normalize_file(path: Path, num: int, title: str) -> bool:
    body = _strip_frontmatter(path.read_text(encoding="utf-8"))
    updated = frontmatter(num, title) + "\n" + body.lstrip("\n")
    original = path.read_text(encoding="utf-8")
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    slides_dir = Path(__file__).resolve().parent.parent / "slides"
    changed = 0
    for num, title in MODULES:
        path = slides_dir / f"module-{num:02d}-marp.md"
        if not path.exists():
            print(f"Missing {path.name}", file=sys.stderr)
            continue
        if normalize_file(path, num, title):
            print(f"Normalized {path.name}")
            changed += 1
    print(f"Done. {changed} file(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
