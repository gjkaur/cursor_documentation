# Module 10: AI Code Tracking and Reporting

## Cursor Training Program — Day 2 (Hands-On + Take-Home Project)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~20 minutes (plus take-home project) |
| **Format** | Hands-on exercise + take-home project |
| **Prerequisites** | Admin API key, Git repository access, Modules 8-9 completed |
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

### Concept (3 minutes)

> *"Per-commit attribution of AI vs. human contributions. This is the 'ROI of AI' metric – showing exactly how much code was AI-generated versus human-written."*

### Key Endpoint: `GET /v1/admin/analytics/commits`

**What this measures:**
- Lines added by AI vs. human
- Files modified by agent vs. manual
- Commit-level attribution
- Per-developer breakdown

### Hands-On Exercise (5 minutes)

**Step 1:** Get AI contribution metrics for your repository

```bash
END=$(date +%Y-%m-%d)
START=$(date -d "30 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/commits?startDate=$START&endDate=$END&repo=https://github.com/YOUR_ORG/YOUR_REPO" \
  | jq '.'
```

**Step 2:** Calculate AI contribution percentage

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

**Step 3:** Python script for AI contribution tracking

```python
#!/usr/bin/env python3
import requests
import os
from datetime import datetime, timedelta

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

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
        f"{BASE_URL}/analytics/commits",
        auth=AUTH,
        params=params
    )
    response.raise_for_status()
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
    
    # Get AI usage cost from analytics
    end = datetime.now()
    start = end - timedelta(days=30)
    usage_response = requests.get(
        f"{BASE_URL}/analytics/usage",
        auth=AUTH,
        params={"startDate": start.strftime("%Y-%m-%d"), "endDate": end.strftime("%Y-%m-%d")}
    )
    usage_cost = usage_response.json().get('summary', {}).get('totalCost', 0)
    
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
    print(f"   AI usage cost: ${usage_cost:.2f}")
    print(f"   Net ROI: ${cost_saved - usage_cost:.0f}")
    
    return {
        "ai_lines": ai_lines,
        "ai_percentage": ai_percentage,
        "hours_saved": hours_saved,
        "net_roi": cost_saved - usage_cost
    }

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

---

## Lesson 10.2: Bulk Export via CSV Streaming

### Concept (3 minutes)

> *"Wiring metrics into BI tools (Tableau, PowerBI, Looker, Metabase). Streaming CSV exports let you pull large datasets efficiently without timeouts."*

### Key Endpoint: `GET /v1/admin/analytics/export/csv` (streaming)

### Hands-On Exercise (4 minutes)

**Step 1:** Stream CSV export directly to file

```bash
START=$(date -d "30 days ago" +%Y-%m-%d)
END=$(date +%Y-%m-%d)

curl -N -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/export/csv?startDate=$START&endDate=$END&type=commits" \
  -o cursor_commits_export.csv

# Check output
head -10 cursor_commits_export.csv
```

**Step 2:** Python script for BI tool ingestion

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
from datetime import datetime, timedelta

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")

def stream_to_dataframe(start_date, end_date, export_type="commits"):
    """Stream export data directly to pandas DataFrame."""
    response = requests.get(
        "https://api.cursor.com/v1/admin/analytics/export/csv",
        auth=AUTH,
        params={
            "startDate": start_date,
            "endDate": end_date,
            "type": export_type
        },
        stream=True
    )
    response.raise_for_status()
    
    # Stream content into DataFrame
    content = b''
    for chunk in response.iter_content(chunk_size=8192):
        content += chunk
    
    df = pd.read_csv(io.BytesIO(content))
    return df

def export_for_bi():
    """Generate CSV files ready for BI tools."""
    end = datetime.now()
    start = end - timedelta(days=30)
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")
    
    # Export commits
    print("📊 Exporting commit data...")
    df_commits = stream_to_dataframe(start_str, end_str, "commits")
    df_commits.to_csv("bi_commits.csv", index=False)
    print(f"   Exported {len(df_commits)} commits")
    
    # Export events
    print("📋 Exporting event data...")
    df_events = stream_to_dataframe(start_str, end_str, "events")
    df_events.to_csv("bi_events.csv", index=False)
    print(f"   Exported {len(df_events)} events")
    
    # Export usage
    print("💰 Exporting usage data...")
    df_usage = stream_to_dataframe(start_str, end_str, "usage")
    df_usage.to_csv("bi_usage.csv", index=False)
    print(f"   Exported {len(df_usage)} usage records")
    
    print("\n✅ Ready for BI import:")
    print("   - bi_commits.csv")
    print("   - bi_events.csv")
    print("   - bi_usage.csv")

def generate_metabase_upload_script():
    """Generate a script for uploading to Metabase."""
    print("\n📤 Metabase Upload Script:")
    print("""
# For Metabase: Use the CSV upload feature
# 1. Go to Settings → Data Model → Uploads
# 2. Configure database table
# 3. Run this command after each export:

curl -X POST https://your-metabase.com/api/dataset/csv \\
  -H "X-Metabase-Session: $METABASE_TOKEN" \\
  -F "file=@bi_commits.csv"
""")

if __name__ == "__main__":
    export_for_bi()
    generate_metabase_upload_script()
```

**Success Criteria:**
- [ ] Streamed CSV export to file
- [ ] Loaded export into pandas DataFrame
- [ ] Created BI-ready export files

---

## Lesson 10.3: Granular AI Change Events

### Concept (3 minutes)

> *"Per-event detail for compliance reporting. Every AI-generated change is tracked – file, line range, model used, timestamp. Essential for SOC2, ISO, and internal audits."*

### Key Endpoint: `GET /v1/admin/analytics/events`

### Hands-On Exercise (4 minutes)

**Step 1:** Get granular change events

```bash
START=$(date -d "7 days ago" +%Y-%m-%d)
END=$(date +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/events?startDate=$START&endDate=$END&limit=100" \
  | jq '.events[] | {user: .user.email, file: .filePath, model: .modelId, accepted: .accepted}'
```

**Step 2:** Generate compliance report

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

**Step 3:** Python compliance export

```python
#!/usr/bin/env python3
import requests
import os
import csv
from datetime import datetime, timedelta
from collections import defaultdict

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

def get_change_events(days=30, limit=1000):
    """Retrieve granular change events."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    all_events = []
    offset = 0
    
    while True:
        response = requests.get(
            f"{BASE_URL}/analytics/events",
            auth=AUTH,
            params={
                "startDate": start.strftime("%Y-%m-%d"),
                "endDate": end.strftime("%Y-%m-%d"),
                "limit": limit,
                "offset": offset
            }
        )
        response.raise_for_status()
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
    events = get_change_events(days=90)
    
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
    
    # Files with most AI changes
    file_stats = defaultdict(int)
    for event in events:
        file_path = event.get('filePath', 'unknown')
        file_stats[file_path] += 1
    
    print("\n📁 Files with Most AI Changes (needs review):")
    top_files = sorted(file_stats.items(), key=lambda x: -x[1])[:10]
    for file_path, count in top_files:
        print(f"   {file_path}: {count} changes")
    
    # Export to CSV for auditor
    with open('compliance_export.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'timestamp', 'user_email', 'model_id', 'file_path', 
            'line_start', 'line_end', 'accepted'
        ])
        writer.writeheader()
        
        for event in events[:10000]:
            writer.writerow({
                'timestamp': event.get('timestamp'),
                'user_email': event.get('user', {}).get('email'),
                'model_id': event.get('modelId'),
                'file_path': event.get('filePath'),
                'line_start': event.get('lineStart'),
                'line_end': event.get('lineEnd'),
                'accepted': event.get('accepted')
            })
    
    print(f"\n✅ Compliance export saved to compliance_export.csv")

if __name__ == "__main__":
    generate_compliance_report()
```

**Success Criteria:**
- [ ] Retrieved granular change events
- [ ] Calculated acceptance rates by model
- [ ] Generated compliance export for auditors

---

## Lesson 10.4: Reporting Dashboard Architecture (Take-Home Project)

### Concept (4 minutes)

> *"Combining Admin, Analytics, and AI Code Tracking data into a single dashboard. This is your take-home project – build a complete operational dashboard for your team."*

### Dashboard Components

| Component | Data Source | Purpose |
|-----------|-------------|---------|
| Usage Overview | Usage API | Cost, tokens, active users |
| AI Contribution | Commits API | ROI, adoption metrics |
| Model Performance | Events API | Acceptance rates, efficiency |
| Team Activity | Members API | Onboarding, licensing |
| Compliance | Events + Audit | Audit trail, security |

### Take-Home Project Starter Code

```python
#!/usr/bin/env python3
"""
Complete Cursor Team Dashboard
Run with: streamlit run cursor_dashboard.py
"""

import streamlit as st
import pandas as pd
import requests
import os
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ============ Configuration ============
st.set_page_config(page_title="Cursor Team Dashboard", layout="wide")

ADMIN_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
AUTH = (ADMIN_KEY, "")
BASE_URL = "https://api.cursor.com/v1/admin"

# ============ Data Fetching (Cached) ============
@st.cache_data(ttl=3600)
def fetch_data(endpoint, params=None):
    """Generic data fetcher with caching."""
    response = requests.get(f"{BASE_URL}{endpoint}", auth=AUTH, params=params)
    if response.status_code == 200:
        return response.json()
    return {}

@st.cache_data(ttl=3600)
def get_usage_data(days=30):
    end = datetime.now()
    start = end - timedelta(days=days)
    return fetch_data("/analytics/usage/daily", {
        "startDate": start.strftime("%Y-%m-%d"),
        "endDate": end.strftime("%Y-%m-%d")
    })

@st.cache_data(ttl=3600)
def get_commit_metrics(days=30):
    end = datetime.now()
    start = end - timedelta(days=days)
    return fetch_data("/analytics/commits", {
        "startDate": start.strftime("%Y-%m-%d"),
        "endDate": end.strftime("%Y-%m-%d")
    })

@st.cache_data(ttl=3600)
def get_team_members():
    return fetch_data("/members")

@st.cache_data(ttl=3600)
def get_model_events(days=30):
    end = datetime.now()
    start = end - timedelta(days=days)
    return fetch_data("/analytics/events", {
        "startDate": start.strftime("%Y-%m-%d"),
        "endDate": end.strftime("%Y-%m-%d"),
        "limit": 1000
    })

# ============ Dashboard UI ============
st.title("🤖 Cursor Team Dashboard")
st.markdown("---")

# Sidebar
st.sidebar.header("Filters")
days = st.sidebar.slider("Time Range (days)", 7, 90, 30)
refresh = st.sidebar.button("🔄 Refresh Data")
if refresh:
    st.cache_data.clear()
    st.rerun()

# Load data
with st.spinner("Loading data..."):
    usage_data = get_usage_data(days)
    commit_data = get_commit_metrics(days)
    members = get_team_members()
    events = get_model_events(days)

# ============ Panel 1: Executive Summary ============
st.header("📊 Executive Summary")

daily_data = usage_data.get("daily", [])
total_cost = sum(d.get('cost', 0) for d in daily_data)
avg_dau = sum(d.get('activeUsers', 0) for d in daily_data) / len(daily_data) if daily_data else 0

summary = commit_data.get("summary", {})
ai_lines = summary.get("aiGeneratedLines", 0)
human_lines = summary.get("humanLines", 0)
total_lines = ai_lines + human_lines
ai_percentage = (ai_lines / total_lines * 100) if total_lines > 0 else 0

member_list = members.get("members", [])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cost (30d)", f"${total_cost:.2f}")
col2.metric("Avg Daily Users", f"{avg_dau:.0f}")
col3.metric("AI Contribution", f"{ai_percentage:.1f}%")
col4.metric("Team Size", len(member_list))

# ============ Panel 2: Usage Analytics ============
st.markdown("---")
st.header("💰 Usage Analytics")

if daily_data:
    df_usage = pd.DataFrame(daily_data)
    fig_cost = px.line(df_usage, x='date', y='cost', title='Daily Cost Trend')
    fig_cost.update_layout(xaxis_title="Date", yaxis_title="Cost (USD)")
    st.plotly_chart(fig_cost, use_container_width=True)

# ============ Panel 3: AI Code Impact ============
st.markdown("---")
st.header("🎯 AI Code Impact")

col1, col2 = st.columns(2)

with col1:
    fig_contrib = go.Figure(data=[
        go.Bar(name='AI Generated', x=['Last 30 Days'], y=[ai_lines]),
        go.Bar(name='Human Written', x=['Last 30 Days'], y=[human_lines])
    ])
    fig_contrib.update_layout(title='AI vs Human Code Contribution', barmode='stack')
    st.plotly_chart(fig_contrib, use_container_width=True)

with col2:
    events_list = events.get("events", [])
    acceptance = {}
    for event in events_list:
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

# ============ Panel 4: Team Management ============
st.markdown("---")
st.header("👥 Team Management")

if member_list:
    df_members = pd.DataFrame(member_list)
    st.dataframe(
        df_members[['email', 'role', 'status', 'createdAt']],
        use_container_width=True
    )
    st.info(f"ℹ️ Total active licenses: {len(member_list)}")

# ============ Panel 5: Compliance Export ============
st.markdown("---")
st.header("🔒 Compliance & Export")

col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Export Events to CSV"):
        df_events = pd.DataFrame(events_list)
        csv = df_events.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"cursor_events_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

with col2:
    st.metric("Total AI Events (30d)", len(events_list))

# Footer
st.markdown("---")
st.caption("Cursor Team Dashboard | Data refreshes every hour")

print("\n✅ Dashboard ready! Run: streamlit run cursor_dashboard.py")
```

### Project Deliverables

| Deliverable | Description |
|-------------|-------------|
| **Working dashboard** | Deploy using Streamlit, Metabase, or custom frontend |
| **Documentation** | Setup instructions and data source descriptions |
| **One insight** | Key finding from your team's data |
| **Export script** | Automated CSV export for compliance |

**Bonus Points:**
- Add alerting (cost threshold exceeded)
- Add user spending limit management UI
- Add model comparison (A/B testing acceptance rates)
- Deploy to cloud (Streamlit Cloud, Railway, etc.)

---

## Module Summary

| Lesson | Topic | Time | Key Skill |
|--------|-------|------|-----------|
| 10.1 | AI Commit Metrics | 5 min | ROI calculation |
| 10.2 | Bulk Export via CSV | 4 min | BI integration |
| 10.3 | Granular Change Events | 4 min | Compliance reporting |
| 10.4 | Dashboard Architecture | 4 min | Complete dashboard |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              AI CODE TRACKING QUICK REFERENCE                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ENDPOINTS:                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ GET /admin/analytics/commits     AI per commit      │   │
│  │ GET /admin/analytics/export/csv  Bulk CSV export    │   │
│  │ GET /admin/analytics/events      Granular events    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  KEY METRICS FOR LEADERSHIP:                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Adoption: DAU / total team size                  │   │
│  │ • ROI: (Hours saved × rate) - AI cost              │   │
│  │ • Quality: Acceptance rate by model                │   │
│  │ • Compliance: Complete change audit trail          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  DASHBOARD DEPLOYMENT OPTIONS:                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Streamlit    (easiest, Python)                   │   │
│  │ • Metabase     (BI tool, SQL-based)                │   │
│  │ • PowerBI      (Enterprise, direct CSV import)     │   │
│  │ • Custom React (most flexible)                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Course Completion

🎉 **Congratulations! You've completed the Cursor Training Program (Day 2).**

**You can now:**
- ✅ Programmatically create and manage Cloud Agents
- ✅ Stream real-time agent responses with SSE
- ✅ Set up webhook notifications with HMAC verification
- ✅ Administer teams and enforce spending policies
- ✅ Analyze usage, model adoption, and AI contribution
- ✅ Track AI vs. human code changes per commit
- ✅ Build complete reporting dashboards for leadership

**Next Steps:**
1. Complete the take-home dashboard project
2. Share your dashboard with your team
3. Set up scheduled exports for your BI tool
4. Implement cost alerts for budget governance
5. Explore custom MCP servers for your team's tools

---

*End of Module 10 — and End of Day 2 Training Program* 🎉