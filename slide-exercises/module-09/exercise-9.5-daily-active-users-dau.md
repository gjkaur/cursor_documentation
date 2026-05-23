# Exercise 9.5: Daily Active Users (DAU)

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.5)  
**Time:** 10 min  
**Difficulty:** Beginner

**Objective:** Report daily active users over a date range.

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
  ".../analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '{avg_weekly: ([.daily[-7:] | .[].activeUsers] | add / length),
         peak: ([.daily[] | .activeUsers] | max)}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

**Python leadership report:**
- Average/median/peak DAU · adoption rate (% of team)
- WoW growth rate · weekly averages
- Health assessment: >80% excellent · >50% good · <30% investigate

**Success Criteria:** Calculated DAU · adoption metrics · leadership-ready report

---

## Success criteria

- [ ] Average/median/peak DAU · adoption rate (% of team)
- [ ] WoW growth rate · weekly averages
- [ ] Health assessment: >80% excellent · >50% good · <30% investigate
- [ ] Calculated DAU · adoption metrics · leadership-ready report

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get Daily Active Users (2 minutes)

Retrieve DAU metrics for your team.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/dau?startDate=7d&endDate=today" | jq '.'
```

**Expected response:**
```json
{
  "data": [
    {
      "date": "2025-01-15",
      "dau": 42,
      "cli_dau": 5,
      "cloud_agent_dau": 37,
      "bugbot_dau": 10
    },
    {
      "date": "2025-01-16",
      "dau": 38,
      "cli_dau": 4,
      "cloud_agent_dau": 34,
      "bugbot_dau": 12
    }
  ],
  "params": {
    "metric": "dau",
    "teamId": 12345,
    "startDate": "2025-01-09",
    "endDate": "2025-01-16"
  }
}
```

---

### Step 2: Calculate Average DAU (2 minutes)

Compute average daily active users over the period.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/dau?startDate=30d&endDate=today" | \
  jq '{avg_dau: ([.data[].dau] | add / length), total_days: (.data | length)}'
```

**Expected output:**
```json
{
  "avg_dau": 38.5,
  "total_days": 30
}
```

---

### Step 3: Track Week-over-Week Growth (2 minutes)

Compare DAU between this week and last week.

**Command:**
```bash
# This week (last 7 days)
THIS_WEEK=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/dau?startDate=7d&endDate=today" | \
  jq '[.data[].dau] | add / length')

# Previous week (days 8-14 ago)
LAST_WEEK=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/dau?startDate=14d&endDate=8d" | \
  jq '[.data[].dau] | add / length')

echo "This week avg DAU: $THIS_WEEK"
echo "Last week avg DAU: $LAST_WEEK"

if (( $(echo "$THIS_WEEK > $LAST_WEEK" | bc -l) )); then
  echo "📈 Growth: +$(echo "scale=1; ($THIS_WEEK - $LAST_WEEK) / $LAST_WEEK * 100" | bc)%"
else
  echo "📉 Decline: $(echo "scale=1; ($LAST_WEEK - $THIS_WEEK) / $LAST_WEEK * 100" | bc)%"
fi
```

---

### Step 4: Get Product-Specific Trends (2 minutes)

Analyze adoption of different Cursor products.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/dau?startDate=30d&endDate=today" | \
  jq '{
    ide_avg: ([.data[].dau] | add / length),
    cli_avg: ([.data[].cli_dau] | add / length),
    cloud_agent_avg: ([.data[].cloud_agent_dau] | add / length),
    bugbot_avg: ([.data[].bugbot_dau] | add / length)
  }'
```

**Expected output:**
```json
{
  "ide_avg": 38.5,
  "cli_avg": 4.2,
  "cloud_agent_avg": 35.1,
  "bugbot_avg": 11.3
}
```

---

### Step 5: Create DAU Dashboard Script (2 minutes)

**Create `dau_dashboard.py`:**
```python
#!/usr/bin/env python3
"""
DAU Dashboard - Track daily active users
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

class DAUDashboard:
    """Daily Active Users Dashboard"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_dau(self, start_date="7d", end_date="today"):
        """Get DAU metrics."""
        url = f"{self.base_url}/analytics/team/dau"
        params = {"startDate": start_date, "endDate": end_date}
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def calculate_trend(self, data):
        """Calculate trend (growth/decline)."""
        if not data or len(data) < 2:
            return 0
        
        values = [day.get("dau", 0) for day in data]
        first_half_avg = sum(values[:len(values)//2]) / (len(values)//2)
        second_half_avg = sum(values[len(values)//2:]) / (len(values) - len(values)//2)
        
        if first_half_avg == 0:
            return 0
        
        return ((second_half_avg - first_half_avg) / first_half_avg) * 100
    
    def generate_dashboard(self, period_days=30):
        """Generate a complete DAU dashboard."""
        start_date = f"{period_days}d"
        end_date = "today"
        
        data = self.get_dau(start_date, end_date)
        
        if not data or not data.get("data"):
            print("No data available")
            return
        
        days = data["data"]
        
        print(f"\n📊 DAU Dashboard")
        print(f"Period: Last {period_days} days")
        print("=" * 50)
        
        # Current metrics
        latest_day = days[-1] if days else {}
        print(f"\n📅 Latest Day ({latest_day.get('date', 'N/A')})")
        print(f"   Total DAU: {latest_day.get('dau', 0)}")
        print(f"   CLI: {latest_day.get('cli_dau', 0)}")
        print(f"   Cloud Agents: {latest_day.get('cloud_agent_dau', 0)}")
        print(f"   Bugbot: {latest_day.get('bugbot_dau', 0)}")
        
        # Averages
        avg_dau = sum(d.get("dau", 0) for d in days) / len(days)
        avg_cli = sum(d.get("cli_dau", 0) for d in days) / len(days)
        avg_cloud = sum(d.get("cloud_agent_dau", 0) for d in days) / len(days)
        avg_bugbot = sum(d.get("bugbot_dau", 0) for d in days) / len(days)
        
        print(f"\n📈 Averages (Last {len(days)} days)")
        print(f"   DAU: {avg_dau:.1f}")
        print(f"   CLI: {avg_cli:.1f}")
        print(f"   Cloud Agents: {avg_cloud:.1f}")
        print(f"   Bugbot: {avg_bugbot:.1f}")
        
        # Trend
        trend = self.calculate_trend(days)
        if trend > 5:
            print(f"\n📈 Trend: Strong growth (+{trend:.1f}%)")
        elif trend > 0:
            print(f"\n📈 Trend: Moderate growth (+{trend:.1f}%)")
        elif trend > -5:
            print(f"\n📊 Trend: Stable ({trend:.1f}%)")
        else:
            print(f"\n📉 Trend: Decline ({trend:.1f}%)")
        
        # Product adoption breakdown
        print(f"\n🎯 Product Adoption (Last {len(days)} days)")
        print("-" * 30)
        
        # Calculate what percentage of DAU use each product
        cli_percent = (avg_cli / avg_dau * 100) if avg_dau > 0 else 0
        cloud_percent = (avg_cloud / avg_dau * 100) if avg_dau > 0 else 0
        bugbot_percent = (avg_bugbot / avg_dau * 100) if avg_dau > 0 else 0
        
        print(f"   CLI: {cli_percent:.1f}% of DAU")
        print(f"   Cloud Agents: {cloud_percent:.1f}% of DAU")
        print(f"   Bugbot: {bugbot_percent:.1f}% of DAU")
        
        # Weekly trend chart (simple ASCII)
        print(f"\n📊 Weekly DAU Trend (Last 7 days)")
        print("-" * 40)
        
        last_7_days = days[-7:] if len(days) >= 7 else days
        max_dau = max(d.get("dau", 0) for d in last_7_days)
        
        for day in last_7_days:
            date = day.get("date", "N/A")[5:]  # Show MM-DD
            dau = day.get("dau", 0)
            bar_length = int((dau / max_dau) * 30) if max_dau > 0 else 0
            bar = "█" * bar_length
            print(f"   {date} {bar} {dau}")
        
        return days
    
    def export_to_csv(self, days, filename="dau_export.csv"):
        """Export DAU data to CSV."""
        import csv
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['date', 'dau', 'cli_dau', 'cloud_agent_dau', 'bugbot_dau']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for day in days:
                writer.writerow({
                    'date': day.get('date'),
                    'dau': day.get('dau'),
                    'cli_dau': day.get('cli_dau'),
                    'cloud_agent_dau': day.get('cloud_agent_dau'),
                    'bugbot_dau': day.get('bugbot_dau')
                })
        
        print(f"\n✅ Exported to {filename}")

def main():
    print("🚀 DAU Dashboard")
    print("=" * 40)
    
    dashboard = DAUDashboard()
    
    # Generate 30-day dashboard
    days = dashboard.generate_dashboard(30)
    
    # Export to CSV
    if days:
        export = input("\n📥 Export to CSV? (y/n): ").lower()
        if export == 'y':
            dashboard.export_to_csv(days)
    
    # Optional: Get user-specific DAU (requires user IDs)
    print("\n💡 To filter by specific users, use:")
    print("   ?users=user_abc123,user_def456")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 DAU Dashboard
========================================

📊 DAU Dashboard
Period: Last 30 days
==================================================

📅 Latest Day (2025-01-16)
   Total DAU: 38
   CLI: 4
   Cloud Agents: 34
   Bugbot: 12

📈 Averages (Last 30 days)
   DAU: 38.5
   CLI: 4.2
   Cloud Agents: 35.1
   Bugbot: 11.3

📈 Trend: Moderate growth (+8.2%)

🎯 Product Adoption (Last 30 days)
------------------------------
   CLI: 10.9% of DAU
   Cloud Agents: 91.2% of DAU
   Bugbot: 29.4% of DAU

📊 Weekly DAU Trend (Last 7 days)
----------------------------------------
   01-10 ████████████████████████████████ 42
   01-11 ██████████████████████████████ 40
   01-12 ████████████████████████████████ 41
   01-13 ████████████████████████████ 37
   01-14 ████████████████████████████ 36
   01-15 ████████████████████████████████ 42
   01-16 ██████████████████████████████ 38

✅ Exported to dau_export.csv
```

---

## Success Criteria

- [ ] Retrieved DAU metrics for team
- [ ] Calculated average DAU
- [ ] Tracked week-over-week growth
- [ ] Analyzed product-specific adoption
- [ ] Created DAU dashboard script
- [ ] Exported data to CSV

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `date` | Date in YYYY-MM-DD format |
| `dau` | Total daily active users |
| `cli_dau` | Users who used CLI |
| `cloud_agent_dau` | Users who used Cloud Agents |
| `bugbot_dau` | Users who used Bugbot |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /analytics/team/dau` |
| **Active user definition** | Used at least one AI feature |
| **Date range** | Maximum 30 days |
| **Default** | Last 7 days if not specified |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data | Team may have no activity in date range |
| 403 Forbidden | Enterprise plan required |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved DAU metrics
- [ ] Calculated averages
- [ ] Tracked week-over-week growth
- [ ] Analyzed product adoption
- [ ] Created dashboard script
- [ ] Exported to CSV

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
