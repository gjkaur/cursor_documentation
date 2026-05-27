#!/usr/bin/env python3
"""Apply shorter beginner steps to module 7-10 slide-exercises only."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SE = REPO / "slide-exercises"

API_WIN_SHORT = (
    "**Environment:** Windows · PowerShell (``Ctrl+` ``) · **`curl.exe`** · keys in `$env:` only (never commit).\n\n"
    "```powershell\n"
    '$env:CURSOR_USER_API_KEY = "cursor_your_key_here"\n'
    '$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"  # Modules 9–10\n'
    "```\n\n"
    "Follow each step in order. Confirm the **Expected result** before moving on.\n"
)

API_ADMIN_SHORT = API_WIN_SHORT

CLOUD_UI_SHORT = (
    "**Environment:** Windows · **Cursor app** + browser (Edge or Chrome).\n\n"
    "Follow each step in order. Confirm the **Expected result** before moving on.\n"
)

API_BASICS_SHORT = """## API basics (read this first)

**Windows:** PowerShell (``Ctrl+` ``) · **`curl.exe`** · store keys in `$env:` — **never** commit keys to git.

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"   # Admin labs (9–10)
```

More examples (Python, jq, bash): see **Detailed reference** below — optional for class.
"""

DETAILED_NOTE = (
    "\n> **Note:** The section below is optional deep dive — not required to finish the in-class steps.\n\n"
)

_PATTERN_STEPS = re.compile(
    r"## Steps from the training slides\n.*?\n---\n\n(?:## Success criteria|> \*\*Note:|## Detailed reference)",
    re.DOTALL,
)

_PATTERN_API_BASICS = re.compile(
    r"## API basics \(read this first\)\n.*?\n---\n\n## Steps from the training slides",
    re.DOTALL,
)


def _steps(body: str) -> str:
    return "## Steps from the training slides\n\n" + body.strip() + "\n"


def _load_easy_steps() -> dict[str, str]:
    from _module_7_10_easy_steps import build_steps

    return build_steps(API_WIN_SHORT, API_ADMIN_SHORT, CLOUD_UI_SHORT, _steps)


def apply() -> int:
    steps_map = _load_easy_steps()
    updated = 0
    for rel in sorted(steps_map.keys()):
        path = SE / rel
        if not path.exists():
            print(f"SKIP missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8")

        # Short API basics (modules 7–10)
        if "## API basics (read this first)" in text:
            m_api = _PATTERN_API_BASICS.search(text)
            if m_api:
                text = (
                    text[: m_api.start()]
                    + API_BASICS_SHORT
                    + "\n---\n\n## Steps from the training slides"
                    + text[m_api.end() :]
                )

        m = _PATTERN_STEPS.search(text)
        if not m:
            print(f"SKIP no steps section: {rel}")
            continue
        tail = m.group(0)[m.group(0).find("\n---\n\n## ") :]
        text = text[: m.start()] + steps_map[rel].rstrip() + tail + text[m.end() :]

        # One-time note before Detailed reference
        if "## Detailed reference" in text and DETAILED_NOTE.strip() not in text:
            text = text.replace(
                "\n## Detailed reference",
                DETAILED_NOTE + "## Detailed reference",
                1,
            )

        path.write_text(text, encoding="utf-8")
        updated += 1
        print(f"OK {rel}")

    print(f"Updated {updated} module 7-10 exercise files")
    return updated


if __name__ == "__main__":
    raise SystemExit(0 if apply() >= 15 else 1)
