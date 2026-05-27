# Simplified step bodies for modules 7–10 (shorter, fewer steps, PowerShell-first).

def build_steps(api_win, admin, cloud_ui, _steps):
    """Re-exported by apply-easy-steps-modules-7-10.py."""
    return {
        "module-07/exercise-7.2-generate-and-test-api-keys.md": _steps(
            api_win
            + """
### Step 1 — Create and store your User API key

**Do this:** Cursor **Settings** → **API Keys** → **Generate** → copy once, then:

```powershell
$env:CURSOR_USER_API_KEY = "cursor_paste_your_key_here"
```

**Expected result:** Key saved in `$env:` for this terminal only (not in git).

---

### Step 2 — Test the key with one curl call

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" https://api.cursor.com/v1/models
```

**Expected result:** JSON model list — not `401 Unauthorized`.

---

### Step 3 — Admin key (only if you have Enterprise Admin API)

**Do this:**

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_paste_here"
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" https://api.cursor.com/v1/teams/members
```

**Expected result:** `200` with team data, or your instructor explains your plan uses User key only.

**Success criteria:** User key works · keys stay in `$env:` only
"""
        ),
        "module-07/exercise-7.3-rate-limits-and-error-handling.md": _steps(
            api_win
            + """
### Step 1 — Make one successful Admin API call

**Do this:**

```powershell
curl.exe -s -D - -o NUL -u "$($env:CURSOR_ADMIN_API_KEY):" `
  https://api.cursor.com/v1/teams/members 2>&1 | Select-String "HTTP/"
```

**Expected result:** Line containing `HTTP/1.1 200`.

---

### Step 2 — Know the common status codes

**Do this:** Learn these three:

- **401** — bad or missing API key → fix `$env:CURSOR_*_API_KEY` (do **not** retry blindly)
- **429** — too many requests → wait, then retry with backoff
- **5xx** — server error → retry a few times with delay

**Expected result:** You can explain why `401` is different from `429`.

---

### Step 3 — Retry rule (discussion)

**Do this:** Say out loud: “Retry on **429** and **5xx**; fix auth on **401**.”

**Expected result:** One-sentence rule you would use in a script (Python examples optional in **Detailed reference**).

**Success criteria:** Got `200` once · explained 401 vs 429
"""
        ),
        "module-07/exercise-7.4-etag-caching.md": _steps(
            api_win.replace("CURSOR_USER", "CURSOR_ADMIN")
            + """
### Step 1 — First request: save the ETag

**Do this:**

```powershell
curl.exe -s -D headers.txt -o body.json -u "$($env:CURSOR_ADMIN_API_KEY):" `
  https://api.cursor.com/v1/teams/members
Select-String -Path headers.txt -Pattern "ETag|HTTP/"
```

**Expected result:** `200` and an `ETag:` line in `headers.txt`.

---

### Step 2 — Second request: send If-None-Match

**Do this:**

```powershell
$etag = (Select-String -Path headers.txt -Pattern "^ETag:").Line.Split(":",2)[1].Trim()
curl.exe -s -D headers2.txt -o body2.json -u "$($env:CURSOR_ADMIN_API_KEY):" `
  -H "If-None-Match: $etag" https://api.cursor.com/v1/teams/members
Select-String -Path headers2.txt -Pattern "HTTP/"
```

**Expected result:** Often `304 Not Modified` — same data, less bandwidth.

---

### Step 3 — When to use ETags

**Do this:** Name one report you would poll often (member list, daily usage).

**Expected result:** You skip re-downloading when nothing changed.

**Success criteria:** Saw ETag · tried If-None-Match · named a use case
"""
        ),
        "module-07/exercise-7.5-list-available-models.md": _steps(
            api_win
            + """
### Step 1 — List models

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" https://api.cursor.com/v1/models |
  ConvertFrom-Json | ConvertTo-Json -Depth 3
```

**Expected result:** Readable JSON in the console.

---

### Step 2 — Pick two models

**Do this:** Choose one model for a **quick fix** and one for a **hard refactor**; write one reason each.

**Expected result:** Two model names + short rationale.

**Success criteria:** Listed models · reasoned choice
"""
        ),
        "module-08/exercise-8.1-create-a-cloud-agent-via-api.md": _steps(
            api_win
            + """
### Step 1 — Set key and create an agent

**Do this:** Replace `YOUR_ORG/YOUR_REPO`, then run:

```powershell
$env:CURSOR_USER_API_KEY = "cursor_paste_your_key_here"
$body = '{"prompt":{"text":"Add a short README with setup steps"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":false}'
$r = curl.exe -s -X POST https://api.cursor.com/v1/agents -u "$($env:CURSOR_USER_API_KEY):" -H "Content-Type: application/json" -d $body | ConvertFrom-Json
$env:AGENT_ID = $r.agent.id
Write-Host "https://cursor.com/agents/$($env:AGENT_ID)"
```

**Expected result:** Agent ID printed; dashboard shows **Running**.

---

### Step 2 — Watch on the dashboard

**Do this:** Open the printed URL in Edge or Chrome.

**Expected result:** Log lines move; status becomes **Completed** or **Failed**.

**Success criteria:** POST worked · opened dashboard
"""
        ),
        "module-08/exercise-8.2-stream-agent-responses-sse.md": _steps(
            api_win
            + """
### Step 1 — Set agent and run IDs

**Do this:** From Exercise 8.1 (or dashboard):

```powershell
$env:AGENT_ID = "paste_agent_id"
$env:RUN_ID = "paste_run_id"
```

**Expected result:** Both variables set.

---

### Step 2 — Stream for one minute

**Do this:**

```powershell
curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" -H "Accept: text/event-stream" `
  "https://api.cursor.com/v1/agents/$($env:AGENT_ID)/runs/$($env:RUN_ID)/stream"
```

Press **Ctrl+C** after ~60 seconds if the run is long.

**Expected result:** Lines with `event:` and `data:` appear in the terminal.

---

### Step 3 — Name what you saw

**Do this:** Point to one **status** event and one **message** or **tool** event in the output.

**Expected result:** You can tell the story of the run without opening the UI.

**Success criteria:** Stream connected · named two event types
"""
        ),
        "module-08/exercise-8.3-list-and-download-artifacts.md": _steps(
            api_win
            + """
### Step 1 — Open a completed agent

**Do this:** In [cursor.com/agents](https://cursor.com/agents), pick a **Completed** run (yours from 8.1 or a demo).

**Expected result:** **Artifacts** tab or file list is visible.

---

### Step 2 — Download in the UI

**Do this:** Download **one file**, then **Download all** (zip) if available.

**Expected result:** Files in your **Downloads** folder.

---

### Step 3 — Optional: list via API

**Do this:**

```powershell
$env:AGENT_ID = "paste_completed_agent_id"
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  "https://api.cursor.com/v1/agents/$($env:AGENT_ID)/artifacts"
```

**Expected result:** JSON list of artifact paths (same as UI).

**Success criteria:** Saw artifacts in UI · downloaded at least one file
"""
        ),
        "module-08/exercise-8.4-webhooks-and-hmac-verification.md": _steps(
            api_win
            + """
### Step 1 — Webhook flow (30 seconds)

**Do this:** Finish this sentence: “When the agent finishes, Cursor sends an HTTPS **POST** to my URL with a signed body; I verify **HMAC** and return **200**.”

**Expected result:** You can draw: Cursor → your server → 200 OK.

---

### Step 2 — Three security checks

**Do this:** List: (1) HTTPS only, (2) verify signature, (3) handle duplicates safely.

**Expected result:** Checklist of three items.

---

### Step 3 — Prepare for ngrok (next lab)

**Do this:** Confirm you have a tiny webhook app on port **5000** (from lab guide) or will pair with a demo.

**Expected result:** Ready for Exercise 8.5 tunnel test.

**Success criteria:** Explained flow · three security checks · ready for 8.5
"""
        ),
        "module-08/exercise-8.5-test-webhooks-with-ngrok.md": _steps(
            api_win
            + """
### Step 1 — Start your webhook server (Terminal A)

**Do this:**

```powershell
cd D:/path/to/webhook-project
python -m flask run --port 5000
```

**Expected result:** Server listening on port 5000.

---

### Step 2 — Start ngrok (Terminal B)

**Do this:**

```powershell
ngrok http 5000
```

Copy the `https://....ngrok-free.app` URL + your path (e.g. `/webhook/cursor`).

**Expected result:** Public HTTPS URL you can paste into agent JSON.

---

### Step 3 — Trigger a webhook

**Do this:** Create a cloud agent (8.1 pattern) with `"webhookUrl": "https://YOUR-NGROK-URL/webhook/cursor"` in the JSON body.

**Expected result:** Terminal A prints an incoming POST; [http://127.0.0.1:4040](http://127.0.0.1:4040) shows the request.

**Success criteria:** ngrok tunnel up · webhook received once
"""
        ),
        "module-09/exercise-9.1-list-team-members.md": _steps(
            admin
            + """
### Step 1 — Set Admin key

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_paste_here"
```

**Expected result:** Variable set for this session.

---

### Step 2 — List members

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  https://api.cursor.com/v1/teams/members | ConvertFrom-Json
```

**Expected result:** `200` and a list of team members.

**Success criteria:** Admin key works · saw member list
"""
        ),
        "module-09/exercise-9.2-daily-usage-data.md": _steps(
            admin
            + """
### Step 1 — Last 7 days (PowerShell dates)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-7).ToString("yyyy-MM-dd")
Write-Host "$start to $end"
```

**Expected result:** Date range printed.

---

### Step 2 — Fetch usage

**Do this:** Call the daily-usage endpoint from your instructor (URL on slides):

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/teams/daily-usage-data?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** JSON with per-day usage you can read aloud.

---

### Step 3 — Explain one day

**Do this:** Pick one date and describe tokens or cost in plain language.

**Expected result:** One sentence a manager would understand.

**Success criteria:** Dates in PowerShell · data returned · one-day summary
"""
        ),
        "module-09/exercise-9.3-set-user-spend-limits.md": _steps(
            admin
            + """
### Step 1 — Pick a user ID

**Do this:** From Exercise 9.1 output, copy one `userId`:

```powershell
$env:TARGET_USER_ID = "paste_user_id"
```

**Expected result:** ID in a variable.

---

### Step 2 — Set a limit (follow instructor URL)

**Do this:** Use the spend-limit API from slides/lab guide (POST or PATCH with a monthly cap).

**Expected result:** `200`/`204` or a clear error you can fix.

---

### Step 3 — Confirm in admin UI

**Do this:** Open team settings → member → spending.

**Expected result:** Limit matches what you set.

**Success criteria:** Set one limit · verified in UI
"""
        ),
        "module-09/exercise-9.4-model-usage-analytics.md": _steps(
            admin
            + """
### Step 1 — Date range (30 days)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
```

---

### Step 2 — Fetch model usage

```powershell
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/team/models?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Per-model usage you can scan in the console.

---

### Step 3 — One optimization

**Do this:** Name the **top** model and one way to reduce cost (e.g. cheaper model for small tasks).

**Expected result:** Model name + one actionable tip.

**Success criteria:** Data retrieved · one optimization idea
"""
        ),
        "module-09/exercise-9.5-daily-active-users-dau.md": _steps(
            admin
            + """
### Step 1 — Fetch DAU (7 days)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-7).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/team/dau?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Daily active user counts.

---

### Step 2 — Trend in one sentence

**Do this:** Say if DAU went **up**, **down**, or **flat** this week.

**Expected result:** One line for leadership.

**Success criteria:** DAU data · trend stated
"""
        ),
        "module-09/exercise-9.6-leaderboards.md": _steps(
            admin
            + """
### Step 1 — Fetch leaderboard

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/team/leaderboard?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Ranked usage data.

---

### Step 2 — Privacy and purpose

**Do this:** Give one **good** use (adoption coaching) and one **bad** use (public shaming); mention anonymizing emails.

**Expected result:** Two examples + privacy note.

**Success criteria:** Leaderboard data · responsible use discussed
"""
        ),
        "module-10/exercise-10.1-ai-commit-metrics.md": _steps(
            admin
            + """
### Step 1 — Fetch AI commit metrics (30 days)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/commits?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** Summary with AI vs human commit fields.

---

### Step 2 — State AI percentage

**Do this:** Compute or read `(AI commits / total commits) × 100` from the response.

**Expected result:** One percentage you can say aloud.

**Success criteria:** Metrics fetched · AI % stated
"""
        ),
        "module-10/exercise-10.2-bulk-export-via-csv-streaming.md": _steps(
            admin
            + """
### Step 1 — Download CSV

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/commits.csv?startDate=$start&endDate=$end" `
  -o cursor_commits_export.csv
```

**Expected result:** File `cursor_commits_export.csv` in the current folder.

---

### Step 2 — Preview and open

```powershell
Get-Content ./cursor_commits_export.csv -Head 5
```

**Do this:** Open the file in Excel.

**Expected result:** Header row + data; columns sortable.

**Success criteria:** CSV saved · opened in a spreadsheet
"""
        ),
        "module-10/exercise-10.3-granular-ai-change-events.md": _steps(
            admin
            + """
### Step 1 — Fetch change events (7 days)

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-7).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/changes?startDate=$start&endDate=$end" |
  ConvertFrom-Json
```

**Expected result:** List of per-edit events (file, model, accepted, etc.).

---

### Step 2 — Compliance question

**Do this:** Name one audit question this data answers (e.g. “What AI model touched file X?”).

**Expected result:** One clear compliance or governance use case.

**Success criteria:** Events retrieved · one audit use case
"""
        ),
        "module-10/exercise-10.4-reporting-dashboard-architecture.md": _steps(
            cloud_ui
            + """
### Step 1 — Pick a dashboard approach

**Do this:** Choose one: **Streamlit** (fast Python), **Metabase** (BI), or **custom** — one reason why.

**Expected result:** One choice + one sentence justification.

---

### Step 2 — Map five panels to APIs

**Do this:** List five panels (e.g. DAU, model mix, AI %, spend, top users) and which Module 9–10 API feeds each.

**Expected result:** Five rows: panel name → API endpoint family.

---

### Step 3 — Data flow (take-home)

**Do this:** Sketch: nightly **CSV export** → database or folder → dashboard refresh.

**Expected result:** Three-step pipeline in bullets (detail optional in **Detailed reference**).

**Success criteria:** Tool choice · five panels mapped · data flow sketched
"""
        ),
    }
