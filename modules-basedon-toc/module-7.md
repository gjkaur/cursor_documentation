# Module 7: Cursor API Foundations

## Cursor Training Program — Day 2

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Concept + hands-on exercise |
| **Prerequisites** | Admin API key generated (or User API key for Cloud Agents API), `curl` and `jq` installed |
| **Module Goal** | Understand the Cursor API landscape, authentication, rate limits, error handling, and caching |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Describe the five Cursor APIs and when to use each
- Generate and test API keys for different use cases
- Handle rate limits with exponential backoff
- Use ETag caching to reduce bandwidth and rate limit usage
- List available models as a simple authentication smoke-test

---

## Lesson 7.1: The Cursor API Landscape

### Concept (10 minutes)

> *"Cursor provides five APIs for programmatic access to your team's data, AI-powered coding agents, and analytics."*

**API Overview:**

| API | What It Does | Best For | Availability |
|-----|--------------|----------|--------------|
| **Cloud Agents API** | Create and manage AI coding agents | Automation, CI/CD integration | Beta (All plans) |
| **Admin API** | Manage team members, usage, spending | Team administration, HR integration | Enterprise |
| **Analytics API** | Track usage, model adoption, active users | Dashboards, usage reports | Enterprise |
| **AI Code Tracking API** | Track AI-generated code in commits | Attribution, compliance | Enterprise |
| **TypeScript SDK** | Run agents from TypeScript code | Custom integrations | Beta |

**API Selection Decision Tree:**

```
START: What do you want to do?

Launch AI agents programmatically?
├─ YES → Cloud Agents API or TypeScript SDK
└─ NO → Continue

Manage team members, set spending limits?
├─ YES → Admin API (Enterprise)
└─ NO → Continue

Track usage, model adoption, user activity?
├─ YES → Analytics API (Enterprise)
└─ NO → Continue

See how much AI code is being committed?
├─ YES → AI Code Tracking API (Enterprise)
└─ NO → Continue

Need both cloud and local agent control in TypeScript?
├─ YES → TypeScript SDK
└─ NO → REST API might be simpler
```

### Discussion (5 minutes)

**Question:** Which APIs are most relevant to your team's needs?

| Team Type | Likely APIs |
|-----------|-------------|
| Individual developer | Cloud Agents API |
| Platform/DevOps | Cloud Agents API, Admin API |
| Engineering leadership | Analytics API, AI Code Tracking API |
| Security/Compliance | Admin API, AI Code Tracking API |

---

## Lesson 7.2: Authentication

### Concept (5 minutes)

> *"All Cursor APIs use Basic Authentication with an API key as the username (password empty)."*

**Authentication Methods:**

```bash
# Method 1: Basic Auth with curl
curl -u YOUR_API_KEY: https://api.cursor.com/v1/me

# Method 2: Bearer token
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.cursor.com/v1/me
```

**Where to Generate API Keys:**

| API Key Type | Where to Generate | Scope |
|--------------|-------------------|-------|
| **Admin API key** | Dashboard → Settings → Advanced → Admin API Keys | `admin:*` (Enterprise) |
| **User API key** | Dashboard → Integrations | User-scoped (Cloud Agents API) |
| **Service account key** | Dashboard → Settings → Service Accounts | Team-scoped (Enterprise) |

**Key Format:** Admin API keys start with `crsr_` (very long). User API keys start with `cursor_user_`.

**Important Notes:**
- API keys are tied to your organization
- Viewable by all admins
- Unaffected by the original creator's account status
- Never commit API keys to version control

### Hands-On Exercise (5 minutes)

**Step 1:** Generate an Admin API key (if you have Enterprise) or User API key

**Step 2:** Set the key as an environment variable:

```bash
export CURSOR_API_KEY="your_key_here"
```

**Step 3:** Test authentication:

```bash
curl -u "$CURSOR_API_KEY:" https://api.cursor.com/v1/me | jq '.'
```

**Expected response:**
```json
{
  "apiKeyName": "Training Key",
  "createdAt": "2025-01-15T10:30:00.000Z",
  "userEmail": "your-email@company.com"
}
```

**Step 4:** Test with Bearer token:

```bash
curl -H "Authorization: Bearer $CURSOR_API_KEY" https://api.cursor.com/v1/me | jq '.'
```

**Success Criteria:**
- [ ] API key generated
- [ ] Authentication returned user info
- [ ] Both Basic Auth and Bearer token work

---

## Lesson 7.3: Rate Limits and Error Handling

### Concept (10 minutes)

> *"Rate limits prevent any single user from overwhelming the API. Different APIs have different limits."*

**Rate Limits by API:**

| API | Endpoint Type | Rate Limit |
|-----|---------------|------------|
| Admin API | Most endpoints | 20 requests/minute |
| Admin API | `/teams/user-spend-limit` | 250 requests/minute |
| Analytics API | Team-level endpoints | 100 requests/minute |
| Analytics API | By-user endpoints | 50 requests/minute |
| AI Code Tracking API | All endpoints | 20 requests/minute |
| Cloud Agents API | All endpoints | Standard rate limiting |

**What Happens When Exceeded:**

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

**Error Response Codes:**

| Status | Meaning | Retryable? |
|--------|---------|------------|
| 400 | Bad Request | ❌ No – fix parameters |
| 401 | Unauthorized | ❌ No – check API key |
| 403 | Forbidden | ❌ No – check permissions/plan |
| 404 | Not Found | ❌ No – fix URL |
| 429 | Rate Limited | ✅ Yes – exponential backoff |
| 500+ | Server Error | ✅ Yes – retry with backoff |

### Exponential Backoff Pattern

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

### Hands-On Exercise (10 minutes)

**Step 1:** Make a valid request:

```bash
curl -s -u "$CURSOR_API_KEY:" \
  "https://api.cursor.com/teams/members" | jq '.'
```

**Step 2:** Make requests until rate limited (if you have Admin API):

```bash
for i in {1..25}; do
  echo "Request $i:"
  curl -s -u "$CURSOR_API_KEY:" \
    "https://api.cursor.com/teams/members" \
    -w "\nHTTP Status: %{http_code}\n"
  echo "---"
done
```

**Step 3:** Observe the 429 response when limit is exceeded

**Step 4:** Create a Python script with exponential backoff:

```python
#!/usr/bin/env python3
import requests
import time
import os

API_KEY = os.environ.get("CURSOR_API_KEY")

def call_api(endpoint):
    url = f"https://api.cursor.com{endpoint}"
    auth = (API_KEY, "")
    
    for attempt in range(5):
        response = requests.get(url, auth=auth)
        
        if response.status_code == 429:
            wait_time = 2 ** attempt
            print(f"Rate limited. Waiting {wait_time}s...")
            time.sleep(wait_time)
            continue
        
        return response
    
    return None

# Test with a valid endpoint
result = call_api("/v1/models")
if result:
    print(f"Status: {result.status_code}")
    print(result.json())
```

**Success Criteria:**
- [ ] Triggered rate limit (optional)
- [ ] Understood exponential backoff
- [ ] Created error handling script

---

## Lesson 7.4: ETag Caching

### Concept (5 minutes)

> *"ETag caching lets you check if data has changed before downloading it. 304 responses have no body and don't count against rate limits."*

**How ETag Caching Works:**

| Step | What Happens |
|------|--------------|
| 1 | Initial request – API returns `ETag` header |
| 2 | Store the ETag value |
| 3 | Next request – include `If-None-Match` header with ETag |
| 4 | If data unchanged – API returns `304 Not Modified` (no body) |

**Which APIs Support Caching:**

| API | Caching Support | Cache Duration |
|-----|-----------------|----------------|
| Analytics API | ✅ Yes | 15 minutes |
| AI Code Tracking API | ✅ Yes | 15 minutes |
| Admin API | ❌ No | N/A |
| Cloud Agents API | ❌ No | N/A |

**Benefits of Caching:**
- Reduces bandwidth usage (304 responses have no body)
- Faster responses when data hasn't changed
- **304 responses don't count against rate limits!**

### Hands-On Exercise (5 minutes)

**Step 1:** Make initial request and capture ETag:

```bash
curl -s -u "$CURSOR_API_KEY:" \
  -D headers.txt \
  "https://api.cursor.com/analytics/team/dau?startDate=7d&endDate=today"

ETAG=$(grep -i "etag" headers.txt | awk '{print $2}' | tr -d '\r')
echo "ETag: $ETAG"
```

**Step 2:** Make conditional request:

```bash
curl -s -u "$CURSOR_API_KEY:" \
  -H "If-None-Match: $ETAG" \
  -w "\nHTTP Status: %{http_code}\n" \
  "https://api.cursor.com/analytics/team/dau?startDate=7d&endDate=today"
```

**Expected output:** `HTTP Status: 304` (if data unchanged)

**Success Criteria:**
- [ ] Captured ETag from initial response
- [ ] Made conditional request
- [ ] Received 304 response

---

## Lesson 7.5: Listing Available Models

### Concept (5 minutes)

> *"The `/v1/models` endpoint returns all available AI models. It's also a great way to test authentication."*

### Hands-On Exercise (5 minutes)

**Step 1:** List all models:

```bash
curl -s -u "$CURSOR_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq '.'
```

**Expected response:**
```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2",
    "gpt-5-mini",
    "claude-4.5-haiku",
    "gpt-5.3-codex",
    "claude-4.7-opus",
    "gemini-3.1-pro",
    "grok-4.3"
  ]
}
```

**Step 2:** Count the models:

```bash
curl -s -u "$CURSOR_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq '.items | length'
```

**Step 3:** Filter by provider:

```bash
# Find all Claude models
curl -s -u "$CURSOR_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq -r '.items[] | select(contains("claude"))'
```

**Success Criteria:**
- [ ] Retrieved models list
- [ ] Counted total number of models
- [ ] Filtered by provider

---

## Module Summary

| Lesson | Key Skill | Time |
|--------|-----------|------|
| 7.1 | API Landscape | 10 min |
| 7.2 | Authentication | 10 min |
| 7.3 | Rate Limits and Error Handling | 10 min |
| 7.4 | ETag Caching | 10 min |
| 7.5 | Listing Models | 5 min |

---

## Quick Reference Card

| API | Base URL | Auth | Rate Limit |
|-----|----------|------|------------|
| Cloud Agents | `https://api.cursor.com/v1/` | User/Service | Standard |
| Admin | `https://api.cursor.com/` | Admin (Enterprise) | 20/min |
| Analytics | `https://api.cursor.com/analytics/` | Admin (Enterprise) | 100/min |
| AI Code Tracking | `https://api.cursor.com/analytics/ai-code/` | Admin (Enterprise) | 20/min |

| Common Error | Meaning | Action |
|--------------|---------|--------|
| 401 | Invalid API key | Check key |
| 403 | Enterprise required | Upgrade plan |
| 429 | Rate limited | Exponential backoff |

---

## Transition to Module 8

> *"Now that you understand API fundamentals, let's put them into practice with the Cloud Agents API and Webhooks."*

---

*End of Module 7*