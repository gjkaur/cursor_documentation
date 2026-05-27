#!/usr/bin/env python3
"""Replace '## Steps from the training slides' in module 5-10 slide-exercises."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SE = REPO / "slide-exercises"

WIN = (
    "**Environment:** Windows 10/11 · **PowerShell** in Cursor (``Ctrl+` `` → **PowerShell**)\n\n"
    "Follow each step in order. Confirm the **Expected result** before moving on.\n"
)

API_WIN = (
    "**Environment:** Windows 10/11 · **PowerShell** · use **`curl.exe`** (not the `curl` alias)\n\n"
    "**Before API calls:** set your key (replace with your real key):\n\n"
    "```powershell\n"
    '$env:CURSOR_USER_API_KEY = "cursor_your_key_here"\n'
    "# Admin exercises use:\n"
    '$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"\n'
    "```\n\n"
    "Follow each step in order. Confirm the **Expected result** before moving on.\n"
)

CLOUD_UI = (
    "**Environment:** Windows · **Cursor app** + web browser (Edge or Chrome)\n\n"
    "Follow each step in order. Confirm the **Expected result** before moving on.\n"
)


def _steps(body: str) -> str:
    return "## Steps from the training slides\n\n" + body.strip() + "\n"


STEPS: dict[str, str] = {
    "module-05/exercise-5.1-interactive-cli.md": _steps(
        WIN
        + """
| Shortcut | Action |
|----------|--------|
| ``Ctrl+` `` | Open terminal → choose **PowerShell** |
| `Ctrl+I` | Open **Agent** panel (editor UI — separate from CLI) |

### Step 1 — Verify CLI installation

**Do this (PowerShell):**

```powershell
agent --version
```

**Expected result:** Version text prints (not `command not found`). If missing, run the install command in **CLI basics** above, then close and reopen the terminal.

---

### Step 2 — Start an interactive session

**Do this:**

```powershell
cd D:/path/to/your/repo
agent
```

**Expected result:** You see a `>` prompt and a welcome message. Working directory should be your project folder.

---

### Step 3 — Ask your first question

**Do this:** At the `>` prompt, paste and press **Enter**:

```
Help me understand the current codebase structure
```

**Expected result:** The Agent lists main files, entry points, or asks one clarifying question.

---

### Step 4 — Session controls (same terminal window)

| Key / command | What it does |
|---------------|--------------|
| Type normally | Your prompt text |
| `Shift+Enter` | New line without sending |
| `Enter` | Send prompt |
| `/help` | List CLI commands |
| `/quit` or `Ctrl+C` twice | Exit CLI |

**Expected result:** `/help` shows commands; `/quit` returns you to the normal PowerShell prompt.

---

### Step 5 — Switch models

**Do this:** Inside `agent`, type:

```
/model
```

Or from PowerShell (outside a session):

```powershell
agent --list-models
```

**Expected result:** A list of available models or the current model name.

---

### Step 6 — Try Ask Mode (read-only)

**Do this (new PowerShell window or after `/quit`):**

```powershell
agent --mode=ask "What does this project's main function do?"
```

**Expected result:** Text answer only — no file edits.

---

### Step 7 — Try Plan Mode

**Do this:**

```powershell
agent --mode=plan "Add user authentication to this API"
```

**Expected result:** A plan outline before any file changes (may ask questions first).

---

### Step 8 — Optional: status line helper

**Do this:**

```powershell
npx -y cursor-statusline
```

**Expected result:** Extra status info in the terminal (model, path, context) if the package runs successfully.

---

### Step 9 — Optional: terminal setup

**Do this (inside `agent`):**

```
/setup-terminal
```

**Expected result:** Setup completes or prints instructions for your shell.

**Success criteria:** CLI verified · interactive session · follow-up prompt · `/help` · tried Ask or Plan mode
"""
    ),
    "module-05/exercise-5.2-one-shot-cli.md": _steps(
        WIN
        + """
### Step 1 — Run a simple one-shot question

**Do this (PowerShell):**

```powershell
agent -p "What is the difference between let and const in JavaScript?"
```

**Expected result:** Answer prints in the terminal; command exits back to `PS>`.

---

### Step 2 — Run another one-shot (code / shell help)

**Do this:**

```powershell
agent -p "Write a PowerShell function that checks if a TCP port is in use"
```

**Expected result:** Function code or clear steps print; no interactive `>` prompt stays open.

---

### Step 3 — Ask Mode in one shot

**Do this:**

```powershell
agent --mode=ask -p "Explain the git rebase command with examples"
```

**Expected result:** Explanation only (read-only).

---

### Step 4 — Pick a specific model

**Do this:**

```powershell
agent --model gpt-5-mini -p "What does Get-ChildItem do in PowerShell?"
```

**Expected result:** Answer from the model you named (or an error if that model is unavailable on your plan).

---

### Step 5 — Understand scriptable review (concept)

**Do this:** In Cursor Agent (`Ctrl+I`), ask it to help you draft a **PowerShell** pre-commit script that runs:

```powershell
agent --mode=ask -p "Review these staged files for debug statements and missing error handling"
```

**Expected result:** You have a `.ps1` sketch you could wire to `git diff --cached` later (full hook optional for this lab).

---

### Step 6 — CI/CD idea (discussion)

**Discuss:** In GitHub Actions you would set `CURSOR_API_KEY` as a secret and run `agent -p "..."` on the runner.

**Expected result:** You can explain one use case (PR review, test log summary) without breaking production CI in class.

**Success criteria:** Ran one-shots · specified a model · understand script/CI use cases
"""
    ),
    "module-05/exercise-5.3-cloud-handoff.md": _steps(
        WIN
        + """
### Step 1 — Start CLI and hand off to Cloud

**Do this:**

```powershell
agent
```

At the `>` prompt, type (note the **`&` at the start**):

```
& Analyze the entire codebase and create a dependency graph.
```

**Expected result:** Message that a **Cloud Agent** started, plus an **Agent ID** and a `https://cursor.com/agents/...` link.

---

### Step 2 — Verify in the browser

**Do this:** Open the link in **Edge** or **Chrome**.

**Expected result:** Dashboard shows the agent **Running** (or **Completed** later).

---

### Step 3 — Close terminal safely

**Do this:** You may close the terminal or type `/quit`. The cloud task should keep running.

**Expected result:** Status on the web dashboard still progresses without your laptop CLI attached.

---

### Step 4 — Hand off an existing conversation

**Do this:** In a new `agent` session, after some local messages:

```
& Continue this conversation in the cloud. I need to log off.
```

**Expected result:** Handoff confirmation and cloud URL.

---

### Step 5 — One-shot cloud handoff

**Do this:**

```powershell
agent -p "& Refactor the auth module to use JWT. Update all tests and docs."
```

**Expected result:** Cloud agent launched from a single command (same `&` semantics).

---

### Step 6 — Resume later

**Do this:** Copy the agent ID from the dashboard, then:

```powershell
agent --resume YOUR_AGENT_ID_HERE
```

**Expected result:** Session resumes or shows cloud status (per your plan/features).

**Success criteria:** Handoff with `&` · dashboard link · agent continues after terminal closed
"""
    ),
    "module-05/exercise-5.4-listing-and-resuming-sessions.md": _steps(
        WIN
        + """
### Step 1 — Create three short sessions

**Do this:** Run three separate one-shot sessions (each exits automatically):

```powershell
agent -p "Reply with exactly one word: frontend-cleanup"
agent -p "Reply with exactly one word: db-optimization"
agent -p "Reply with exactly one word: docs-update"
```

**Expected result:** Three one-word replies; three saved sessions in history.

---

### Step 2 — List sessions

**Do this:** Start interactive CLI:

```powershell
agent
```

Then type:

```
/resume
```

**Expected result:** Numbered list of recent sessions with names or timestamps.

---

### Step 3 — Resume by ID

**Do this:** From the list, copy a session ID, exit (`/quit`), then:

```powershell
agent --resume PASTE_SESSION_ID_HERE
```

**Expected result:** Prior conversation context is available; Agent remembers earlier messages.

---

### Step 4 — Two terminals (optional)

**Do this:** Open two PowerShell terminals. Resume different sessions in each.

**Expected result:** Two independent CLI conversations at once.

---

### Step 5 — Compress long context

**Do this:** Inside a long `agent` session:

```
/compress
```

**Expected result:** Conversation summarized; more context window free.

---

### Step 6 — Naming convention (practice)

**Do this:** When starting real work, use descriptive first prompts, e.g. `api-auth-fix` or `docs-update`.

**Expected result:** `/resume` list is readable a week later.

**Success criteria:** Created sessions · listed with `/resume` · resumed one · tried `/compress`
"""
    ),
}

_PATTERN = re.compile(
    r"## Steps from the training slides\n.*?\n---\n\n## (?:Success criteria|Detailed reference)",
    re.DOTALL,
)


def _load_part2() -> dict[str, str]:
    path = Path(__file__).parent / "_module_6_10_steps_data.py"
    ns: dict = {"STEPS_PART2": {}}
    code = path.read_text(encoding="utf-8")
    # Strip broken import line; data file uses _steps() calls defined here
    code = re.sub(r"^from apply.*\n", "", code)
    code = re.sub(r"^from apply_beginner.*\n", "", code)
    exec(compile(code, str(path), "exec"), {"_steps": _steps, "WIN": WIN, "API_WIN": API_WIN, "CLOUD_UI": CLOUD_UI}, ns)
    return ns["STEPS_PART2"]


def apply_all() -> int:
    all_steps = {**STEPS, **_load_part2()}
    updated = 0
    for rel, new_block in sorted(all_steps.items()):
        path = SE / rel
        if not path.exists():
            print(f"SKIP missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        m = _PATTERN.search(text)
        if not m:
            print(f"SKIP no section: {rel}")
            continue
        tail = m.group(0)[m.group(0).find("\n---\n\n## ") :]
        text = text[: m.start()] + new_block.rstrip() + tail + text[m.end() :]
        path.write_text(text, encoding="utf-8")
        updated += 1
        print(f"OK {rel}")
    print(f"Updated {updated} files")
    return len(all_steps) if updated == len(all_steps) else 0


if __name__ == "__main__":
    raise SystemExit(0 if apply_all() else 1)
