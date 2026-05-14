# API Exercise 23: Build a Complete Dashboard

**Objective:** Build a full-stack dashboard that displays team analytics, model usage, and AI commit metrics from all Cursor APIs.

**Time:** 25 minutes

**Difficulty:** Advanced

**Real-World Scenario:** Your team needs a centralized dashboard to track Cursor adoption, model usage costs, and AI code contribution. You'll build a web application that aggregates data from multiple Cursor APIs into a single view.

---

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] Python 3.8+ with Flask
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Create the Dashboard Backend (10 minutes)

**Create `dashboard_app.py`:**
```python
#!/usr/bin/env python3
"""
Cursor Analytics Dashboard - Backend
Combines data from multiple Cursor APIs
"""

from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests
import os
from datetime import datetime, timedelta
from collections import defaultdict
import json

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    exit(1)

BASE_URL = "https://api.cursor.com"
auth = (API_KEY, "")

def get_dau(start_date="7d", end_date="today"):
    """Get Daily Active Users data."""
    url = f"{BASE_URL}/analytics/team/dau"
    params = {"startDate": start_date, "endDate": end_date}
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code != 200:
        return []
    
    return response.json().get("data", [])

def get_model_usage(start_date="7d", end_date="today"):
    """Get model usage data."""
    url = f"{BASE_URL}/analytics/team/models"
    params = {"startDate": start_date, "endDate": end_date}
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code != 200:
        return []
    
    return response.json().get("data", [])

def get_leaderboard(start_date="30d", end_date="today", limit=10):
    """Get user leaderboard."""
    url = f"{BASE_URL}/analytics/team/leaderboard"
    params = {"startDate": start_date, "endDate": end_date, "pageSize": limit}
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code != 200:
        return {}
    
    return response.json().get("data", {})

def get_ai_commits(start_date="7d", end_date="now"):
    """Get AI commit metrics."""
    url = f"{BASE_URL}/analytics/ai-code/commits"
    params = {"startDate": start_date, "endDate": end_date, "pageSize": 100}
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code != 200:
        return []
    
    return response.json().get("items", [])

def get_conversation_insights(start_date="7d", end_date="today"):
    """Get conversation insights."""
    url = f"{BASE_URL}/analytics/team/conversation-insights"
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "include": "intents,categories,workTypes,complexity"
    }
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code != 200:
        return {}
    
    return response.json().get("data", {})

def get_team_members():
    """Get team members list."""
    url = f"{BASE_URL}/teams/members"
    
    response = requests.get(url, auth=auth)
    
    if response.status_code != 200:
        return []
    
    return response.json().get("teamMembers", [])

@app.route('/api/dashboard')
def dashboard_data():
    """Return all dashboard data."""
    
    # Get data from various APIs
    dau_data = get_dau("30d", "today")
    model_data = get_model_usage("30d", "today")
    leaderboard = get_leaderboard("30d", "today", 10)
    commits = get_ai_commits("30d", "now")
    insights = get_conversation_insights("30d", "today")
    members = get_team_members()
    
    # Calculate summary metrics
    total_members = len(members)
    active_members = len([m for m in members if not m.get("isRemoved", False)])
    
    # AI commit summary
    total_lines = sum(c.get("totalLinesAdded", 0) for c in commits)
    ai_lines = sum(c.get("tabLinesAdded", 0) + c.get("composerLinesAdded", 0) for c in commits)
    ai_percentage = (ai_lines / total_lines * 100) if total_lines > 0 else 0
    
    # Model usage summary
    model_totals = defaultdict(lambda: {"messages": 0, "users": 0})
    for day in model_data:
        for model, stats in day.get("model_breakdown", {}).items():
            model_totals[model]["messages"] += stats.get("messages", 0)
            model_totals[model]["users"] = max(
                model_totals[model]["users"],
                stats.get("users", 0)
            )
    
    # Daily trend
    daily_trend = []
    for day in dau_data[-7:]:  # Last 7 days
        daily_trend.append({
            "date": day.get("date"),
            "dau": day.get("dau", 0),
            "cloud_agents": day.get("cloud_agent_dau", 0),
            "cli": day.get("cli_dau", 0)
        })
    
    # Prepare response
    response = {
        "summary": {
            "total_members": total_members,
            "active_members": active_members,
            "total_commits": len(commits),
            "total_lines_added": total_lines,
            "ai_lines_added": ai_lines,
            "ai_percentage": round(ai_percentage, 1),
            "top_model": max(model_totals.items(), key=lambda x: x[1]["messages"])[0] if model_totals else "N/A"
        },
        "daily_active_users": daily_trend,
        "model_usage": [
            {"model": model, "messages": stats["messages"], "users": stats["users"]}
            for model, stats in sorted(model_totals.items(), key=lambda x: -x[1]["messages"])[:5]
        ],
        "leaderboard": {
            "tab": leaderboard.get("tab_leaderboard", {}).get("data", [])[:5],
            "agent": leaderboard.get("agent_leaderboard", {}).get("data", [])[:5]
        },
        "conversation_insights": {
            "intents": insights.get("intents", {}).get("distribution", []),
            "work_types": insights.get("workTypes", {}).get("distribution", []),
            "complexity": insights.get("complexity", {}).get("distribution", [])
        },
        "timestamp": datetime.now().isoformat()
    }
    
    return jsonify(response)

@app.route('/')
def index():
    """Serve the dashboard HTML."""
    return render_template('dashboard.html')

if __name__ == '__main__':
    print("🚀 Cursor Analytics Dashboard")
    print("=" * 40)
    print("Starting server at http://localhost:5001")
    app.run(debug=True, port=5001)
```

---

### Step 2: Create the Dashboard Frontend (10 minutes)

**Create `templates/dashboard.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cursor Analytics Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }
        
        .dashboard {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: #666;
            margin-bottom: 30px;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .stat-value {
            font-size: 32px;
            font-weight: bold;
            color: #0066cc;
        }
        
        .stat-label {
            color: #666;
            font-size: 14px;
            margin-top: 5px;
        }
        
        .chart-container {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .chart-title {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 20px;
            color: #333;
        }
        
        .two-columns {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .leaderboard-table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .leaderboard-table th,
        .leaderboard-table td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }
        
        .leaderboard-table th {
            font-weight: 600;
            color: #666;
        }
        
        .rank-1 { background-color: #ffd70020; font-weight: bold; }
        .rank-2 { background-color: #c0c0c020; }
        .rank-3 { background-color: #cd7f3220; }
        
        .loading {
            text-align: center;
            padding: 50px;
            color: #666;
        }
        
        .error {
            background: #fee;
            color: #c00;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        canvas {
            max-height: 300px;
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>📊 Cursor Analytics Dashboard</h1>
        <div class="subtitle">Team AI Usage & Adoption Metrics</div>
        
        <div id="loading" class="loading">Loading dashboard data...</div>
        
        <div id="content" style="display: none;">
            <!-- Stats Cards -->
            <div class="stats-grid" id="stats-cards"></div>
            
            <!-- DAU Trend Chart -->
            <div class="chart-container">
                <div class="chart-title">📈 Daily Active Users (Last 7 Days)</div>
                <canvas id="dauChart"></canvas>
            </div>
            
            <!-- Model Usage & Leaderboard -->
            <div class="two-columns">
                <div class="chart-container">
                    <div class="chart-title">🤖 Model Usage (Last 30 Days)</div>
                    <canvas id="modelChart"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">🏆 Top Users by Tab Accepts</div>
                    <table class="leaderboard-table" id="tab-leaderboard">
                        <thead>
                            <tr><th>Rank</th><th>User</th><th>Accepts</th><th>Lines</th></tr>
                        </thead>
                        <tbody></tbody>
                    </table>
                </div>
            </div>
            
            <!-- AI Contribution & Conversation Insights -->
            <div class="two-columns">
                <div class="chart-container">
                    <div class="chart-title">💚 AI vs Human Code Contribution</div>
                    <canvas id="aiContributionChart" style="max-height: 250px;"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">💬 Conversation Intents</div>
                    <canvas id="intentsChart"></canvas>
                </div>
            </div>
            
            <!-- Work Types -->
            <div class="chart-container">
                <div class="chart-title">🛠️ Work Types</div>
                <canvas id="workTypesChart"></canvas>
            </div>
        </div>
    </div>
    
    <script>
        let dauChart, modelChart, aiChart, intentsChart, workTypesChart;
        
        async function loadDashboard() {
            try {
                const response = await fetch('/api/dashboard');
                const data = await response.json();
                
                updateStatsCards(data.summary);
                updateDAUChart(data.daily_active_users);
                updateModelChart(data.model_usage);
                updateLeaderboard(data.leaderboard);
                updateAIChart(data.summary.ai_percentage);
                updateIntentsChart(data.conversation_insights.intents);
                updateWorkTypesChart(data.conversation_insights.work_types);
                
                document.getElementById('loading').style.display = 'none';
                document.getElementById('content').style.display = 'block';
            } catch (error) {
                document.getElementById('loading').innerHTML = 
                    '<div class="error">❌ Error loading dashboard: ' + error.message + '</div>';
            }
        }
        
        function updateStatsCards(summary) {
            const cards = [
                { label: 'Active Members', value: summary.active_members },
                { label: 'Total Commits (30d)', value: summary.total_commits.toLocaleString() },
                { label: 'AI Lines Added', value: summary.ai_lines_added.toLocaleString() },
                { label: 'AI %', value: summary.ai_percentage + '%' },
                { label: 'Top Model', value: summary.top_model }
            ];
            
            const container = document.getElementById('stats-cards');
            container.innerHTML = cards.map(card => `
                <div class="stat-card">
                    <div class="stat-value">${card.value}</div>
                    <div class="stat-label">${card.label}</div>
                </div>
            `).join('');
        }
        
        function updateDAUChart(dailyData) {
            const ctx = document.getElementById('dauChart').getContext('2d');
            const dates = dailyData.map(d => d.date.slice(5));
            const dau = dailyData.map(d => d.dau);
            const cloudAgents = dailyData.map(d => d.cloud_agents);
            
            if (dauChart) dauChart.destroy();
            
            dauChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [
                        {
                            label: 'Total DAU',
                            data: dau,
                            borderColor: '#0066cc',
                            backgroundColor: 'rgba(0,102,204,0.1)',
                            fill: true
                        },
                        {
                            label: 'Cloud Agents',
                            data: cloudAgents,
                            borderColor: '#00aa55',
                            backgroundColor: 'rgba(0,170,85,0.1)',
                            fill: true
                        }
                    ]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
        }
        
        function updateModelChart(modelUsage) {
            const ctx = document.getElementById('modelChart').getContext('2d');
            const models = modelUsage.map(m => m.model);
            const messages = modelUsage.map(m => m.messages);
            
            if (modelChart) modelChart.destroy();
            
            modelChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: models,
                    datasets: [{
                        label: 'Messages',
                        data: messages,
                        backgroundColor: '#0066cc'
                    }]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
        }
        
        function updateLeaderboard(leaderboard) {
            const tabBody = document.querySelector('#tab-leaderboard tbody');
            tabBody.innerHTML = leaderboard.tab.map((user, idx) => `
                <tr class="${idx === 0 ? 'rank-1' : idx === 1 ? 'rank-2' : idx === 2 ? 'rank-3' : ''}">
                    <td>${idx + 1}</td>
                    <td>${user.email.split('@')[0]}</td>
                    <td>${user.total_accepts?.toLocaleString() || 0}</td>
                    <td>${user.total_lines_accepted?.toLocaleString() || 0}</td>
                </tr>
            `).join('');
        }
        
        function updateAIChart(aiPercentage) {
            const ctx = document.getElementById('aiContributionChart').getContext('2d');
            
            if (aiChart) aiChart.destroy();
            
            aiChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['AI Generated', 'Human Written'],
                    datasets: [{
                        data: [aiPercentage, 100 - aiPercentage],
                        backgroundColor: ['#00aa55', '#cccccc']
                    }]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
        }
        
        function updateIntentsChart(intents) {
            const ctx = document.getElementById('intentsChart').getContext('2d');
            const labels = intents.map(i => i.intent);
            const counts = intents.map(i => i.count);
            
            if (intentsChart) intentsChart.destroy();
            
            intentsChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: labels,
                    datasets: [{
                        data: counts,
                        backgroundColor: ['#0066cc', '#00aa55', '#ffaa00']
                    }]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
        }
        
        function updateWorkTypesChart(workTypes) {
            const ctx = document.getElementById('workTypesChart').getContext('2d');
            const labels = workTypes.map(w => {
                const mapping = { 'new_feature': 'New Features', 'bug': 'Bug Fixing', 'maintenance': 'Maintenance' };
                return mapping[w.workType] || w.workType;
            });
            const counts = workTypes.map(w => w.count);
            
            if (workTypesChart) workTypesChart.destroy();
            
            workTypesChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Conversations',
                        data: counts,
                        backgroundColor: '#ffaa00'
                    }]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
        }
        
        // Load dashboard on page load
        loadDashboard();
        // Refresh every 5 minutes
        setInterval(loadDashboard, 300000);
    </script>
</body>
</html>
```

---

### Step 3: Install Dependencies (2 minutes)

**Command:**
```bash
pip install flask flask-cors requests
```

**Create directory structure:**
```bash
mkdir templates
# Place dashboard.html in templates/
```

---

### Step 4: Run the Dashboard (2 minutes)

**Command:**
```bash
export CURSOR_ADMIN_API_KEY="your_api_key_here"
python dashboard_app.py
```

**Expected output:**
```
🚀 Cursor Analytics Dashboard
========================================
Starting server at http://localhost:5001
 * Running on http://127.0.0.1:5001
```

---

### Step 5: View the Dashboard (1 minute)

Open your browser to: `http://localhost:5001`

**Expected dashboard includes:**
- Active members and commit statistics
- DAU trend chart (last 7 days)
- Model usage bar chart
- Top users leaderboard
- AI vs Human code contribution doughnut chart
- Conversation intents pie chart
- Work types bar chart

---

## Expected Dashboard View

```
┌─────────────────────────────────────────────────────────────────┐
│  📊 Cursor Analytics Dashboard                                  │
│  Team AI Usage & Adoption Metrics                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────┐│
│  │Active    │ │Total     │ │AI Lines  │ │AI %     │ │Top    ││
│  │Members:25│ │Commits:  │ │Added:    │ │64.8%    │ │Model: ││
│  │          │ │1,234     │ │29,876    │ │         │ │claude ││
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └───────┘│
├─────────────────────────────────────────────────────────────────┤
│  📈 Daily Active Users (Last 7 Days)                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Line Chart                            │   │
│  └─────────────────────────────────────────────────────────┘   │
├──────────────────────────────┬──────────────────────────────────┤
│  🤖 Model Usage              │  🏆 Top Users by Tab Accepts     │
│  ┌────────────────────────┐  │  ┌─────┬─────────┬────────┬─────┐│
│  │      Bar Chart         │  │  │Rank │ User    │Accepts │Lines││
│  └────────────────────────┘  │  │ 1   │ alice   │ 1,334  │3,455││
│                              │  │ 2   │ bob     │ 796    │2,090││
│                              │  │ 3   │ carol   │ 654    │1,890││
│                              │  └─────────────────────────────┘│
├──────────────────────────────┴──────────────────────────────────┤
│  💚 AI vs Human Code Contribution                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Doughnut Chart                          │   │
│  │            AI 64.8%  │  Human 35.2%                     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

- [ ] Dashboard backend created
- [ ] Dashboard frontend created
- [ ] All APIs integrated (Analytics, AI Code Tracking, Admin)
- [ ] Charts render correctly
- [ ] Data refreshes automatically
- [ ] Dashboard accessible via browser

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Check Admin API key |
| Empty charts | No data in selected date range |
| CORS error | Flask-CORS should handle this |
| Port in use | Change port number |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Multi-API integration** | Combine data from 4+ Cursor APIs |
| **Real-time updates** | 5-minute auto-refresh |
| **Visual analytics** | Charts for all key metrics |
| **Team insights** | Usage, adoption, contribution |

---

## Exercise Complete ✓

Check off when done:
- [ ] Created Flask backend
- [ ] Created HTML dashboard
- [ ] Integrated all APIs
- [ ] Charts render correctly
- [ ] Dashboard auto-refreshes

---

## 🎉 Congratulations! You've Completed All 23 API Exercises! 🎉

You can now:
- ✅ Authenticate and use all Cursor APIs
- ✅ Create and manage Cloud Agents programmatically
- ✅ Stream real-time agent responses
- ✅ Track team usage and analytics
- ✅ Analyze AI code contribution
- ✅ Set spending limits and manage users
- ✅ Handle webhooks and notifications
- ✅ Build custom dashboards and automation
