# Exercise 9.2: Daily Usage Data

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.2)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Pull daily usage and build a weekly cost report.

---

## API basics (read this first)

1. Use **PowerShell** or **Git Bash** in Cursor's terminal (``Ctrl+` ``).
2. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

3. Prefer `curl.exe` on Windows (not the `curl` alias) or Python `requests`.
4. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps from the training slides

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
END=$(date +%Y-%m-%d)
START=$(date -d "7 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '.daily[] | {date: .date, cost: .cost, tokens: .totalTokens, users: .activeUsers}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Python `generate_cost_report()` for last 30 days:

- Total cost · total tokens · average daily cost/users
- Week-over-week change · top 5 costliest days
- Daily breakdown table (last 14 days)
- Budget alerts at $300 / $500 thresholds

**Success Criteria:** Retrieved date range · calculated trends · generated readable report

---

## Success criteria

- [ ] Total cost · total tokens · average daily cost/users
- [ ] Week-over-week change · top 5 costliest days
- [ ] Daily breakdown table (last 14 days)
- [ ] Budget alerts at $300 / $500 thresholds
- [ ] Retrieved date range · calculated trends · generated readable report

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get Active Users Usage Data (2 minutes)

Get usage data for active users only (those with activity during the date range).

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/daily-usage-data \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": "7d",
    "endDate": "now"
  }' | jq '.'
```

**Expected response:**
```json
{
  "data": [
    {
      "userId": 12345,
      "day": "2025-01-15",
      "date": 1736928000000,
      "email": "alex@company.com",
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "bugbotUsages": 3,
      "mostUsedModel": "claude-4.5-sonnet",
      "clientVersion": "0.42.3"
    }
  ],
  "period": {
    "startDate": 1736294400000,
    "endDate": 1736899200000
  }
}
```

---

### Step 2: Get All Team Members with Pagination (3 minutes)

To get all team members (including inactive ones), use pagination parameters.

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/daily-usage-data \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": "7d",
    "endDate": "now",
    "page": 1,
    "pageSize": 100
  }' | jq '.'
```

**Note:** When using pagination, the response includes an `isActive` field for each user.

---

### Step 3: Calculate Team AI Acceptance Rate (3 minutes)

Calculate the percentage of AI-suggested lines that were accepted.

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/daily-usage-data \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": "7d",
    "endDate": "now"
  }' | jq '{
    total_lines_added: [.data[].totalLinesAdded] | add,
    total_lines_accepted: [.data[].acceptedLinesAdded] | add,
    acceptance_rate: (([.data[].acceptedLinesAdded] | add) / ([.data[].totalLinesAdded] | add) * 100 | floor)
  }'
```

**Expected output:**
```json
{
  "total_lines_added": 8234,
  "total_lines_accepted": 5891,
  "acceptance_rate": 71
}
```

---

### Step 4: Get Most Used Models (2 minutes)

Find the most popular AI models across your team.

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/daily-usage-data \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": "7d",
    "endDate": "now"
  }' | jq -r '.data[] | .mostUsedModel' | sort | uniq -c | sort -rn
```

**Expected output:**
```
  8 claude-4.5-sonnet
  3 gpt-5.2
  2 composer-2
  1 claude-4.7-opus
```

---

### Step 5: Get User-Specific Usage (Optional)

Filter usage data for a specific user.

**Command:**
```bash
# First get user email from team members
USER_EMAIL="alex@company.com"

curl -s -X POST https://api.cursor.com/teams/daily-usage-data \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": "7d",
    "endDate": "now"
  }' | jq --arg email "$USER_EMAIL" '.data[] | select(.email == $email)'
```

---

## Expected Output

### Step 1 Output:
```json
{
  "data": [
    {
      "userId": 12345,
      "day": "2025-01-15",
      "email": "alex@company.com",
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "bugbotUsages": 3,
      "mostUsedModel": "claude-4.5-sonnet"
    }
  ]
}
```

### Step 3 Output:
```json
{
  "total_lines_added": 8234,
  "total_lines_accepted": 5891,
  "acceptance_rate": 71
}
```

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `userId` | Unique identifier for the user |
| `day` | Date (ISO format) |
| `email` | User's email address |
| `isActive` | Whether user had activity (pagination only) |
| `totalLinesAdded` | Total lines of code added |
| `totalLinesDeleted` | Total lines of code deleted |
| `acceptedLinesAdded` | AI-suggested lines accepted |
| `totalTabsShown` | Tab completions shown |
| `totalTabsAccepted` | Tab completions accepted |
| `composerRequests` | Number of Composer/Agent requests |
| `chatRequests` | Number of chat requests |
| `bugbotUsages` | Number of Bugbot usages |
| `mostUsedModel` | Most frequently used AI model |
| `clientVersion` | Cursor client version |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Active vs All** | Without pagination = active users only. With pagination = all team members. |
| **Date range** | Maximum 30 days per request |
| **Polling frequency** | Data aggregated hourly – poll at most once per hour |
| **Rate limit** | 20 requests per minute per team |

---

## Success Criteria

- [ ] Retrieved active users usage data
- [ ] Retrieved all team members with pagination
- [ ] Calculated team AI acceptance rate
- [ ] Identified most used models
- [ ] Filtered usage for specific user

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key, not User API key |
| 403 Forbidden | Admin API requires Enterprise plan |
| No data returned | No activity in date range; try different dates |
| Date range error | Maximum 30 days; use smaller range |

---

## Bonus Challenge

Create a Python script to generate a weekly usage report:

```python
#!/usr/bin/env python3
"""
Generate weekly usage report
"""

import requests
import os
import sys
from datetime import datetime, timedelta

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

def get_usage_data(start_date, end_date):
    """Fetch usage data from API."""
    url = "https://api.cursor.com/teams/daily-usage-data"
    auth = (API_KEY, "")

    payload = {
        "startDate": start_date,
        "endDate": end_date
    }

    response = requests.post(url, auth=auth, json=payload)

    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        return None

    return response.json()

def generate_report(data):
    """Generate human-readable report."""
    if not data or not data.get("data"):
        print("No data available")
        return

    items = data["data"]

    total_lines = sum(i.get("totalLinesAdded", 0) for i in items)
    accepted_lines = sum(i.get("acceptedLinesAdded", 0) for i in items)
    tab_accepts = sum(i.get("totalTabsAccepted", 0) for i in items)
    agent_requests = sum(i.get("agentRequests", 0) for i in items)

    print("\n" + "=" * 50)
    print("📊 Cursor Weekly Usage Report")
    print("=" * 50)
    print(f"Period: {data.get('period', {}).get('startDate', 'N/A')} - {data.get('period', {}).get('endDate', 'N/A')}")
    print(f"Active users: {len(items)}")
    print("-" * 50)
    print(f"📝 Total lines added: {total_lines:,}")
    print(f"✅ AI lines accepted: {accepted_lines:,}")
    print(f"📈 Acceptance rate: {(accepted_lines / total_lines * 100) if total_lines > 0 else 0:.1f}%")
    print("-" * 50)
    print(f"🔧 Tab completions accepted: {tab_accepts:,}")
    print(f"🤖 Agent requests: {agent_requests:,}")
    print("=" * 50)

if __name__ == "__main__":
    end_date = "now"
    start_date = "7d"

    data = get_usage_data(start_date, end_date)
    if data:
        generate_report(data)
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved active users usage data
- [ ] Retrieved all team members with pagination
- [ ] Calculated team AI acceptance rate
- [ ] Identified most used models
- [ ] Filtered usage for specific user
- [ ] (Bonus) Created weekly report generator

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Terminal command fails on Windows | Use **PowerShell**; use `curl.exe` instead of `curl` |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
