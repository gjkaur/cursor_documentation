# Module 9: Admin and Analytics APIs

## Cursor Training Program — Day 2 (Hands-On + Demonstrations)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~75 minutes |
| **Format** | Hands-on exercise + demonstrations |
| **Prerequisites** | Admin API key (not User key), Python 3.8+, Module 7-8 completed |
| **Module Goal** | Master team management, usage analytics, cost governance, and safe admin operations |

---

## Learning Objectives

By the end of this module, participants will be able to:

- List and manage team members programmatically
- Retrieve daily usage data for cost tracking and reporting
- Set user spend limits for budget governance
- Analyze model usage for cost optimization insights
- Track daily active users for leadership reporting
- Build responsible leaderboards without privacy violations
- Analyze conversation intent and complexity (demonstration)
- Safely remove team members with proper patterns (demonstration)

---

## Lesson 9.1: Listing Team Members

### Concept (5 minutes)

> *"The simplest Admin API call and a good entry point. This endpoint confirms your Admin API key works and gives you the basic building block for all other team management operations."*

### Key Differences: User vs. Admin API

| Aspect | User API Key | Admin API Key |
|--------|--------------|---------------|
| **Scope** | Your user only | Entire organization |
| **Can list members** | ❌ No | ✅ Yes |
| **Can view others' usage** | ❌ No | ✅ Yes |
| **Can modify policies** | ❌ No | ✅ Yes |
| **Format** | `cursor_xxx...` | `cursor_admin_xxx...` |

### Key Endpoint: `GET /v1/admin/members`

### Hands-On Exercise (8 minutes)

**Step 1:** Set up Admin API key

```bash
# Get from cursor.com → Organization Settings → API Keys
export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx"

# Verify it works
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/organization | jq '.'
```

**Step 2:** List all team members

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members" | jq '.'
```

**Step 3:** Pretty-print member information

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members" \
  | jq '.members[] | {email: .email, role: .role, status: .status, joined: .createdAt}'
```

**Step 4:** Handle pagination for large teams

```bash
# First page
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?limit=10&offset=0" \
  | jq '.members[].email'

# Second page
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?limit=10&offset=10" \
  | jq '.members[].email'
```

**Step 5:** Python script to export team roster

```python
#!/usr/bin/env python3
import requests
import os
import csv
from datetime import datetime

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def export_team_roster(output_file="team_roster.csv"):
    """Export all team members to CSV."""
    all_members = []
    offset = 0
    limit = 50
    
    while True:
        response = requests.get(
            f"{BASE_URL}/members",
            auth=AUTH,
            params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        data = response.json()
        members = data.get("members", [])
        
        if not members:
            break
        
        all_members.extend(members)
        
        if len(members) < limit:
            break
        
        offset += limit
    
    # Write to CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "email", "role", "status", "createdAt", "lastActiveAt", "id"
        ])
        writer.writeheader()
        
        for member in all_members:
            writer.writerow({
                "email": member.get("email", ""),
                "role": member.get("role", "member"),
                "status": member.get("status", "active"),
                "createdAt": member.get("createdAt", ""),
                "lastActiveAt": member.get("lastActiveAt", ""),
                "id": member.get("id", "")
            })
    
    print(f"✅ Exported {len(all_members)} members to {output_file}")
    return all_members

def get_user_id_by_email(email: str):
    """Get user ID from email address."""
    response = requests.get(
        f"{BASE_URL}/members",
        auth=AUTH,
        params={"email": email}
    )
    response.raise_for_status()
    members = response.json().get("members", [])
    
    if members:
        return members[0].get("id")
    return None

if __name__ == "__main__":
    export_team_roster()
    
    # Example: Find user ID
    user_id = get_user_id_by_email("admin@company.com")
    print(f"Admin user ID: {user_id}")
```

**Success Criteria:**
- [ ] Successfully authenticated with Admin API
- [ ] Retrieved list of team members
- [ ] Handled pagination correctly
- [ ] Exported team roster to CSV

---

## Lesson 9.2: Daily Usage Data

### Concept (5 minutes)

> *"The most-asked-for admin report. Finance wants to know: 'What did we spend yesterday?' Engineering leads want: 'Who's using what?' This endpoint answers both."*

### Key Endpoint: `GET /v1/admin/analytics/usage/daily`

**Returns:**
- Cost per day (granular for trend analysis)
- Input/output token counts
- Active users per day
- Breakdown by user and model (optional)

### Hands-On Exercise (10 minutes)

**Step 1:** Get daily usage for the past week

```bash
END=$(date +%Y-%m-%d)
START=$(date -d "7 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '.daily[] | {date: .date, cost: .cost, tokens: .totalTokens, users: .activeUsers}'
```

**Step 2:** Generate daily cost report with running total

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '[.daily[] | {date: .date, cost: .cost}] | 
         (.[0] | .running_total = .cost) as $first |
         [ $first ] + 
         [ .[1:] | reduce .[] as $item ({prev: $first.cost, arr: []}; 
            .arr += [$item + {running_total: (.prev + $item.cost)}] | 
            {prev: (.prev + $item.cost), arr: .arr}) | .arr[] ]'
```

**Step 3:** Python script for daily usage analytics

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta
from collections import defaultdict

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def get_daily_usage(days=30):
    """Retrieve daily usage for the last N days."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        f"{BASE_URL}/analytics/usage/daily",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    response.raise_for_status()
    return response.json().get("daily", [])

def generate_cost_report():
    """Create a comprehensive cost report."""
    daily_data = get_daily_usage(days=30)
    
    if not daily_data:
        print("No data available")
        return
    
    # Calculate metrics
    total_cost = sum(d['cost'] for d in daily_data)
    total_tokens = sum(d.get('totalTokens', 0) for d in daily_data)
    avg_daily_cost = total_cost / len(daily_data)
    avg_daily_users = sum(d.get('activeUsers', 0) for d in daily_data) / len(daily_data)
    
    # Week-over-week comparison
    last_week = daily_data[-7:] if len(daily_data) >= 7 else daily_data
    prev_week = daily_data[-14:-7] if len(daily_data) >= 14 else []
    
    last_week_cost = sum(d['cost'] for d in last_week)
    prev_week_cost = sum(d['cost'] for d in prev_week) if prev_week else last_week_cost
    
    wow_change = ((last_week_cost - prev_week_cost) / prev_week_cost * 100) if prev_week_cost > 0 else 0
    
    # Costliest days
    costliest_days = sorted(daily_data, key=lambda x: x['cost'], reverse=True)[:5]
    
    print("📊 DAILY USAGE REPORT")
    print("=" * 50)
    print(f"Period: {daily_data[0]['date']} to {daily_data[-1]['date']}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Total tokens: {total_tokens:,}")
    print(f"Average daily cost: ${avg_daily_cost:.2f}")
    print(f"Average daily users: {avg_daily_users:.0f}")
    
    arrow = "↑" if wow_change > 0 else "↓"
    print(f"Week-over-week change: {arrow} {abs(wow_change):.1f}%")
    
    print("\n💰 Top 5 Costliest Days:")
    for day in costliest_days:
        print(f"  {day['date']}: ${day['cost']:.2f} ({day.get('activeUsers', 0)} users)")
    
    print("\n📈 Daily breakdown (last 14 days):")
    print(f"{'Date':<12} {'Cost':<10} {'Tokens (K)':<12} {'Users':<8}")
    print("-" * 45)
    
    for day in daily_data[-14:]:
        tokens_k = day.get('totalTokens', 0) / 1000
        print(f"{day['date']:<12} ${day['cost']:<9.2f} {tokens_k:<11.1f} {day.get('activeUsers', 0):<8}")
    
    # Cost alert if over budget
    if total_cost > 500:
        print(f"\n⚠️ BUDGET ALERT: Monthly cost ${total_cost:.2f} exceeds $500")
    elif total_cost > 300:
        print(f"\n⚠️ BUDGET WARNING: Monthly cost ${total_cost:.2f} approaching limit")

if __name__ == "__main__":
    generate_cost_report()
```

**Success Criteria:**
- [ ] Retrieved daily usage for date range
- [ ] Calculated cost trends and week-over-week changes
- [ ] Generated readable cost report

---

## Lesson 9.3: Setting User Spend Limits

### Concept (5 minutes)

> *"Programmatic cost governance. Prevent bill shock by setting monthly caps per user. Great for protecting against runaway agent usage or expensive model overuse."*

### Key Endpoint: `PATCH /v1/admin/policies/users/{userId}/limits`

**Exceedance Action Options:**

| Action | Behavior |
|--------|----------|
| `alert` | Send notification but allow usage |
| `block` | Prevent any further requests for the month |

### Hands-On Exercise (8 minutes)

**Step 1:** Get user ID from email

```bash
EMAIL="developer@company.com"

USER_ID=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?email=$EMAIL" \
  | jq -r '.members[0].id')

echo "User ID: $USER_ID"
```

**Step 2:** Set a monthly spending limit

```bash
curl -X PATCH "https://api.cursor.com/v1/admin/policies/users/$USER_ID/limits" \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "monthlyLimit": 50.00,
    "exceedanceAction": "block"
  }' | jq '.'
```

**Step 3:** Check a user's current limit and usage

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/policies/users/$USER_ID/limits" \
  | jq '{monthlyLimit: .monthlyLimit, currentUsage: .currentMonthUsage, remaining: (.monthlyLimit - .currentMonthUsage)}'
```

**Step 4:** Python script for bulk limit setting

```python
#!/usr/bin/env python3
import requests
import os
import csv

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def set_user_limit(email: str, monthly_limit: float, action: str = "block"):
    """Set spending limit for a specific user."""
    
    # Get user ID
    resp = requests.get(
        f"{BASE_URL}/members",
        auth=AUTH,
        params={"email": email}
    )
    resp.raise_for_status()
    members = resp.json().get("members", [])
    
    if not members:
        print(f"❌ User not found: {email}")
        return False
    
    user_id = members[0]['id']
    
    # Set the limit
    response = requests.patch(
        f"{BASE_URL}/policies/users/{user_id}/limits",
        auth=AUTH,
        json={"monthlyLimit": monthly_limit, "exceedanceAction": action}
    )
    
    if response.status_code == 200:
        print(f"✅ Set ${monthly_limit} limit for {email}")
        return True
    else:
        print(f"❌ Failed for {email}: {response.text}")
        return False

def bulk_set_limits(csv_file: str):
    """Set limits from CSV: email, monthly_limit, action."""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            set_user_limit(
                row['email'],
                float(row['monthly_limit']),
                row.get('action', 'block')
            )

def get_users_exceeding_limit(threshold: float = 100):
    """Find users who have exceeded a spending threshold."""
    
    # Get usage for current month
    start = datetime.now().replace(day=1).strftime("%Y-%m-%d")
    end = datetime.now().strftime("%Y-%m-%d")
    
    response = requests.get(
        f"{BASE_URL}/analytics/usage/users",
        auth=AUTH,
        params={"startDate": start, "endDate": end}
    )
    response.raise_for_status()
    users = response.json().get("users", [])
    
    exceeding = [u for u in users if u.get('cost', 0) > threshold]
    
    print(f"\n💰 Users exceeding ${threshold} this month:")
    for user in sorted(exceeding, key=lambda x: x['cost'], reverse=True):
        print(f"  {user['user']['email']}: ${user['cost']:.2f}")
    
    return exceeding

if __name__ == "__main__":
    # Set a single user limit
    set_user_limit("new-hire@company.com", 30.00)
    
    # Or bulk set from CSV
    # bulk_set_limits("limits.csv")
    
    # Find heavy users
    get_users_exceeding_limit(100)
```

**Example `limits.csv`:**
```csv
email,monthly_limit,action
intern@company.com,20,block
contractor@company.com,50,alert
lead@company.com,200,alert
```

**Success Criteria:**
- [ ] Retrieved user ID from email
- [ ] Set monthly spending limit
- [ ] Verified limit was applied
- [ ] Implemented bulk limit setting

---

## Lesson 9.4: Model Usage Analytics

### Concept (5 minutes)

> *"Direct insight into cost and adoption. Which models are actually being used? Is the expensive Opus model worth the cost? Should you train people on cheaper alternatives?"*

### Key Endpoint: `GET /v1/admin/analytics/usage/models`

### Hands-On Exercise (8 minutes)

**Step 1:** Get model usage for current month

```bash
START=$(date -d "$(date +%Y-%m-01)" +%Y-%m-%d)
END=$(date +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/models?startDate=$START&endDate=$END" \
  | jq '.models[] | {model: .modelId, cost: .cost, requests: .requestCount, users: .userCount}'
```

**Step 2:** Identify expensive model overuse

```bash
# Find which users are using expensive Opus model
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/users?startDate=$START&endDate=$END" \
  | jq '.users[] | select(.modelBreakdown."claude-4.7-opus" != null) | 
         {email: .user.email, opus_cost: .modelBreakdown."claude-4.7-opus".cost, total_cost: .cost}'
```

**Step 3:** Python cost optimization report

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

# Model pricing reference (from Module 7)
MODEL_PRICING = {
    "gpt-5-mini": {"input": 0.25, "output": 2.00},
    "claude-4.5-haiku": {"input": 1.00, "output": 5.00},
    "gemini-3.1-pro": {"input": 2.00, "output": 12.00},
    "claude-4.6-sonnet": {"input": 3.00, "output": 15.00},
    "gpt-5.3-codex": {"input": 1.75, "output": 14.00},
    "claude-4.7-opus": {"input": 5.00, "output": 25.00},
    "gpt-5.5": {"input": 5.00, "output": 30.00}
}

def get_model_usage(days=30):
    """Get model usage for the last N days."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        f"{BASE_URL}/analytics/usage/models",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    response.raise_for_status()
    return response.json().get("models", [])

def get_user_model_breakdown(days=30):
    """Get per-user model usage."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        f"{BASE_URL}/analytics/usage/users",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    response.raise_for_status()
    return response.json().get("users", [])

def generate_optimization_report():
    """Identify cost-saving opportunities."""
    models = get_model_usage(days=30)
    users = get_user_model_breakdown(days=30)
    
    print("🤖 MODEL USAGE & OPTIMIZATION REPORT")
    print("=" * 60)
    
    if not models:
        print("No model usage data available")
        return
    
    # Sort by cost
    sorted_models = sorted(models, key=lambda x: x.get('cost', 0), reverse=True)
    
    print("\n📊 Model Cost Breakdown:")
    print(f"{'Model':<25} {'Cost':<12} {'Requests':<10} {'Users':<8} {'% of Total':<10}")
    print("-" * 65)
    
    total_cost = sum(m.get('cost', 0) for m in models)
    
    for model in sorted_models:
        model_id = model.get('modelId', 'unknown')
        cost = model.get('cost', 0)
        percentage = (cost / total_cost * 100) if total_cost > 0 else 0
        print(f"{model_id[:24]:<25} ${cost:<11.2f} {model.get('requestCount', 0):<10} "
              f"{model.get('userCount', 0):<8} {percentage:.1f}%")
    
    # Identify optimization opportunities
    print("\n💡 OPTIMIZATION OPPORTUNITIES:")
    
    # 1. Find expensive model users
    opus_users = []
    for user in users:
        breakdown = user.get('modelBreakdown', {})
        if 'claude-4.7-opus' in breakdown:
            opus_users.append({
                'email': user['user']['email'],
                'opus_cost': breakdown['claude-4.7-opus']['cost']
            })
    
    if opus_users:
        print(f"\n  Users using Claude Opus (expensive):")
        for user in sorted(opus_users, key=lambda x: x['opus_cost'], reverse=True)[:5]:
            print(f"    - {user['email']}: ${user['opus_cost']:.2f}")
        print("    → Suggest switching to Claude Sonnet for non-critical tasks")
    
    # 2. Recommend cheaper alternatives
    sonnet_cost = sum(m.get('cost', 0) for m in models if 'sonnet' in m.get('modelId', '').lower())
    
    if sonnet_cost > 100:
        print(f"\n  High Sonnet usage: ${sonnet_cost:.2f}")
        print("    → Consider GPT-5.3 Codex for 40% cost reduction")
    
    # 3. Total savings estimate
    if total_cost > 500:
        estimated_savings = total_cost * 0.25  # Rough estimate
        print(f"\n  Estimated monthly savings: ${estimated_savings:.2f} (25%)")
        print("    → Implement model usage guidelines and spend limits")

if __name__ == "__main__":
    generate_optimization_report()
```

**Success Criteria:**
- [ ] Retrieved model usage breakdown
- [ ] Identified expensive model users
- [ ] Generated cost optimization recommendations

---

## Lesson 9.5: Daily Active Users (DAU)

### Concept (4 minutes)

> *"The headline adoption metric for leadership. DAU tells you if your team is actually using Cursor or if licenses are being wasted."*

### Why This Metric Matters

- Track adoption after rollout
- Identify unused licenses for reallocation
- Measure impact of training sessions
- Justify renewal and expansion

### Key Endpoint: `GET /v1/admin/analytics/usage/daily` (aggregate activeUsers)

### Hands-On Exercise (6 minutes)

**Step 1:** Calculate DAU from daily usage data

```bash
START=$(date -d "30 days ago" +%Y-%m-%d)
END=$(date +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '{dates: [.daily[] | {date: .date, activeUsers: .activeUsers}], 
         avg_weekly: ([.daily[-7:] | .[].activeUsers] | add / length),
         peak: ([.daily[] | .activeUsers] | max)}'
```

**Step 2:** Leadership-ready DAU report

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta
import statistics

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def get_daily_active_users(days=30):
    """Calculate DAU trend."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        f"{BASE_URL}/analytics/usage/daily",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    response.raise_for_status()
    return response.json().get("daily", [])

def generate_dau_report():
    """Create DAU report for leadership."""
    data = get_daily_active_users(days=30)
    
    if not data:
        print("No data available")
        return
    
    # Get total team size
    resp = requests.get(f"{BASE_URL}/members", auth=AUTH)
    total_members = len(resp.json().get("members", []))
    
    # Calculate metrics
    daily_users = [d['activeUsers'] for d in data]
    avg_daily = statistics.mean(daily_users)
    median_daily = statistics.median(daily_users)
    max_daily = max(daily_users)
    min_daily = min(daily_users)
    std_dev = statistics.stdev(daily_users) if len(daily_users) > 1 else 0
    
    # Weekly trends
    weeks = [data[i:i+7] for i in range(0, len(data), 7) if len(data[i:i+7]) == 7]
    weekly_avgs = [sum(w[d]['activeUsers'] for d in range(len(w))) / len(w) for w in weeks]
    
    # Growth rate
    first_week_avg = weekly_avgs[0] if weekly_avgs else avg_daily
    last_week_avg = weekly_avgs[-1] if weekly_avgs else avg_daily
    growth_rate = ((last_week_avg - first_week_avg) / first_week_avg * 100) if first_week_avg > 0 else 0
    
    print("📊 DAILY ACTIVE USERS (DAU) REPORT")
    print("=" * 50)
    print(f"Reporting period: {data[0]['date']} to {data[-1]['date']}")
    print(f"Total team members: {total_members}")
    
    print(f"\n📈 Key Metrics:")
    print(f"   Average DAU: {avg_daily:.0f}")
    print(f"   Median DAU: {median_daily:.0f}")
    print(f"   Peak DAU: {max_daily}")
    print(f"   Lowest DAU: {min_daily}")
    print(f"   Standard deviation: {std_dev:.1f}")
    print(f"   Adoption rate: {(avg_daily / total_members * 100):.1f}%")
    
    arrow = "↑" if growth_rate > 0 else "↓"
    print(f"\n   Growth rate (WoW): {arrow} {abs(growth_rate):.1f}%")
    
    # Health assessment
    print(f"\n🏥 Adoption Health Assessment:")
    if avg_daily / total_members > 0.8:
        print("   ✅ Excellent: Over 80% of team active daily")
    elif avg_daily / total_members > 0.5:
        print("   ✅ Good: Over 50% of team active daily")
    elif avg_daily / total_members > 0.3:
        print("   ⚠️ Moderate: Only 30-50% active daily")
    else:
        print("   ❌ Low: Less than 30% active daily - investigate")
    
    # Weekly breakdown for leadership
    if weekly_avgs:
        print("\n📅 Weekly DAU Averages:")
        for i, week_avg in enumerate(weekly_avgs):
            week_start = data[i*7]['date']
            print(f"   Week of {week_start}: {week_avg:.0f} users")
    
    # Low activity days
    low_days = [d for d in data if d['activeUsers'] < avg_daily * 0.5]
    if low_days:
        print(f"\n⚠️ Low activity days: {len(low_days)} days below 50% average")
        print("   Consider team reminders or training on these days")

if __name__ == "__main__":
    generate_dau_report()
```

**Success Criteria:**
- [ ] Calculated DAU from daily data
- [ ] Generated adoption rate and growth metrics
- [ ] Created leadership-ready report

---

## Lesson 9.6: Leaderboards

### Concept (5 minutes)

> *"Usage rankings and how to present them responsibly. Leaderboards can drive engagement OR create unhealthy competition. Here's the balanced approach."*

### Responsible Leaderboard Principles

| Principle | Implementation |
|-----------|----------------|
| **Anonymize** | Use roles or anonymized names, not full emails |
| **Focus on positive metrics** | Show savings, not spending |
| **Opt-in only** | Allow users to choose public visibility |
| **Include context** | Show team size, role differences |

### Hands-On Exercise (6 minutes)

**Step 1:** Create anonymous leaderboard

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta
from collections import defaultdict

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def get_user_usage(days=30):
    """Get per-user usage data."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        f"{BASE_URL}/analytics/usage/users",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    response.raise_for_status()
    return response.json().get("users", [])

def get_user_roles():
    """Get mapping of user emails to roles."""
    response = requests.get(f"{BASE_URL}/members", auth=AUTH)
    members = response.json().get("members", [])
    return {m['email']: m.get('role', 'member') for m in members}

def anonymize_email(email: str) -> str:
    """Anonymize email for leaderboard display."""
    local_part = email.split('@')[0]
    if len(local_part) <= 3:
        return local_part[0] + "***"
    return local_part[:2] + "..." + local_part[-2:]

def generate_anonymous_leaderboard():
    """Create anonymized leaderboard for team sharing."""
    users = get_user_usage(days=30)
    roles = get_user_roles()
    
    # Sort by requests (engagement, not cost)
    sorted_users = sorted(users, key=lambda x: x.get('requestCount', 0), reverse=True)
    
    print("🏆 CURSOR ENGAGEMENT LEADERBOARD (Last 30 Days)")
    print("=" * 60)
    print("Note: Names are anonymized. This measures engagement, not performance.")
    print()
    
    print(f"{'Rank':<6} {'User':<20} {'Requests':<12} {'Cost':<10} {'Efficiency':<12}")
    print("-" * 65)
    
    for i, user in enumerate(sorted_users[:10], 1):
        email = user.get('user', {}).get('email', 'unknown')
        anon_name = anonymize_email(email)
        role = roles.get(email, 'member')
        
        # Calculate efficiency (requests per dollar)
        cost = user.get('cost', 0)
        requests_count = user.get('requestCount', 0)
        efficiency = requests_count / cost if cost > 0 else 0
        
        medal = ""
        if i == 1:
            medal = "🥇 "
        elif i == 2:
            medal = "🥈 "
        elif i == 3:
            medal = "🥉 "
        
        print(f"{medal}{i:<4} {anon_name:<20} {requests_count:<12} ${cost:<9.2f} {efficiency:<11.1f}")

def generate_efficiency_leaderboard():
    """Focus on efficiency (most value per dollar)."""
    users = get_user_usage(days=30)
    
    # Calculate efficiency (tokens per dollar)
    efficient_users = []
    for user in users:
        cost = user.get('cost', 0)
        tokens = user.get('totalTokens', 0)
        efficiency = tokens / cost if cost > 0 else 0
        efficient_users.append({
            'email': user['user']['email'],
            'efficiency': efficiency,
            'cost': cost,
            'tokens': tokens
        })
    
    sorted_users = sorted(efficient_users, key=lambda x: x['efficiency'], reverse=True)
    
    print("\n💰 EFFICIENCY LEADERBOARD (Best value per dollar)")
    print("=" * 60)
    print("Ranking by tokens generated per dollar spent.\n")
    
    print(f"{'Rank':<6} {'User (anonymized)':<20} {'Tokens/$':<12} {'Total Cost':<12}")
    print("-" * 55)
    
    for i, user in enumerate(sorted_users[:10], 1):
        anon_name = anonymize_email(user['email'])
        print(f"{i:<6} {anon_name:<20} {user['efficiency']:<11,.0f} ${user['cost']:<11.2f}")

def generate_savings_leaderboard():
    """Focus on savings from using cheaper models."""
    users = get_user_usage(days=30)
    
    savings_list = []
    for user in users:
        email = user.get('user', {}).get('email', 'unknown')
        breakdown = user.get('modelBreakdown', {})
        
        # Calculate savings if Opus usage was switched to Sonnet
        opus_cost = 0
        if 'claude-4.7-opus' in breakdown:
            opus_cost = breakdown['claude-4.7-opus'].get('cost', 0)
        
        # Approximate savings (Opus is ~67% more than Sonnet)
        savings = opus_cost * 0.4  # Conservative estimate
        
        if savings > 5:  # Only show meaningful savings
            savings_list.append({'email': email, 'savings': savings})
    
    sorted_savings = sorted(savings_list, key=lambda x: x['savings'], reverse=True)
    
    print("\n💡 SAVINGS LEADERBOARD (Smart model choices)")
    print("=" * 60)
    print("Users who saved money by choosing efficient models.\n")
    
    for i, saver in enumerate(sorted_savings[:5], 1):
        anon_name = anonymize_email(saver['email'])
        print(f"{i}. {anon_name}: ~${saver['savings']:.2f} saved")

if __name__ == "__main__":
    generate_anonymous_leaderboard()
    generate_efficiency_leaderboard()
    generate_savings_leaderboard()
```

**Success Criteria:**
- [ ] Created anonymized leaderboard
- [ ] Built efficiency-focused leaderboard
- [ ] Implemented savings leaderboard (positive metric)

---

## Lesson 9.7: Conversation Insights (Demonstration)

### Concept (6 minutes)

> *"Intent, complexity, and category analysis. This is a demonstration of advanced analytics – understanding WHAT users are doing, not just how much."*

### What Conversation Insights Reveal

- Are users asking simple questions or complex refactors?
- What categories of tasks are most common?
- Where are users getting stuck?
- Which models perform best for which task types?

**Note:** This endpoint may require Enterprise plan.

### Demonstration (6 minutes)

```python
#!/usr/bin/env python3
"""
Conversation Insights - Demonstration
Note: This requires Enterprise plan or special access
"""

import requests
import os
from collections import Counter
from datetime import datetime, timedelta

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def get_conversations(days=30):
    """Retrieve conversation metadata (demo)."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    # This endpoint may require Enterprise plan
    response = requests.get(
        f"{BASE_URL}/analytics/conversations",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
            "limit": 500
        }
    )
    
    if response.status_code == 200:
        return response.json().get("conversations", [])
    else:
        print(f"⚠️ Conversation insights endpoint unavailable: {response.status_code}")
        print("   (May require Enterprise plan)")
        return []

def demonstrate_intent_analysis():
    """Show what users are trying to accomplish."""
    convos = get_conversations()
    
    if not convos:
        print("Demo data not available. Showing expected output structure.")
        print("\n🎯 CONVERSATION INTENT ANALYSIS (Example)")
        print("=" * 50)
        print("What users are trying to do:\n")
        print("  debug              ████████████ 35.2%")
        print("  refactor           ████████ 22.1%")
        print("  document           ██████ 16.8%")
        print("  test               ████ 11.5%")
        print("  feature            ███ 8.9%")
        print("  understand         ██ 5.5%")
        return
    
    intents = [c.get('intent', 'unknown') for c in convos]
    intent_counts = Counter(intents)
    
    print("🎯 CONVERSATION INTENT ANALYSIS")
    print("=" * 50)
    print("What are users trying to do?\n")
    
    total = len(convos)
    for intent, count in intent_counts.most_common():
        percentage = (count / total) * 100
        bar_length = int(percentage / 2)
        bar = "█" * bar_length
        print(f"{intent:<15} {percentage:5.1f}% {bar}")

def demonstrate_complexity_analysis():
    """Show task complexity distribution."""
    convos = get_conversations()
    
    if not convos:
        print("\n📊 COMPLEXITY DISTRIBUTION (Example)")
        print("=" * 50)
        print("How hard are the tasks?\n")
        print("  simple        45.2% ████████████████████")
        print("  moderate      32.8% ███████████████")
        print("  complex       15.3% ███████")
        print("  architectural  6.7% ███")
        return
    
    complexity_levels = ['simple', 'moderate', 'complex', 'architectural']
    complexity_counts = Counter(c.get('complexity', 'simple') for c in convos)
    
    print("\n📊 COMPLEXITY DISTRIBUTION")
    print("=" * 50)
    print("How hard are the tasks?\n")
    
    total = len(convos)
    for level in complexity_levels:
        count = complexity_counts.get(level, 0)
        percentage = (count / total) * 100
        bar_length = int(percentage / 2)
        bar = "█" * bar_length
        print(f"{level:<12} {percentage:5.1f}% {bar}")

def demonstrate_category_analysis():
    """Show which domains users work in."""
    convos = get_conversations()
    
    if not convos:
        print("\n📂 CATEGORY ANALYSIS (Example)")
        print("=" * 50)
        print("What domains are users working in?\n")
        print("  backend          40.2% ████████████████████")
        print("  frontend         28.5% ██████████████")
        print("  database         15.3% ███████")
        print("  devops           10.1% █████")
        print("  security          6.0% ███")
        return
    
    categories = []
    for c in convos:
        cats = c.get('categories', [])
        categories.extend(cats)
    
    category_counts = Counter(categories)
    total = len(categories)
    
    print("\n📂 CATEGORY ANALYSIS")
    print("=" * 50)
    print("What domains are users working in?\n")
    
    for category, count in category_counts.most_common(10):
        percentage = (count / total) * 100 if total > 0 else 0
        bar_length = int(percentage / 2)
        bar = "█" * bar_length
        print(f"{category:<15} {percentage:5.1f}% {bar}")

def identify_stuck_patterns():
    """Find where users struggle."""
    convos = get_conversations()
    
    if not convos:
        print("\n⚠️ USERS GETTING STUCK (Example)")
        print("=" * 50)
        print("Found 12 conversations where users struggled.")
        print("\nCommon challenging intent types:")
        print("   - debugging: 8 occurrences")
        print("   - refactoring: 3 occurrences")
        print("   - integration: 1 occurrence")
        print("\n💡 SUGGESTIONS:")
        print("   - Create documentation for debugging tasks")
        print("   - Consider training on refactoring workflows")
        return
    
    stuck = [c for c in convos 
             if c.get('duration', 0) > 300  # >5 minutes
             and c.get('success', True) == False]
    
    if stuck:
        print(f"\n⚠️ USERS GETTING STUCK")
        print("=" * 50)
        print(f"Found {len(stuck)} conversations where users struggled.")
        
        stuck_intents = Counter([c.get('intent') for c in stuck])
        print("\nCommon challenging intent types:")
        for intent, count in stuck_intents.most_common(3):
            print(f"   - {intent}: {count} occurrences")
        
        print("\n💡 SUGGESTIONS:")
        print("   - Create documentation for 'debugging' tasks")
        print("   - Consider training on 'refactoring' workflows")
        print("   - Add team examples for complex patterns")
    else:
        print("\n✅ No stuck patterns detected")

if __name__ == "__main__":
    print("🔍 CONVERSATION INSIGHTS DEMONSTRATION")
    print("=" * 60)
    print("This demonstrates the type of analytics available with Enterprise plan.\n")
    
    demonstrate_intent_analysis()
    demonstrate_complexity_analysis()
    demonstrate_category_analysis()
    identify_stuck_patterns()
```

**Success Criteria (Demonstration):**
- [ ] Understood conversation insights capabilities
- [ ] Saw intent distribution analysis
- [ ] Understood complexity and category tracking
- [ ] Learned how to identify stuck patterns

---

## Lesson 9.8: Destructive Admin Operations (Demonstration)

### Concept (6 minutes)

> *"Safe patterns for removing a team member. Destructive operations require care – here's the proper playbook."*

### The Safety Playbook

```
┌─────────────────────────────────────────────────────────────┐
│              SAFE REMOVAL PLAYBOOK                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Step 1: AUDIT FIRST                                         │
│  └── What resources does the user own?                       │
│      • Active agents                                         │
│      • Recent runs                                           │
│      • API keys                                              │
│                                                              │
│  Step 2: SOFT DELETE                                         │
│  └── Deactivate before removing                              │
│      • User cannot create new agents                         │
│      • Existing agents continue running                      │
│      • Can be reactivated                                    │
│                                                              │
│  Step 3: TRANSFER OWNERSHIP                                  │
│  └── Move important resources to new owner                   │
│      • Critical agents                                       │
│      • Webhook configurations                                │
│                                                              │
│  Step 4: LOG EVERYTHING                                      │
│  └── For compliance and audit trails                         │
│                                                              │
│  Step 5: CONFIRM BEFORE DELETE                               │
│  └── Require explicit confirmation                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Demonstration (6 minutes)

```python
#!/usr/bin/env python3
"""
Safe Removal Pattern - Demonstration
This shows the proper workflow for removing a team member
"""

import requests
import os
from datetime import datetime
import json

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

class SafeRemovalDemo:
    """Demonstrate safe user removal workflow."""
    
    def __init__(self, email: str):
        self.email = email
        self.user_id = None
        self.resources = None
        self.audit_log = []
    
    def _log(self, action: str, details: dict):
        """Internal audit logging."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "user": self.email,
            "details": details
        }
        self.audit_log.append(entry)
        print(f"📝 LOG: {action} - {json.dumps(details)[:100]}")
    
    def step1_find_user(self):
        """Locate the user by email."""
        print("\n🔍 Step 1: Finding user...")
        
        response = requests.get(
            f"{BASE_URL}/members",
            auth=AUTH,
            params={"email": self.email}
        )
        
        if response.status_code != 200:
            print(f"❌ API error: {response.status_code}")
            return False
        
        members = response.json().get("members", [])
        
        if not members:
            print(f"❌ User {self.email} not found")
            return False
        
        self.user_id = members[0]['id']
        print(f"✅ Found user: {self.user_id}")
        self._log("find_user", {"user_id": self.user_id})
        return True
    
    def step2_audit_resources(self):
        """List all resources owned by the user."""
        print("\n📋 Step 2: Auditing user's resources...")
        
        response = requests.get(
            f"{BASE_URL}/members/{self.user_id}/resources",
            auth=AUTH
        )
        
        if response.status_code != 200:
            print(f"⚠️ Could not fetch resources: {response.status_code}")
            self.resources = {"agents": [], "runs": []}
        else:
            self.resources = response.json()
        
        agents = self.resources.get('agents', [])
        runs = self.resources.get('runs', [])
        
        print(f"   Agents owned: {len(agents)}")
        print(f"   Runs executed: {len(runs)}")
        
        if agents:
            print(f"   Recent agents:")
            for agent in agents[:3]:
                print(f"     - {agent.get('id', 'unknown')}: {agent.get('status', 'unknown')}")
        
        self._log("audit_resources", {
            "agent_count": len(agents),
            "run_count": len(runs)
        })
        return True
    
    def step3_deactivate(self):
        """Soft delete - deactivate first."""
        print("\n⚠️ Step 3: Deactivating user (soft delete)...")
        
        # In a real implementation:
        # response = requests.patch(
        #     f"{BASE_URL}/members/{self.user_id}/status",
        #     auth=AUTH,
        #     json={"status": "inactive"}
        # )
        
        # Demo simulation
        print(f"   User {self.email} would be deactivated")
        print("   Effect: Cannot create new agents or runs")
        print("   Existing agents continue running")
        
        self._log("deactivate_user", {"status": "inactive"})
        return True
    
    def step4_transfer_resources(self, new_owner_email: str):
        """Transfer ownership of critical resources."""
        print(f"\n🔄 Step 4: Transferring resources to {new_owner_email}...")
        
        # Find new owner ID
        resp = requests.get(
            f"{BASE_URL}/members",
            auth=AUTH,
            params={"email": new_owner_email}
        )
        
        if resp.status_code != 200:
            print(f"⚠️ Could not find new owner")
            return False
        
        members = resp.json().get("members", [])
        if not members:
            print(f"❌ New owner {new_owner_email} not found")
            return False
        
        new_owner_id = members[0]['id']
        
        # Transfer each agent (demo simulation)
        agents = self.resources.get('agents', [])
        for agent in agents:
            print(f"   Transferring agent: {agent.get('id', 'unknown')}")
            # In real implementation:
            # requests.post(f"/v1/agents/{agent['id']}/transfer", ...)
        
        self._log("transfer_resources", {
            "new_owner": new_owner_email,
            "agent_count": len(agents)
        })
        return True
    
    def step5_hard_delete(self):
        """Permanent removal (use sparingly)."""
        print("\n🗑️ Step 5: Permanent removal...")
        print("   ⚠️ This action is permanent and cannot be undone")
        print("   ⚠️ Only use for GDPR compliance or security incidents")
        
        # In real implementation with confirmation:
        # response = requests.delete(f"{BASE_URL}/members/{self.user_id}", auth=AUTH)
        
        print("   [Demo] User would be permanently removed")
        
        self._log("hard_delete_user", {"permanent": True})
        return True
    
    def generate_audit_report(self):
        """Generate audit report for compliance."""
        print("\n📄 AUDIT REPORT")
        print("=" * 50)
        print(f"User: {self.email}")
        print(f"User ID: {self.user_id}")
        print("\nActions taken:")
        
        for entry in self.audit_log:
            print(f"  [{entry['timestamp'][:19]}] {entry['action']}")
    
    def demonstrate_complete_workflow(self, new_owner_email: str = None):
        """Run the complete safe removal demonstration."""
        print("=" * 60)
        print("🔐 SAFE USER REMOVAL DEMONSTRATION")
        print("=" * 60)
        
        if not self.step1_find_user():
            return False
        
        self.step2_audit_resources()
        self.step3_deactivate()
        
        if new_owner_email:
            self.step4_transfer_resources(new_owner_email)
        
        # Hard delete is optional - most orgs skip this
        print("\n💡 Note: Hard delete is often skipped.")
        print("   Deactivated users no longer incur costs.")
        print("   Hard delete is only for GDPR compliance.")
        
        self.generate_audit_report()
        return True

def demonstrate_bulk_deactivation():
    """Demonstrate deactivating inactive users."""
    print("\n" + "=" * 60)
    print("📦 BULK DEACTIVATION DEMONSTRATION")
    print("=" * 60)
    print("Finding users inactive for 90+ days...")
    
    # In real implementation:
    # 1. Get user usage data
    # 2. Filter users with no activity in last 90 days
    # 3. Generate report
    # 4. Require approval before deactivation
    
    print("\n   Found 3 potentially inactive users:")
    print("     - contractor@company.com (last active: 95 days ago)")
    print("     - intern@company.com (last active: 120 days ago)")
    print("     - former-employee@company.com (last active: 180 days ago)")
    
    print("\n   Recommended action:")
    print("     1. Review with team leads")
    print("     2. Send notification emails")
    print("     3. Deactivate after 7 days if no response")
    print("     4. Archive and remove after 30 days")

if __name__ == "__main__":
    # Demonstrate single user removal
    demo = SafeRemovalDemo("contractor@company.com")
    demo.demonstrate_complete_workflow(new_owner_email="team-lead@company.com")
    
    # Demonstrate bulk deactivation
    demonstrate_bulk_deactivation()
```

**Success Criteria (Demonstration):**
- [ ] Understood the 5-step safe removal pattern
- [ ] Saw audit-first principle in action
- [ ] Learned soft delete vs hard delete
- [ ] Understood resource transfer requirements
- [ ] Saw bulk deactivation pattern

---

## Module Summary

| Lesson | Topic | Time | Type |
|--------|-------|------|------|
| 9.1 | Listing Team Members | 8 min | Exercise |
| 9.2 | Daily Usage Data | 10 min | Exercise |
| 9.3 | Setting User Spend Limits | 8 min | Exercise |
| 9.4 | Model Usage Analytics | 8 min | Exercise |
| 9.5 | Daily Active Users | 6 min | Exercise |
| 9.6 | Leaderboards | 6 min | Exercise |
| 9.7 | Conversation Insights | 6 min | Demo |
| 9.8 | Destructive Operations | 6 min | Demo |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              ADMIN API QUICK REFERENCE                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ENDPOINTS:                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ GET    /admin/members                  List members  │   │
│  │ GET    /admin/analytics/usage/daily    Daily usage   │   │
│  │ GET    /admin/analytics/usage/models   Model usage   │   │
│  │ GET    /admin/analytics/usage/users    Per-user      │   │
│  │ PATCH  /admin/policies/users/{id}/limits  Set limits │   │
│  │ GET    /admin/members/{id}/resources  User resources │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  RESPONSIBLE LEADERBOARD PRINCIPLES:                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Anonymize user emails                            │   │
│  │ • Focus on positive metrics (savings, efficiency)  │   │
│  │ • Opt-in only for public visibility                │   │
│  │ • Include role context                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  SAFE REMOVAL PLAYBOOK:                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 1. Audit resources                                 │   │
│  │ 2. Soft delete (deactivate)                        │   │
│  │ 3. Transfer ownership                              │   │
│  │ 4. Log everything                                  │   │
│  │ 5. Confirm before hard delete                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 10

> *"Now that you can manage your team and analyze usage, Module 10 will cover AI Code Tracking and Reporting – attributing AI contributions per commit, exporting metrics to BI tools, and building complete dashboards."*

---

*End of Module 9*