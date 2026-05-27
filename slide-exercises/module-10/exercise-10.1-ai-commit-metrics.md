# Exercise 10.1: AI Commit Metrics

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 10, Lesson 10.1)  
**Time:** 8 min  
**Difficulty:** Beginner

**Objective:** Fetch AI commit metrics and calculate contribution percentage.

---

## API basics (read this first)

**Windows:** PowerShell (``Ctrl+` ``) · **`curl.exe`** · store keys in `$env:` — **never** commit keys to git.

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"   # Admin labs (9–10)
```

More examples (Python, jq, bash): see **Detailed reference** below — optional for class.

---

## Steps from the training slides

**Environment:** Windows · PowerShell (``Ctrl+` ``) · **`curl.exe`** · keys in `$env:` only (never commit).

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"  # Modules 9–10
```

Follow each step in order. Confirm the **Expected result** before moving on.

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
---

## Success criteria

- [ ] Retrieved metrics · calculated AI % · generated ROI analysis

---

> **Note:** The section below is optional deep dive — not required to finish the in-class steps.

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan (AI Code Tracking API)
- [ ] Git repository with Cursor-tracked commits
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get AI Commit Metrics (2 minutes)

Retrieve commit metrics with AI attribution.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=10" | jq '.'
```

**Expected response:**
```json
{
  "items": [
    {
      "commitHash": "a1b2c3d4e5f6",
      "userId": "user_3k9x8q7w6e",
      "userEmail": "alice@company.com",
      "repoName": "company/main-app",
      "branchName": "main",
      "isPrimaryBranch": true,
      "commitSource": "ide",
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Add new feature with error handling",
      "commitTs": "2025-01-15T14:12:03.000Z",
      "createdAt": "2025-01-15T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 10
}
```

---

### Step 2: Calculate AI Contribution Percentage (2 minutes)

Compute what percentage of code was written by AI.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=30d&endDate=now&pageSize=100" | \
  jq '{
    total_lines: ([.items[].totalLinesAdded] | add),
    ai_lines: ([.items[].tabLinesAdded] | add) + ([.items[].composerLinesAdded] | add),
    ai_percentage: ((([.items[].tabLinesAdded] | add) + ([.items[].composerLinesAdded] | add)) / ([.items[].totalLinesAdded] | add) * 100 | floor)
  }'
```

**Expected output:**
```json
{
  "total_lines": 15234,
  "ai_lines": 9876,
  "ai_percentage": 64
}
```

---

### Step 3: Break Down by AI Source (2 minutes)

Separate Tab completions from Agent edits.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=30d&endDate=now&pageSize=100" | \
  jq '{
    tab_lines: ([.items[].tabLinesAdded] | add),
    composer_lines: ([.items[].composerLinesAdded] | add),
    tab_percentage: (([.items[].tabLinesAdded] | add) / ([.items[].totalLinesAdded] | add) * 100 | floor),
    composer_percentage: (([.items[].composerLinesAdded] | add) / ([.items[].totalLinesAdded] | add) * 100 | floor)
  }'
```

**Expected output:**
```json
{
  "tab_lines": 4567,
  "composer_lines": 5309,
  "tab_percentage": 30,
  "composer_percentage": 35
}
```

---

### Step 4: Filter by Specific User (2 minutes)

Get AI commit metrics for a specific developer.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=30d&endDate=now&user=alice@company.com&pageSize=50" | \
  jq '{
    user: (.items[0].userEmail // "N/A"),
    total_commits: .totalCount,
    ai_percentage: ((([.items[].tabLinesAdded] | add) + ([.items[].composerLinesAdded] | add)) / ([.items[].totalLinesAdded] | add) * 100 | floor)
  }'
```

---

### Step 5: Create AI Commit Metrics Report (2 minutes)

**Create `ai_commit_report.py`:**
```python
#!/usr/bin/env python3
"""
AI Commit Metrics Report - Track AI-generated code in commits
"""

import requests
import os
import sys
from datetime import datetime, timedelta
import json

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class AICommitMetrics:
    """AI Commit Metrics Analytics"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_commits(self, start_date="7d", end_date="now", page=1, page_size=100, user=None):
        """Get AI commit metrics."""
        url = f"{self.base_url}/analytics/ai-code/commits"
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "page": page,
            "pageSize": page_size
        }
        
        if user:
            params["user"] = user
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def calculate_summary(self, commits_data):
        """Calculate summary statistics from commit data."""
        if not commits_data or not commits_data.get("items"):
            return None
        
        items = commits_data["items"]
        
        total_lines = sum(c.get("totalLinesAdded", 0) for c in items)
        tab_lines = sum(c.get("tabLinesAdded", 0) for c in items)
        composer_lines = sum(c.get("composerLinesAdded", 0) for c in items)
        ai_lines = tab_lines + composer_lines
        non_ai_lines = sum(c.get("nonAiLinesAdded", 0) for c in items)
        
        return {
            "total_commits": commits_data.get("totalCount", 0),
            "total_lines": total_lines,
            "tab_lines": tab_lines,
            "composer_lines": composer_lines,
            "ai_lines": ai_lines,
            "non_ai_lines": non_ai_lines,
            "ai_percentage": (ai_lines / total_lines * 100) if total_lines > 0 else 0,
            "tab_percentage": (tab_lines / total_lines * 100) if total_lines > 0 else 0,
            "composer_percentage": (composer_lines / total_lines * 100) if total_lines > 0 else 0
        }
    
    def generate_report(self, start_date="30d", end_date="now"):
        """Generate a complete AI commit report."""
        print(f"\n📊 AI Commit Metrics Report")
        print(f"Period: {start_date} to {end_date}")
        print("=" * 60)
        
        data = self.get_commits(start_date, end_date, page_size=500)
        
        if not data:
            print("No commit data available")
            return
        
        summary = self.calculate_summary(data)
        
        if not summary:
            print("No commits found in period")
            return
        
        print(f"\n📈 Overall Statistics")
        print("-" * 40)
        print(f"   Total commits: {summary['total_commits']:,}")
        print(f"   Total lines added: {summary['total_lines']:,}")
        print(f"   AI-generated lines: {summary['ai_lines']:,}")
        print(f"   Human-written lines: {summary['non_ai_lines']:,}")
        
        print(f"\n🤖 AI Contribution Breakdown")
        print("-" * 40)
        print(f"   Tab completions: {summary['tab_lines']:,} ({summary['tab_percentage']:.1f}%)")
        print(f"   Agent edits: {summary['composer_lines']:,} ({summary['composer_percentage']:.1f}%)")
        print(f"   Total AI: {summary['ai_percentage']:.1f}%")
        
        # Visual bar
        ai_pct = summary['ai_percentage']
        bar_length = int(ai_pct / 2)
        human_pct = 100 - ai_pct
        bar = "█" * bar_length + "░" * (50 - bar_length)
        print(f"\n   AI vs Human: [{bar}]")
        print(f"   {'AI':<10} {ai_pct:.1f}%{' ' * (int(ai_pct/2)-2)}{'Human':>10} {human_pct:.1f}%")
        
        # Commits by source
        print(f"\n📝 Commit Source Breakdown")
        print("-" * 40)
        sources = {}
        for commit in data.get("items", []):
            source = commit.get("commitSource", "unknown")
            sources[source] = sources.get(source, 0) + 1
        
        for source, count in sources.items():
            pct = (count / summary['total_commits'] * 100) if summary['total_commits'] > 0 else 0
            print(f"   {source}: {count} ({pct:.1f}%)")
        
        return summary
    
    def get_user_breakdown(self, start_date="30d", end_date="now"):
        """Get AI metrics broken down by user."""
        data = self.get_commits(start_date, end_date, page_size=1000)
        
        if not data:
            return {}
        
        user_stats = {}
        
        for commit in data.get("items", []):
            email = commit.get("userEmail", "unknown")
            if email not in user_stats:
                user_stats[email] = {
                    "total_lines": 0,
                    "tab_lines": 0,
                    "composer_lines": 0,
                    "commits": 0
                }
            
            user_stats[email]["total_lines"] += commit.get("totalLinesAdded", 0)
            user_stats[email]["tab_lines"] += commit.get("tabLinesAdded", 0)
            user_stats[email]["composer_lines"] += commit.get("composerLinesAdded", 0)
            user_stats[email]["commits"] += 1
        
        # Calculate percentages
        for email, stats in user_stats.items():
            ai_lines = stats["tab_lines"] + stats["composer_lines"]
            stats["ai_percentage"] = (ai_lines / stats["total_lines"] * 100) if stats["total_lines"] > 0 else 0
        
        return user_stats

def main():
    print("🚀 AI Commit Metrics")
    print("=" * 40)
    
    metrics = AICommitMetrics()
    
    # Generate report for last 30 days
    summary = metrics.generate_report("30d", "now")
    
    # Get user breakdown
    print(f"\n👥 User Breakdown (Top 10 by AI usage)")
    print("-" * 40)
    
    user_stats = metrics.get_user_breakdown("30d", "now")
    
    # Sort by AI percentage
    sorted_users = sorted(user_stats.items(), key=lambda x: x[1]["ai_percentage"], reverse=True)
    
    for i, (email, stats) in enumerate(sorted_users[:10], 1):
        print(f"   {i}. {email[:25]:<25} {stats['ai_percentage']:>5.1f}% AI ({stats['commits']} commits)")
    
    print(f"\n💡 Tip: AI percentage shows what portion of code was AI-generated")
    print("   Tab = inline completions, Composer = Agent edits")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 AI Commit Metrics
========================================

📊 AI Commit Metrics Report
Period: 30d to now
============================================================

📈 Overall Statistics
----------------------------------------
   Total commits: 156
   Total lines added: 15,234
   AI-generated lines: 9,876
   Human-written lines: 5,358

🤖 AI Contribution Breakdown
----------------------------------------
   Tab completions: 4,567 (30.0%)
   Agent edits: 5,309 (34.8%)
   Total AI: 64.8%

   AI vs Human: [████████████████████████████████░░░░░░░░░░░░░░░░░░░░]
   AI         64.8%                                    Human 35.2%

📝 Commit Source Breakdown
----------------------------------------
   ide: 142 (91.0%)
   cloud: 10 (6.4%)
   cli: 4 (2.6%)

👥 User Breakdown (Top 10 by AI usage)
----------------------------------------
   1. alice@company.com           78.2% AI (45 commits)
   2. bob@company.com             71.4% AI (38 commits)
   3. carol@company.com           65.3% AI (32 commits)
   4. dave@company.com            52.1% AI (28 commits)
```

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `commitHash` | Git commit hash |
| `userId` | Encoded user ID |
| `userEmail` | User's email address |
| `repoName` | Repository name |
| `commitSource` | Where commit originated (`ide`, `cli`, `cloud`) |
| `totalLinesAdded` | Total lines added in commit |
| `tabLinesAdded` | Lines added via Tab completions |
| `composerLinesAdded` | Lines added via Agent edits |
| `nonAiLinesAdded` | Human-written lines |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Availability** | Enterprise only, AI Code Tracking API |
| **Data collection** | On-device detection, only line counts stored |
| **Date range** | Maximum 30 days per request |
| **Pagination** | Use `page` and `pageSize` for large datasets |

---

## Success Criteria

- [ ] Retrieved AI commit metrics
- [ ] Calculated AI contribution percentage
- [ ] Broke down by AI source (Tab vs Composer)
- [ ] Filtered by specific user
- [ ] Created AI commit report script
- [ ] Generated user breakdown

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key |
| 403 Forbidden | AI Code Tracking requires Enterprise plan |
| No data | No commits with AI tracking in date range |
| Empty items | Try longer date range or different repo |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved AI commit metrics
- [ ] Calculated AI contribution percentage
- [ ] Broke down by Tab vs Composer
- [ ] Filtered by specific user
- [ ] Created report script
- [ ] Generated user breakdown

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

