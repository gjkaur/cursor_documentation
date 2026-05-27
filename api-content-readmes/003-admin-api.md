# Admin API – Complete Beginner's Guide

This document explains the **Admin API** in detail – how to programmatically manage your Cursor team, access usage data, control spending, and administer users.

Think of this as the **API version of the team dashboard** for administrators.

Let me break this down for a complete beginner.

---

## What Is the Admin API? (The 10-Second Summary)

**The Admin API lets you programmatically manage your Cursor team** – access member information, usage metrics, spending details, and more.

| Without Admin API | With Admin API |
|-------------------|----------------|
| Click through dashboard manually | Automate team management |
| Manual reporting | Programmatic data extraction |
| One-off user changes | Bulk and automated user management |

> *"The Admin API uses Basic Authentication with your API key as the username."*

**Important:** Most Admin API endpoints require an **Enterprise plan**.

---

## Authentication

All Admin API requests use **Basic Authentication** with an **Admin API Key**.

```bash
curl -X GET https://api.cursor.com/teams/members \
  -u YOUR_ADMIN_API_KEY:
```

**Note:** The colon after the API key is required (empty password).

### Where to Get an Admin API Key:

1. Log into Cursor Dashboard
2. Go to **Settings → Advanced → Admin API Keys**
3. Click **Create New API Key**
4. Give it a descriptive name (e.g., "Usage Dashboard")
5. Copy the key immediately (it won't be shown again)

**Key format:** `crsr_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

## Available Endpoints Overview

| Category | Endpoint | Method | What it does |
|----------|----------|--------|--------------|
| **Team Management** | `/teams/members` | GET | List all team members |
| **Audit Logs** | `/teams/audit-logs` | GET | Track security events |
| **Usage Data** | `/teams/daily-usage-data` | POST | Daily usage metrics |
| **Spending** | `/teams/spend` | POST | Spending by user |
| **Usage Events** | `/teams/filtered-usage-events` | POST | Detailed API call logs |
| **User Limits** | `/teams/user-spend-limit` | POST | Set user spending limits |
| **User Removal** | `/teams/remove-member` | POST | Remove team members |
| **Repo Blocklists** | `/settings/repo-blocklists/repos` | GET | List blocked repos |
| **Repo Blocklists** | `/settings/repo-blocklists/repos/upsert` | POST | Add/update blocklists |
| **Repo Blocklists** | `/settings/repo-blocklists/repos/:repoId` | DELETE | Remove from blocklist |
| **Billing Groups** | `/teams/groups` | GET | List billing groups |
| **Billing Groups** | `/teams/groups` | POST | Create group |
| **Billing Groups** | `/teams/groups/:groupId` | GET | Get group details |
| **Billing Groups** | `/teams/groups/:groupId` | PATCH | Update group |
| **Billing Groups** | `/teams/groups/:groupId` | DELETE | Delete group |
| **Billing Groups** | `/teams/groups/:groupId/members` | POST | Add members to group |
| **Billing Groups** | `/teams/groups/:groupId/members` | DELETE | Remove members from group |

---

## 1. Get Team Members (GET /teams/members)

Retrieve all team members and their details.

### Example Request

```bash
curl -X GET https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | number | Unique identifier for the team member |
| `email` | string | Email address of the team member |
| `name` | string | Display name of the team member |
| `role` | string | Role in the team (`member` or `owner`) |
| `isRemoved` | boolean | Whether the member has been removed |

### Response Example

```json
{
  "teamMembers": [
    {
      "id": 12345,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "isRemoved": false
    },
    {
      "id": 12346,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "isRemoved": false
    }
  ]
}
```

### Use Cases

- Sync team roster with your HR system
- Build a custom team directory
- Audit who has access to Cursor

---

## 2. Get Audit Logs (GET /teams/audit-logs)

Retrieve audit log events for your team – track team activity, security events, and configuration changes.

**Rate limit:** 20 requests per minute per team

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startTime` | string/number | 7 days ago | Start time (see Date Formats) |
| `endTime` | string/number | now | End time (see Date Formats) |
| `eventTypes` | string | - | Comma-separated event types to filter |
| `search` | string | - | Search term to filter events |
| `page` | number | 1 | Page number (1-indexed) |
| `pageSize` | number | 100 | Results per page (1-500) |
| `users` | string | - | Filter by users (comma-separated emails or IDs) |

### Event Types

| Category | Event Types |
|----------|-------------|
| **Authentication** | `login`, `logout` |
| **User Management** | `add_user`, `remove_user`, `update_user_role` |
| **API Keys** | `team_api_key`, `user_api_key` |
| **Settings** | `team_settings`, `privacy_mode` |
| **Spending** | `user_spend_limit` |
| **Rules** | `team_rule`, `team_repo`, `team_hook`, `team_command` |
| **Directory Groups** | `create_directory_group`, `delete_directory_group`, `update_directory_group`, `add_user_to_directory_group`, `remove_user_from_directory_group` |
| **Bugbot** | `bugbot_installation`, `bugbot_repo_settings`, `bugbot_team_rule`, `bugbot_team_settings` |

### Date Formats

| Format | Example |
|--------|---------|
| Relative shortcuts | `7d`, `5h`, `300s`, `today`, `yesterday` |
| ISO 8601 | `2024-01-15T12:00:00Z` |
| YYYY-MM-DD | `2024-01-15` |
| Unix timestamps | `1705315200` (seconds) or `1705315200000` (milliseconds) |

### Example Request

```bash
curl -X GET "https://api.cursor.com/teams/audit-logs?users=admin@company.com&eventTypes=login,add_user&startTime=7d&endTime=now" \
  -u YOUR_API_KEY:
```

### Response Example

```json
{
  "events": [
    {
      "event_id": "evt_abc123",
      "timestamp": "2024-01-15T12:30:00.000Z",
      "ip_address": "203.0.113.42",
      "user_email": "admin@company.com",
      "event_type": "add_user",
      "event_data": {
        "email": "newuser@company.com",
        "method": "manual"
      }
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 100,
    "totalCount": 2,
    "totalPages": 1,
    "hasNextPage": false,
    "hasPreviousPage": false
  }
}
```

### Use Cases

- Security compliance auditing
- Investigate who changed team settings
- Track user onboarding/offboarding

---

## 3. Get Daily Usage Data (POST /teams/daily-usage-data)

Retrieve daily usage metrics for your team. Data is aggregated at the hourly level.

> *"We recommend polling this endpoint at most once per hour."*

**Rate limit:** 20 requests per minute per team

### Important: Active Users vs. All Members

| Without Pagination | With Pagination |
|--------------------|-----------------|
| Returns **active users only** (those with activity) | Returns **all team members** |
| Faster response | Includes inactive users (isActive: false) |

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `startDate` | number | ✅ | Start date in epoch milliseconds |
| `endDate` | number | ✅ | End date in epoch milliseconds |
| `page` | number | ❌ | Page number (enables pagination) |
| `pageSize` | number | ❌ | Number of users per page |

### Response Fields

| Field | Description |
|-------|-------------|
| `userId` | Unique identifier for the user |
| `day` | Date (ISO format, e.g., `2024-03-18`) |
| `email` | User's email address |
| `isActive` | Whether user had activity (pagination only) |
| `totalLinesAdded` | Total lines of code added |
| `totalLinesDeleted` | Total lines of code deleted |
| `acceptedLinesAdded` | AI-suggested lines accepted |
| `totalTabsShown` | Tab completions shown |
| `totalTabsAccepted` | Tab completions accepted |
| `composerRequests` | Number of Composer requests |
| `chatRequests` | Number of chat requests |
| `agentRequests` | Number of Agent mode requests |
| `bugbotUsages` | Number of Bugbot usages |
| `mostUsedModel` | Most frequently used AI model |
| `clientVersion` | Cursor client version used |

### Example: Active Users Only

```bash
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

### Example: All Members (with Pagination)

```bash
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000,
    "page": 1,
    "pageSize": 1000
  }'
```

### Response Example (Active Users)

```json
{
  "data": [
    {
      "userId": 12345,
      "day": "2024-03-18",
      "email": "developer@company.com",
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-5",
      "clientVersion": "0.25.1"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

### Use Cases

- Measure team productivity
- Track AI adoption over time
- Identify power users
- Generate usage reports for leadership

---

## 4. Get Spending Data (POST /teams/spend)

Retrieve spending information for the current billing cycle.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `searchTerm` | string | - | Search in user names and emails |
| `sortBy` | string | `date` | Sort by: `amount`, `date`, `user` |
| `sortDirection` | string | `desc` | `asc` or `desc` |
| `page` | number | 1 | Page number (1-indexed) |
| `pageSize` | number | - | Results per page |

### Response Fields

| Field | Description |
|-------|-------------|
| `userId` | Unique identifier for the user |
| `name` | Display name of the user |
| `email` | Email address of the user |
| `role` | Role in the team (`member`, `owner`) |
| `spendCents` | On-demand spend in cents (excludes included usage) |
| `overallSpendCents` | Total spend (including included usage) |
| `fastPremiumRequests` | Number of premium requests |
| `monthlyLimitDollars` | Monthly spending limit in dollars |

### Example Request

```bash
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

### Response Example

```json
{
  "teamMemberSpend": [
    {
      "userId": 12345,
      "spendCents": 2450,
      "overallSpendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "monthlyLimitDollars": 200
    }
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

### Use Cases

- Track team spending against budget
- Identify high-cost users
- Prepare for billing reviews
- Cost allocation by department

---

## 5. Get Usage Events Data (POST /teams/filtered-usage-events)

Retrieve detailed usage events – granular insights into individual API calls, model usage, token consumption, and costs.

> *"We recommend polling this endpoint at most once per hour."*

**Rate limit:** 20 requests per minute per team

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `startDate` | number | Start date in epoch milliseconds (inclusive) |
| `endDate` | number | End date in epoch milliseconds (inclusive) |
| `userId` | number | Filter by specific user ID |
| `email` | string | Filter by user email address |
| `page` | number | Page number (default: 1) |
| `pageSize` | number | Results per page (default: 10) |

### Response Fields

| Field | Description |
|-------|-------------|
| `timestamp` | Event timestamp |
| `userEmail` | Email address of the user |
| `model` | AI model used |
| `kind` | Billing category (`Usage-based`, `Included`) |
| `maxMode` | Whether request used max mode |
| `isTokenBasedCall` | Whether billed by token usage |
| `isChargeable` | Whether event incurs a charge |
| `tokenUsage.inputTokens` | Input tokens consumed |
| `tokenUsage.outputTokens` | Output tokens generated |
| `chargedCents` | Total cost in cents (model + Cursor Token Rate) |
| `cursorTokenFee` | Cursor Token Rate in cents (if applicable) |

### Example Request

```bash
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

### Response Example

```json
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "userEmail": "developer@company.com",
      "model": "claude-4.5-sonnet",
      "kind": "Usage-based",
      "maxMode": true,
      "isTokenBasedCall": true,
      "isChargeable": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18
      },
      "chargedCents": 21.36,
      "cursorTokenFee": 1.18
    }
  ]
}
```

### Use Cases

- Detailed cost analysis per API call
- Track token usage by model
- Identify expensive queries
- Audit individual user activity

---

## 6. Set User Spend Limit (POST /teams/user-spend-limit)

Set spending limits for individual team members.

**Rate limit:** 250 requests per minute per team

**Availability:** Enterprise only

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `userEmail` | string | ✅ | Email address of the team member |
| `spendLimitDollars` | number/null | ✅ | Limit in dollars (integer). Set `null` to remove |

### Example: Set Limit

```bash
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

### Example: Remove Limit

```bash
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": null
  }'
```

### Successful Response

```json
{
  "outcome": "success",
  "message": "Spend limit set to $100 for user developer@company.com"
}
```

### Error Response

```json
{
  "outcome": "error",
  "message": "Invalid email format"
}
```

### Use Cases

- Enforce budget controls
- Prevent unexpected overages
- Tiered access based on role
- Monthly budget reset automation

---

## 7. Remove Team Member (POST /teams/remove-member)

Remove a member from your team programmatically – useful for automating offboarding workflows.

**Rate limit:** 50 requests per minute per team

**Availability:** Enterprise only

### Parameters

Provide either `userId` or `email` (not both)

| Parameter | Type | Description |
|-----------|------|-------------|
| `userId` | string | Encoded user ID (e.g., `user_abc123`) |
| `email` | string | Email address of the team member |

### Constraints

- At least one paid member must remain on the team
- At least one admin must remain on the team

### Example by Email

```bash
curl -X POST https://api.cursor.com/teams/remove-member \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "email": "developer@company.com"
  }'
```

### Example by User ID

```bash
curl -X POST https://api.cursor.com/teams/remove-member \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "user_PDSPmvukpYgZEDXsoNirw3CFhy"
  }'
```

### Successful Response

```json
{
  "success": true,
  "userId": "user_PDSPmvukpYgZEDXsoNirw3CFhy",
  "hasBillingCycleUsage": true
}
```

### Error Responses

```json
{
  "error": "User is not a member of this team"
}
```

```json
{
  "error": "Either userId or email must be provided"
}
```

### Use Cases

- Automate offboarding when employees leave
- Integrate with HR systems
- Bulk user removal
- Clean up inactive users

---

## 8. Repository Blocklists

Control which repositories and files Cursor can access.

### Get Blocklists (GET /settings/repo-blocklists/repos)

```bash
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u YOUR_API_KEY:
```

### Pattern Examples

| Pattern | What it blocks |
|---------|----------------|
| `*` | Entire repository |
| `*.env` | All .env files |
| `config/*` | All files in config directory |
| `**/*.secret` | All .secret files in any subdirectory |
| `src/api/keys.ts` | Specific file |

### Response Example

```json
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    }
  ]
}
```

### Add/Update Blocklist (POST /settings/repo-blocklists/repos/upsert)

```bash
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      }
    ]
  }'
```

### Delete Blocklist (DELETE /settings/repo-blocklists/repos/:repoId)

```bash
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u YOUR_API_KEY:
```

**Response:** `204 No Content`

### Use Cases

- Prevent AI from accessing sensitive files
- Block entire repositories with proprietary code
- Enforce security policies

---

## 9. Billing Groups (Enterprise)

Billing groups allow you to organize users for cost allocation and reporting.

### List Groups (GET /teams/groups)

```bash
curl -X GET "https://api.cursor.com/teams/groups?billingCycle=2025-01-15" \
  -u YOUR_API_KEY:
```

### Create Group (POST /teams/groups)

```bash
curl -X POST https://api.cursor.com/teams/groups \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{"name": "Engineering"}'
```

### Get Group (GET /teams/groups/:groupId)

```bash
curl -X GET "https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy" \
  -u YOUR_API_KEY:
```

### Update Group (PATCH /teams/groups/:groupId)

```bash
curl -X PATCH https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{"name": "Platform Engineering"}'
```

### Delete Group (DELETE /teams/groups/:groupId)

```bash
curl -X DELETE https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy \
  -u YOUR_API_KEY:
```

**Response:** `204 No Content`

### Add Members to Group (POST /teams/groups/:groupId/members)

```bash
curl -X POST https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy/members \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": ["user_abc123", "user_def456"]
  }'
```

### Remove Members from Group (DELETE /teams/groups/:groupId/members)

```bash
curl -X DELETE https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy/members \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": ["user_def456"]
  }'
```

### Use Cases

- Department cost allocation (Engineering vs. Product vs. Design)
- Chargebacks to business units
- Budget tracking by team
- Internal reporting

---

## Complete Example: Python Script

```python
#!/usr/bin/env python3
"""
Admin API Examples
"""

import requests
import json
from datetime import datetime, timedelta

API_KEY = "your_admin_api_key_here"
BASE_URL = "https://api.cursor.com"

def admin_request(endpoint, method="GET", data=None):
    """Make an authenticated request to the Admin API."""
    url = f"{BASE_URL}{endpoint}"
    auth = (API_KEY, "")
    headers = {"Content-Type": "application/json"}
    
    if method == "GET":
        response = requests.get(url, auth=auth, headers=headers, params=data)
    elif method == "POST":
        response = requests.post(url, auth=auth, headers=headers, json=data)
    elif method == "DELETE":
        response = requests.delete(url, auth=auth, headers=headers, json=data)
    else:
        raise ValueError(f"Unsupported method: {method}")
    
    return response

# 1. Get all team members
members = admin_request("/teams/members")
print("Team Members:", members.json())

# 2. Get audit logs for last 7 days
audit = admin_request("/teams/audit-logs", params={
    "startTime": "7d",
    "endTime": "now",
    "eventTypes": "login,logout"
})
print("Audit Logs:", audit.json())

# 3. Get daily usage for last 7 days
end_date = int(datetime.now().timestamp() * 1000)
start_date = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)

usage = admin_request("/teams/daily-usage-data", method="POST", data={
    "startDate": start_date,
    "endDate": end_date
})
print("Daily Usage:", usage.json())

# 4. Get spending data
spend = admin_request("/teams/spend", method="POST", data={
    "page": 1,
    "pageSize": 50
})
print("Spending:", spend.json())

# 5. Set user spend limit (Enterprise only)
# limit = admin_request("/teams/user-spend-limit", method="POST", data={
#     "userEmail": "developer@company.com",
#     "spendLimitDollars": 100
# })
# print("Set Limit:", limit.json())

# 6. List billing groups (Enterprise only)
groups = admin_request("/teams/groups")
print("Billing Groups:", groups.json())
```

---

## Rate Limits Summary

| Endpoint | Rate Limit |
|----------|------------|
| Most Admin API endpoints | 20 requests/minute |
| `/teams/user-spend-limit` | 250 requests/minute |
| `/teams/remove-member` | 50 requests/minute |
| Billing groups endpoints | 20 requests/minute |

---

## Common Error Responses

| Status | Error | Meaning |
|--------|-------|---------|
| 400 | Bad Request | Invalid parameters |
| 401 | Unauthorized | Invalid or missing API key |
| 403 | Forbidden | Enterprise plan required |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limit exceeded |

---

## Quick Reference Card

| What You Want | Endpoint | Method |
|---------------|----------|--------|
| List team members | `/teams/members` | GET |
| View audit logs | `/teams/audit-logs` | GET |
| Get daily usage | `/teams/daily-usage-data` | POST |
| Get spending | `/teams/spend` | POST |
| Get detailed events | `/teams/filtered-usage-events` | POST |
| Set user spend limit | `/teams/user-spend-limit` | POST |
| Remove team member | `/teams/remove-member` | POST |
| List repo blocklists | `/settings/repo-blocklists/repos` | GET |
| Add repo blocklist | `/settings/repo-blocklists/repos/upsert` | POST |
| Delete repo blocklist | `/settings/repo-blocklists/repos/:repoId` | DELETE |
| List billing groups | `/teams/groups` | GET |
| Create billing group | `/teams/groups` | POST |
| Get billing group | `/teams/groups/:groupId` | GET |
| Update billing group | `/teams/groups/:groupId` | PATCH |
| Delete billing group | `/teams/groups/:groupId` | DELETE |
| Add members to group | `/teams/groups/:groupId/members` | POST |
| Remove members from group | `/teams/groups/:groupId/members` | DELETE |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is the Admin API?** | Programmatic team management |
| **Who can use it?** | Team administrators (Enterprise for most features) |
| **How do I authenticate?** | Admin API key with Basic Auth |
| **What can I do?** | List members, view usage, set spend limits, remove users |
| **Rate limits?** | 20-250 requests/minute depending on endpoint |
| **Where do I get an API key?** | Dashboard → Settings → Advanced → Admin API Keys |

---

## The Bottom Line

**The Admin API gives enterprise teams programmatic control over team management, usage monitoring, spending controls, and compliance.**

**Think of it as:**
- **Dashboard** = Manual, click-based management 🖱️
- **Admin API** = Programmatic, scriptable management 💻

**For enterprise admins:** This API is essential for:
- Automating user offboarding (integrate with HR systems)
- Building custom usage dashboards
- Enforcing spending limits programmatically
- Tracking team activity for compliance
- Managing cost allocation across departments

**Key rules to remember:**
1. **Rate limits apply** – implement exponential backoff
2. **Some endpoints require Enterprise** – check availability
3. **At least one admin and paid member must remain** when removing users
4. **Date ranges limited to 30 days** for audit logs and usage data
