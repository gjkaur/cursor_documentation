# Analytics API – Complete Beginner's Guide

This document explains the **Analytics API** in detail – how to programmatically retrieve usage metrics, adoption data, and performance insights for your Cursor team.

Think of this as the **API version of the analytics dashboard** – getting data about how your team uses Cursor.

Let me break this down for a complete beginner.

---

## What Is the Analytics API? (The 10-Second Summary)

**The Analytics API lets you programmatically retrieve usage metrics for your Cursor team** – including AI-assisted coding, model usage, active users, and feature adoption.

| Without Analytics API | With Analytics API |
|----------------------|---------------------|
| Manually check dashboard | Automate data collection |
| Click through reports | Programmatic insights |
| One-off analysis | Regular reporting |

> *"Availability: Only for enterprise teams"*

**Important:** This API is for **team administrators** – not regular users.

---

## Authentication

All Analytics API requests use **Basic Authentication** with an **admin-scoped API key**.

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/analytics/team/agent-edits
```

**Note:** The colon after the API key is required (empty password).

### Where to Get an API Key:

1. Log into Cursor Dashboard
2. Go to **Team Settings** → API Keys
3. Generate an API key with `admin:*` scope

---

## Rate Limits

| Endpoint Type | Rate Limit |
|---------------|------------|
| **Team-level endpoints** | 100 requests/minute per team |
| **By-user endpoints** | 50 requests/minute per team |

**When exceeded:** Returns `429 Too Many Requests`

---

## Common Query Parameters (All Endpoints)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `startDate` | string | No | Start date (default: 7 days ago) |
| `endDate` | string | No | End date (default: today) |
| `users` | string | No | Filter to specific users (comma-separated) |

### Date Formats (Important!)

| Format | Example | Caching | Recommendation |
|--------|---------|---------|----------------|
| `YYYY-MM-DD` | `2025-01-15` | Excellent | ✅ **Recommended** |
| Shortcuts | `7d`, `30d`, `today`, `yesterday` | Good | ✅ Good for quick queries |
| ISO 8601 | `2025-01-15T14:30:00Z` | Poor | ❌ Avoid (prevents caching) |

**Key Rules:**
- Time is ignored – all dates resolve to day level
- Maximum date range: **30 days**
- Omit both dates → defaults to last 7 days

### User Filtering Examples

```bash
# Filter by emails
?users=alice@company.com,bob@company.com

# Filter by user IDs
?users=user_abc123,user_def456

# Mix both formats
?users=alice@company.com,user_def456
```

---

## Available Endpoints Overview

### Team-Level Endpoints (Aggregated)

| Endpoint | What it tells you |
|----------|-------------------|
| `/analytics/team/agent-edits` | AI-suggested code edits accepted/rejected |
| `/analytics/team/tabs` | Tab autocomplete usage |
| `/analytics/team/dau` | Daily active users |
| `/analytics/team/client-versions` | Which Cursor versions your team uses |
| `/analytics/team/models` | Which AI models are being used |
| `/analytics/team/top-file-extensions` | Most edited file types |
| `/analytics/team/mcp` | MCP tool adoption |
| `/analytics/team/commands` | Slash command usage |
| `/analytics/team/plans` | Plan mode adoption |
| `/analytics/team/skills` | Skills adoption |
| `/analytics/team/ask-mode` | Ask mode adoption |
| `/analytics/team/conversation-insights` | Work classification (Enterprise) |
| `/analytics/team/leaderboard` | User rankings |
| `/analytics/team/bugbot` | Bugbot PR analytics |

### By-User Endpoints (Per-User)

Same metrics as team-level, but broken down by individual user with pagination.

| Endpoint | Pattern |
|----------|---------|
| Agent edits | `/analytics/by-user/agent-edits` |
| Tab usage | `/analytics/by-user/tabs` |
| Model usage | `/analytics/by-user/models` |
| Top files | `/analytics/by-user/top-file-extensions` |
| Client versions | `/analytics/by-user/client-versions` |
| MCP | `/analytics/by-user/mcp` |
| Commands | `/analytics/by-user/commands` |
| Plans | `/analytics/by-user/plans` |
| Skills | `/analytics/by-user/skills` |
| Ask mode | `/analytics/by-user/ask-mode` |

---

## Team-Level Endpoints (Detailed)

### 1. Agent Edits (GET /analytics/team/agent-edits)

Get metrics on AI-suggested code edits accepted by your team.

**What the numbers mean:**
- `total_suggested_diffs` – Number of edit suggestions made
- `total_accepted_diffs` – Number accepted by users
- `total_rejected_diffs` – Number rejected
- `total_lines_accepted` – Lines of code accepted (most important metric)

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/agent-edits?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "total_suggested_diffs": 145,
      "total_accepted_diffs": 98,
      "total_rejected_diffs": 47,
      "total_lines_accepted": 980
    }
  ]
}
```

**Use Case:** Track how often your team accepts AI suggestions. High acceptance = good AI assistance.

---

### 2. Tab Usage (GET /analytics/team/tabs)

Get metrics on Tab autocomplete usage.

**Key fields:**
- `total_suggestions` – Tab completions shown
- `total_accepts` – Tab completions accepted
- `total_lines_accepted` – Lines of code accepted

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/tabs?startDate=7d&endDate=today"
```

**Use Case:** Measure how much time Tab saves your developers.

---

### 3. Daily Active Users (DAU) – GET /analytics/team/dau

Get daily active user counts. An active user has used at least one AI feature.

**Response includes:**
- `dau` – Total daily active users
- `cli_dau` – Active CLI users
- `cloud_agent_dau` – Active Cloud Agent users
- `bugbot_dau` – Active Bugbot users

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/dau?startDate=14d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "date": "2025-01-15",
      "dau": 42,
      "cli_dau": 5,
      "cloud_agent_dau": 37,
      "bugbot_dau": 10
    }
  ]
}
```

**Use Case:** Track adoption over time. See if your team is actually using Cursor.

---

### 4. Client Versions (GET /analytics/team/client-versions)

Get distribution of Cursor client versions used by your team.

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/client-versions?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-01",
      "client_version": "0.42.3",
      "user_count": 35,
      "percentage": 0.833
    },
    {
      "event_date": "2025-01-01",
      "client_version": "0.42.2",
      "user_count": 7,
      "percentage": 0.167
    }
  ]
}
```

**Use Case:** Ensure your team is on the latest version. See who needs to update.

---

### 5. Model Usage (GET /analytics/team/models)

Get metrics on AI model usage across your team.

**Response shows:**
- Which models are being used
- How many messages per model
- How many unique users per model

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/models?startDate=30d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "date": "2025-01-15",
      "model_breakdown": {
        "claude-sonnet-4.5": {
          "messages": 1250,
          "users": 28
        },
        "gpt-4o": {
          "messages": 450,
          "users": 15
        }
      }
    }
  ]
}
```

**Use Case:** Understand which models your team prefers. Track model adoption trends.

---

### 6. Top File Extensions (GET /analytics/team/top-file-extensions)

Get the most frequently edited file extensions across your team.

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/top-file-extensions?startDate=30d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "file_extension": "tsx",
      "total_files": 156,
      "total_accepts": 98,
      "total_lines_accepted": 2340
    },
    {
      "event_date": "2025-01-15",
      "file_extension": "ts",
      "total_files": 142,
      "total_accepts": 89,
      "total_lines_accepted": 2100
    }
  ]
}
```

**Use Case:** Identify which languages/types your team works with most.

---

### 7. MCP Adoption (GET /analytics/team/mcp)

Get metrics on MCP (Model Context Protocol) tool adoption.

**Response shows:**
- Which MCP tools are being used
- Which MCP servers
- Daily usage counts

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/mcp?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "tool_name": "read_file",
      "mcp_server_name": "filesystem",
      "usage": 245
    },
    {
      "event_date": "2025-01-15",
      "tool_name": "search_web",
      "mcp_server_name": "brave-search",
      "usage": 128
    }
  ]
}
```

**Use Case:** Track which external tools your team integrates via MCP.

---

### 8. Commands Adoption (GET /analytics/team/commands)

Get metrics on slash command usage.

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/commands?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "command_name": "explain",
      "usage": 89
    },
    {
      "event_date": "2025-01-15",
      "command_name": "refactor",
      "usage": 45
    }
  ]
}
```

**Use Case:** See which slash commands are most popular. Identify training opportunities.

---

### 9. Plans Adoption (GET /analytics/team/plans)

Get metrics on Plan mode adoption.

**Note:** `"default"` as model name means user has "Auto" model selection enabled.

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/plans?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "model": "claude-sonnet-4.5",
      "usage": 156
    },
    {
      "event_date": "2025-01-15",
      "model": "default",
      "usage": 42
    }
  ]
}
```

**Use Case:** Track how often your team uses Plan mode vs. jumping straight to Agent.

---

### 10. Skills Adoption (GET /analytics/team/skills)

Get metrics on Skills adoption.

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/skills?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "skill_name": "react-best-practices",
      "usage": 53
    },
    {
      "event_date": "2025-01-15",
      "skill_name": "usage-billing",
      "usage": 41
    }
  ]
}
```

**Use Case:** See which skills your team finds most valuable.

---

### 11. Ask Mode Adoption (GET /analytics/team/ask-mode)

Get metrics on Ask mode usage.

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/ask-mode?startDate=7d&endDate=today"
```

**Response Example:**

```json
{
  "data": [
    {
      "event_date": "2025-01-15",
      "model": "claude-sonnet-4.5",
      "usage": 203
    },
    {
      "event_date": "2025-01-15",
      "model": "gpt-4o",
      "usage": 67
    }
  ]
}
```

**Use Case:** Track how often your team uses read-only Ask mode vs. Agent mode.

---

### 12. Conversation Insights (GET /analytics/team/conversation-insights)

**Enterprise only.** Get classified work data – what types of work your team is doing with Cursor.

**Available only if Conversation Insights is enabled.** If disabled, returns `401`.

**Parameters:**
- `include` – Required. Which insights to return: `intents`, `complexity`, `categories`, `guidanceLevels`, `workTypes`

**What each insight means:**

| Insight | What it measures |
|---------|------------------|
| `intents` | What users are trying to do (Write Code, Ask, Plan) |
| `complexity` | How complex the conversations are (high, medium, low) |
| `categories` | Type of work (New Features, Bug Fixing, Refactoring, etc.) |
| `guidanceLevels` | How specific user prompts are |
| `workTypes` | Maintenance vs. Bug Fixing vs. New Features |

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/conversation-insights?startDate=2026-03-01&endDate=2026-03-07&include=intents,complexity,categories" \
```

**Use Case:** Understand what kind of work your team is using AI for. Identify if AI is being used for new features or just debugging.

---

### 13. Leaderboard (GET /analytics/team/leaderboard)

Get a leaderboard of team members ranked by AI usage metrics.

**Rankings:**
- Tab autocomplete (accepts, lines accepted)
- Agent edits (accepts, lines accepted)

**Parameters:**
- `page` – Page number (default: 1)
- `pageSize` – Users per page (default: 10, max: 500)
- `users` – Filter to specific users

**Example Request:**

```bash
# Top 10 users
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/leaderboard?page=1&pageSize=10"
```

**Response Example:**

```json
{
  "data": {
    "tab_leaderboard": {
      "data": [
        {
          "email": "alice@example.com",
          "total_accepts": 1334,
          "total_lines_accepted": 3455,
          "rank": 1
        }
      ],
      "total_users": 142
    },
    "agent_leaderboard": {
      "data": [
        {
          "email": "alice@example.com",
          "total_accepts": 914,
          "total_lines_accepted": 65947,
          "rank": 1
        }
      ],
      "total_users": 142
    }
  },
  "pagination": {
    "page": 1,
    "pageSize": 10,
    "totalUsers": 142,
    "totalPages": 15,
    "hasNextPage": true
  }
}
```

**Use Case:** Recognize power users. Identify who might need more training.

---

### 14. Bugbot Analytics (GET /analytics/team/bugbot)

Get per-PR Bugbot review analytics.

**Parameters:**
- `prState` – `merged` (default) or `all`
- `repo` – Filter by repository
- `page`, `pageSize` – Pagination

**Response shows:**
- Issues found by severity (high, medium, low)
- Issues resolved

**Example Request:**

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/bugbot?startDate=30d&endDate=today&prState=merged"
```

**Response Example:**

```json
{
  "data": [
    {
      "repo": "github.com/acme/app",
      "pr_number": 42,
      "issues": {
        "total": 5,
        "by_severity": {
          "high": 1,
          "medium": 2,
          "low": 2
        }
      },
      "issues_resolved": {
        "total": 2,
        "by_severity": {
          "high": 1,
          "medium": 1,
          "low": 0
        }
      }
    }
  ]
}
```

**Use Case:** Measure Bugbot's effectiveness. Track how many critical issues it catches.

---

## By-User Endpoints

By-user endpoints provide the same metrics as team-level endpoints, but **organized by individual user** with pagination.

### Common Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `page` | 1 | Page number |
| `pageSize` | 100 | Users per page (max 500) |
| `users` | - | Filter to specific users |

### Response Format

```json
{
  "data": {
    "user1@example.com": [ /* user's metrics */ ],
    "user2@example.com": [ /* user's metrics */ ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 100,
    "totalUsers": 250,
    "totalPages": 3,
    "hasNextPage": true
  },
  "params": {
    "metric": "agent-edits",
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### Example: Agent Edits By User

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/by-user/agent-edits?page=1&pageSize=50"
```

**Use Case:** Generate per-user reports. See who the power users are.

---

## Complete Example: Python Script

```python
#!/usr/bin/env python3
"""
Analytics API Examples
"""

import requests
import json
from datetime import datetime, timedelta

API_KEY = "your_api_key_here"
BASE_URL = "https://api.cursor.com"

def get_analytics(endpoint, params=None):
    """Fetch analytics data."""
    url = f"{BASE_URL}{endpoint}"
    auth = (API_KEY, "")
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code == 429:
        print("Rate limit exceeded. Try again later.")
        return None
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    return response.json()

# 1. Get agent edits for last 7 days
agent_edits = get_analytics("/analytics/team/agent-edits")
print("Agent Edits (last 7 days):", json.dumps(agent_edits, indent=2))

# 2. Get daily active users for last 30 days
dau = get_analytics("/analytics/team/dau", {"startDate": "30d", "endDate": "today"})
print("Daily Active Users:", json.dumps(dau, indent=2))

# 3. Get model usage for last 7 days
models = get_analytics("/analytics/team/models")
print("Model Usage:", json.dumps(models, indent=2))

# 4. Get leaderboard (top 20 users)
leaderboard = get_analytics("/analytics/team/leaderboard", {"pageSize": 20})
if leaderboard:
    tab_leaders = leaderboard.get("data", {}).get("tab_leaderboard", {}).get("data", [])
    print("\n🏆 Top Tab Users:")
    for user in tab_leaders[:5]:
        print(f"  {user['email']}: {user['total_accepts']} accepts")

# 5. Get per-user agent edits
user_edits = get_analytics("/analytics/by-user/agent-edits", {"page": 1, "pageSize": 10})
if user_edits:
    print("\n📊 Per-User Agent Edits:")
    for email, data in user_edits.get("data", {}).items():
        total_accepted = sum(day.get("total_accepted_diffs", 0) for day in data)
        print(f"  {email}: {total_accepted} accepted edits")
```

---

## Complete Example: Bash Script

```bash
#!/bin/bash

API_KEY="your_api_key_here"
BASE_URL="https://api.cursor.com"

# Get agent edits
curl -u "$API_KEY:" \
  "$BASE_URL/analytics/team/agent-edits?startDate=7d&endDate=today"

# Get daily active users
curl -u "$API_KEY:" \
  "$BASE_URL/analytics/team/dau?startDate=30d&endDate=today"

# Get model usage
curl -u "$API_KEY:" \
  "$BASE_URL/analytics/team/models?startDate=7d&endDate=today"

# Get leaderboard
curl -u "$API_KEY:" \
  "$BASE_URL/analytics/team/leaderboard?pageSize=20"

# Get per-user agent edits
curl -u "$API_KEY:" \
  "$BASE_URL/analytics/by-user/agent-edits?page=1&pageSize=50"
```

---

## Endpoints Summary

### Team-Level (Aggregated)

| Endpoint | What it measures |
|----------|------------------|
| `/analytics/team/agent-edits` | AI-suggested code acceptance |
| `/analytics/team/tabs` | Tab autocomplete usage |
| `/analytics/team/dau` | Daily active users |
| `/analytics/team/client-versions` | Cursor version distribution |
| `/analytics/team/models` | Model usage |
| `/analytics/team/top-file-extensions` | Most edited file types |
| `/analytics/team/mcp` | MCP tool adoption |
| `/analytics/team/commands` | Slash command usage |
| `/analytics/team/plans` | Plan mode adoption |
| `/analytics/team/skills` | Skills adoption |
| `/analytics/team/ask-mode` | Ask mode adoption |
| `/analytics/team/conversation-insights` | Work classification (Enterprise) |
| `/analytics/team/leaderboard` | User rankings |
| `/analytics/team/bugbot` | Bugbot PR analytics |

### By-User (Per-User)

| Endpoint | Pattern |
|----------|---------|
| Agent edits | `/analytics/by-user/agent-edits` |
| Tab usage | `/analytics/by-user/tabs` |
| Model usage | `/analytics/by-user/models` |
| Top files | `/analytics/by-user/top-file-extensions` |
| Client versions | `/analytics/by-user/client-versions` |
| MCP | `/analytics/by-user/mcp` |
| Commands | `/analytics/by-user/commands` |
| Plans | `/analytics/by-user/plans` |
| Skills | `/analytics/by-user/skills` |
| Ask mode | `/analytics/by-user/ask-mode` |

---

## Best Practices

| Practice | Why |
|----------|-----|
| **Use YYYY-MM-DD date format** | Better HTTP caching |
| **Keep date ranges ≤30 days** | API limitation |
| **Use pagination for large teams** | Avoid timeouts |
| **Filter by users when possible** | Reduce query time |
| **Use by-user endpoints for per-user data** | Pagination built-in |

---

## Common Beginner Questions

### Q: What's the difference between team-level and by-user endpoints?
**A:** Team-level returns aggregated totals. By-user returns per-user breakdowns with pagination.

### Q: How far back can I query?
**A:** Maximum 30 days per request. Use multiple requests for longer periods.

### Q: Why use YYYY-MM-DD instead of timestamps?
**A:** YYYY-MM-DD caches better. Timestamps with times prevent cache hits.

### Q: Can I filter by specific users?
**A:** Yes – use the `users` parameter with emails or user IDs.

### Q: What does `"default"` mean in model usage?
**A:** User has "Auto" model selection enabled.

### Q: How do I handle rate limits?
**A:** Implement exponential backoff when you receive 429 responses.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Base URL** | `https://api.cursor.com/analytics/` |
| **Authentication** | Basic Auth with admin-scoped API key |
| **Availability** | Enterprise teams only |
| **Rate limits** | 100/min (team), 50/min (by-user) |
| **Date range max** | 30 days |
| **Default date range** | Last 7 days |
| **Pagination max** | 500 per page (by-user) |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is the Analytics API?** | Programmatic access to team usage metrics |
| **Who can use it?** | Enterprise teams only |
| **What can I track?** | Agent edits, model usage, active users, feature adoption, user rankings |
| **How far back?** | Up to 30 days per request |
| **Rate limits?** | 100 requests/minute (team), 50 (by-user) |

---

## The Bottom Line

**The Analytics API lets you programmatically track how your team uses Cursor – from AI adoption to model usage to per-user metrics.**

**Think of it as:**
- **Dashboard** = Manual, visual analytics 📊
- **Analytics API** = Programmatic, scriptable analytics 💻

**Use cases for enterprise teams:**
- Automating usage reports
- Building custom dashboards
- Tracking adoption trends
- Identifying power users
- Measuring Bugbot effectiveness

**Key rules to remember:**
- **Use YYYY-MM-DD date format** for better caching
- **Maximum 30-day date range** per request
- **Implement exponential backoff** for rate limits
- **Use by-user endpoints** for per-user data
