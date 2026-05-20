# Module 9: Admin and Analytics APIs

## Cursor Training Program — Day 2 (Hands-On)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~75 minutes |
| **Format** | Hands-on exercise + demonstrations |
| **Prerequisites** | Admin API key (not User key), Python 3.8+, jq installed |
| **Module Goal** | Master team management, usage analytics, cost governance, and safe admin operations |

---

## Learning Objectives

By the end of this module, participants will be able to:

- List and manage team members programmatically
- Retrieve daily usage data for cost tracking
- Set user spend limits for budget governance
- Analyze model usage for cost optimization
- Track daily active users for leadership reporting
- Build responsible leaderboards without privacy violations
- Analyze conversation intent and complexity
- Safely remove team members with proper patterns

---

## Lesson 9.1: Listing Team Members

### Concept (5 minutes)

> *"The simplest Admin API call and a good entry point. This endpoint confirms your Admin API key works and gives you the basic building block for all other operations."*

**What this teaches you:**
- How to authenticate with Admin API (different from User API)
- The structure of team membership data
- Pagination basics (teams can have hundreds of members)

**Key Endpoint:** `GET /v1/admin/members`

### Hands-On Exercise (8 minutes)

**Step 1:** Set up environment and test authentication:

```bash
# Set your Admin API key (get from cursor.com/organization-settings/api-keys)
export CURSOR_ADMIN_API_KEY="cursor_admin_..."

# Test the connection by listing members
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/members \
  | jq '.'
```

**Step 2:** Pretty-print just the essential information:

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/members \
  | jq '.members[] | {email: .email, role: .role, status: .status, joined: .createdAt}'
```

**Step 3:** Handle pagination for large teams:

```bash
# First page
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?limit=10&offset=0" \
  | jq '.members[].email'

# Second page (if needed)
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?limit=10&offset=10" \
  | jq '.members[].email'
```

**Step 4:** Python script for exporting team roster:

```python
#!/usr/bin/env python3
import requests
import os
import csv
from datetime import datetime

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def export_team_roster(output_file="team_roster.csv"):
    """Export all team members to CSV."""
    all_members = []
    offset = 0
    limit = 50
    
    while True:
        response = requests.get(
            "https://api.cursor.com/v1/admin/members",
            auth=AUTH,
            params={"limit": limit, "offset": offset}
        )
        data = response.json()
        members = data.get("members", [])
        
        if not members:
            break
            
        all_members.extend(members)
        offset += limit
        
        # Check if we've got all pages
        if len(members) < limit:
            break
    
    # Write to CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["email", "role", "status", "createdAt", "lastActive"])
        writer.writeheader()
        for member in all_members:
            writer.writerow({
                "email": member.get("email"),
                "role": member.get("role", "member"),
                "status": member.get("status", "active"),
                "createdAt": member.get("createdAt", ""),
                "lastActive": member.get("lastActiveAt", "")
            })
    
    print(f"✅ Exported {len(all_members)} members to {output_file}")

if __name__ == "__main__":
    export_team_roster()
```

**Success Criteria:**
- [ ] Successfully authenticated with Admin API
- [ ] Retrieved list of team members
- [ ] Handled pagination correctly
- [ ] Exported team roster to CSV

---

## Lesson 9.2: Daily Usage Data

### Concept (8 minutes)

> *"The most-asked-for admin report. Finance wants to know: 'What did we spend yesterday?' Engineering leads want: 'Who's using what?' This endpoint answers both."*

**What you can get:**
- Cost per day (granular for trend analysis)
- Input/output token counts
- Breakdown by user, model, or both

**Key Endpoint:** `GET /v1/admin/analytics/usage/daily`

### Hands-On Exercise (12 minutes)

**Step 1:** Get daily usage for the past week:

```bash
# Calculate dates
END=$(date +%Y-%m-%d)
START=$(date -d "7 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '.daily[] | {date: .date, cost: .cost, tokens: .totalTokens, users: .activeUsers}'
```

**Step 2:** Create a daily cost report with running total:

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

**Step 3:** Generate daily usage report with Python (for charting):

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta
import json

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_daily_usage(days=30):
    """Retrieve daily usage for the last N days."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/usage/daily",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    
    return response.json().get("daily", [])

def generate_cost_trend_report():
    """Create a report showing cost trends."""
    daily_data = get_daily_usage(days=30)
    
    if not daily_data:
        print("No data available")
        return
    
    # Calculate averages and trends
    total_cost = sum(d['cost'] for d in daily_data)
    avg_daily = total_cost / len(daily_data)
    
    # Last 7 days trend
    last_7 = daily_data[-7:] if len(daily_data) >= 7 else daily_data
    last_7_avg = sum(d['cost'] for d in last_7) / len(last_7)
    
    # Week-over-week comparison
    if len(daily_data) >= 14:
        prev_7 = daily_data[-14:-7]
        prev_7_avg = sum(d['cost'] for d in prev_7) / len(prev_7)
        wow_change = ((last_7_avg - prev_7_avg) / prev_7_avg) * 100
    else:
        wow_change = None
    
    print("📊 DAILY USAGE REPORT")
    print("=" * 50)
    print(f"Period: {daily_data[0]['date']} to {daily_data[-1]['date']}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Average daily: ${avg_daily:.2f}")
    print(f"Last 7 days avg: ${last_7_avg:.2f}")
    
    if wow_change is not None:
        arrow = "↑" if wow_change > 0 else "↓"
        print(f"Week-over-week: {arrow} {abs(wow_change):.1f}%")
    
    print("\n📈 Daily breakdown:")
    print(f"{'Date':<12} {'Cost':<10} {'Tokens (M)':<12} {'Users':<8}")
    print("-" * 45)
    
    for day in daily_data[-14:]:  # Last 14 days
        tokens_m = day.get('totalTokens', 0) / 1_000_000
        print(f"{day['date']:<12} ${day['cost']:<9.2f} {tokens_m:<11.1f} {day.get('activeUsers', 0):<8}")

if __name__ == "__main__":
    generate_cost_trend_report()
```

**Success Criteria:**
- [ ] Retrieved daily usage for date range
- [ ] Calculated cost trends
- [ ] Generated a readable cost report

---

## Lesson 9.3: Setting User Spend Limits

### Concept (8 minutes)

> *"Programmatic cost governance. Prevent bill shock by setting monthly caps per user. Great for protecting against runaway agent usage or expensive model overuse."*

**Why this matters:**
- A junior dev might accidentally run 1000 Opus agents
- External contractors should have lower limits than full-time staff
- Teams can have different budgets per department

**Key Endpoint:** `PATCH /v1/admin/policies/users/{userId}/limits`

### Hands-On Exercise (10 minutes)

**Step 1:** First, get a user's ID from their email:

```bash
# Find user ID by email
EMAIL="developer@company.com"

USER_ID=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?email=$EMAIL" \
  | jq -r '.members[0].id')

echo "User ID: $USER_ID"
```

**Step 2:** Set a monthly spending limit for that user:

```bash
curl -X PATCH "https://api.cursor.com/v1/admin/policies/users/$USER_ID/limits" \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "monthlyLimit": 50.00,
    "exceedanceAction": "block"
  }' | jq '.'
```

**Exceedance Action Options:**

| Action | Behavior |
|--------|----------|
| `alert` | Send notification but allow usage |
| `block` | Prevent any further requests for the month |
| `throttle` | Slow down but don't block (API may not support) |

**Step 3:** Set different limits for different roles:

```python
#!/usr/bin/env python3
import requests
import os
import csv

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def set_user_limit(email, monthly_limit, action="block"):
    """Set spending limit for a specific user."""
    # First get user ID
    resp = requests.get(
        "https://api.cursor.com/v1/admin/members",
        auth=AUTH,
        params={"email": email}
    )
    user_id = resp.json().get("members", [{}])[0].get("id")
    
    if not user_id:
        print(f"❌ User not found: {email}")
        return False
    
    # Set the limit
    response = requests.patch(
        f"https://api.cursor.com/v1/admin/policies/users/{user_id}/limits",
        auth=AUTH,
        json={"monthlyLimit": monthly_limit, "exceedanceAction": action}
    )
    
    if response.status_code == 200:
        print(f"✅ Set ${monthly_limit} limit for {email}")
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def bulk_set_limits(csv_file):
    """Set limits from CSV: email, monthly_limit, action"""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            set_user_limit(
                row['email'],
                float(row['monthly_limit']),
                row.get('action', 'block')
            )

# Example CSV: limits.csv
# email,monthly_limit,action
# intern@company.com,20,block
# contractor@company.com,50,alert
# lead@company.com,200,alert

if __name__ == "__main__":
    # Set a single user limit
    set_user_limit("new-hire@company.com", 30.00)
    
    # Or bulk set from CSV
    # bulk_set_limits("limits.csv")
```

**Step 4:** Check a user's current limit and usage:

```bash
# Get user's current limit
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/policies/users/$USER_ID/limits" \
  | jq '{monthlyLimit: .monthlyLimit, currentUsage: .currentMonthUsage, remaining: (.monthlyLimit - .currentMonthUsage)}'
```

**Success Criteria:**
- [ ] Retrieved user ID from email
- [ ] Set monthly spending limit
- [ ] Verified limit was applied
- [ ] Implemented bulk limit setting

---

## Lesson 9.4: Model Usage Analytics

### Concept (8 minutes)

> *"Direct insight into cost and adoption. Which models are actually being used? Is the expensive Opus model worth the cost? Should you train people on cheaper alternatives?"*

**What this answers:**
- What's the cost breakdown by model?
- Which users are using expensive models?
- Are there unused models you could disable?

**Key Endpoint:** `GET /v1/admin/analytics/usage/models`

### Hands-On Exercise (10 minutes)

**Step 1:** Get model usage for the current month:

```bash
START=$(date -d "$(date +%Y-%m-01)" +%Y-%m-%d)
END=$(date +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/models?startDate=$START&endDate=$END" \
  | jq '.models[] | {model: .modelId, cost: .cost, requests: .requestCount, users: .userCount}'
```

**Step 2:** Identify expensive model overuse:

```bash
# Find which users are using Opus (expensive model)
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/users?startDate=$START&endDate=$END" \
  | jq '.users[] | select(.modelBreakdown.opus > 0) | 
         {email: .user.email, opus_cost: .modelBreakdown.opus.cost, total_cost: .cost}'
```

**Step 3:** Generate model cost optimization report:

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_model_usage(days=30):
    """Get model usage for the last N days."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/usage/models",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    return response.json().get("models", [])

def generate_optimization_report():
    """Identify cost-saving opportunities."""
    models = get_model_usage(days=30)
    
    # Define model pricing tiers (from Module 8 chat)
    pricing = {
        "gpt-5-mini": 0.25,
        "claude-4.5-haiku": 1.00,
        "gemini-3.1-pro": 2.00,
        "claude-4.6-sonnet": 3.00,
        "claude-4.7-opus": 5.00,
        "gpt-5.3-codex": 1.75,
        "gpt-5.5": 5.00
    }
    
    print("🤖 MODEL USAGE & OPTIMIZATION REPORT")
    print("=" * 60)
    
    for model in sorted(models, key=lambda x: x.get('cost', 0), reverse=True):
        model_id = model.get('modelId', 'unknown')
        cost = model.get('cost', 0)
        requests_count = model.get('requestCount', 0)
        user_count = model.get('userCount', 0)
        
        # Calculate potential savings if downgraded
        cheaper_alternative = "claude-4.6-sonnet"
        cheaper_price = pricing.get(cheaper_alternative, 3.00)
        current_price = pricing.get(model_id, 3.00)
        
        if current_price > cheaper_price:
            # Estimate token count from cost
            estimated_tokens = (cost / current_price) * 1_000_000
            potential_savings = (current_price - cheaper_price) * (estimated_tokens / 1_000_000)
            
            print(f"\n📊 {model_id}")
            print(f"   Cost: ${cost:.2f}")
            print(f"   Requests: {requests_count}")
            print(f"   Users: {user_count}")
            print(f"   💡 Could save ~${potential_savings:.2f} by using {cheaper_alternative}")
    
    # Recommendations
    print("\n" + "=" * 60)
    print("🎯 RECOMMENDATIONS")
    
    # Find if anyone is using both cheap and expensive models
    users_response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/usage/users",
        auth=AUTH
    )
    users = users_response.json().get("users", [])
    
    mixed_users = []
    for user in users:
        models_used = user.get('modelBreakdown', {}).keys()
        if 'claude-4.7-opus' in models_used and 'gpt-5-mini' in models_used:
            mixed_users.append(user['user']['email'])
    
    if mixed_users:
        print(f"\n   Users mixing Opus and Mini: {len(mixed_users)}")
        print(f"   Consider training these users on when to use each model")
    
    # Calculate cost if everyone switched to Sonnet
    total_cost = sum(m.get('cost', 0) for m in models)
    print(f"\n   Current monthly cost: ${total_cost:.2f}")
    print(f"   Potential with Sonnet-only: ~${total_cost * 0.6:.2f}")

if __name__ == "__main__":
    generate_optimization_report()
```

**Success Criteria:**
- [ ] Retrieved model usage breakdown
- [ ] Identified expensive model users
- [ ] Generated cost optimization recommendations

---

## Lesson 9.5: Daily Active Users (DAU)

### Concept (5 minutes)

> *"The headline adoption metric for leadership. DAU tells you if your team is actually using Cursor or if licenses are being wasted."*

**Why this metric matters:**
- Track adoption after rollout
- Identify unused licenses
- Measure impact of training

**Key Endpoint:** `GET /v1/admin/analytics/usage/daily` (with aggregation)

### Hands-On Exercise (10 minutes)

**Step 1:** Calculate DAU from daily usage data:

```bash
START=$(date -d "30 days ago" +%Y-%m-%d)
END=$(date +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '{dates: [.daily[] | {date: .date, activeUsers: .activeUsers}], 
         avg_weekly: ([.daily[-7:] | .[].activeUsers] | add / length),
         peak: ([.daily[] | .activeUsers] | max)}'
```

**Step 2:** Create leadership-ready DAU report:

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta
import json

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_daily_active_users(days=30):
    """Calculate DAU trend."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/usage/daily",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    
    daily_data = response.json().get("daily", [])
    return daily_data

def generate_dau_report():
    """Create DAU report for leadership."""
    data = get_daily_active_users(days=30)
    
    if not data:
        print("No data available")
        return
    
    # Get total team size
    members_resp = requests.get(
        "https://api.cursor.com/v1/admin/members",
        auth=AUTH
    )
    total_members = len(members_resp.json().get("members", []))
    
    # Calculate metrics
    daily_users = [d['activeUsers'] for d in data]
    avg_daily = sum(daily_users) / len(daily_users)
    max_daily = max(daily_users)
    min_daily = min(daily_users)
    
    # Weekly trends
    weeks = [data[i:i+7] for i in range(0, len(data), 7)]
    weekly_avgs = [sum(w[d]['activeUsers'] for d in range(len(w))) / len(w) for w in weeks if len(w) == 7]
    
    print("📊 DAILY ACTIVE USERS (DAU) REPORT")
    print("=" * 50)
    print(f"Reporting period: {data[0]['date']} to {data[-1]['date']}")
    print(f"Total team members: {total_members}")
    print(f"\n📈 Key Metrics:")
    print(f"   Average DAU: {avg_daily:.0f}")
    print(f"   Peak DAU: {max_daily}")
    print(f"   Lowest DAU: {min_daily}")
    print(f"   Adoption rate: {(avg_daily / total_members * 100):.1f}%")
    
    if len(weekly_avgs) >= 2:
        trend = weekly_avgs[-1] - weekly_avgs[-2]
        arrow = "↑" if trend > 0 else "↓"
        print(f"\n   Weekly trend: {arrow} {abs(trend):.1f} users")
    
    # Weekly breakdown for leadership
    print("\n📅 Weekly DAU Averages:")
    for i, week_avg in enumerate(weekly_avgs):
        week_start = data[i*7]['date']
        print(f"   Week of {week_start}: {week_avg:.0f} users")
    
    # Retention warning
    low_days = [d for d in data if d['activeUsers'] < avg_daily * 0.5]
    if low_days:
        print(f"\n⚠️ Low activity days: {len(low_days)} days below 50% average")
        print("   Consider sending reminders or training on these days")

if __name__ == "__main__":
    generate_dau_report()
```

**Success Criteria:**
- [ ] Calculated DAU from daily data
- [ ] Generated adoption rate
- [ ] Created leadership-ready report

---

## Lesson 9.6: Leaderboards

### Concept (8 minutes)

> *"Usage rankings and how to present them responsibly. Leaderboards can drive engagement OR create unhealthy competition. Here's the balanced approach."*

**Responsible Leaderboard Principles:**
1. **Anonymize** when possible (use roles, not names)
2. **Focus on positive metrics** (savings, not spending)
3. **Opt-in only** for public rankings
4. **Include context** (team size, role differences)

### Hands-On Exercise (10 minutes)

**Step 1:** Create a responsible usage leaderboard:

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_user_usage(days=30):
    """Get per-user usage data."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/usage/users",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    return response.json().get("users", [])

def generate_anonymous_leaderboard():
    """Create anonymized leaderboard for team sharing."""
    users = get_user_usage(days=30)
    
    # Sort by cost (descending)
    sorted_users = sorted(users, key=lambda x: x.get('cost', 0), reverse=True)
    
    print("🏆 CURSOR USAGE LEADERBOARD (Last 30 Days)")
    print("=" * 60)
    print("Note: Names are anonymized. This measures engagement, not performance.")
    print()
    
    # Anonymize by role
    print(f"{'Rank':<6} {'Role':<15} {'Cost':<12} {'Requests':<12} {'Efficiency':<12}")
    print("-" * 60)
    
    for i, user in enumerate(sorted_users[:10], 1):
        # Get user's role from member list
        email = user.get('user', {}).get('email', 'unknown')
        resp = requests.get(
            "https://api.cursor.com/v1/admin/members",
            auth=AUTH,
            params={"email": email}
        )
        role = resp.json().get('members', [{}])[0].get('role', 'member')
        
        # Calculate efficiency (tokens per dollar - higher is better)
        cost = user.get('cost', 0)
        tokens = user.get('totalTokens', 0)
        efficiency = tokens / cost if cost > 0 else 0
        
        medal = ""
        if i == 1:
            medal = "🥇 "
        elif i == 2:
            medal = "🥈 "
        elif i == 3:
            medal = "🥉 "
        
        print(f"{medal}{i:<4} {role:<15} ${cost:<11.2f} {user.get('requestCount', 0):<12} {efficiency:,.0f}")

def generate_savings_leaderboard():
    """Focus on efficiency, not spending."""
    users = get_user_usage(days=30)
    
    # Calculate potential savings from model choice
    print("\n💰 EFFICIENCY LEADERBOARD (Who saves the most?)")
    print("=" * 60)
    print("Ranking by efficient model selection, not raw usage.\n")
    
    savings_list = []
    for user in users:
        email = user.get('user', {}).get('email', 'unknown')
        model_breakdown = user.get('modelBreakdown', {})
        
        # Calculate cost if they used Sonnet instead of Opus
        opus_cost = model_breakdown.get('claude-4.7-opus', {}).get('cost', 0)
        savings = opus_cost * 0.4  # Rough estimate (Opus is ~40% more than Sonnet)
        
        if savings > 0:
            savings_list.append({'email': email, 'savings': savings})
    
    sorted_savings = sorted(savings_list, key=lambda x: x['savings'], reverse=True)
    
    print(f"{'Rank':<6} {'User (anonymized)':<20} {'Savings':<12}")
    print("-" * 40)
    
    for i, saver in enumerate(sorted_savings[:5], 1):
        # Anonymize email
        username = saver['email'].split('@')[0]
        anon_name = username[0] + "*" * (len(username) - 1) if len(username) > 1 else "User"
        print(f"{i:<6} {anon_name:<20} ${saver['savings']:.2f}")

if __name__ == "__main__":
    generate_anonymous_leaderboard()
    generate_savings_leaderboard()
```

**Step 2:** Create opt-in public leaderboard:

```python
# optin_leaderboard.py - Only show users who opted in
# Requires storing opt-in status in your own database

def get_optin_users(optin_list_file="optin_users.txt"):
    """Read list of users who consented to appear."""
    try:
        with open(optin_list_file, 'r') as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def generate_optin_leaderboard():
    """Leaderboard showing only opted-in users."""
    optin_users = get_optin_users()
    users = get_user_usage(days=30)
    
    # Filter to opted-in users only
    eligible = [u for u in users 
                if u.get('user', {}).get('email') in optin_users]
    
    if not eligible:
        print("No users have opted in to the leaderboard yet.")
        print("Add emails to optin_users.txt to enable.")
        return
    
    sorted_eligible = sorted(eligible, key=lambda x: x.get('cost', 0), reverse=True)
    
    print("🏆 OPT-IN LEADERBOARD")
    print("=" * 40)
    print("These users agreed to appear publicly.\n")
    
    for i, user in enumerate(sorted_eligible[:10], 1):
        email = user.get('user', {}).get('email', 'unknown')
        cost = user.get('cost', 0)
        print(f"{i}. {email} - ${cost:.2f}")
```

**Success Criteria:**
- [ ] Created anonymized leaderboard
- [ ] Built efficiency-focused leaderboard (positive metric)
- [ ] Implemented opt-in pattern for public sharing

---

## Lesson 9.7: Conversation Insights

### Concept (10 minutes)

> *"Intent, complexity, and category analysis. This is a demonstration of advanced analytics – understanding WHAT users are doing, not just how much."*

**What conversation insights reveal:**
- Are users asking simple questions or complex refactors?
- What categories of tasks are most common?
- Where are users getting stuck?

**Note:** This uses the `conversations` endpoint (may require Enterprise plan)

### Demonstration (10 minutes)

**Step 1:** Retrieve conversation metadata:

```bash
# Get conversations for analysis
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/conversations?startDate=$START&endDate=$END&limit=100" \
  | jq '.conversations[] | {user: .user.email, intent: .intent, complexity: .complexity, duration: .duration}'
```

**Step 2:** Python script for intent analysis:

```python
#!/usr/bin/env python3
"""
Conversation Insights - Demonstrates advanced analytics
Note: This requires Enterprise plan or special access
"""

import requests
import os
from collections import Counter
from datetime import datetime, timedelta

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_conversations(days=30):
    """Retrieve conversation metadata."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    # This is a demonstration - actual endpoint may differ
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/conversations",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
            "limit": 500
        }
    )
    return response.json().get("conversations", [])

def analyze_intent_distribution():
    """Show what users are trying to accomplish."""
    convos = get_conversations()
    
    intents = [c.get('intent', 'unknown') for c in convos]
    intent_counts = Counter(intents)
    
    print("🎯 CONVERSATION INTENT ANALYSIS")
    print("=" * 50)
    print("What are users trying to do?\n")
    
    for intent, count in intent_counts.most_common():
        percentage = (count / len(convos)) * 100
        bar = "█" * int(percentage / 2)
        print(f"{intent:<20} {percentage:5.1f}% {bar}")

def analyze_complexity_distribution():
    """Show task complexity distribution."""
    convos = get_conversations()
    
    complexity_levels = ['simple', 'moderate', 'complex', 'architectural']
    complexity_counts = Counter(c.get('complexity', 'simple') for c in convos)
    
    print("\n📊 COMPLEXITY DISTRIBUTION")
    print("=" * 50)
    print("How hard are the tasks?\n")
    
    for level in complexity_levels:
        count = complexity_counts.get(level, 0)
        percentage = (count / len(convos)) * 100 if convos else 0
        bar = "█" * int(percentage / 2)
        print(f"{level:<12} {percentage:5.1f}% {bar}")

def identify_stuck_patterns():
    """Find where users struggle."""
    convos = get_conversations()
    
    # Conversations with high duration and low success
    stuck = [c for c in convos 
             if c.get('duration', 0) > 300  # >5 minutes
             and c.get('success', True) == False]
    
    if stuck:
        print("\n⚠️ USERS GETTING STUCK")
        print("=" * 50)
        print(f"Found {len(stuck)} conversations where users struggled.")
        
        # Common intents when stuck
        stuck_intents = Counter([c.get('intent') for c in stuck])
        print("\nCommon challenging intent types:")
        for intent, count in stuck_intents.most_common(3):
            print(f"   - {intent}: {count} occurrences")
        
        print("\n💡 SUGGESTIONS:")
        print("   - Create documentation for 'debugging' tasks")
        print("   - Consider training on 'refactoring' workflows")
    else:
        print("\n✅ No stuck patterns detected")

if __name__ == "__main__":
    analyze_intent_distribution()
    analyze_complexity_distribution()
    identify_stuck_patterns()
```

**Step 3:** Category analysis (what domains users work in):

```python
def analyze_categories():
    """Show which code domains are most common."""
    convos = get_conversations()
    
    categories = []
    for c in convos:
        # Extract categories from conversation metadata
        cats = c.get('categories', [])
        categories.extend(cats)
    
    category_counts = Counter(categories)
    
    print("\n📂 CATEGORY ANALYSIS")
    print("=" * 50)
    print("What domains are users working in?\n")
    
    for category, count in category_counts.most_common(10):
        percentage = (count / len(categories)) * 100 if categories else 0
        print(f"{category:<20} {percentage:5.1f}%")

# Run category analysis
analyze_categories()
```

**Success Criteria (Demonstration):**
- [ ] Retrieved conversation metadata
- [ ] Analyzed intent distribution
- [ ] Identified stuck patterns
- [ ] Generated category analysis

---

## Lesson 9.8: Destructive Admin Operations

### Concept (10 minutes)

> *"Safe patterns for removing a team member. Destructive operations require care – here's the proper playbook."*

**The Safety Playbook:**
1. **Audit first** – See what the user has done
2. **Soft delete** – Deactivate before removing
3. **Transfer ownership** – Move their agents/runs
4. **Log everything** – For compliance
5. **Confirm before delete** – Double-check the ID

**Key Endpoints:**
- `GET /v1/admin/members/{userId}/resources` – List user's resources
- `PATCH /v1/admin/members/{userId}/status` – Deactivate
- `DELETE /v1/admin/members/{userId}` – Remove (requires confirmation)

### Demonstration (10 minutes)

**Step 1:** Safe removal workflow demonstration:

```python
#!/usr/bin/env python3
"""
Safe Removal Pattern - Demonstration script
This shows the proper workflow for removing a team member
"""

import requests
import os
from datetime import datetime

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

class SafeRemoval:
    def __init__(self, email):
        self.email = email
        self.user_id = None
        self.resources = None
    
    def step1_find_user(self):
        """Locate the user by email."""
        print(f"🔍 Step 1: Finding user {self.email}")
        resp = requests.get(
            "https://api.cursor.com/v1/admin/members",
            auth=AUTH,
            params={"email": self.email}
        )
        members = resp.json().get("members", [])
        
        if not members:
            print(f"❌ User {self.email} not found")
            return False
        
        self.user_id = members[0]['id']
        print(f"✅ Found user: {self.user_id}")
        return True
    
    def step2_audit_resources(self):
        """List all resources owned by the user."""
        print(f"\n📋 Step 2: Auditing user's resources")
        resp = requests.get(
            f"https://api.cursor.com/v1/admin/members/{self.user_id}/resources",
            auth=AUTH
        )
        self.resources = resp.json()
        
        agents = self.resources.get('agents', [])
        runs = self.resources.get('runs', [])
        
        print(f"   Agents owned: {len(agents)}")
        print(f"   Runs executed: {len(runs)}")
        
        if agents:
            print(f"   Recent agents:")
            for agent in agents[:3]:
                print(f"     - {agent['id']}: {agent.get('status', 'unknown')}")
        
        return True
    
    def step3_deactivate(self):
        """Soft delete - deactivate first."""
        print(f"\n⚠️ Step 3: Deactivating user (soft delete)")
        
        # Confirm action
        confirm = input(f"Deactivate {self.email}? [y/N]: ")
        if confirm.lower() != 'y':
            print("Cancelled")
            return False
        
        resp = requests.patch(
            f"https://api.cursor.com/v1/admin/members/{self.user_id}/status",
            auth=AUTH,
            json={"status": "inactive"}
        )
        
        if resp.status_code == 200:
            print(f"✅ User deactivated")
            print(f"   Note: User cannot create new agents or runs")
            return True
        else:
            print(f"❌ Failed: {resp.text}")
            return False
    
    def step4_transfer_resources(self, new_owner_email):
        """Transfer ownership of critical resources."""
        print(f"\n🔄 Step 4: Transferring resources")
        
        # Find new owner ID
        resp = requests.get(
            "https://api.cursor.com/v1/admin/members",
            auth=AUTH,
            params={"email": new_owner_email}
        )
        members = resp.json().get("members", [])
        
        if not members:
            print(f"❌ New owner {new_owner_email} not found")
            return False
        
        new_owner_id = members[0]['id']
        
        # Transfer each agent
        agents = self.resources.get('agents', [])
        for agent in agents:
            transfer_resp = requests.post(
                f"https://api.cursor.com/v1/agents/{agent['id']}/transfer",
                auth=AUTH,
                json={"newOwnerId": new_owner_id}
            )
            if transfer_resp.status_code == 200:
                print(f"   Transferred agent: {agent['id']}")
        
        return True
    
    def step5_hard_delete(self):
        """Permanent removal (use sparingly)."""
        print(f"\n🗑️ Step 5: Permanent removal")
        
        print("⚠️ WARNING: This action is permanent and cannot be undone")
        confirm = input(f"Permanently remove {self.email}? Type 'DELETE' to confirm: ")
        
        if confirm != 'DELETE':
            print("Cancelled - user remains deactivated but not removed")
            return False
        
        resp = requests.delete(
            f"https://api.cursor.com/v1/admin/members/{self.user_id}",
            auth=AUTH
        )
        
        if resp.status_code == 200:
            print(f"✅ User permanently removed")
            self._log_audit_event()
            return True
        else:
            print(f"❌ Failed: {resp.text}")
            return False
    
    def _log_audit_event(self):
        """Log removal for compliance."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": "user_removed",
            "user_email": self.email,
            "user_id": self.user_id,
            "performed_by": "admin_script"
        }
        
        # Append to audit log file
        with open("removal_audit.log", "a") as f:
            f.write(f"{log_entry}\n")
        print(f"📝 Logged to removal_audit.log")

# Demonstration of safe removal
def demonstrate_safe_removal():
    """Run through the complete safe removal workflow."""
    print("=" * 60)
    print("🔐 SAFE USER REMOVAL DEMONSTRATION")
    print("=" * 60)
    print("This demonstrates the proper pattern for removing a user.")
    print("In production, you would implement each step with proper error handling.\n")
    
    # Example: removing a contractor who finished their engagement
    remover = SafeRemoval("contractor@company.com")
    
    remover.step1_find_user()
    remover.step2_audit_resources()
    remover.step3_deactivate()
    remover.step4_transfer_resources("team-lead@company.com")
    
    # Hard delete is optional - many orgs skip this step
    print("\n💡 Note: Hard delete is often skipped.")
    print("   Deactivated users no longer incur costs.")
    print("   Hard delete is only for GDPR-style compliance.")

if __name__ == "__main__":
    demonstrate_safe_removal()
```

**Step 2:** Bulk removal with safety checks:

```python
def bulk_deactivate_inactive_users(days_inactive=90):
    """Deactivate users who haven't been active."""
    users = get_user_usage(days=days_inactive)
    
    inactive = []
    for user in users:
        last_active = user.get('lastActiveAt')
        if last_active:
            # Check if never active or inactive too long
            pass
    
    print(f"Found {len(inactive)} potentially inactive users")
    
    for user in inactive:
        print(f"Would deactivate: {user['email']} (last active: {user.get('lastActiveAt', 'never')})")
    
    # Require explicit confirmation
    confirm = input("\nDeactivate these users? Type number of users to confirm: ")
    if confirm == str(len(inactive)):
        # Proceed with deactivation
        pass
```

**Success Criteria (Demonstration):**
- [ ] Understood the 5-step safe removal pattern
- [ ] Saw audit-first principle in action
- [ ] Learned soft delete vs hard delete
- [ ] Understood resource transfer requirements

---

## Module Summary

| Lesson | Topic | Time | Type |
|--------|-------|------|------|
| 9.1 | Listing Team Members | 8 min | Exercise |
| 9.2 | Daily Usage Data | 12 min | Exercise |
| 9.3 | Setting User Spend Limits | 10 min | Exercise |
| 9.4 | Model Usage Analytics | 10 min | Exercise |
| 9.5 | Daily Active Users | 10 min | Exercise |
| 9.6 | Leaderboards | 10 min | Exercise |
| 9.7 | Conversation Insights | 10 min | Demo |
| 9.8 | Destructive Operations | 10 min | Demo |

---

## Quick Reference Card

| What | Endpoint | Method |
|------|----------|--------|
| List members | `/v1/admin/members` | GET |
| Daily usage | `/v1/admin/analytics/usage/daily` | GET |
| Model usage | `/v1/admin/analytics/usage/models` | GET |
| Set spend limit | `/v1/admin/policies/users/{id}/limits` | PATCH |
| User resources | `/v1/admin/members/{id}/resources` | GET |
| Deactivate user | `/v1/admin/members/{id}/status` | PATCH |
| Remove user | `/v1/admin/members/{id}` | DELETE |

**Safety Checklist for Destructive Ops:**
- [ ] Audit user's resources first
- [ ] Soft delete (deactivate) before hard delete
- [ ] Transfer ownership of important resources
- [ ] Log all removal actions
- [ ] Require confirmation for deletion

---

*End of Module 9*