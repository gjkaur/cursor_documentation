# Exercise 9.4: Model Usage Analytics

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 9, Lesson 9.4)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Analyze model usage and identify optimization opportunities.

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

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/models?startDate=$START&endDate=$END" \
  | jq '.models[] | {model: .modelId, cost: .cost, requests: .requestCount}'

# Find Opus overuse per user
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/users?startDate=$START&endDate=$END" \
  | jq '.users[] | select(.modelBreakdown."claude-4.7-opus" != null)'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

`generate_optimization_report()`:

- Model cost breakdown (% of total)
- Users on Claude Opus → suggest Sonnet for non-critical tasks
- High Sonnet usage → suggest GPT-5.3 Codex (40% savings)
- Estimated monthly savings if guidelines applied

**Success Criteria:** Retrieved model breakdown · identified expensive users · generated recommendations

---

## Success criteria

- [ ] Model cost breakdown (% of total)
- [ ] Users on Claude Opus → suggest Sonnet for non-critical tasks
- [ ] High Sonnet usage → suggest GPT-5.3 Codex (40% savings)
- [ ] Estimated monthly savings if guidelines applied
- [ ] Retrieved model breakdown · identified expensive users · generated recommendations

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get Team Model Usage (2 minutes)

Retrieve model usage metrics for your entire team.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/models?startDate=7d&endDate=today" | jq '.'
```

**Expected response:**
```json
{
  "data": [
    {
      "date": "2025-01-15",
      "model_breakdown": {
        "claude-4.5-sonnet": {
          "messages": 1250,
          "users": 28
        },
        "gpt-5.2": {
          "messages": 450,
          "users": 15
        },
        "claude-4.7-opus": {
          "messages": 320,
          "users": 12
        },
        "composer-2.5": {
          "messages": 890,
          "users": 22
        },
        "gpt-5-mini": {
          "messages": 1200,
          "users": 18
        }
      }
    },
    {
      "date": "2025-01-16",
      "model_breakdown": {
        "claude-4.5-sonnet": {
          "messages": 1180,
          "users": 26
        },
        "gpt-5.2": {
          "messages": 420,
          "users": 14
        }
      }
    }
  ]
}
```

---

### Step 2: Calculate Total Usage per Model (2 minutes)

Aggregate message counts across all dates for each model.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/models?startDate=7d&endDate=today" | \
  jq '[.data[].model_breakdown | to_entries[]] | group_by(.key) | map({model: .[0].key, messages: (map(.value.messages) | add), users: (map(.value.users) | max)}) | sort_by(-.messages)'
```

**Expected output:**
```json
[
  {
    "model": "claude-4.5-sonnet",
    "messages": 8520,
    "users": 28
  },
  {
    "model": "gpt-5-mini",
    "messages": 5600,
    "users": 18
  },
  {
    "model": "composer-2.5",
    "messages": 4500,
    "users": 22
  },
  {
    "model": "gpt-5.2",
    "messages": 3100,
    "users": 15
  },
  {
    "model": "claude-4.7-opus",
    "messages": 2100,
    "users": 12
  }
]
```

---

### Step 3: Get Per-User Model Usage (2 minutes)

Retrieve model usage broken down by individual user.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/by-user/models?startDate=7d&endDate=today&page=1&pageSize=10" | jq '.'
```

**Expected response:**
```json
{
  "data": {
    "alice@company.com": [
      {
        "date": "2025-01-15",
        "model_breakdown": {
          "claude-4.5-sonnet": {
            "messages": 85,
            "users": 1
          },
          "claude-4.7-opus": {
            "messages": 12,
            "users": 1
          }
        }
      }
    ],
    "bob@company.com": [
      {
        "date": "2025-01-15",
        "model_breakdown": {
          "composer-2.5": {
            "messages": 120,
            "users": 1
          },
          "gpt-5-mini": {
            "messages": 45,
            "users": 1
          }
        }
      }
    ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 10,
    "totalUsers": 25,
    "totalPages": 3,
    "hasNextPage": true
  }
}
```

---

### Step 4: Identify Costly Model Usage (2 minutes)

Flag usage of expensive models (like Opus) that may need cost controls.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/models?startDate=7d&endDate=today" | \
  jq '[.data[].model_breakdown | to_entries[] | select(.key | contains("opus"))] | group_by(.key) | map({model: .[0].key, messages: (map(.value.messages) | add)})'
```

**Expected output:**
```json
[
  {
    "model": "claude-4.7-opus",
    "messages": 2100
  }
]
```

---

### Step 5: Create Model Usage Report Script (2 minutes)

**Create `model_usage_report.py`:**
```python
#!/usr/bin/env python3
"""
Generate model usage analytics report
"""

import requests
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class ModelAnalytics:
    """Model usage analytics"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_team_model_usage(self, start_date="7d", end_date="today"):
        """Get team model usage."""
        url = f"{self.base_url}/analytics/team/models"
        params = {"startDate": start_date, "endDate": end_date}
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def get_user_model_usage(self, page=1, page_size=100):
        """Get per-user model usage."""
        url = f"{self.base_url}/analytics/by-user/models"
        params = {"page": page, "pageSize": page_size}
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def aggregate_model_usage(self, data):
        """Aggregate model usage across all dates."""
        if not data or not data.get("data"):
            return {}
        
        model_totals = defaultdict(lambda: {"messages": 0, "users": 0})
        
        for day in data.get("data", []):
            breakdown = day.get("model_breakdown", {})
            for model, stats in breakdown.items():
                model_totals[model]["messages"] += stats.get("messages", 0)
                model_totals[model]["users"] = max(
                    model_totals[model]["users"],
                    stats.get("users", 0)
                )
        
        return dict(model_totals)
    
    def generate_report(self, start_date="7d", end_date="today"):
        """Generate a complete model usage report."""
        print(f"\n📊 Model Usage Report")
        print(f"Period: {start_date} to {end_date}")
        print("=" * 50)
        
        # Get team data
        data = self.get_team_model_usage(start_date, end_date)
        if not data:
            return
        
        # Aggregate
        usage = self.aggregate_model_usage(data)
        
        if not usage:
            print("No model usage data available")
            return
        
        # Sort by messages
        sorted_models = sorted(usage.items(), key=lambda x: x[1]["messages"], reverse=True)
        
        print(f"\n📈 Model Usage Summary")
        print("-" * 50)
        print(f"{'Model':<25} {'Messages':>12} {'Users':>8} {'Avg/User':>10}")
        print("-" * 50)
        
        for model, stats in sorted_models:
            messages = stats["messages"]
            users = stats["users"]
            avg_per_user = messages // users if users > 0 else 0
            print(f"{model:<25} {messages:>12,} {users:>8} {avg_per_user:>10,}")
        
        # Calculate percentages
        total_messages = sum(s["messages"] for s in usage.values())
        
        print("\n📊 Market Share")
        print("-" * 50)
        for model, stats in sorted_models[:5]:  # Top 5
            percentage = (stats["messages"] / total_messages) * 100
            bar_length = int(percentage / 2)  # 2% per character
            bar = "█" * bar_length
            print(f"{model:<25} {percentage:>5.1f}% {bar}")
        
        # Cost estimation (simplified - adjust rates as needed)
        print("\n💰 Estimated Cost (approximate)")
        print("-" * 50)
        print("Note: Actual costs vary by token usage and pricing plan")
        
        # Approximate rates per 1M messages (adjust based on your plan)
        cost_rates = {
            "claude-4.7-opus": 25.00,
            "claude-4.5-sonnet": 3.00,
            "gpt-5.2": 2.50,
            "composer-2.5": 2.50,
            "gpt-5-mini": 0.50,
        }
        
        total_cost = 0
        for model, stats in sorted_models:
            rate = cost_rates.get(model, 1.00)
            # Rough estimate: 1000 messages ~ 1M tokens
            cost = (stats["messages"] / 1000) * rate
            total_cost += cost
            if cost > 0.01:  # Only show significant costs
                print(f"   {model:<25} ${cost:>10.2f}")
        
        print("-" * 50)
        print(f"   {'Estimated total':<25} ${total_cost:>10.2f}")
        print("\n💡 Tip: Use composer-2.5 or gpt-5-mini for cost savings")
        
        return usage

def main():
    print("🚀 Model Usage Analytics")
    print("=" * 40)
    
    analytics = ModelAnalytics()
    
    # Generate report for last 30 days
    analytics.generate_report("30d", "today")
    
    # Optional: Get per-user breakdown
    print("\n" + "=" * 40)
    print("👥 Per-User Model Usage (First 5 users)")
    print("=" * 40)
    
    user_data = analytics.get_user_model_usage(page=1, page_size=5)
    
    if user_data and user_data.get("data"):
        for email, days in list(user_data["data"].items())[:5]:
            print(f"\n📧 {email}")
            # Aggregate user's model usage
            user_models = defaultdict(int)
            for day in days:
                for model, stats in day.get("model_breakdown", {}).items():
                    user_models[model] += stats.get("messages", 0)
            
            for model, count in sorted(user_models.items(), key=lambda x: -x[1])[:3]:
                print(f"   {model}: {count} messages")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 Model Usage Analytics
========================================

📊 Model Usage Report
Period: 30d to today
==================================================

📈 Model Usage Summary
--------------------------------------------------
Model                          Messages    Users   Avg/User
--------------------------------------------------
claude-4.5-sonnet                 8,520       28        304
gpt-5-mini                        5,600       18        311
composer-2.5                        4,500       22        204
gpt-5.2                           3,100       15        206
claude-4.7-opus                   2,100       12        175

📊 Market Share
--------------------------------------------------
claude-4.5-sonnet                 35.5% █████████████████
gpt-5-mini                        23.3% ███████████
composer-2.5                        18.8% █████████
gpt-5.2                           12.9% ██████
claude-4.7-opus                    8.8% ████

💰 Estimated Cost (approximate)
--------------------------------------------------
   claude-4.7-opus                  $52.50
   claude-4.5-sonnet                $25.56
   gpt-5.2                           $7.75
   composer-2.5                       $11.25
--------------------------------------------------
   Estimated total                 $101.31

💡 Tip: Use composer-2.5 or gpt-5-mini for cost savings
```

---

## Success Criteria

- [ ] Retrieved team model usage data
- [ ] Calculated total usage per model
- [ ] Retrieved per-user model usage
- [ ] Identified costly model usage
- [ ] Created model usage report script
- [ ] Estimated costs based on usage

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /analytics/team/models` |
| **Authentication** | Admin API key (Enterprise) |
| **Response** | Daily breakdown by model |
| **Per-user** | `GET /analytics/by-user/models` |
| **Date range** | Maximum 30 days |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key |
| 403 Forbidden | Enterprise plan required |
| No data | Check date range and team activity |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved team model usage
- [ ] Calculated totals per model
- [ ] Retrieved per-user model usage
- [ ] Identified costly models
- [ ] Created report script with cost estimation

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
