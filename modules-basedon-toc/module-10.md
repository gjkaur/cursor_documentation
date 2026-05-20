# Module 10: AI Code Tracking and Reporting

## Cursor Training Program — Day 2 (Final Module)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~20 minutes (plus take-home project) |
| **Format** | Hands-on exercise + take-home project |
| **Prerequisites** | Admin API key, Git repository access, Module 9 completion |
| **Module Goal** | Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Attribute AI vs. human contributions per commit
- Stream metrics to BI tools via CSV export
- Access granular AI change events for compliance
- Build a complete reporting dashboard combining all data sources

---

## Lesson 10.1: AI Commit Metrics

### Concept (4 minutes)

> *"Per-commit attribution of AI vs. human contributions. This is the 'ROI of AI' metric – showing exactly how much code was AI-generated versus human-written."*

**What this measures:**
- Lines added by AI vs. human
- Files modified by agent vs. manual
- Commit-level attribution
- Model contributions breakdown

**Key Endpoint:** `GET /v1/admin/analytics/commits`

### Hands-On Exercise (6 minutes)

**Step 1:** Get AI contribution metrics for a repository:

```bash
# Set date range for last 30 days
END=$(date +%Y-%m-%d)
START=$(date -d "30 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/commits?startDate=$START&endDate=$END&repo=https://github.com/YOUR_ORG/YOUR_REPO" \
  | jq '.'
```

**Step 2:** Calculate AI contribution percentage:

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/commits?startDate=$START&endDate=$END" \
  | jq '{
      total_commits: .summary.totalCommits,
      ai_commits: .summary.aiAuthoredCommits,
      ai_percentage: (.summary.aiAuthoredCommits / .summary.totalCommits * 100),
      lines_saved: .summary.aiGeneratedLines
    }'
```

**Step 3:** Python script for per-developer attribution:

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta
from collections import defaultdict

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_commit_metrics(days=30, repo_url=None):
    """Retrieve AI commit metrics."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    params = {
        "startDate": start.strftime("%Y-%m-%d"),
        "endDate": end.strftime("%Y-%m-%d")
    }
    if repo_url:
        params["repo"] = repo_url
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/commits",
        auth=AUTH,
        params=params
    )
    return response.json()

def calculate_ai_roi():
    """Calculate ROI of AI coding assistance."""
    metrics = get_commit_metrics(days=30)
    
    summary = metrics.get('summary', {})
    ai_lines = summary.get('aiGeneratedLines', 0)
    human_lines = summary.get('humanLines', 0)
    total_lines = ai_lines + human_lines
    ai_percentage = (ai_lines / total_lines * 100) if total_lines > 0 else 0
    
    # Estimated time saved (assuming 10 lines per minute for human)
    minutes_saved = ai_lines / 10
    hours_saved = minutes_saved / 60
    cost_saved = hours_saved * 100  # $100/hour developer cost
    
    # Cost of AI usage (from Module 9)
    usage = get_usage_cost(days=30)
    
    print("🤖 AI CODE CONTRIBUTION REPORT")
    print("=" * 50)
    print(f"Period: Last 30 days")
    print(f"\n📝 Code Contribution Breakdown:")
    print(f"   AI-generated lines: {ai_lines:,} ({ai_percentage:.1f}%)")
    print(f"   Human-written lines: {human_lines:,} ({100-ai_percentage:.1f}%)")
    print(f"   Total lines: {total_lines:,}")
    
    print(f"\n💰 ROI Analysis:")
    print(f"   Estimated time saved: {hours_saved:.1f} hours")
    print(f"   Estimated cost saved: ${cost_saved:.0f}")
    print(f"   AI usage cost: ${usage:.2f}")
    print(f"   Net ROI: ${cost_saved - usage:.0f}")

def get_usage_cost(days=30):
    """Helper to get usage cost from analytics."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/usage",
        auth=AUTH,
        params={"startDate": start.strftime("%Y-%m-%d"), "endDate": end.strftime("%Y-%m-%d")}
    )
    return response.json().get('summary', {}).get('totalCost', 0)

def contributor_breakdown():
    """Show AI contribution per developer."""
    metrics = get_commit_metrics(days=30)
    contributors = metrics.get('contributors', [])
    
    print("\n👥 CONTRIBUTOR BREAKDOWN")
    print("=" * 50)
    print(f"{'Developer':<30} {'AI %':<10} {'AI Lines':<12} {'Commits':<8}")
    print("-" * 60)
    
    for dev in sorted(contributors, key=lambda x: x.get('aiPercentage', 0), reverse=True):
        print(f"{dev.get('email', 'unknown')[:28]:<30} "
              f"{dev.get('aiPercentage', 0):>5.1f}%     "
              f"{dev.get('aiLines', 0):>8,}   "
              f"{dev.get('commitCount', 0):>6}")

if __name__ == "__main__":
    calculate_ai_roi()
    contributor_breakdown()
```

**Success Criteria:**
- [ ] Retrieved AI commit metrics
- [ ] Calculated AI contribution percentage
- [ ] Generated ROI analysis
- [ ] Created per-developer breakdown

---

## Lesson 10.2: Bulk Export via CSV Streaming

### Concept (3 minutes)

> *"Wiring metrics into BI tools (Tableau, PowerBI, Looker, Metabase). Streaming CSV exports let you pull large datasets efficiently without timeouts."*

**Why CSV streaming matters:**
- Handle millions of rows without memory issues
- Direct import into data warehouses
- Scheduled exports for dashboards

**Key Endpoint:** `GET /v1/admin/analytics/export/csv` (streaming)

### Hands-On Exercise (5 minutes)

**Step 1:** Stream CSV export directly to file:

```bash
curl -N -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/export/csv?startDate=$START&endDate=$END&type=commits" \
  -o cursor_commits_export.csv

# Check output
head -10 cursor_commits_export.csv
```

**Step 2:** Stream to BI tool (example with Python + pandas):

```python
#!/usr/bin/env python3
"""
Stream CSV export directly to pandas DataFrame
Perfect for loading into BI dashboards
"""

import requests
import pandas as pd
import io
import os

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def stream_commits_to_dataframe(start_date, end_date):
    """Stream commit data directly to pandas DataFrame."""
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/export/csv",
        auth=AUTH,
        params={
            "startDate": start_date,
            "endDate": end_date,
            "type": "commits"
        },
        stream=True
    )
    
    # Stream content into DataFrame
    content = b''
    for chunk in response.iter_content(chunk_size=8192):
        content += chunk
    
    df = pd.read_csv(io.BytesIO(content))
    return df

def stream_events_to_dataframe(start_date, end_date):
    """Stream granular event data."""
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/export/csv",
        auth=AUTH,
        params={
            "startDate": start_date,
            "endDate": end_date,
            "type": "events"
        },
        stream=True
    )
    
    content = b''
    for chunk in response.iter_content(chunk_size=8192):
        content += chunk
    
    df = pd.read_csv(io.BytesIO(content))
    return df

def export_to_bi_connector():
    """Generate CSV files ready for BI tools."""
    from datetime import datetime, timedelta
    
    end = datetime.now()
    start = end - timedelta(days=30)
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")
    
    # Export commits
    print("📊 Exporting commit data...")
    df_commits = stream_commits_to_dataframe(start_str, end_str)
    df_commits.to_csv("bi_commits.csv", index=False)
    print(f"   Exported {len(df_commits)} commits")
    
    # Export events
    print("📋 Exporting event data...")
    df_events = stream_events_to_dataframe(start_str, end_str)
    df_events.to_csv("bi_events.csv", index=False)
    print(f"   Exported {len(df_events)} events")
    
    # Summary for BI dashboard
    summary = {
        "total_commits": len(df_commits),
        "total_events": len(df_events),
        "date_range": f"{start_str} to {end_str}"
    }
    
    print("\n✅ Ready for BI import:")
    print("   - bi_commits.csv")
    print("   - bi_events.csv")

if __name__ == "__main__":
    export_to_bi_connector()
```

**Step 3:** Scheduled export for Metabase/Tableau:

```bash
#!/bin/bash
# schedule_export.sh - Run daily via cron

#!/bin/bash
# Run daily at 2 AM: 0 2 * * * /path/to/schedule_export.sh

export CURSOR_ADMIN_API_KEY="your_key"
DATE=$(date +%Y-%m-%d)

# Export last 7 days of commit data
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/export/csv?startDate=$(date -d '7 days ago' +%Y-%m-%d)&endDate=$DATE&type=commits" \
  -o "/var/lib/cursor_exports/commits_$DATE.csv"

# Export to S3 or BI tool's data warehouse
# aws s3 cp /var/lib/cursor_exports/commits_$DATE.csv s3://your-bucket/cursor-exports/

echo "Export complete: commits_$DATE.csv"
```

**Success Criteria:**
- [ ] Streamed CSV export to file
- [ ] Loaded export into pandas DataFrame
- [ ] Created schedule-ready export script

---

## Lesson 10.3: Granular AI Change Events

### Concept (3 minutes)

> *"Per-event detail for compliance reporting. Every AI-generated change is tracked – file, line range, model used, timestamp. Essential for SOC2, ISO, and internal audits."*

**What each event contains:**
- File path and line range
- Model that generated the change
- User who accepted/rejected
- Timestamp
- Original code (before) and new code (after)

**Key Endpoint:** `GET /v1/admin/analytics/events`

### Hands-On Exercise (5 minutes)

**Step 1:** Get granular change events:

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/events?startDate=$START&endDate=$END&limit=100" \
  | jq '.events[] | {user: .user.email, file: .filePath, model: .modelId, lines: .lineCount, accepted: .accepted}'
```

**Step 2:** Generate compliance report (acceptance rate by model):

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/events?startDate=$START&endDate=$END" \
  | jq '[.events[] | {model: .modelId, accepted: .accepted}] | 
         group_by(.model) | 
         map({model: .[0].model, 
              total: length, 
              accepted: map(select(.accepted == true)) | length,
              acceptance_rate: ((map(select(.accepted == true)) | length) / length * 100)}) |
         sort_by(-.acceptance_rate)'
```

**Step 3:** Python script for compliance auditing:

```python
#!/usr/bin/env python3
import requests
import os
import csv
from datetime import datetime, timedelta
from collections import defaultdict

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def get_change_events(days=30, limit=1000):
    """Retrieve granular change events."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    all_events = []
    offset = 0
    
    while True:
        response = requests.get(
            "https://api.cursor.com/v1/admin/analytics/events",
            auth=AUTH,
            params={
                "startDate": start.strftime("%Y-%m-%d"),
                "endDate": end.strftime("%Y-%m-%d"),
                "limit": limit,
                "offset": offset
            }
        )
        events = response.json().get('events', [])
        
        if not events:
            break
            
        all_events.extend(events)
        offset += limit
        
        if len(events) < limit:
            break
    
    return all_events

def generate_compliance_report():
    """Create audit-ready compliance report."""
    events = get_change_events(days=90)  # Last 90 days for compliance
    
    print("🔍 AI CODE CHANGE COMPLIANCE REPORT")
    print("=" * 60)
    print(f"Reporting period: Last 90 days")
    print(f"Total AI-generated changes: {len(events)}")
    
    # Acceptance rate by model
    model_stats = defaultdict(lambda: {'total': 0, 'accepted': 0})
    
    for event in events:
        model = event.get('modelId', 'unknown')
        accepted = event.get('accepted', False)
        
        model_stats[model]['total'] += 1
        if accepted:
            model_stats[model]['accepted'] += 1
    
    print("\n📊 Acceptance Rate by Model:")
    print(f"{'Model':<25} {'Total':<10} {'Accepted':<10} {'Rate':<10}")
    print("-" * 55)
    
    for model, stats in sorted(model_stats.items(), key=lambda x: -x[1]['accepted']/x[1]['total']):
        rate = (stats['accepted'] / stats['total']) * 100
        print(f"{model[:24]:<25} {stats['total']:<10} {stats['accepted']:<10} {rate:.1f}%")
    
    # Files with most AI changes (for review prioritization)
    file_stats = defaultdict(int)
    for event in events:
        file_path = event.get('filePath', 'unknown')
        file_stats[file_path] += 1
    
    print("\n📁 Files with Most AI Changes (needs human review):")
    top_files = sorted(file_stats.items(), key=lambda x: -x[1])[:10]
    for file_path, count in top_files:
        print(f"   {file_path}: {count} changes")
    
    # Export to CSV for auditor
    with open('compliance_export.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'timestamp', 'user_email', 'model_id', 'file_path', 
            'line_start', 'line_end', 'accepted', 'original_snippet'
        ])
        writer.writeheader()
        
        for event in events[:10000]:  # Limit for practicality
            writer.writerow({
                'timestamp': event.get('timestamp'),
                'user_email': event.get('user', {}).get('email'),
                'model_id': event.get('modelId'),
                'file_path': event.get('filePath'),
                'line_start': event.get('lineStart'),
                'line_end': event.get('lineEnd'),
                'accepted': event.get('accepted'),
                'original_snippet': event.get('originalCode', '')[:200]  # Truncate for CSV
            })
    
    print(f"\n✅ Compliance export saved to compliance_export.csv")
    print(f"   Total events in export: {min(len(events), 10000)}")

def find_unaccepted_changes():
    """Find changes that were rejected (for quality analysis)."""
    events = get_change_events(days=30)
    
    rejected = [e for e in events if not e.get('accepted', False)]
    
    print(f"\n❌ REJECTED AI CHANGES ({len(rejected)} total)")
    print("=" * 50)
    
    # Group by reason (if available)
    reasons = defaultdict(int)
    for event in rejected:
        reason = event.get('rejectionReason', 'unknown')
        reasons[reason] += 1
    
    print("Rejection reasons:")
    for reason, count in reasons.items():
        print(f"   {reason}: {count}")
    
    # Show examples
    print("\nSample rejected changes:")
    for event in rejected[:5]:
        print(f"   File: {event.get('filePath')}")
        print(f"   Model: {event.get('modelId')}")
        print(f"   Reason: {event.get('rejectionReason', 'not specified')}")
        print()

if __name__ == "__main__":
    generate_compliance_report()
    find_unaccepted_changes()
```

**Success Criteria:**
- [ ] Retrieved granular change events
- [ ] Calculated acceptance rates by model
- [ ] Generated compliance export for auditors
- [ ] Analyzed rejected changes

---

## Lesson 10.4: Reporting Dashboard Architecture (Take-Home Project)

### Concept (5 minutes)

> *"Combining Admin, Analytics, and AI Code Tracking data into a single dashboard. This is your take-home project – build a complete operational dashboard for your team."*

**Dashboard Components:**

| Component | Data Source | Purpose |
|-----------|-------------|---------|
| Usage Overview | Usage API | Cost, tokens, active users |
| AI Contribution | Commits API | ROI, adoption metrics |
| Model Performance | Events API | Acceptance rates, efficiency |
| Team Activity | Members API | Onboarding, licensing |
| Compliance | Events + Audit | Audit trail, security |

### Take-Home Project (Build on your own time)

**Project: Build a Complete Cursor Team Dashboard**

**Requirements:**

1. **Backend (Python/Flask or FastAPI)**
   - Fetch data from all 4 API categories
   - Cache responses for performance
   - Expose JSON endpoints for frontend

2. **Frontend (Choose your tool)**
   - Option A: Streamlit (easiest)
   - Option B: Metabase (BI tool)
   - Option C: Custom React/Next.js
   - Option D: Google Sheets + Apps Script (simplest)

3. **Dashboard Panels (Required)**

   **Panel 1: Executive Summary**
   - Total monthly cost
   - Active users (DAU/MAU)
   - AI contribution percentage
   - ROI estimate

   **Panel 2: Usage Analytics**
   - Daily cost trend (line chart)
   - Cost by model (pie chart)
   - Top users by usage (bar chart)

   **Panel 3: AI Code Impact**
   - AI vs human lines (stacked bar)
   - Acceptance rate by model
   - Files with most AI changes

   **Panel 4: Team Management**
   - Member list with roles
   - Spending limits per user
   - Inactive users warning

   **Panel 5: Compliance (Auditor View)**
   - Change event log
   - Export to CSV button
   - Date range picker

**Starter Code (Streamlit Version):**

```python
# cursor_dashboard.py - Complete dashboard starter
# Run with: streamlit run cursor_dashboard.py

import streamlit as st
import pandas as pd
import requests
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Configuration
st.set_page_config(page_title="Cursor Team Dashboard", layout="wide")

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

# Cache data to avoid repeated API calls (TTL: 1 hour)
@st.cache_data(ttl=3600)
def fetch_usage_data(days=30):
    """Fetch usage analytics."""
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

@st.cache_data(ttl=3600)
def fetch_commit_metrics(days=30):
    """Fetch AI commit metrics."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/commits",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d")
        }
    )
    return response.json()

@st.cache_data(ttl=3600)
def fetch_team_members():
    """Fetch team member list."""
    response = requests.get(
        "https://api.cursor.com/v1/admin/members",
        auth=AUTH
    )
    return response.json().get("members", [])

@st.cache_data(ttl=3600)
def fetch_model_events(days=30):
    """Fetch granular events for model analysis."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/events",
        auth=AUTH,
        params={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
            "limit": 1000
        }
    )
    return response.json().get("events", [])

# Main Dashboard
st.title("🤖 Cursor Team Dashboard")
st.markdown("---")

# Sidebar filters
st.sidebar.header("Filters")
days = st.sidebar.slider("Time Range (days)", 7, 90, 30)
refresh = st.sidebar.button("🔄 Refresh Data")

if refresh:
    st.cache_data.clear()
    st.rerun()

# Load data
with st.spinner("Loading data..."):
    usage_data = fetch_usage_data(days)
    commit_data = fetch_commit_metrics(days)
    members = fetch_team_members()
    events = fetch_model_events(days)

# ============ PANEL 1: Executive Summary ============
st.header("📊 Executive Summary")

col1, col2, col3, col4 = st.columns(4)

total_cost = sum(d.get('cost', 0) for d in usage_data)
avg_dau = sum(d.get('activeUsers', 0) for d in usage_data) / len(usage_data) if usage_data else 0
ai_lines = commit_data.get('summary', {}).get('aiGeneratedLines', 0)
human_lines = commit_data.get('summary', {}).get('humanLines', 0)
ai_percentage = (ai_lines / (ai_lines + human_lines) * 100) if (ai_lines + human_lines) > 0 else 0

col1.metric("Total Cost (30d)", f"${total_cost:.2f}")
col2.metric("Avg Daily Users", f"{avg_dau:.0f}")
col3.metric("AI Contribution", f"{ai_percentage:.1f}%")
col4.metric("Team Size", len(members))

# ============ PANEL 2: Usage Analytics ============
st.markdown("---")
st.header("💰 Usage Analytics")

# Daily cost trend
if usage_data:
    df_usage = pd.DataFrame(usage_data)
    fig_cost = px.line(df_usage, x='date', y='cost', title='Daily Cost Trend')
    fig_cost.update_layout(xaxis_title="Date", yaxis_title="Cost (USD)")
    st.plotly_chart(fig_cost, use_container_width=True)

# Two-column layout for cost breakdown
col1, col2 = st.columns(2)

with col1:
    # Cost by model (from events)
    model_costs = {}
    for event in events:
        model = event.get('modelId', 'unknown')
        model_costs[model] = model_costs.get(model, 0) + 0.01  # Approximate
    
    if model_costs:
        df_models = pd.DataFrame([
            {'Model': k, 'Cost': v} for k, v in model_costs.items()
        ])
        fig_models = px.pie(df_models, values='Cost', names='Model', title='Cost by Model')
        st.plotly_chart(fig_models, use_container_width=True)

with col2:
    # Top users (simplified)
    user_events = {}
    for event in events:
        user = event.get('user', {}).get('email', 'unknown')
        user_events[user] = user_events.get(user, 0) + 1
    
    if user_events:
        df_users = pd.DataFrame([
            {'User': k, 'Activity': v} for k, v in sorted(user_events.items(), key=lambda x: -x[1])[:10]
        ])
        fig_users = px.bar(df_users, x='User', y='Activity', title='Top Users by Activity')
        fig_users.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_users, use_container_width=True)

# ============ PANEL 3: AI Code Impact ============
st.markdown("---")
st.header("🎯 AI Code Impact")

col1, col2 = st.columns(2)

with col1:
    # AI vs Human contributions
    fig_contrib = go.Figure(data=[
        go.Bar(name='AI Generated', x=['Last 30 Days'], y=[ai_lines]),
        go.Bar(name='Human Written', x=['Last 30 Days'], y=[human_lines])
    ])
    fig_contrib.update_layout(title='AI vs Human Code Contribution', barmode='stack')
    st.plotly_chart(fig_contrib, use_container_width=True)

with col2:
    # Acceptance rate by model
    acceptance = {}
    for event in events:
        model = event.get('modelId', 'unknown')
        accepted = event.get('accepted', False)
        
        if model not in acceptance:
            acceptance[model] = {'total': 0, 'accepted': 0}
        acceptance[model]['total'] += 1
        if accepted:
            acceptance[model]['accepted'] += 1
    
    if acceptance:
        df_accept = pd.DataFrame([
            {'Model': m, 'Acceptance Rate': (s['accepted'] / s['total']) * 100}
            for m, s in acceptance.items()
        ])
        fig_accept = px.bar(df_accept, x='Model', y='Acceptance Rate', title='Acceptance Rate by Model')
        fig_accept.update_layout(yaxis_range=[0, 100])
        st.plotly_chart(fig_accept, use_container_width=True)

# ============ PANEL 4: Team Management ============
st.markdown("---")
st.header("👥 Team Management")

if members:
    df_members = pd.DataFrame(members)
    
    # Show member table
    st.dataframe(
        df_members[['email', 'role', 'status', 'createdAt']],
        use_container_width=True,
        column_config={
            'email': 'Email',
            'role': 'Role',
            'status': 'Status',
            'createdAt': 'Joined'
        }
    )
    
    # Inactive users warning
    # (Would require lastActiveAt field - simplified here)
    st.info(f"ℹ️ Total active licenses: {len(members)}")

# ============ PANEL 5: Compliance Export ============
st.markdown("---")
st.header("🔒 Compliance & Export")

col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Export Events to CSV"):
        df_events = pd.DataFrame(events)
        csv = df_events.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"cursor_events_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

with col2:
    st.markdown("**Audit Summary**")
    st.metric("Total AI Events (30d)", len(events))
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Footer
st.markdown("---")
st.caption("Cursor Team Dashboard | Data refreshes every hour")
```

**Project Deliverables:**

1. **Working dashboard** (any platform)
2. **Documentation** of your setup
3. **One insight** you discovered from your data
4. **Export script** for compliance reporting

**Bonus Points:**
- Add alerting (cost threshold exceeded)
- Add user spending limit management UI
- Add model comparison (A/B testing acceptance rates)
- Deploy to cloud (Streamlit Cloud, Railway, etc.)

---

## Module Summary

| Lesson | Topic | Time | Type |
|--------|-------|------|------|
| 10.1 | AI Commit Metrics | 6 min | Exercise |
| 10.2 | Bulk Export via CSV | 5 min | Exercise |
| 10.3 | Granular Change Events | 5 min | Exercise |
| 10.4 | Dashboard Architecture | 5 min | Take-home project |

---

## Quick Reference Card

| Need | API Endpoint | Output |
|------|--------------|--------|
| AI per commit | `/admin/analytics/commits` | Lines, percentage by dev |
| Bulk export | `/admin/analytics/export/csv` | Streaming CSV |
| Granular events | `/admin/analytics/events` | Per-change audit trail |
| Dashboard | Combine all above | Complete reporting |

**Key Metrics for Leadership:**
- **Adoption:** DAU / total team size
- **ROI:** (Hours saved × developer rate) - AI cost
- **Quality:** Acceptance rate by model
- **Compliance:** Complete change audit trail

---

## Course Completion

🎉 **Congratulations! You've completed the Cursor Training Program (Day 2).**

You can now:
- ✅ Programmatically create and manage Cloud Agents
- ✅ Stream real-time agent responses
- ✅ Set up webhook notifications
- ✅ Administer teams and enforce spending policies
- ✅ Analyze usage and model adoption
- ✅ Track AI code contributions
- ✅ Build complete reporting dashboards

**Next Steps:**
1. Complete the take-home dashboard project
2. Share your dashboard with your team
3. Set up scheduled exports for your BI tool
4. Implement cost alerts for budget governance

---

*End of Module 10 — and End of Day 2 Training Program* 🎉