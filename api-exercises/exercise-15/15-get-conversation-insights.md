# API Exercise 15: Get Conversation Insights

**Objective:** Retrieve classified conversation insights showing what types of work your team is doing with AI – including intents, complexity, categories, and work types.

**Time:** 10 minutes

**Difficulty:** Intermediate

**Real-World Scenario:** Your engineering leadership wants to understand how AI is being used across the team. Are people using it for new feature development, bug fixing, refactoring, or just asking questions? Conversation Insights provides this classification automatically.

---

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] Conversation Insights enabled in team settings
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Get Conversation Insights (2 minutes)

Retrieve conversation insights for your team.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/conversation-insights?startDate=7d&endDate=today&include=intents,complexity,categories,guidanceLevels,workTypes" | jq '.'
```

**Expected response:**
```json
{
  "data": {
    "intents": {
      "distribution": [
        {"intent": "Write Code", "count": 156},
        {"intent": "Ask", "count": 89},
        {"intent": "Plan", "count": 34}
      ],
      "topValues": [
        {"intent": "Write Code", "count": 156},
        {"intent": "Ask", "count": 89}
      ],
      "timeSeries": [
        {"date": "2025-01-15", "intent": "Write Code", "count": 22},
        {"date": "2025-01-15", "intent": "Ask", "count": 12}
      ],
      "subcategories": {
        "askMode": [
          {"subcategory": "error_fix", "count": 32},
          {"subcategory": "explanation", "count": 28}
        ],
        "planMode": [
          {"subcategory": "implementation", "count": 18},
          {"subcategory": "architecture", "count": 12}
        ],
        "writeCode": [
          {"subcategory": "feature", "count": 78},
          {"subcategory": "refactor", "count": 45},
          {"subcategory": "test", "count": 23}
        ]
      }
    },
    "complexity": {
      "distribution": [
        {"complexity": "high", "count": 45},
        {"complexity": "medium", "count": 89},
        {"complexity": "low", "count": 145}
      ],
      "timeSeries": [
        {"date": "2025-01-15", "complexity": "high", "count": 6},
        {"date": "2025-01-15", "complexity": "medium", "count": 12}
      ]
    },
    "categories": {
      "distribution": [
        {"category": "New Features", "count": 78},
        {"category": "Bug Fixing & Debugging", "count": 45},
        {"category": "Code Refactoring", "count": 34},
        {"category": "Testing", "count": 23},
        {"category": "Documentation", "count": 18}
      ],
      "timeSeries": [
        {"date": "2025-01-15", "category": "New Features", "count": 11}
      ]
    },
    "guidanceLevels": {
      "distribution": [
        {"guidanceLevel": "high", "count": 45},
        {"guidanceLevel": "medium", "count": 89},
        {"guidanceLevel": "low", "count": 145}
      ],
      "timeSeries": [
        {"date": "2025-01-15", "guidanceLevel": "high", "count": 6}
      ]
    },
    "workTypes": {
      "distribution": [
        {"workType": "new_feature", "count": 78},
        {"workType": "bug", "count": 45},
        {"workType": "maintenance", "count": 34}
      ],
      "timeSeries": [
        {"date": "2025-01-15", "workType": "new_feature", "count": 11}
      ]
    }
  },
  "params": {
    "metric": "conversation-insights",
    "teamId": 12345,
    "startDate": "2025-01-09",
    "endDate": "2025-01-16",
    "include": ["intents", "complexity", "categories", "guidanceLevels", "workTypes"]
  }
}
```

---

### Step 2: Get Specific Insights (2 minutes)

Retrieve only specific insight categories.

**Command (only intents and complexity):**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/conversation-insights?startDate=7d&endDate=today&include=intents,complexity" | jq '.data | {intents: .intents.distribution, complexity: .complexity.distribution}'
```

**Expected output:**
```json
{
  "intents": [
    {"intent": "Write Code", "count": 156},
    {"intent": "Ask", "count": 89},
    {"intent": "Plan", "count": 34}
  ],
  "complexity": [
    {"complexity": "low", "count": 145},
    {"complexity": "medium", "count": 89},
    {"complexity": "high", "count": 45}
  ]
}
```

---

### Step 3: Filter by Specific Users (2 minutes)

Get conversation insights for specific team members.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/conversation-insights?startDate=7d&endDate=today&include=categories&users=alice@company.com,bob@company.com" | jq '.data.categories.distribution'
```

---

### Step 4: Analyze Work Type Distribution (2 minutes)

Calculate percentages for different work types.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/team/conversation-insights?startDate=30d&endDate=today&include=workTypes" | \
  jq '.data.workTypes.distribution | map({workType, count, percentage: (count / (. | map(.count) | add) * 100 | floor)})'
```

**Expected output:**
```json
[
  {"workType": "new_feature", "count": 234, "percentage": 48},
  {"workType": "bug", "count": 135, "percentage": 28},
  {"workType": "maintenance", "count": 102, "percentage": 21}
]
```

---

### Step 5: Create Conversation Insights Report (2 minutes)

**Create `insights_report.py`:**
```python
#!/usr/bin/env python3
"""
Conversation Insights Report - Understand how AI is being used
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

class ConversationInsights:
    """Conversation Insights Analytics"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_insights(self, start_date="7d", end_date="today", include=None, users=None):
        """Get conversation insights."""
        url = f"{self.base_url}/analytics/team/conversation-insights"
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        
        if include:
            params["include"] = ",".join(include) if isinstance(include, list) else include
        
        if users:
            params["users"] = users
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code == 401:
            print("❌ Conversation Insights not enabled. Enable in team settings.")
            return None
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def generate_report(self, start_date="30d", end_date="today"):
        """Generate a complete insights report."""
        print(f"\n📊 Conversation Insights Report")
        print(f"Period: {start_date} to {end_date}")
        print("=" * 60)
        
        data = self.get_insights(start_date, end_date, 
                                 include=["intents", "complexity", "categories", "workTypes"])
        
        if not data or not data.get("data"):
            print("No insights data available")
            print("Tip: Enable Conversation Insights in team settings")
            return
        
        insights = data["data"]
        
        # Intents (What users are trying to do)
        print("\n🎯 USER INTENTS")
        print("-" * 40)
        intents = insights.get("intents", {}).get("distribution", [])
        total_intents = sum(i.get("count", 0) for i in intents)
        
        for intent in intents:
            name = intent.get("intent", "Unknown")
            count = intent.get("count", 0)
            pct = (count / total_intents * 100) if total_intents > 0 else 0
            bar = "█" * int(pct / 2)
            print(f"   {name:<15} {count:>6} ({pct:>5.1f}%) {bar}")
        
        # Work Types (What kind of work)
        print("\n🛠️ WORK TYPES")
        print("-" * 40)
        work_types = insights.get("workTypes", {}).get("distribution", [])
        total_work = sum(w.get("count", 0) for w in work_types)
        
        work_type_labels = {
            "new_feature": "New Features",
            "bug": "Bug Fixing",
            "maintenance": "Maintenance"
        }
        
        for work in work_types:
            wt = work.get("workType", "unknown")
            label = work_type_labels.get(wt, wt)
            count = work.get("count", 0)
            pct = (count / total_work * 100) if total_work > 0 else 0
            bar = "█" * int(pct / 2)
            print(f"   {label:<15} {count:>6} ({pct:>5.1f}%) {bar}")
        
        # Categories (Specific work categories)
        print("\n📂 WORK CATEGORIES")
        print("-" * 40)
        categories = insights.get("categories", {}).get("distribution", [])
        total_cats = sum(c.get("count", 0) for c in categories)
        
        for cat in categories[:8]:  # Top 8 categories
            name = cat.get("category", "Unknown")
            count = cat.get("count", 0)
            pct = (count / total_cats * 100) if total_cats > 0 else 0
            bar = "█" * int(pct / 2)
            print(f"   {name:<25} {count:>6} ({pct:>5.1f}%) {bar}")
        
        # Complexity
        print("\n📈 COMPLEXITY DISTRIBUTION")
        print("-" * 40)
        complexity = insights.get("complexity", {}).get("distribution", [])
        total_complexity = sum(c.get("count", 0) for c in complexity)
        
        for comp in complexity:
            level = comp.get("complexity", "unknown").capitalize()
            count = comp.get("count", 0)
            pct = (count / total_complexity * 100) if total_complexity > 0 else 0
            bar = "█" * int(pct / 2)
            print(f"   {level:<10} {count:>6} ({pct:>5.1f}%) {bar}")
        
        # Subcategories (What within each intent)
        print("\n🔍 DETAILED BREAKDOWN")
        print("-" * 40)
        
        subcats = insights.get("intents", {}).get("subcategories", {})
        
        if "writeCode" in subcats:
            print("\n   Write Code Subcategories:")
            for sub in subcats["writeCode"][:5]:
                print(f"      • {sub.get('subcategory', 'Unknown')}: {sub.get('count', 0)}")
        
        if "askMode" in subcats:
            print("\n   Ask Mode Subcategories:")
            for sub in subcats["askMode"][:5]:
                print(f"      • {sub.get('subcategory', 'Unknown')}: {sub.get('count', 0)}")
        
        return insights
    
    def get_trends(self, metric="categories"):
        """Get trends over time for a specific metric."""
        # Get daily data for last 7 days
        data = self.get_insights("7d", "today", include=[metric])
        
        if not data or not data.get("data"):
            return []
        
        time_series = data["data"].get(metric, {}).get("timeSeries", [])
        
        # Aggregate by date
        trends = {}
        for entry in time_series:
            date = entry.get("date")
            name = entry.get("category") or entry.get("workType") or entry.get("intent")
            count = entry.get("count", 0)
            
            if date not in trends:
                trends[date] = {}
            trends[date][name] = trends[date].get(name, 0) + count
        
        return trends

def main():
    print("🚀 Conversation Insights")
    print("=" * 40)
    print("Note: Insights require Conversation Insights enabled in team settings")
    
    insights = ConversationInsights()
    
    # Generate report for last 30 days
    insights.generate_report("30d", "today")
    
    # Get trends
    print("\n📈 DAILY TRENDS (Last 7 days)")
    print("-" * 40)
    trends = insights.get_trends("categories")
    
    if trends:
        for date, categories in list(trends.items())[-7:]:
            print(f"\n   {date}:")
            for cat, count in list(categories.items())[:3]:
                print(f"      {cat}: {count}")
    
    print("\n💡 Tip: Use different date ranges to see patterns")
    print("   Example: startDate=90d to see quarterly trends")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 Conversation Insights
========================================
Note: Insights require Conversation Insights enabled in team settings

📊 Conversation Insights Report
Period: 30d to today
============================================================

🎯 USER INTENTS
----------------------------------------
   Write Code        156 (48.2%) ████████████████████████
   Ask                89 (27.5%) ██████████████
   Plan               34 (10.5%) █████

🛠️ WORK TYPES
----------------------------------------
   New Features       78 (39.8%) ███████████████████
   Bug Fixing         45 (23.0%) ███████████
   Maintenance        34 (17.3%) ████████

📂 WORK CATEGORIES
----------------------------------------
   New Features                78 (29.7%) ██████████████
   Bug Fixing & Debugging      45 (17.1%) ████████
   Code Refactoring            34 (12.9%) ██████
   Testing                     23 (8.7%)  ████
   Documentation               18 (6.8%)  ███

📈 COMPLEXITY DISTRIBUTION
----------------------------------------
   Low         145 (52.0%) ██████████████████████████
   Medium       89 (31.9%) ███████████████
   High         45 (16.1%) ████████

🔍 DETAILED BREAKDOWN
----------------------------------------

   Write Code Subcategories:
      • feature: 78
      • refactor: 45
      • test: 23

   Ask Mode Subcategories:
      • error_fix: 32
      • explanation: 28
```

---

## Insight Categories Reference

| Category | Description |
|----------|-------------|
| **Intents** | What users are trying to do (Write Code, Ask, Plan) |
| **Work Types** | Type of work (New Features, Bug Fixing, Maintenance) |
| **Categories** | Specific work categories (Testing, Documentation, Refactoring) |
| **Complexity** | Task complexity (High, Medium, Low) |
| **Guidance Levels** | How specific user prompts are |

### Intent Subcategories

| Subcategory | Description |
|-------------|-------------|
| `feature` | New feature development |
| `refactor` | Code refactoring |
| `test` | Writing tests |
| `error_fix` | Fixing errors |
| `explanation` | Asking for explanations |
| `implementation` | Implementation planning |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Availability** | Enterprise only, must be enabled in team settings |
| **Data classification** | Runs on-device, no PII leaves the machine |
| **Required parameter** | `include` must specify which insights to return |
| **User filtering** | Supports `users` parameter for specific users |

---

## Success Criteria

- [ ] Retrieved conversation insights
- [ ] Filtered to specific insight categories
- [ ] Filtered by specific users
- [ ] Analyzed work type distribution
- [ ] Created insights report script
- [ ] Identified top work categories

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Enable Conversation Insights in team settings |
| No data | Ensure feature is enabled and team has activity |
| 403 Forbidden | Enterprise plan required |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved conversation insights
- [ ] Filtered to specific categories
- [ ] Filtered by specific users
- [ ] Analyzed work type distribution
- [ ] Created report script
- [ ] Identified top work categories
