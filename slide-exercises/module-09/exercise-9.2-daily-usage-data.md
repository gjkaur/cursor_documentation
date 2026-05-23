# Exercise 9.2: Daily Usage Data

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.2)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Pull daily usage and build a weekly cost report.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

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

---

## Success criteria

- [ ] Total cost · total tokens · average daily cost/users
- [ ] Week-over-week change · top 5 costliest days
- [ ] Daily breakdown table (last 14 days)
- [ ] Budget alerts at $300 / $500 thresholds
- [ ] Retrieved date range · calculated trends · generated readable report

---

## Additional reference

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
