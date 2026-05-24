# Exercise 10.3: Granular AI Change Events

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/module-10-marp.md` (Lesson 10.3)  
**Time:** 7 min  
**Difficulty:** Beginner

**Objective:** Query per-change AI events for compliance reporting.

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
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/events?startDate=$START&endDate=$END&limit=100" \
  | jq '.events[] | {user: .user.email, file: .filePath, model: .modelId, accepted: .accepted}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Acceptance rate by model: group events → total vs. accepted per model

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

`generate_compliance_report()` for last 90 days:

- Acceptance rate by model (table)
- Top 10 files with most AI changes (needs review)
- Export `compliance_export.csv` for auditors:
  - timestamp, user_email, model_id, file_path, line_start, line_end, accepted

**Success Criteria:** Retrieved events · calculated acceptance rates · compliance export

---

## Success criteria

- [ ] Acceptance rate by model (table)
- [ ] Top 10 files with most AI changes (needs review)
- [ ] Export `compliance_export.csv` for auditors:
- [ ] timestamp, user_email, model_id, file_path, line_start, line_end, accepted
- [ ] Retrieved events · calculated acceptance rates · compliance export

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan (AI Code Tracking API)
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get AI Change Metrics (2 minutes)

Retrieve granular AI change events.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/changes?startDate=7d&endDate=now&page=1&pageSize=20" | jq '.'
```

**Expected response:**
```json
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_abc123",
      "userEmail": "alice@company.com",
      "source": "COMPOSER",
      "model": "claude-4.5-sonnet",
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-01-15T15:10:12.000Z",
      "metadata": [
        {
          "fileName": "src/auth/login.ts",
          "fileExtension": "ts",
          "linesAdded": 12,
          "linesDeleted": 3
        },
        {
          "fileName": "src/auth/validation.ts",
          "fileExtension": "ts",
          "linesAdded": 6,
          "linesDeleted": 1
        }
      ]
    },
    {
      "changeId": "749356202",
      "userId": "user_abc123",
      "userEmail": "alice@company.com",
      "source": "TAB",
      "model": null,
      "totalLinesAdded": 8,
      "totalLinesDeleted": 2,
      "createdAt": "2025-01-15T15:08:45.000Z",
      "metadata": [
        {
          "fileName": "src/utils/helpers.ts",
          "fileExtension": "ts",
          "linesAdded": 8,
          "linesDeleted": 2
        }
      ]
    }
  ],
  "totalCount": 1250,
  "page": 1,
  "pageSize": 20
}
```

---

### Step 2: Calculate Acceptance Statistics (2 minutes)

Compute totals and averages for AI changes.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/changes?startDate=30d&endDate=now&pageSize=100" | \
  jq '{
    total_changes: .totalCount,
    composer_changes: [.items[] | select(.source == "COMPOSER")] | length,
    tab_changes: [.items[] | select(.source == "TAB")] | length,
    avg_lines_per_change: ([.items[].totalLinesAdded] | add) / (.items | length),
    total_lines_added: ([.items[].totalLinesAdded] | add)
  }'
```

**Expected output:**
```json
{
  "total_changes": 1250,
  "composer_changes": 456,
  "tab_changes": 794,
  "avg_lines_per_change": 12.4,
  "total_lines_added": 15500
}
```

---

### Step 3: Analyze by File Extension (2 minutes)

Find which file types have the highest AI acceptance.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/changes?startDate=30d&endDate=now&pageSize=500" | \
  jq '[.items[].metadata[]] | group_by(.fileExtension) | map({ext: .[0].fileExtension, total_lines: (map(.linesAdded) | add), count: length}) | sort_by(-.total_lines) | .[:5]'
```

**Expected output:**
```json
[
  {"ext": "ts", "total_lines": 12500, "count": 450},
  {"ext": "tsx", "total_lines": 8900, "count": 320},
  {"ext": "py", "total_lines": 5600, "count": 210},
  {"ext": "js", "total_lines": 3400, "count": 150},
  {"ext": "c", "total_lines": 2100, "count": 80}
]
```

---

### Step 4: Filter by Source Type (2 minutes)

Get statistics for Tab vs Composer changes separately.

**Command (TAB):**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/changes?startDate=30d&endDate=now&pageSize=100" | \
  jq '[.items[] | select(.source == "TAB")] | {count: length, avg_lines: ([.[].totalLinesAdded] | add) / length}'
```

**Expected output:**
```json
{
  "count": 794,
  "avg_lines": 4.2
}
```

**Command (COMPOSER):**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/changes?startDate=30d&endDate=now&pageSize=100" | \
  jq '[.items[] | select(.source == "COMPOSER")] | {count: length, avg_lines: ([.[].totalLinesAdded] | add) / length}'
```

**Expected output:**
```json
{
  "count": 456,
  "avg_lines": 24.8
}
```

---

### Step 5: Create Change Metrics Report (2 minutes)

**Create `change_metrics_report.py`:**
```python
#!/usr/bin/env python3
"""
Granular AI Change Metrics Report
"""

import requests
import os
import sys
from collections import defaultdict
from datetime import datetime

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class ChangeMetrics:
    """Granular AI Change Metrics"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_changes(self, start_date="7d", end_date="now", page=1, page_size=500):
        """Get AI change metrics."""
        url = f"{self.base_url}/analytics/ai-code/changes"
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
    
    def get_all_changes(self, start_date="30d", end_date="now"):
        """Get all changes (handles pagination)."""
        all_items = []
        page = 1
        page_size = 500
        
        while True:
            data = self.get_changes(start_date, end_date, page, page_size)
            
            if not data:
                break
            
            items = data.get("items", [])
            all_items.extend(items)
            
            if len(items) < page_size:
                break
            
            page += 1
        
        return all_items
    
    def generate_report(self, start_date="30d", end_date="now"):
        """Generate a complete change metrics report."""
        print(f"\n📊 Granular AI Change Metrics Report")
        print(f"Period: {start_date} to {end_date}")
        print("=" * 60)
        
        changes = self.get_all_changes(start_date, end_date)
        
        if not changes:
            print("No change data available")
            return
        
        # Basic statistics
        total_changes = len(changes)
        composer_changes = [c for c in changes if c.get("source") == "COMPOSER"]
        tab_changes = [c for c in changes if c.get("source") == "TAB"]
        
        total_lines = sum(c.get("totalLinesAdded", 0) for c in changes)
        composer_lines = sum(c.get("totalLinesAdded", 0) for c in composer_changes)
        tab_lines = sum(c.get("totalLinesAdded", 0) for c in tab_changes)
        
        print(f"\n📈 Overall Statistics")
        print("-" * 40)
        print(f"   Total AI changes: {total_changes:,}")
        print(f"   Total lines added: {total_lines:,}")
        print(f"   Average lines/change: {total_lines/total_changes:.1f}")
        
        print(f"\n🔧 Breakdown by Source")
        print("-" * 40)
        print(f"   COMPOSER (Agent): {len(composer_changes):,} changes ({composer_lines/total_lines*100:.1f}% lines)")
        print(f"   TAB (Completions): {len(tab_changes):,} changes ({tab_lines/total_lines*100:.1f}% lines)")
        print(f"   Avg COMPOSER size: {composer_lines/len(composer_changes) if composer_changes else 0:.1f} lines")
        print(f"   Avg TAB size: {tab_lines/len(tab_changes) if tab_changes else 0:.1f} lines")
        
        # File extension analysis
        ext_stats = defaultdict(lambda: {"lines": 0, "count": 0})
        
        for change in changes:
            for meta in change.get("metadata", []):
                ext = meta.get("fileExtension", "unknown")
                lines = meta.get("linesAdded", 0)
                ext_stats[ext]["lines"] += lines
                ext_stats[ext]["count"] += 1
        
        print(f"\n📁 Top File Extensions by Lines Added")
        print("-" * 40)
        sorted_exts = sorted(ext_stats.items(), key=lambda x: x[1]["lines"], reverse=True)
        
        for ext, stats in sorted_exts[:8]:
            print(f"   .{ext:<8} {stats['lines']:>8,} lines ({stats['count']:>4} changes)")
        
        # Model distribution (for COMPOSER changes)
        model_stats = defaultdict(int)
        for change in composer_changes:
            model = change.get("model", "unknown")
            model_stats[model] += 1
        
        if model_stats:
            print(f"\n🧠 Model Distribution (COMPOSER changes only)")
            print("-" * 40)
            for model, count in sorted(model_stats.items(), key=lambda x: -x[1])[:5]:
                pct = count / len(composer_changes) * 100 if composer_changes else 0
                print(f"   {model:<25} {count:>4} ({pct:.1f}%)")
        
        # Daily trend
        daily_stats = defaultdict(lambda: {"total": 0, "composer": 0, "tab": 0})
        
        for change in changes:
            date = change.get("createdAt", "")[:10]
            source = change.get("source", "unknown")
            lines = change.get("totalLinesAdded", 0)
            daily_stats[date]["total"] += lines
            if source == "COMPOSER":
                daily_stats[date]["composer"] += lines
            else:
                daily_stats[date]["tab"] += lines
        
        print(f"\n📅 Daily AI Acceptance (Last 7 days)")
        print("-" * 40)
        
        for date in sorted(daily_stats.keys())[-7:]:
            stats = daily_stats[date]
            total = stats["total"]
            bar = "█" * int(total / 100) if total < 1000 else "█" * 10
            print(f"   {date} {bar} {total:>5,} lines")
        
        return changes

def main():
    print("🚀 Granular AI Change Metrics")
    print("=" * 40)
    
    metrics = ChangeMetrics()
    
    # Generate report for last 30 days
    metrics.generate_report("30d", "now")
    
    print(f"\n💡 Tip: Each change represents one AI acceptance event")
    print("   COMPOSER = Agent edit, TAB = inline completion")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 Granular AI Change Metrics
========================================

📊 Granular AI Change Metrics Report
Period: 30d to now
============================================================

📈 Overall Statistics
----------------------------------------
   Total AI changes: 1,250
   Total lines added: 15,500
   Average lines/change: 12.4

🔧 Breakdown by Source
----------------------------------------
   COMPOSER (Agent): 456 changes (61.2% lines)
   TAB (Completions): 794 changes (38.8% lines)
   Avg COMPOSER size: 24.8 lines
   Avg TAB size: 4.2 lines

📁 Top File Extensions by Lines Added
----------------------------------------
   .ts        12,500 lines ( 450 changes)
   .tsx        8,900 lines ( 320 changes)
   .py         5,600 lines ( 210 changes)
   .js         3,400 lines ( 150 changes)
   .c          2,100 lines (  80 changes)

🧠 Model Distribution (COMPOSER changes only)
----------------------------------------
   claude-4.5-sonnet          234 (51.3%)
   composer-2.5                 123 (27.0%)
   gpt-5.2                     67 (14.7%)
   claude-4.7-opus             32 ( 7.0%)

📅 Daily AI Acceptance (Last 7 days)
----------------------------------------
   2025-01-25 ████████ 845 lines
   2025-01-26 ███████ 723 lines
   2025-01-27 ██████████ 1,023 lines
   2025-01-28 ███████ 698 lines
   2025-01-29 ████████ 812 lines
   2025-01-30 ██████ 567 lines
   2025-01-31 █████████ 945 lines
```

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `changeId` | Unique ID for this acceptance event |
| `userId` | Encoded user ID |
| `userEmail` | User's email address |
| `source` | Source of AI change (`TAB` or `COMPOSER`) |
| `model` | AI model used (COMPOSER only) |
| `totalLinesAdded` | Lines added in this change |
| `metadata` | File-level details (fileName, fileExtension, linesAdded, linesDeleted) |

---

## Success Criteria

- [ ] Retrieved granular AI change metrics
- [ ] Calculated acceptance statistics
- [ ] Analyzed by file extension
- [ ] Filtered by source type (TAB vs COMPOSER)
- [ ] Created change metrics report script
- [ ] Analyzed model distribution

---

## Important Notes

| Note | Description |
|------|-------------|
| **Granularity** | Each change is a single AI acceptance event |
| **vs Commits** | Changes can span multiple files (unlike commits) |
| **Metadata** | May be omitted in privacy mode |
| **Pagination** | Use `page` and `pageSize` for large datasets |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data | No AI acceptances in date range |
| Empty metadata | Privacy mode may be enabled |
| 403 Forbidden | Enterprise plan required |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved granular AI change metrics
- [ ] Calculated acceptance statistics
- [ ] Analyzed by file extension
- [ ] Filtered by source type (TAB vs COMPOSER)
- [ ] Created change metrics report script
- [ ] Analyzed model distribution

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
