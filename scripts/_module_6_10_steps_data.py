# Step bodies for modules 6-10 (loaded by apply-beginner-steps-modules-5-10.py)
STEPS_PART2 = {
    "module-06/exercise-6.1-launching-a-cloud-agent.md": _steps(
        CLOUD_UI
        + """
| Where | What |
|-------|------|
| Cursor sidebar | **Cloud** / cloud icon, or **Command Palette** (`Ctrl+Shift+P`) → **Cloud Agents** |
| Browser | [https://cursor.com/agents](https://cursor.com/agents) |

### Step 1 — Open Cloud Agents

**Do this:** In Cursor, open **Cloud Agents**. Also open [cursor.com/agents](https://cursor.com/agents) in your browser.

**Expected result:** Empty list or previous runs; **+ New** (or **New Agent**) is visible.

---

### Step 2 — Create a new agent

**Do this:** Click **+ New** and fill in:

| Field | Example |
|-------|---------|
| Repository | `https://github.com/YOUR_ORG/YOUR_REPO` |
| Branch | `main` |
| Prompt | See below |
| Model | `claude-4.6-sonnet` (or course default) |
| Auto-create PR | Off for first try |

**Prompt to paste:**

```
Read README and main source files. Summarize:
- What this project does
- Key dependencies
- How to run locally
- Common issues
```

**Expected result:** Agent status **Running**; log lines appear (clone repo, read files, etc.).

---

### Step 3 — Watch the live log

**Do this:** Keep the run page open 2–5 minutes.

**Expected result:** Timestamped log lines; eventual **Completed** (or clear error).

---

### Step 4 — Review settings (gear icon)

**Do this:** Open settings and note: default model, auto-PR, notifications, webhook URL, max runtime.

**Expected result:** You know where to change defaults for the next run.

---

### Step 5 — Optional: run with auto-PR

**Do this:** New agent with **Auto-create PR** on and prompt:

```
Add CONTRIBUTING.md with dev setup, tests, PR process, and code style
```

**Expected result:** Completed run may show a PR link on the dashboard.

---

### Step 6 — Share the run URL

**Do this:** Copy the agent URL from the browser address bar for a teammate.

**Expected result:** URL format like `https://cursor.com/agents/agt_...` opens the same run when signed in.

**Success criteria:** Launched agent · watched log · understand settings · optional PR run
"""
    ),
    "module-06/exercise-6.2-cloud-agent-artifacts.md": _steps(
        CLOUD_UI
        + API_WIN
        + """
### Step 1 — Launch an agent that creates artifacts

**Do this:** New Cloud Agent with this prompt:

```
Generate:
1. api_documentation.md — API-style docs for main endpoints
2. test_report.json — test summary (real or plausible for demo)
3. dependencies.txt — packages and versions

Place all files in an artifacts/ folder in the repo.
```

**Expected result:** Run completes; **Artifacts** tab or section lists files.

---

### Step 2 — Download from the UI

**Do this:** On the completed run: download **one file**, then try **Download All (zip)** if shown.

**Expected result:** Files save to your **Downloads** folder; zip opens in File Explorer.

---

### Step 3 — Preview in browser

**Do this:** Open `.md` / `.json` from the UI preview if available.

**Expected result:** Markdown renders; JSON is readable.

---

### Step 4 — List artifacts via API (PowerShell)

**Do this:** Set IDs from the dashboard, then:

```powershell
$env:AGENT_ID = "your_agent_id_here"
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  "https://api.cursor.com/v1/agents/$($env:AGENT_ID)/artifacts"
```

**Expected result:** JSON listing artifact paths (use `ConvertFrom-Json` if helpful).

---

### Step 5 — Download one artifact via API (optional)

**Do this:** Follow the lab guide’s presigned-URL pattern with `curl.exe -L -o filename ...`.

**Expected result:** File saved locally; matches UI download.

**Success criteria:** Artifacts created · downloaded in UI · listed via API
"""
    ),
    "module-07/exercise-7.2-generate-and-test-api-keys.md": _steps(
        API_WIN
        + """
### Step 1 — Create a User API key (UI)

**Do this:** **Cursor** → **Settings** → **API Keys** (or team dashboard per your plan) → **Generate** → copy the key once.

**Expected result:** Key string starting with `cursor_...` (you cannot view it again later).

---

### Step 2 — Store in PowerShell session

**Do this:**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_paste_your_key_here"
$env:CURSOR_USER_API_KEY.Substring(0, 12) + "..."
```

**Expected result:** First line sets variable; second prints a short prefix (not the full secret).

---

### Step 3 — Test with curl.exe

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" https://api.cursor.com/v1/models
```

**Expected result:** JSON with model names (or `items` array). Not `401 Unauthorized`.

---

### Step 4 — Test with Python (optional)

**Do this:** Save `test_models.py`:

```python
import os, requests
key = os.environ["CURSOR_USER_API_KEY"]
r = requests.get("https://api.cursor.com/v1/models", auth=(key, ""), timeout=30)
print(r.status_code, r.text[:500])
```

Run: `python test_models.py`

**Expected result:** Status `200` and JSON body.

---

### Step 5 — Admin key (Enterprise only)

**Do this:** Generate **Admin API key** in dashboard →:

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_paste_here"
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" https://api.cursor.com/v1/teams/members
```

**Expected result:** `200` with team data, or clear message if your plan lacks Admin API.

---

### Step 6 — Revocation (know how)

**Do this:** In **Settings → API Keys**, find **Revoke** for a test key (only if instructor allows).

**Expected result:** Old key returns `401` on next API call.

**Success criteria:** User key works in curl · optional Admin key · keys only in `$env:`, not in git
"""
    ),
    "module-07/exercise-7.3-rate-limits-and-error-handling.md": _steps(
        API_WIN
        + """
### Step 1 — Make one successful call

**Do this:**

```powershell
curl.exe -s -D - -o NUL -u "$($env:CURSOR_ADMIN_API_KEY):" `
  https://api.cursor.com/v1/teams/members 2>&1 | Select-String -Pattern "HTTP/|X-RateLimit"
```

**Expected result:** `HTTP/1.1 200` and rate-limit headers if present.

---

### Step 2 — Read rate-limit headers

**Do this:** Run the call again and note `X-RateLimit-Limit`, `Remaining`, `Reset` (names may vary slightly).

**Expected result:** You can state how many calls remain in the window.

---

### Step 3 — Add retry logic (Python)

**Do this:** Save `retry_demo.py` from the slide deck / lab guide pattern: retry on `429` and `5xx`, honor `Retry-After`, do **not** retry most `4xx`.

Run against `/v1/models` with your user key.

**Expected result:** Script exits cleanly on `200`; on forced errors, backs off instead of crashing.

---

### Step 4 — Discuss client errors

**Do this:** With a partner, explain why `401` should not be retried with the same key.

**Expected result:** One-sentence rule: fix auth, then call again.

---

### Step 5 — Optional: slow down requests

**Do this:** Add `Start-Sleep -Seconds 3` between five curl calls in a loop.

**Expected result:** No `429` during normal class pacing.

**Success criteria:** Saw headers · retry on 429/5xx · no infinite retry on 401
"""
    ),
    "module-07/exercise-7.4-etag-caching.md": _steps(
        API_WIN
        + """
### Step 1 — First request (no cache)

**Do this:**

```powershell
curl.exe -s -D headers.txt -o body.json -u "$($env:CURSOR_ADMIN_API_KEY):" `
  https://api.cursor.com/v1/teams/members
Select-String -Path headers.txt -Pattern "ETag|HTTP/"
```

**Expected result:** `200` and an `ETag:` header value in `headers.txt`.

---

### Step 2 — Second request with If-None-Match

**Do this:** Copy the ETag value (without quotes issues), then:

```powershell
$etag = (Select-String -Path headers.txt -Pattern "^ETag:").Line.Split(":",2)[1].Trim()
curl.exe -s -D headers2.txt -o body2.json -u "$($env:CURSOR_ADMIN_API_KEY):" `
  -H "If-None-Match: $etag" https://api.cursor.com/v1/teams/members
Select-String -Path headers2.txt -Pattern "HTTP/"
```

**Expected result:** Often `304 Not Modified` (smaller/faster); same data as before.

---

### Step 3 — Python ETag helper (optional)

**Do this:** Implement `get_with_etag(url, previous_etag)` from the slides in a short script; call twice.

**Expected result:** Second call returns `None` for body on `304` and reuses cached JSON in code.

---

### Step 4 — When to use ETags

**Do this:** Name one Analytics or Admin poll that should use ETags (daily usage, member list).

**Expected result:** You save bandwidth on unchanged responses.

**Success criteria:** Captured ETag · got 200 then 304 · explained use case
"""
    ),
    "module-07/exercise-7.5-list-available-models.md": _steps(
        API_WIN
        + """
### Step 1 — List models with curl.exe

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" https://api.cursor.com/v1/models
```

**Expected result:** JSON listing model IDs (shape may be `items` or `data` — inspect once).

---

### Step 2 — Pretty-print in PowerShell

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" https://api.cursor.com/v1/models |
  ConvertFrom-Json | ConvertTo-Json -Depth 5
```

**Expected result:** Readable list in the console.

---

### Step 3 — Python table (optional)

**Do this:** Loop models and print columns: ID, context window, pricing if present.

**Expected result:** Table of at least 3 models.

---

### Step 4 — Pick a model for a task

**Do this:** Choose one model for “quick fix” and one for “hard refactor”; say why (speed vs quality).

**Expected result:** Two model names + one-line rationale each.

**Success criteria:** Listed models · formatted output · reasoned selection
"""
    ),
    "module-08/exercise-8.1-create-a-cloud-agent-via-api.md": _steps(
        API_WIN
        + """
### Step 1 — Set User API key

**Do this:**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_paste_your_key_here"
```

**Expected result:** Variable set for this PowerShell session.

---

### Step 2 — Create agent (POST)

**Do this:** Replace `YOUR_ORG/YOUR_REPO` with a repo you are allowed to use:

```powershell
$body = @{
  prompt = @{ text = "Add a README.md with setup instructions" }
  repos = @(@{ url = "https://github.com/YOUR_ORG/YOUR_REPO"; startingRef = "main" })
  autoCreatePR = $true
} | ConvertTo-Json -Depth 5

$response = curl.exe -s -X POST https://api.cursor.com/v1/agents `
  -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Content-Type: application/json" `
  -d $body | ConvertFrom-Json

$env:AGENT_ID = $response.agent.id
$env:RUN_ID = $response.run.id
Write-Host "Agent ID: $($env:AGENT_ID)"
Write-Host "Open: https://cursor.com/agents/$($env:AGENT_ID)"
```

**Expected result:** JSON with `agent.id` and `run.id`; dashboard shows **Running**.

---

### Step 3 — Confirm on dashboard

**Do this:** Open the printed URL in the browser.

**Expected result:** Same agent ID; log activity visible.

---

### Step 4 — Optional model in JSON

**Do this:** Add `"model": @{ id = "claude-4.6-sonnet" }` to `$body` and create a second test agent.

**Expected result:** Run uses the named model (or API error explaining restriction).

**Success criteria:** POST succeeded · IDs saved · visible on cursor.com/agents
"""
    ),
    "module-08/exercise-8.2-stream-agent-responses-sse.md": _steps(
        API_WIN
        + """
### Step 1 — Set IDs from Exercise 8.1

**Do this:**

```powershell
$env:AGENT_ID = "paste_agent_id"
$env:RUN_ID = "paste_run_id"
```

**Expected result:** Both variables set (from create-agent response or dashboard).

---

### Step 2 — Stream events (curl.exe)

**Do this:**

```powershell
curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Accept: text/event-stream" `
  "https://api.cursor.com/v1/agents/$($env:AGENT_ID)/runs/$($env:RUN_ID)/stream"
```

**Expected result:** Lines starting with `event:` and `data:` scroll in the terminal until the run finishes.

---

### Step 3 — Read the stream

**Do this:** Identify at least: one **assistant** text chunk, one **tool** or status event, and a **completed** or **failed** event.

**Expected result:** You can narrate what the agent did from the log alone.

---

### Step 4 — Resume with Last-Event-ID (concept)

**Do this:** Note an `id:` line from the stream; discuss reconnecting with header `Last-Event-ID` (see lab guide).

**Expected result:** You understand SSE resume after network drop.

**Success criteria:** Stream connected · parsed event types · IDs were set first
"""
    ),
    "module-08/exercise-8.3-list-and-download-artifacts.md": _steps(
        API_WIN
        + """
### Step 1 — Use a completed agent ID

**Do this:** Pick a **Completed** cloud agent from the dashboard (yours or demo).

```powershell
$env:AGENT_ID = "paste_completed_agent_id"
```

**Expected result:** Agent is not still running (artifacts ready).

---

### Step 2 — Poll status (optional)

**Do this:** Call status endpoint until `completed` (see lab guide Python `wait_for_completion`).

**Expected result:** You know how to wait programmatically.

---

### Step 3 — List artifacts

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  "https://api.cursor.com/v1/agents/$($env:AGENT_ID)/artifacts" | ConvertFrom-Json
```

**Expected result:** List of paths or artifact objects.

---

### Step 4 — Download one file

**Do this:** Request download URL for one path (per API docs in lab guide), then:

```powershell
curl.exe -L -o downloaded_file.txt "PASTE_PRESIGNED_URL"
```

**Expected result:** File on disk matches artifact from UI.

**Success criteria:** Listed artifacts · downloaded one file · understand wait/list/download order
"""
    ),
    "module-08/exercise-8.4-webhooks-and-hmac-verification.md": _steps(
        API_WIN
        + """
### Step 1 — Understand the webhook flow

**Do this:** Draw or describe: Cursor → HTTPS POST → your server → verify HMAC → return 200.

**Expected result:** You can explain why returning 200 quickly matters.

---

### Step 2 — Review verify_signature (Python)

**Do this:** Open the `verify_signature` snippet in the lab guide; identify: raw body, header name, secret.

**Expected result:** You know tampering breaks the HMAC match.

---

### Step 3 — Create agent with webhook URL (when server ready)

**Do this:** After Exercise 8.5 tunnel exists, POST agent JSON including `webhookUrl` (PowerShell `curl.exe` like 8.1).

**Expected result:** Agent accepts URL (or validation error you can fix).

---

### Step 4 — Security rules

**Do this:** List three checks: HTTPS, HMAC verify, idempotent handler.

**Expected result:** Checklist you would use in code review.

**Success criteria:** Explained flow · understand HMAC · ready for ngrok test in 8.5
"""
    ),
    "module-08/exercise-8.5-test-webhooks-with-ngrok.md": _steps(
        API_WIN
        + """
### Step 0 — Prerequisites

**Do this:** Complete webhook receiver setup from 8.4 (Flask/FastAPI on port **5000**). Install ngrok: [ngrok.com/download](https://ngrok.com/download) or `winget install ngrok.ngrok`.

**Expected result:** Local server responds on `http://127.0.0.1:5000/health` (or your route).

---

### Step 1 — Terminal A: run your webhook server

**Do this:** In PowerShell:

```powershell
cd D:/path/to/your/webhook-project
python -m flask run --port 5000
```

**Expected result:** Server listening on port 5000.

---

### Step 2 — Terminal B: start ngrok

**Do this:** New PowerShell window:

```powershell
ngrok http 5000
```

**Expected result:** Line like `Forwarding https://xxxx.ngrok-free.app -> http://localhost:5000`.

---

### Step 3 — Copy HTTPS URL

**Do this:** Copy the `https://....ngrok-free.app` URL; append your path, e.g. `/webhook/cursor`.

**Expected result:** Full webhook URL ready for agent create JSON.

---

### Step 4 — Create agent with webhook

**Do this:** POST `/v1/agents` with `webhookUrl` set to your ngrok URL (use `curl.exe` pattern from 8.1).

**Expected result:** Agent starts; your Flask terminal prints an incoming POST.

---

### Step 5 — Inspect in ngrok UI

**Do this:** Open [http://127.0.0.1:4040](http://127.0.0.1:4040) in the browser.

**Expected result:** Request list shows POST body and headers (including signature header).

**Success criteria:** Tunnel up · webhook received · verified or logged signature · inspected in ngrok UI
"""
    ),
    "module-09/exercise-9.1-list-team-members.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Set Admin API key

**Do this:**

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_paste_here"
```

**Expected result:** Key set for this session only.

---

### Step 2 — List team members

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  https://api.cursor.com/v1/teams/members | ConvertFrom-Json
```

**Expected result:** `200` and member records (emails, roles, etc.).

---

### Step 3 — Pagination

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/teams/members?limit=10&offset=0"
```

**Expected result:** First page of members; note if more pages needed.

---

### Step 4 — Export to CSV (optional)

**Do this:** Use lab guide Python to write `team_roster.csv`.

**Expected result:** CSV opens in Excel with columns you chose.

**Success criteria:** Admin auth works · listed members · tried pagination
"""
    ),
    "module-09/exercise-9.2-daily-usage-data.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Date range in PowerShell

**Do this:**

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-7).ToString("yyyy-MM-dd")
Write-Host "Start: $start End: $end"
```

**Expected result:** Seven-day window printed (not bash `date -d`).

---

### Step 2 — Fetch daily usage

**Do this:** Use the endpoint from your lab guide / course slides (Admin or Analytics daily usage). Example shape:

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/teams/daily-usage-data?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** JSON with per-day usage fields; adjust URL if instructor provides the canonical path.

---

### Step 3 — Interpret one day

**Do this:** Pick one date and read tokens, requests, or cost fields shown.

**Expected result:** You can explain one day’s usage in plain language.

---

### Step 4 — Optional report script

**Do this:** Sketch `generate_cost_report()` outputs (totals, top users) per lab guide.

**Expected result:** List of metrics you would show a manager.

**Success criteria:** Windows dates · API returned data · explained one day
"""
    ),
    "module-09/exercise-9.3-set-user-spend-limits.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Get a user ID

**Do this:** From 9.1 member list, copy one `userId` or email identifier.

```powershell
$env:TARGET_USER_ID = "paste_user_id"
```

**Expected result:** ID stored in a variable.

---

### Step 2 — Set spend limit

**Do this:** Call the spend-limit endpoint from the lab guide (POST/PATCH per current API docs), e.g. monthly cap in dollars.

**Expected result:** `200`/`204` or clear validation message.

---

### Step 3 — Verify in dashboard

**Do this:** Open team admin UI → member → spending limit.

**Expected result:** UI matches the limit you set (may take a minute).

---

### Step 4 — Bulk CSV format (discussion)

**Do this:** Review CSV columns: `email, monthly_limit_usd` from slides.

**Expected result:** You could automate onboarding limits from HR export.

**Success criteria:** Set one limit · verified · understand bulk pattern
"""
    ),
    "module-09/exercise-9.4-model-usage-analytics.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Date range

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
```

**Expected result:** 30-day window for analytics.

---

### Step 2 — Fetch model usage

**Do this:** Call team model-usage endpoint from lab guide:

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/team/models?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Per-model token or cost breakdown (field names per API response).

---

### Step 3 — Find top model

**Do this:** Identify highest-cost or highest-token model.

**Expected result:** One model name + number you can cite.

---

### Step 4 — Optimization idea

**Do this:** Write two bullets: what to change if costs are too high.

**Expected result:** Actionable suggestions (cheaper model for simple tasks, etc.).

**Success criteria:** Retrieved analytics · named top model · one optimization
"""
    ),
    "module-09/exercise-9.5-daily-active-users-dau.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Date range (7 days)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-7).ToString("yyyy-MM-dd")
```

---

### Step 2 — Fetch DAU

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/team/dau?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Daily active user counts per day.

---

### Step 3 — Trend

**Do this:** State whether DAU went up, down, or flat across the week.

**Expected result:** One-sentence trend for leadership.

**Success criteria:** DAU data retrieved · trend stated
"""
    ),
    "module-09/exercise-9.6-leaderboards.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Fetch leaderboard

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/team/leaderboard?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Ranked users by chosen metric (tokens, accepts, etc.).

---

### Step 2 — Privacy

**Do this:** Discuss anonymizing emails before showing leaderboard company-wide.

**Expected result:** Policy: hash or redact emails in exported reports.

---

### Step 3 — Use case

**Do this:** One appropriate use (adoption champion) and one inappropriate use (public shaming).

**Expected result:** Two clear examples.

**Success criteria:** Leaderboard data · privacy discussion · use cases
"""
    ),
    "module-10/exercise-10.1-ai-commit-metrics.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Date range (30 days)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
```

---

### Step 2 — Fetch commit metrics

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/commits?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Summary with AI vs human commit stats (field names per response).

---

### Step 3 — Calculate AI percentage

**Do this:** Compute `(ai_commits / total_commits) * 100` from summary fields.

**Expected result:** One percentage you can state aloud.

---

### Step 4 — ROI discussion

**Do this:** List inputs for ROI: lines saved, hourly cost, API spend (qualitative OK).

**Expected result:** Simple ROI story for a manager.

**Success criteria:** Metrics fetched · AI % calculated · ROI narrative
"""
    ),
    "module-10/exercise-10.2-bulk-export-via-csv-streaming.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Stream CSV download

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/commits.csv?startDate=$start&endDate=$end" `
  -o cursor_commits_export.csv
```

**Expected result:** File `cursor_commits_export.csv` created in current directory.

---

### Step 2 — Preview rows

```powershell
Get-Content .\cursor_commits_export.csv -Head 10
```

**Expected result:** Header row + data rows visible in PowerShell.

---

### Step 3 — Open in Excel

**Do this:** Double-click CSV or **Open with** Excel.

**Expected result:** Columns sortable; suitable for pivot tables.

**Success criteria:** CSV downloaded · previewed · opened in spreadsheet tool
"""
    ),
    "module-10/exercise-10.3-granular-ai-change-events.md": _steps(
        API_WIN.replace("CURSOR_USER", "CURSOR_ADMIN")
        + """
### Step 1 — Fetch change events

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-7).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/changes?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** List of granular edit events (file, lines, model, accepted flag).

---

### Step 2 — Acceptance rate

**Do this:** From one page of data, estimate accepted vs rejected ratio.

**Expected result:** Rough acceptance percentage.

---

### Step 3 — Compliance use case

**Do this:** Name one audit question this API can answer.

**Expected result:** e.g. “Which AI model edited file X on date Y?”

**Success criteria:** Events retrieved · acceptance discussed · compliance example
"""
    ),
    "module-10/exercise-10.4-reporting-dashboard-architecture.md": _steps(
        CLOUD_UI
        + """
### Step 1 — Review architecture options

**Do this:** Read the slide table: Streamlit vs Metabase vs custom frontend.

**Expected result:** You pick one option and justify for a small team.

---

### Step 2 — Define five panels

**Do this:** List five dashboard panels (DAU, model mix, AI %, spend, leaderboard).

**Expected result:** Each panel maps to an API from modules 9–10.

---

### Step 3 — Data flow

**Do this:** Sketch: nightly CSV export → database → dashboard refresh.

**Expected result:** One diagram or bullet pipeline.

---

### Step 4 — Windows setup for Streamlit (take-home)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install streamlit pandas requests
streamlit run dashboard.py
```

**Expected result:** Local dashboard URL opens in browser (when `dashboard.py` exists).

---

### Step 5 — Deliverables checklist

**Do this:** Note deliverables: working demo, setup doc, one insight, export script.

**Expected result:** Take-home scope is clear.

**Success criteria:** Architecture choice · five panels · data flow · optional Streamlit run
"""
    ),
}
