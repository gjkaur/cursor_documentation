# API Exercise 1: Generate and Test API Keys

**Objective:** Generate different types of API keys (Admin API key, User API key, Service Account key) and test authentication with Cursor's APIs.

**Time:** 10 minutes

**Difficulty:** Beginner

**Real-World Scenario:** You need to set up programmatic access to Cursor for your team's automation scripts, CI/CD pipelines, and custom dashboards. Different use cases require different types of API keys with appropriate permissions.

---

## Prerequisites

- [ ] Admin access to Cursor Dashboard
- [ ] Cursor Enterprise plan (for Admin API key)
- [ ] Browser access to cursor.com

---

## Step-by-Step Instructions

### Step 1: Generate an Admin API Key (5 minutes)

Admin API keys are used for team management, analytics, and AI Code Tracking.

**Instructions:**

1. Log into Cursor Dashboard at `cursor.com/dashboard`
2. Navigate to **Settings → Advanced → Admin API Keys**
3. Click **Create New API Key**
4. Enter a descriptive name: `"Training - Admin Key"`
5. Click **Create**
6. **Copy the key immediately** – it will only be shown once!

**Key format:** `crsr_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

**Save it securely:**

```bash
# Save to environment variable (temporary)
export CURSOR_ADMIN_API_KEY="crsr_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Or save to a secure file (not recommended for production)
echo "CURSOR_ADMIN_API_KEY=crsr_xxxxxxxx..." > .env.api
chmod 600 .env.api
```

---

### Step 2: Generate a User API Key (3 minutes)

User API keys are used for Cloud Agents API (available on all plans).

**Instructions:**

1. Navigate to **Dashboard → Integrations**
2. Scroll to **API Keys** section
3. Click **Generate New API Key**
4. Enter a name: `"Training - User Key"`
5. Click **Generate**
6. **Copy the key immediately**

**Save it:**

```bash
export CURSOR_USER_API_KEY="cursor_user_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

### Step 3: Generate a Service Account API Key (2 minutes - Enterprise only)

Service account keys are for automation and CI/CD pipelines (non-human accounts).

**Instructions:**

1. Navigate to **Dashboard → Settings → Service Accounts**
2. Click **New Service Account**
3. Enter name: `"Training Automation"`
4. Click **Create**
5. **Copy the API key immediately**

**Save it:**

```bash
export CURSOR_SERVICE_API_KEY="crsr_sa_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

### Step 4: Test Admin API Key Authentication (5 minutes)

Test that your Admin API key works with the Admin API.

**Command:**

```bash
# Test getting team members
curl -X GET "https://api.cursor.com/teams/members" \
  -u "$CURSOR_ADMIN_API_KEY:" \
  --silent | jq '.'
```

**Expected response:**

```json
{
  "teamMembers": [
    {
      "id": 12345,
      "name": "Your Name",
      "email": "you@company.com",
      "role": "owner",
      "isRemoved": false
    }
  ]
}
```

**Test with Bearer token (alternative):**

```bash
curl -X GET "https://api.cursor.com/teams/members" \
  -H "Authorization: Bearer $CURSOR_ADMIN_API_KEY" \
  --silent | jq '.'
```

---

### Step 5: Test User API Key Authentication (3 minutes)

Test that your User API key works with the Cloud Agents API.

**Command:**

```bash
# Test getting available models
curl -X GET "https://api.cursor.com/v1/models" \
  -u "$CURSOR_USER_API_KEY:" \
  --silent | jq '.'
```

**Expected response:**

```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2",
    "gpt-5-mini"
  ]
}
```

---

### Step 6: Test API Key Info Endpoint (2 minutes)

Get information about the API key being used.

**Command:**

```bash
curl -X GET "https://api.cursor.com/v1/me" \
  -u "$CURSOR_USER_API_KEY:" \
  --silent | jq '.'
```

**Expected response:**

```json
{
  "apiKeyName": "Training - User Key",
  "createdAt": "2025-01-15T10:30:00.000Z",
  "userEmail": "your-email@company.com"
}
```

---

## Expected Output

### Step 4 Output (Admin API):

```json
{
  "teamMembers": [
    {
      "id": 12345,
      "name": "Alex Developer",
      "email": "alex@company.com",
      "role": "owner",
      "isRemoved": false
    }
  ]
}
```

### Step 5 Output (Cloud Agents API):

```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2",
    "gpt-5-mini"
  ]
}
```

### Step 6 Output (API Key Info):

```json
{
  "apiKeyName": "Training - User Key",
  "createdAt": "2025-01-15T10:30:00.000Z",
  "userEmail": "alex@company.com"
}
```

---

## Success Criteria

- [ ] Admin API key generated and saved securely
- [ ] User API key generated and saved securely
- [ ] Service account key generated (if Enterprise)
- [ ] Admin API key successfully tested with `/teams/members` endpoint
- [ ] User API key successfully tested with `/v1/models` endpoint
- [ ] API key info endpoint returned correct information

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `401 Unauthorized` | Check that the API key is correct and includes the colon after it in Basic Auth |
| `403 Forbidden` | Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead |
| Key not found in dashboard | Check correct section: Admin Keys vs Integrations vs Service Accounts |
| `curl: (6) Could not resolve host` | Check internet connection |
| `jq: command not found` | Install jq: `brew install jq` (Mac) or `apt-get install jq` (Linux) |

---

## Key Takeaways

| Key Type | Best For | Where to Generate | Scope |
|----------|----------|-------------------|-------|
| **Admin API Key** | Team management, analytics, AI Code Tracking | Settings → Advanced → Admin API Keys | `admin:*` |
| **User API Key** | Cloud Agents API, personal automation | Dashboard → Integrations | User-scoped |
| **Service Account Key** | CI/CD, automation, non-human workflows | Dashboard → Settings → Service Accounts | Team-scoped |

**Important Notes:**

- Admin API keys require **Enterprise plan**
- API keys are **tied to your organization** – all admins can see them
- Keys are **unaffected** when the creator leaves the team
- **Never commit API keys** to version control
- Use **environment variables** for local development
- Use **secrets managers** (GitHub Secrets, AWS Secrets Manager) for CI/CD

---

## Bonus Challenge

Create a simple Python script that tries all three authentication methods and reports which work:

```python
#!/usr/bin/env python3
"""Test all Cursor API keys"""

import os
import requests

def test_api_key(api_key, name, base_url, expected_status=200):
    """Test an API key against an endpoint."""
    url = f"{base_url}"
    auth = (api_key, "")

    try:
        response = requests.get(url, auth=auth, timeout=10)
        status = "WORKING" if response.status_code == expected_status else f"FAILED ({response.status_code})"
        print(f"{name}: {status}")
        return response.status_code == expected_status
    except Exception as e:
        print(f"{name}: ERROR - {str(e)[:50]}")
        return False

# Load keys from environment
admin_key = os.environ.get("CURSOR_ADMIN_API_KEY")
user_key = os.environ.get("CURSOR_USER_API_KEY")
service_key = os.environ.get("CURSOR_SERVICE_API_KEY")

print("\nTesting Cursor API Keys")
print("=" * 40)

if admin_key:
    test_api_key(admin_key, "Admin API Key", "https://api.cursor.com/teams/members")
else:
    print("Admin API Key: Not set (Enterprise required)")

if user_key:
    test_api_key(user_key, "User API Key", "https://api.cursor.com/v1/models")
else:
    print("User API Key: Not set")

if service_key:
    test_api_key(service_key, "Service Account Key", "https://api.cursor.com/v1/models")
else:
    print("Service Account Key: Not set (Enterprise)")

print("\nTip: Set keys with:")
print("  export CURSOR_ADMIN_API_KEY=your_key")
print("  export CURSOR_USER_API_KEY=your_key")
print("  export CURSOR_SERVICE_API_KEY=your_key")
```

---

## Exercise Complete

Check off when done:

- [ ] Generated Admin API key
- [ ] Generated User API key
- [ ] Generated Service Account key (optional)
- [ ] Tested Admin API key with `/teams/members`
- [ ] Tested User API key with `/v1/models`
- [ ] Tested API key info endpoint
- [ ] (Bonus) Created key testing script
