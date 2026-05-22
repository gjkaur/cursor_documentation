#!/usr/bin/env python3
"""Tag ASCII diagram code fences and normalize boxed diagram alignment in Marp slides."""

from __future__ import annotations

import re
import sys
from pathlib import Path

BOX_CHARS = set("┌┐└┘├┤┬┴┼│─")
DIAGRAM_ARROW_THRESHOLD = 3

CODE_LANGUAGES = {
    "python",
    "bash",
    "powershell",
    "sh",
    "json",
    "yaml",
    "yml",
    "javascript",
    "js",
    "typescript",
    "ts",
    "sql",
    "html",
    "css",
    "xml",
    "java",
    "go",
    "rust",
    "ruby",
    "php",
    "csharp",
    "cs",
    "cpp",
    "c",
    "http",
    "curl",
}


def is_diagram_block(lang: str, body: str) -> bool:
    if lang in CODE_LANGUAGES:
        return False
    box_count = sum(1 for char in body if char in BOX_CHARS)
    if box_count >= 4:
        return True
    if body.count("→") >= DIAGRAM_ARROW_THRESHOLD and "import " not in body and "def " not in body:
        return True
    if "├──" in body or "└──" in body:
        return True
    if re.search(r"←─{3,}→", body):
        return True
    if "█" in body and body.count("█") >= 4:
        return True
    return False


def normalize_box_line(line: str, width: int) -> str:
    if line.startswith("│") and line.endswith("│") and len(line) >= 2:
        inner = line[1:-1].rstrip()
        if len(inner) > width - 2:
            inner = inner[: width - 2]
        padded = inner + " " * (width - 2 - len(inner))
        return f"│{padded}│"
    if line.startswith("┌") and line.endswith("┐"):
        return "┌" + "─" * (width - 2) + "┐"
    if line.startswith("├") and line.endswith("┤"):
        return "├" + "─" * (width - 2) + "┤"
    if line.startswith("└") and line.endswith("┘"):
        return "└" + "─" * (width - 2) + "┘"
    return line


def is_simple_box_line(line: str) -> bool:
    if line.startswith("│") and line.endswith("│"):
        return line.count("│") == 2
    if line.startswith(("┌", "├", "└")) and line.endswith(("┐", "┤", "┘")):
        return line.count("─") == len(line) - 2
    return False


def normalize_boxed_diagram(body: str) -> str:
    lines = body.rstrip("\n").split("\n")
    box_lines = [line for line in lines if line.strip() and is_simple_box_line(line)]
    if len(box_lines) < 3:
        return body

    border_widths = [len(line) for line in box_lines if line.startswith(("┌", "├", "└"))]
    if not border_widths:
        return body

    width = max(border_widths)
    normalized: list[str] = []
    for line in lines:
        if is_simple_box_line(line):
            normalized.append(normalize_box_line(line, width))
        else:
            normalized.append(line)
    return "\n".join(normalized)


def process_markdown(text: str) -> tuple[str, int]:
    pattern = re.compile(r"```([^\n]*)\n(.*?)```", re.DOTALL)
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        lang = match.group(1).strip().lower()
        body = match.group(2)
        if not is_diagram_block(lang, body):
            return match.group(0)

        normalized = normalize_boxed_diagram(body)
        if lang != "text" or normalized != body.rstrip("\n"):
            changes += 1
        return f"```text\n{normalized}\n```"

    return pattern.sub(repl, text), changes


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    slides_dir = repo / "slides"
    total = 0

    for path in sorted(slides_dir.glob("module-*-marp.md")):
        original = path.read_text(encoding="utf-8")
        updated, count = process_markdown(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            print(f"{path.name}: {count} diagram block(s) updated")
            total += count

    print(f"Done. {total} diagram block(s) updated across module files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
