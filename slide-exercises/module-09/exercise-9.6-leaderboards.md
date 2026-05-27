# Exercise 9.6: Leaderboards

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 9, Lesson 9.6)  
**Time:** 11 min  
**Difficulty:** Beginner

**Objective:** Build leaderboards for tabs, AI lines, and agent runs.

---

## API basics (read this first)

**Demonstration (Windows):** Use **PowerShell** in Cursor's terminal (``Ctrl+` ``).

1. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

2. Use **`curl.exe`** (not the `curl` alias) or Python `requests`.
3. Install **jq** for JSON parsing: `winget install jqlang.jq` or use Python instead.
4. Bash `curl` examples below each have a **PowerShell** equivalent — use those on Windows.
5. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps from the training slides

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**1. Engagement leaderboard** — rank by request count (anonymized emails)

**2. Efficiency leaderboard** — tokens per dollar spent

**3. Savings leaderboard** — users who saved by choosing efficient models over Opus

```python
def anonymize_email(email):
    local = email.split('@')[0]
    return local[:2] + "..." + local[-2:]
```

**Success Criteria:** Anonymized · efficiency-focused · savings-focused leaderboards

---

## Success criteria

- [ ] Anonymized · efficiency-focused · savings-focused leaderboards

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get Leaderboard (Default) (2 minutes)

Retrieve the default leaderboard (top 10 users by combined metrics).

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/leaderboard?startDate=30d&endDate=today" | jq '.'
```

**Expected response:**
```json
{
  "data": {
    "tab_leaderboard": {
      "data": [
        {
          "email": "alice@company.com",
          "user_id": "user_abc123",
          "profile_picture_url": "https://example.com/avatars/alice.jpg",
          "total_accepts": 1334,
          "total_lines_accepted": 3455,
          "total_lines_suggested": 15307,
          "line_acceptance_ratio": 0.2256,
          "accept_ratio": 0.2331,
          "rank": 1
        },
        {
          "email": "bob@company.com",
          "user_id": "user_def456",
          "profile_picture_url": "https://example.com/avatars/bob.jpg",
          "total_accepts": 796,
          "total_lines_accepted": 2090,
          "total_lines_suggested": 7689,
          "line_acceptance_ratio": 0.2718,
          "accept_ratio": 0.2731,
          "rank": 2
        }
      ],
      "total_users": 142
    },
    "agent_leaderboard": {
      "data": [
        {
          "email": "alice@company.com",
          "user_id": "user_abc123",
          "profile_picture_url": "https://example.com/avatars/alice.jpg",
          "total_accepts": 914,
          "total_lines_accepted": 65947,
          "total_lines_suggested": 201467,
          "line_acceptance_ratio": 0.3273,
          "rank": 1
        },
        {
          "email": "bob@company.com",
          "user_id": "user_def456",
          "profile_picture_url": "https://example.com/avatars/bob.jpg",
          "total_accepts": 843,
          "total_lines_accepted": 61709,
          "total_lines_suggested": 51092,
          "line_acceptance_ratio": 1.2078,
          "rank": 2
        }
      ],
      "total_users": 142
    }
  },
  "pagination": {
    "page": 1,
    "pageSize": 10,
    "totalUsers": 142,
    "totalPages": 15,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "leaderboard",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 10
  }
}
```

---

### Step 2: Get Top Tab Users (2 minutes)

Extract the top Tab completion users.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/leaderboard?startDate=30d&endDate=today&pageSize=5" | \
  jq '.data.tab_leaderboard.data[] | {rank, email, total_accepts, total_lines_accepted, accept_ratio}'
```

**Expected output:**
```json
{
  "rank": 1,
  "email": "alice@company.com",
  "total_accepts": 1334,
  "total_lines_accepted": 3455,
  "accept_ratio": 0.2331
}
{
  "rank": 2,
  "email": "bob@company.com",
  "total_accepts": 796,
  "total_lines_accepted": 2090,
  "accept_ratio": 0.2731
}
```

---

### Step 3: Get Top Agent Users (2 minutes)

Extract the top Agent edit users.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/leaderboard?startDate=30d&endDate=today&pageSize=5" | \
  jq '.data.agent_leaderboard.data[] | {rank, email, total_accepts, total_lines_accepted, line_acceptance_ratio}'
```

**Expected output:**
```json
{
  "rank": 1,
  "email": "alice@company.com",
  "total_accepts": 914,
  "total_lines_accepted": 65947,
  "line_acceptance_ratio": 0.3273
}
{
  "rank": 2,
  "email": "bob@company.com",
  "total_accepts": 843,
  "total_lines_accepted": 61709,
  "line_acceptance_ratio": 1.2078
}
```

---

### Step 4: Filter Leaderboard by Specific Users (2 minutes)

Get leaderboard data for specific users only.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/leaderboard?startDate=30d&endDate=today&users=alice@company.com,bob@company.com" | \
  jq '.data.tab_leaderboard.data[] | {email, rank, total_accepts}'
```

**Note:** When filtering by users, they appear with their actual team-wide rank (e.g., if Alice is #1 overall, she'll show rank 1).

---

### Step 5: Create Leaderboard Report Script (2 minutes)

**Create `leaderboard_report.py`:**
```python
#!/usr/bin/env python3
"""
Leaderboard Report - Track top users by AI usage
"""

import requests
import os
import sys
from datetime import datetime
import json

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class LeaderboardReport:
    """Generate leaderboard reports"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_leaderboard(self, start_date="30d", end_date="today", page=1, page_size=20):
        """Get leaderboard data."""
        url = f"{self.base_url}/analytics/team/leaderboard"
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "page": page,
            "pageSize": page_size
        }
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def generate_report(self, start_date="30d", end_date="today"):
        """Generate a complete leaderboard report."""
        print(f"\n🏆 Cursor Leaderboard Report")
        print(f"Period: {start_date} to {end_date}")
        print("=" * 60)
        
        data = self.get_leaderboard(start_date, end_date)
        
        if not data:
            return
        
        # Tab Leaderboard
        tab_data = data.get("data", {}).get("tab_leaderboard", {})
        tab_users = tab_data.get("data", [])
        tab_total = tab_data.get("total_users", 0)
        
        print(f"\n📋 TAB COMPLETIONS LEADERBOARD")
        print(f"Total users: {tab_total}")
        print("-" * 60)
        print(f"{'Rank':<6} {'User':<30} {'Accepts':>10} {'Lines':>10} {'Accept %':>10}")
        print("-" * 60)
        
        for user in tab_users[:10]:  # Top 10
            rank = user.get('rank')
            email = user.get('email', 'N/A')[:28]
            accepts = user.get('total_accepts', 0)
            lines = user.get('total_lines_accepted', 0)
            accept_pct = user.get('accept_ratio', 0) * 100
            print(f"{rank:<6} {email:<30} {accepts:>10,} {lines:>10,} {accept_pct:>9.1f}%")
        
        # Agent Leaderboard
        agent_data = data.get("data", {}).get("agent_leaderboard", {})
        agent_users = agent_data.get("data", [])
        agent_total = agent_data.get("total_users", 0)
        
        print(f"\n🤖 AGENT EDITS LEADERBOARD")
        print(f"Total users: {agent_total}")
        print("-" * 60)
        print(f"{'Rank':<6} {'User':<30} {'Accepts':>10} {'Lines':>10} {'Line Accept %':>12}")
        print("-" * 60)
        
        for user in agent_users[:10]:  # Top 10
            rank = user.get('rank')
            email = user.get('email', 'N/A')[:28]
            accepts = user.get('total_accepts', 0)
            lines = user.get('total_lines_accepted', 0)
            line_accept_pct = user.get('line_acceptance_ratio', 0) * 100
            print(f"{rank:<6} {email:<30} {accepts:>10,} {lines:>10,} {line_accept_pct:>11.1f}%")
        
        # Pagination info
        pagination = data.get("pagination", {})
        print(f"\n📄 Page {pagination.get('page', 1)} of {pagination.get('totalPages', 1)}")
        print(f"   Showing top {len(tab_users)} of {tab_total} users")
        
        return data
    
    def get_user_rank(self, email, start_date="30d", end_date="today"):
        """Get rank for a specific user."""
        data = self.get_leaderboard(start_date, end_date, page=1, page_size=500)
        
        if not data:
            return None
        
        # Search in tab leaderboard
        for user in data.get("data", {}).get("tab_leaderboard", {}).get("data", []):
            if user.get("email") == email:
                return {
                    "tab_rank": user.get("rank"),
                    "tab_accepts": user.get("total_accepts"),
                    "tab_lines": user.get("total_lines_accepted")
                }
        
        return None
    
    def get_top_performers(self, metric="lines", limit=5):
        """Get top performers by a specific metric."""
        data = self.get_leaderboard(page=1, page_size=limit)
        
        if not data:
            return []
        
        tab_users = data.get("data", {}).get("tab_leaderboard", {}).get("data", [])
        
        if metric == "accepts":
            return sorted(tab_users, key=lambda x: x.get("total_accepts", 0), reverse=True)[:limit]
        elif metric == "lines":
            return sorted(tab_users, key=lambda x: x.get("total_lines_accepted", 0), reverse=True)[:limit]
        elif metric == "ratio":
            return sorted(tab_users, key=lambda x: x.get("accept_ratio", 0), reverse=True)[:limit]
        
        return tab_users[:limit]

def main():
    print("🚀 Leaderboard Report Generator")
    print("=" * 40)
    
    report = LeaderboardReport()
    
    # Generate full report
    report.generate_report("30d", "today")
    
    # Get top performers by lines accepted
    print("\n🏅 Top Performers (by lines accepted)")
    print("-" * 40)
    top_users = report.get_top_performers(metric="lines", limit=5)
    for i, user in enumerate(top_users, 1):
        print(f"   {i}. {user.get('email')}: {user.get('total_lines_accepted', 0):,} lines")
    
    # Get a specific user's rank
    print("\n🔍 Check your rank (replace with your email)")
    # user_rank = report.get_user_rank("your-email@company.com")
    # if user_rank:
    #     print(f"   Tab rank: #{user_rank['tab_rank']}")
    #     print(f"   Tab accepts: {user_rank['tab_accepts']}")
    #     print(f"   Tab lines: {user_rank['tab_lines']}")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 Leaderboard Report Generator
========================================

🏆 Cursor Leaderboard Report
Period: 30d to today
============================================================

📋 TAB COMPLETIONS LEADERBOARD
Total users: 142
------------------------------------------------------------
Rank   User                           Accepts      Lines   Accept %
------------------------------------------------------------
1      alice@company.com                 1,334      3,455      23.3%
2      bob@company.com                     796      2,090      27.3%
3      carol@company.com                   654      1,890      24.1%
4      dave@company.com                    521      1,234      22.8%
5      eve@company.com                     498      1,102      21.5%

🤖 AGENT EDITS LEADERBOARD
Total users: 142
------------------------------------------------------------
Rank   User                           Accepts      Lines   Line Accept %
------------------------------------------------------------
1      alice@company.com                   914     65,947        32.7%
2      bob@company.com                     843     61,709       120.8%
3      carol@company.com                   712     54,321        34.2%
4      dave@company.com                    598     43,210        29.8%
5      eve@company.com                     445     32,109        27.6%

📄 Page 1 of 15
   Showing top 10 of 142 users

🏅 Top Performers (by lines accepted)
----------------------------------------
   1. alice@company.com: 3,455 lines
   2. bob@company.com: 2,090 lines
   3. carol@company.com: 1,890 lines
   4. dave@company.com: 1,234 lines
   5. eve@company.com: 1,102 lines
```

---

## Response Fields Reference

### Tab Leaderboard Fields

| Field | Description |
|-------|-------------|
| `email` | User's email address |
| `user_id` | Encoded user ID |
| `total_accepts` | Number of Tab completions accepted |
| `total_lines_accepted` | Lines accepted via Tab |
| `total_lines_suggested` | Lines suggested by Tab |
| `accept_ratio` | Acceptance rate (accepts / suggestions) |
| `line_acceptance_ratio` | Lines accepted / lines suggested |
| `rank` | User's rank (1 = best) |

### Agent Leaderboard Fields

| Field | Description |
|-------|-------------|
| `total_accepts` | Number of Agent edits accepted |
| `total_lines_accepted` | Lines accepted via Agent |
| `line_acceptance_ratio` | Lines accepted / lines suggested |

---

## Success Criteria

- [ ] Retrieved default leaderboard
- [ ] Extracted top Tab users
- [ ] Extracted top Agent users
- [ ] Filtered leaderboard by specific users
- [ ] Created leaderboard report script
- [ ] Generated top performers list

---

## Important Notes

| Note | Description |
|------|-------------|
| **Filtered users show actual rank** | They appear with team-wide rank, not filtered rank |
| **Two separate leaderboards** | Tab completions and Agent edits are separate |
| **Pagination** | Use `page` and `pageSize` for large teams |
| **Default pageSize** | 10 users per page |
| **Max pageSize** | 500 users per page |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data | Team may have no activity in date range |
| 403 Forbidden | Enterprise plan required |
| User not found in filter | Check email spelling or user ID format |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved default leaderboard
- [ ] Extracted top Tab users
- [ ] Extracted top Agent users
- [ ] Filtered by specific users
- [ ] Created report script
- [ ] Generated top performers list

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
