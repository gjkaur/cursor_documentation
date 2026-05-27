# Cursor APIs Overview – Complete Beginner's Guide

This document provides a comprehensive overview of all Cursor APIs – what they do, which one to use, how to authenticate, rate limits, caching, and best practices.

Think of this as the **"API Map"** – showing you which API to use for each task and how to use them effectively.

Let me break this down for a complete beginner.

---

## What Are Cursor APIs? (The 10-Second Summary)

**Cursor provides multiple APIs that let you programmatically access your team's data, control AI coding agents, and track analytics.**

| Without APIs | With APIs |
|--------------|-----------|
| Manual dashboard clicks | Automated data collection |
| One-off reports | Scheduled, repeatable analytics |
| No programmatic control | Full automation capabilities |

---

## Available APIs at a Glance

| API | What It Does | Best For | Availability |
|-----|--------------|----------|--------------|
| **Admin API** | Manage team members, settings, usage, spending | Team administration, HR integration | Enterprise |
| **Analytics API** | Track usage metrics, model adoption, active users | Dashboards, usage reports | Enterprise |
| **AI Code Tracking API** | Track AI-generated code in commits | Attribution, compliance | Enterprise |
| **Cloud Agents API** | Create and manage AI coding agents | Automation, CI/CD integration | Beta (All Plans) |
| **TypeScript SDK** | Run agents from TypeScript code | Custom integrations | Beta |

---

## API Selection Decision Tree

```
START: What do you want to do?

Manage team members, set spending limits, control access?
├─ YES → Admin API
└─ NO → Continue

Track usage, model adoption, user activity?
├─ YES → Analytics API
└─ NO → Continue

See how much AI code is being committed?
├─ YES → AI Code Tracking API
└─ NO → Continue

Launch and monitor AI coding agents programmatically?
├─ YES → Cloud Agents API or TypeScript SDK
└─ NO → Continue

Need both cloud and local agent control in TypeScript?
├─ YES → TypeScript SDK
└─ NO → REST API might be simpler
```

---

## 1. Admin API

### What It Does

The **Admin API** lets you programmatically manage your Cursor team – members, settings, usage data, and spending.

| Capability | Example |
|------------|---------|
| **Team management** | Add/remove members, change roles |
| **Usage data** | Get daily usage metrics for all users |
| **Spending controls** | Set individual user spend limits |
| **Audit logs** | Track security events (Enterprise) |
| **Billing groups** | Organize users for cost allocation (Enterprise) |

### Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/teams/daily-usage-data` | POST | Get daily usage metrics |
| `/teams/user-spend-limit` | POST | Set user spending limit |
| `/teams/remove-member` | POST | Remove team member |
| `/teams/groups` | GET | List billing groups |
| `/audit-logs/search` | POST | Search audit events |

### Example Usage

```bash
# Get usage data for last 7 days
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_ADMIN_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{"startDate": "7d", "endDate": "now"}'
```

### Availability

**Enterprise only**

### Rate Limits

| Endpoint Type | Limit |
|---------------|-------|
| Most endpoints | 20 requests/minute |
| `/teams/user-spend-limit` | 250 requests/minute |
| `/teams/remove-member` | 50 requests/minute |

---

## 2. Analytics API

### What It Does

The **Analytics API** provides comprehensive insights into your team's Cursor usage – who's using what models, how much, and adoption trends.

| Capability | Example |
|------------|---------|
| **Model usage** | Which models are most popular |
| **Feature adoption** | Ask mode, Plan mode, Skills, MCP usage |
| **User leaderboard** | Top users by activity |
| **Team metrics** | Daily active users, message counts |

### Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/analytics/team/models` | GET | Model usage across team |
| `/analytics/team/agent-edits` | GET | Agent edit metrics |
| `/analytics/team/leaderboard` | GET | User rankings |
| `/analytics/by-user/tabs` | GET | Tab usage per user |
| `/analytics/team/bugbot` | GET | Bugbot analytics |

### Example Usage

```bash
# Get model usage for last 30 days
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/team/models?startDate=30d&endDate=today"
```

### Date Format Best Practices

| Format | Example | Caching |
|--------|---------|---------|
| Recommended | `2025-01-15` | Excellent |
| Shortcuts | `7d`, `30d`, `today` | Good |
| Avoid | `2025-01-15T14:30:00Z` | Poor (prevents caching) |

### Availability

**Enterprise only**

### Rate Limits

| Endpoint Type | Limit |
|---------------|-------|
| Team-level endpoints | 100 requests/minute |
| By-user endpoints | 50 requests/minute |
| `/analytics/team/conversation-insights` | 20 requests/minute |

---

## 3. AI Code Tracking API

### What It Does

The **AI Code Tracking API** lets you see exactly how much AI-generated code is being committed to your repositories – line by line, commit by commit.

| Capability | Example |
|------------|---------|
| **Commit attribution** | See AI vs human lines per commit |
| **Source tracking** | Tab completions vs Agent edits |
| **Repository breakdown** | AI usage by repo |
| **CSV export** | Large data extraction |

### How It Works

1. Cursor records signatures of AI-suggested lines (on-device)
2. When user commits, signatures are compared
3. Lines are attributed to Tab, Agent, or Human
4. Only line counts (metadata) are stored – not your code

### Key Endpoints

| Endpoint | Method | Format | Purpose |
|----------|--------|--------|---------|
| `/analytics/ai-code/commits` | GET | JSON | Commit metrics with pagination |
| `/analytics/ai-code/commits.csv` | GET | CSV | Large data export (streaming) |
| `/analytics/ai-code/changes` | GET | JSON | Granular AI change events |
| `/analytics/ai-code/commits/:hash` | GET | JSON | Detailed commit info (alpha) |

### Example Usage

```bash
# Get AI commit metrics for last 7 days
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now"

# Download CSV for last 90 days
curl -L -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=90d&endDate=now" \
  -o ai_commits_90d.csv
```

### Understanding the Data

```
totalLinesAdded = tabLinesAdded + composerLinesAdded + nonAiLinesAdded
```

| Source | Description |
|--------|-------------|
| `TAB` | Inline completions accepted by user |
| `COMPOSER` | Agent edits accepted by user |
| `ide` | Commit from Cursor IDE |
| `cli` | Commit from Cursor CLI |
| `cloud` | Commit from Cloud Agent |

### Availability

**Enterprise only**

### Rate Limits

| Endpoint Type | Limit |
|---------------|-------|
| All endpoints | 20 requests/minute per endpoint |

---

## 4. Cloud Agents API

### What It Does

The **Cloud Agents API** lets you programmatically create and manage AI-powered coding agents – perfect for automation and CI/CD integration.

| Capability | Example |
|------------|---------|
| **Create agents** | Launch agents from scripts |
| **Stream responses** | Real-time agent output |
| **Download artifacts** | Get screenshots, logs, generated files |
| **Manage lifecycle** | Archive, unarchive, delete agents |

### Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/agents` | POST | Create agent and start run |
| `/v1/agents/{id}/runs/{runId}/stream` | GET | Stream SSE events |
| `/v1/agents/{id}/artifacts` | GET | List artifacts |
| `/v1/agents/{id}/artifacts/download` | GET | Download artifact |
| `/v1/agents/{id}/archive` | POST | Soft delete agent |

### Example Usage

```bash
# Create an agent
curl -X POST https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a README.md file"},
    "repos": [{"url": "https://github.com/your-org/your-repo"}],
    "autoCreatePR": true
  }'
```

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | Durable entity with conversation history |
| **Run** | Single execution (one prompt) |
| **Artifact** | Files produced by agent (screenshots, logs) |

### Availability

**Beta – All plans**

### Status

> *"Public beta – APIs may change before general availability."*

---

## 5. TypeScript SDK

### What It Does

The **TypeScript SDK** lets you run Cursor agents directly from your TypeScript/JavaScript code – with one interface for both local and cloud runtimes.

| Capability | Example |
|------------|---------|
| **Local agents** | Run on your machine |
| **Cloud agents** | Run in Cursor's cloud |
| **Streaming** | Real-time responses |
| **Type safety** | Full TypeScript support |

### Installation

```bash
npm install @cursor/sdk
```

### Example Usage

```typescript
import { Agent } from "@cursor/sdk";

// One-shot prompt
const result = await Agent.prompt(
  "What does this code do?",
  {
    apiKey: process.env.CURSOR_API_KEY,
    model: { id: "composer-2.5" },
    local: { cwd: process.cwd() }
  }
);

console.log(result.result);
```

### Runtimes

| Runtime | When to Use |
|---------|-------------|
| **Local** | Dev scripts, CI checks against working tree |
| **Cloud (Cursor-hosted)** | Caller doesn't have repo, need parallel agents |
| **Cloud (self-hosted)** | Code must stay in your environment |

### Availability

**Beta – All plans**

---

## Authentication (For All APIs)

### How to Authenticate

All Cursor APIs use **Basic Authentication** with an API key.

```bash
# Method 1: Basic Auth with curl
curl -u YOUR_API_KEY: https://api.cursor.com/endpoint

# Method 2: Bearer token
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.cursor.com/endpoint
```

**Note:** The colon after the API key is required (empty password).

### Where to Get API Keys

| API | Where to Generate |
|-----|-------------------|
| **Admin API** | Dashboard → Settings → Advanced → Admin API Keys |
| **Analytics API** | Team settings page |
| **AI Code Tracking API** | Same as Admin API |
| **Cloud Agents API** | Dashboard → Integrations (user key) or Team settings (service account) |

### API Key Format

Admin API keys start with: `crsr_xxxxxxxx...` (very long)

### Required Scope

Most APIs require `admin:*` scope for full access.

### Important Notes

- API keys are **tied to your organization**
- **Viewable by all admins**
- **Unaffected** by the original creator's account status

---

## Rate Limits (Important!)

Rate limits are enforced **per team** and reset **every minute**.

### Rate Limits by API

| API | Endpoint Type | Limit |
|-----|---------------|-------|
| **Admin API** | Most endpoints | 20/min |
| **Admin API** | `/teams/user-spend-limit` | 250/min |
| **Analytics API** | Team-level endpoints | 100/min |
| **Analytics API** | `/analytics/team/conversation-insights` | 20/min |
| **Analytics API** | By-user endpoints | 50/min |
| **AI Code Tracking API** | All endpoints | 20/min per endpoint |
| **Cloud Agents API** | All endpoints | Standard rate limiting |

### What Happens When Exceeded?

You receive a `429 Too Many Requests` response:

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

### How to Handle Rate Limits (Exponential Backoff)

```python
import time
import requests

def make_request_with_backoff(url, headers, max_retries=5):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 429:
            wait_time = 2 ** attempt  # 1s, 2s, 4s, 8s, 16s
            print(f"Rate limited. Waiting {wait_time}s...")
            time.sleep(wait_time)
            continue
        
        return response
    
    raise Exception("Max retries exceeded")
```

---

## Caching (Reduces Bandwidth & Rate Limits)

### Which APIs Support Caching

| API | Caching Support |
|-----|-----------------|
| **Analytics API** | Yes (all endpoints) |
| **AI Code Tracking API** | Yes |
| **Admin API** | No |
| **Cloud Agents API** | No |

### How Caching Works

| Step | What Happens |
|------|--------------|
| 1 | Make initial request – API returns `ETag` header |
| 2 | Store the ETag value |
| 3 | Next request – include `If-None-Match` header with ETag |
| 4 | If data unchanged – API returns `304 Not Modified` (no data) |

### Example

```bash
# Initial request – get ETag
curl -X GET "https://api.cursor.com/analytics/team/dau" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -D headers.txt

# Response includes: ETag: "abc123xyz"

# Subsequent request – send ETag back
curl -X GET "https://api.cursor.com/analytics/team/dau" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "If-None-Match: \"abc123xyz\""

# Returns 304 Not Modified (no body) if data hasn't changed
```

### Cache Duration

| Setting | Value |
|---------|-------|
| **Duration** | 15 minutes |
| **Cache-Control** | `public, max-age=900` |
| **304 responses** | Do NOT count against rate limits |

### Benefits of Caching

| Benefit | Why It Matters |
|---------|----------------|
| **Reduces bandwidth** | 304 responses have no body |
| **Faster responses** | Avoids processing unchanged data |
| **Rate limit friendly** | 304 responses don't count against limits |

---

## Best Practices Summary

| Practice | Why |
|----------|-----|
| **Use exponential backoff** | Handle rate limits gracefully |
| **Distribute requests over time** | Avoid burst traffic |
| **Leverage ETag caching** | Reduce bandwidth and rate limit usage |
| **Use date shortcuts (`7d`, `30d`)** | Better caching for Analytics API |
| **Poll at appropriate intervals** | Don't over-poll hourly data |
| **Handle errors gracefully** | Check for 401, 403, 429, 500 |
| **Use CSV endpoints for large exports** | Streams data efficiently |

---

## Common Error Responses

| Status Code | Meaning | What to Do |
|-------------|---------|------------|
| **400** | Bad Request | Check your parameters |
| **401** | Unauthorized | Check API key |
| **403** | Forbidden | Need Enterprise plan or higher permissions |
| **404** | Not Found | Check endpoint URL and IDs |
| **429** | Rate Limit | Implement exponential backoff |
| **500** | Server Error | Try again later; contact support if persistent |

---

## Quick Reference Card

| API | Best For | Auth | Rate Limit | Caching | Enterprise |
|-----|----------|------|------------|---------|-------------|
| **Admin** | Team management | Admin API key | 20-250/min | No | Yes |
| **Analytics** | Usage insights | API key | 20-100/min | Yes | Yes |
| **AI Code Tracking** | Code attribution | Admin API key | 20/min | Yes | Yes |
| **Cloud Agents** | Agent automation | User/Service account | Standard | No | No |
| **TypeScript SDK** | Custom integrations | API key | Same as Cloud | No | No |

---

## Common Beginner Questions

### Q: Which API should I use first?
**A:** Start with the **Cloud Agents API** (available on all plans, in beta) to understand the basics. Then move to Analytics or Admin APIs (Enterprise).

### Q: Do I need an Enterprise plan for all APIs?
**A:** Admin API, Analytics API, and AI Code Tracking API require Enterprise. Cloud Agents API and TypeScript SDK work on all plans.

### Q: How do I get an API key?
**A:** Dashboard → Settings → API Keys (location varies by API type)

### Q: What's the difference between user API key and service account?
**A:** User keys are tied to your personal account. Service accounts are non-human accounts for automation (Enterprise).

### Q: Why am I getting 403 Forbidden?
**A:** You're trying to access an Enterprise-only feature on a non-Enterprise plan.

### Q: How can I avoid rate limits?
**A:** Use caching (ETags), exponential backoff, and spread requests over time.

### Q: Can I use these APIs from Python?
**A:** Yes – all APIs use standard HTTP, so you can use `requests`, `httpx`, or any HTTP client.

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Cursor APIs?** | Programmatic access to Cursor features |
| **How many APIs are there?** | 5 (Admin, Analytics, AI Code Tracking, Cloud Agents, TypeScript SDK) |
| **Which one do I need?** | See decision tree above |
| **How do I authenticate?** | Basic Auth with API key |
| **What are rate limits?** | Limits on requests per minute |
| **What is caching?** | ETags – 304 responses don't count against limits |
| **Do I need Enterprise?** | For Admin, Analytics, AI Code Tracking – yes |

---

## The Bottom Line

**Cursor's APIs give you programmatic control over team management, analytics, AI code tracking, and agent automation.**

**Think of it as:**
- **Dashboard** = Manual, click-based interface
- **APIs** = Programmatic, scriptable interface

**For beginners:** Start with the **Cloud Agents API** (available on all plans). Learn to create an agent, stream responses, and download artifacts. Then explore Analytics or Admin APIs as needed (Enterprise).

**Key rules to remember:**
1. **Respect rate limits** – implement exponential backoff
2. **Use caching** (ETags) for Analytics and AI Code Tracking
3. **Store API keys securely** – never commit them to code
4. **Check error responses** – they tell you what's wrong
5. **Use YYYY-MM-DD date format** for better caching
