#!/usr/bin/env python3
"""Normalize slides and core exercises for Windows demonstration."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

WINDOWS_DEMO_LINE = (
    "**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · "
    "Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**"
)

SUBS = [
    (
        r"\*\*Platform:\*\* Windows 10/11 · Prompts → \*\*Agent panel\*\* ``Ctrl\+L`` · Diffs → \*\*Editor\*\*",
        WINDOWS_DEMO_LINE,
    ),
    (
        r"\*\*Platform:\*\* Windows 10/11 · Agent → ``Ctrl\+L`` · Shell → \*\*PowerShell\*\* · Browser for dashboards",
        "**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards",
    ),
    (
        "**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)",
        "**Where:** **Agent panel** — ``Ctrl+I``",
    ),
    (
        "**Where:** **Cursor Agent panel** — ``Ctrl+L``",
        "**Where:** **Agent panel** — ``Ctrl+I``",
    ),
    (
        "Open **Agent panel** — ``Ctrl+I`` (Mac: ``Cmd+I``)",
        "Open **Agent panel** — ``Ctrl+I``",
    ),
    (
        "**Step 2:** Open the Agent (Ctrl+I on Windows/Linux · Cmd+I on Mac)",
        "**Step 2:** Open the Agent panel — ``Ctrl+I``",
    ),
    (
        "# Windows/Linux: Ctrl+Shift+S · Mac: Cmd+Shift+S",
        "# Windows: ``Ctrl+Shift+S`` (Mac: ``Cmd+Shift+S``)",
    ),
    (
        "Use **PowerShell**, **Git Bash**, or **CMD** in Cursor's integrated terminal (Ctrl+`):",
        "**Windows (PowerShell)** in Cursor's integrated terminal (``Ctrl+` `` → **PowerShell**):",
    ),
]

SLIDE_ONLY_SUBS = [
    (
        "**Step 2 — Run test suite**\n\n**Goal:** Compile and run tests — all should pass first.\n\n**Windows:**",
        "**Step 2 — Run test suite**\n\n**Goal:** Compile and run tests — all should pass first.\n\n**Windows (use this in the demo):**",
    ),
    (
        "**Mac/Linux:**\n```\nRun ./run_tests.sh (chmod +x if needed).\nShow full output: compilation OK? how many tests passed?\n```\n\n**Look for:**",
        "**Other platforms (optional):** Mac/Linux — `./run_tests.sh` (run `chmod +x run_tests.sh` if needed).\n\n**Look for:**",
    ),
]


def apply_subs(text: str, subs: list[tuple[str, str]]) -> str:
    for old, new in subs:
        text = text.replace(old, new)
    return text


def apply_regex_subs(text: str, patterns: list[tuple[str, str]]) -> str:
    for pattern, repl in patterns:
        text = re.sub(pattern, repl, text)
    return text


REGEX_SUBS = [
    (
        r"\*\*Platform:\*\* Windows 10/11 · Prompts → \*\*Agent panel\*\* ``Ctrl\+L`` · Diffs → \*\*Editor\*\*",
        WINDOWS_DEMO_LINE,
    ),
    (
        r"\*\*Platform:\*\* Windows 10/11 · Agent → ``Ctrl\+L`` · Shell → \*\*PowerShell\*\* · Browser for dashboards",
        "**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards",
    ),
    (
        r"\*\*Platform:\*\* Windows 10/11 · \*\*PowerShell\*\* ``Ctrl\+` `` \(Git Bash/WSL for ``\.sh`` scripts\)",
        "**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent ``Ctrl+I``",
    ),
    (
        r"\*\*Cursor Agent panel\*\* \(`Ctrl\+L`\) is for natural-language prompts — not a shell\.",
        "**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.",
    ),
]


def normalize_file(path: Path, extra_subs: list[tuple[str, str]] | None = None) -> bool:
    original = path.read_text(encoding="utf-8")
    text = apply_subs(original, SUBS)
    text = apply_regex_subs(text, REGEX_SUBS)
    if extra_subs:
        text = apply_subs(text, extra_subs)
    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    changed = 0
    for path in sorted((REPO / "slides").glob("module-*-marp.md")):
        extra = SLIDE_ONLY_SUBS if path.name == "module-03-marp.md" else None
        if normalize_file(path, extra):
            print(f"Updated {path.relative_to(REPO)}")
            changed += 1

    for folder in ("core-exercises", "api-exercises"):
        root = REPO / folder
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if normalize_file(path):
                print(f"Updated {path.relative_to(REPO)}")
                changed += 1

    print(f"Done. {changed} file(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
