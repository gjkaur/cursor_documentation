#!/usr/bin/env python3
"""Add Windows platform and terminal guidance to exercise slides in module Marp files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

WINDOWS_GUIDE_SLIDE = """## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**
"""

PLATFORM_UI = "**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**"

PLATFORM_AGENT_TERMINAL = "**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Agent commands → **PowerShell** ``Ctrl+` ``"

PLATFORM_CLI = "**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)"

PLATFORM_API = "**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`"

PLATFORM_MIXED = "**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards"

EXERCISE_TITLE = re.compile(r"^## Exercise .+$", re.MULTILINE)
STEP_LINE = re.compile(r"^(\*\*Step (\d+):\*\*.*)$", re.MULTILINE)
HAS_PLATFORM = "**Platform:**"


def _classify_slide(slide: str) -> str:
    lower = slide.lower()
    has_bash = "```bash" in slide
    has_curl = "curl " in lower or "curl.exe" in lower
    has_agent_cli = has_bash and bool(re.search(r"^agent\b| agent |`agent", lower, re.MULTILINE))
    has_python = "```python" in slide
    has_ngrok = "ngrok" in lower
    has_browser = any(k in lower for k in ("browser", "dashboard", "cursor.com/agents", "web ui"))
    ui_prompt_count = len(re.findall(r"```\n[^`]", slide))

    if has_curl or (has_python and has_bash):
        return "api"
    if has_agent_cli:
        return "cli"
    if has_ngrok or (has_browser and has_bash):
        return "mixed"
    if "executing:" in lower or "agent terminal loop" in lower:
        return "agent_terminal"
    if has_bash and ui_prompt_count >= 1 and not has_agent_cli:
        return "mixed"
    if has_bash and not has_agent_cli and ("git clone" in lower or "mkdir" in lower):
        return "mixed"
    if has_bash and has_agent_cli:
        return "cli"
    if "terminal" in lower and "agent" in lower:
        return "agent_terminal"
    return "ui"


def _platform_block(kind: str) -> str:
    return {
        "ui": PLATFORM_UI,
        "agent_terminal": PLATFORM_AGENT_TERMINAL,
        "cli": PLATFORM_CLI,
        "api": PLATFORM_API,
        "mixed": PLATFORM_MIXED,
    }[kind]


def _step_terminal_note(kind: str, step_text: str) -> str:
    step_lower = step_text.lower()
    if any(k in step_lower for k in ("browser", "dashboard", "web ui", "sign in to cursor")):
        return "**Where:** **Web browser** — Edge or Chrome"
    if any(k in step_lower for k in ("agent panel", "open the agent", "ctrl+l", "ctrl+i", "cmd+i", "plan mode", "checkpoint", "review", "approve", "reject", "diff", "restore", "select a", "open a specific file", "ask ", "prompt", "compare", "mention", "@")):
        return "**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)"
    if kind == "agent_terminal" or ("command" in step_lower and "approve" in step_lower):
        return "**Where:** Agent proposes commands → approve in **PowerShell** terminal (``Ctrl+` ``)"
    if kind in ("cli", "api", "mixed"):
        if any(k in step_lower for k in (".sh", "bash", "hook", "for file in", "pre-commit")):
            return "**Terminal:** **Git Bash** or **Ubuntu (WSL)** — bash syntax required"
        if "python" in step_lower or ".py" in step_lower:
            return "**Terminal:** **PowerShell** — `python script.py`"
        if "ngrok" in step_lower or "curl" in step_lower or "export " in step_lower or "agent" in step_lower:
            return "**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor"
        if "git clone" in step_lower or "cd " in step_lower or "cursor ." in step_lower:
            return "**Terminal:** **PowerShell** — clone/open repo, then continue in Agent panel"
    if kind == "ui":
        return "**Where:** **Cursor Agent panel** — ``Ctrl+L``"
    return "**Terminal:** **PowerShell** — unless step notes Git Bash or WSL"


def _annotate_steps(slide_body: str, kind: str) -> str:
    if "**Where:**" in slide_body or "**Terminal:**" in slide_body:
        return slide_body

    def replacer(match: re.Match[str]) -> str:
        step_line = match.group(1)
        note = _step_terminal_note(kind, step_line)
        return f"{step_line}\n{note}"

    return STEP_LINE.sub(replacer, slide_body)


def _add_powershell_hint_after_bash(slide: str) -> str:
    """Add a short PowerShell note after bash blocks on API/CLI slides."""
    if "**PowerShell (Windows):**" in slide:
        return slide

    def repl(match: re.Match[str]) -> str:
        bash_block = match.group(0)
        content = match.group(1)
        if "export " in content or "curl " in content or "$(" in content:
            return (
                bash_block
                + "\n\n**PowerShell (Windows):** Same steps in **PowerShell** — "
                "use `$env:NAME = \"value\"` instead of `export`, and `curl.exe` instead of `curl`."
            )
        if content.strip().startswith("agent"):
            return bash_block + "\n\n**PowerShell (Windows):** Run the same `agent` commands in **PowerShell**."
        if "git clone" in content:
            return (
                bash_block
                + "\n\n**PowerShell (Windows):** Same commands work in **PowerShell** — "
                "`git clone ...` then `cd detectron2` then `cursor .`"
            )
        return bash_block

    return re.sub(r"```bash\n(.*?)```", repl, slide, flags=re.DOTALL)


def _augment_exercise_slide(slide: str) -> str:
    slide = slide.strip("\n")
    if HAS_PLATFORM in slide:
        return slide
    title_match = EXERCISE_TITLE.search(slide)
    if not title_match:
        return slide

    title = title_match.group(0)
    before = slide[: title_match.start()].strip()
    body = slide[title_match.end() :].lstrip("\n")
    kind = _classify_slide(slide)
    body = _annotate_steps(body, kind)
    body = _add_powershell_hint_after_bash(body) if kind in ("cli", "api", "mixed") else body

    parts = [p for p in (before, title, _platform_block(kind), body) if p]
    return "\n\n".join(parts)


def _insert_guide_before_first_exercise(markdown: str) -> str:
    if "## Windows Exercise Environment" in markdown:
        return markdown
    match = EXERCISE_TITLE.search(markdown)
    if not match:
        return markdown
    insert_at = markdown.rfind("\n---\n", 0, match.start())
    if insert_at == -1:
        return markdown
    guide = "\n---\n\n" + WINDOWS_GUIDE_SLIDE.strip() + "\n\n"
    return markdown[:insert_at] + guide + markdown[insert_at:]


def augment_module(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    slides = text.split("\n---\n")
    exercise_count = 0
    changed = 0
    new_slides: list[str] = []
    for slide in slides:
        if EXERCISE_TITLE.search(slide.strip()):
            exercise_count += 1
            updated = _augment_exercise_slide(slide)
            if updated != slide.strip("\n"):
                changed += 1
            new_slides.append(updated)
        else:
            new_slides.append(slide)
    result = "\n---\n".join(new_slides)
    result = _insert_guide_before_first_exercise(result)
    if result != text:
        path.write_text(result, encoding="utf-8")
    return exercise_count, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--slides-dir",
        type=Path,
        default=Path("slides"),
    )
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    slides_dir = args.slides_dir if args.slides_dir.is_absolute() else repo / args.slides_dir

    total_exercises = 0
    total_changed = 0
    for module_num in range(2, 11):
        path = slides_dir / f"module-{module_num:02d}-marp.md"
        if not path.exists():
            continue
        count, changed = augment_module(path)
        total_exercises += count
        total_changed += changed
        print(f"{path.name}: {count} exercise slides, {changed} augmented")

    print(f"Total: {total_exercises} exercise slides, {total_changed} updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
