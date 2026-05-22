#!/usr/bin/env python3
"""Replace bash-only API hints with full PowerShell command blocks in module slides."""

from __future__ import annotations

import re
from pathlib import Path

REPLACEMENTS: list[tuple[str, str]] = [
    (
        r'```bash\nexport CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"\n\necho \$CURSOR_USER_API_KEY\n```\n\n\*\*PowerShell \(Windows\):\*\*[^\n]+\n',
        '''**Terminal:** **PowerShell**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
$env:CURSOR_USER_API_KEY
```

**Terminal (alternative):** **Git Bash** or **Ubuntu (WSL)** — use the `export` / `echo` bash block above.
''',
    ),
    (
        r'```bash\nexport CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"\n\necho \$CURSOR_USER_API_KEY\n```\n\n\*\*PowerShell \(Windows\):\*\*[^\n]+\n',
        '''**Terminal:** **PowerShell**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
$env:CURSOR_USER_API_KEY
```
''',
    ),
    (
        r'```bash\ncurl -s -u "\$CURSOR_USER_API_KEY:" \\\n  https://api\.cursor\.com/v1/models \| head -20\n```\n\n\*\*PowerShell \(Windows\):\*\*[^\n]+\n',
        '''**Terminal:** **PowerShell**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  https://api.cursor.com/v1/models | Select-Object -First 20
```

**Terminal (alternative):** **Git Bash** / **WSL** — bash `curl` block above.
''',
    ),
    (
        r'```bash\nexport CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"\n\ncurl -X POST https://api\.cursor\.com/v1/agents \\\n  -u "\$CURSOR_USER_API_KEY:" \\\n  -H "Content-Type: application/json" \\\n  -d \'\{\n    "prompt": \{"text": "Add a README\.md file with setup instructions"\},\n    "repos": \[\{"url": "https://github\.com/YOUR_ORG/YOUR_REPO", "startingRef": "main"\}\],\n    "autoCreatePR": true\n  \}\' \| jq \'\.\'\n```\n\n\*\*PowerShell \(Windows\):\*\*[^\n]+\n',
        '''**Step 1 — set API key · Terminal:** **PowerShell**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
```

**Step 2 — create agent · Terminal:** **PowerShell**

```powershell
curl.exe -X POST https://api.cursor.com/v1/agents `
  -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Content-Type: application/json" `
  -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' `
  | ConvertFrom-Json
```

**Terminal (alternative):** **Git Bash** / **WSL** — bash block below.

```bash
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' | jq '.'
```
''',
    ),
    (
        r'```bash\nAGENT_ID=\$\(echo "\$RESPONSE" \| jq -r \'\.\agent\.id\'\)\nRUN_ID=\$\(echo "\$RESPONSE" \| jq -r \'\.\run\.id\'\)\n\necho "Agent ID: \$AGENT_ID"\necho "Dashboard: https://cursor\.com/agents/\$AGENT_ID"\n```\n\n\*\*PowerShell \(Windows\):\*\*[^\n]+\n',
        '''**Terminal:** **PowerShell** — paste after saving JSON response to `$response`

```powershell
$response = curl.exe ... | ConvertFrom-Json   # from previous step
$agentId = $response.agent.id
$runId = $response.run.id
Write-Host "Agent ID: $agentId"
Write-Host "Dashboard: https://cursor.com/agents/$agentId"
```

**Terminal (alternative):** **Git Bash** / **WSL**

```bash
AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')
echo "Agent ID: $AGENT_ID"
echo "Dashboard: https://cursor.com/agents/$AGENT_ID"
```
''',
    ),
    (
        r'```bash\ncurl -N -u "\$CURSOR_USER_API_KEY:" \\\n  -H "Accept: text/event-stream" \\\n  "https://api\.cursor\.com/v1/agents/\$AGENT_ID/runs/\$RUN_ID/stream"\n```\n\n\*\*PowerShell \(Windows\):\*\*[^\n]+\n',
        '''**Terminal:** **PowerShell**

```powershell
curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Accept: text/event-stream" `
  "https://api.cursor.com/v1/agents/$env:AGENT_ID/runs/$env:RUN_ID/stream"
```

Set IDs first: `$env:AGENT_ID = "..."` · `$env:RUN_ID = "..."`

**Terminal (alternative):** **Git Bash** / **WSL** — bash `curl -N` block above.
''',
    ),
    (
        r'```bash\nexport CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx"\ncurl -s -u "\$CURSOR_ADMIN_API_KEY:"\n```',
        '''**Terminal:** **PowerShell**

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_xxxxxxxxxxxx"
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):"
```
''',
    ),
]

STEP_NOTE_FIXES: list[tuple[str, str]] = [
    (
        "**Step 4:** Test with Python requests:\n**Where:** **Cursor Agent panel**",
        "**Step 4:** Test with Python requests:\n**Terminal:** **PowerShell** — save as `test_models.py`, then `python test_models.py`",
    ),
    (
        "**Step 5:** Test with OpenAI SDK:\n**Where:** **Cursor Agent panel**",
        "**Step 5:** Test with OpenAI SDK:\n**Terminal:** **PowerShell** — `python test_openai_sdk.py`",
    ),
    (
        "**Step 2:** Navigate the session\n**Terminal:** **PowerShell**",
        "**Step 2:** Navigate the session (inside the running `agent` session — same terminal window)",
    ),
    (
        "**Step 1:** Generate User API Key via Cursor Settings → API Keys → Generate New Key\n**Terminal:** **PowerShell**",
        "**Step 1:** Generate User API Key — **Where:** **Cursor app** → Settings → API Keys → Generate New Key (browser not required)",
    ),
]


def fix_slide_separators(text: str) -> str:
    text = re.sub(r"\n---\n## Exercise ", r"\n---\n\n## Exercise ", text)
    text = re.sub(r"\n---\n<!-- _class:", r"\n---\n\n<!-- _class:", text)
    return text


def apply_replacements(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    for pattern, replacement in REPLACEMENTS:
        text, count = re.subn(pattern, replacement, text, count=1)
    for old, new in STEP_NOTE_FIXES:
        text = text.replace(old, new)
    text = fix_slide_separators(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


def main() -> None:
    repo = Path(__file__).resolve().parent.parent
    for module_num in range(2, 11):
        path = repo / "slides" / f"module-{module_num:02d}-marp.md"
        if path.exists() and apply_replacements(path):
            print(f"Updated {path.name}")


if __name__ == "__main__":
    main()
