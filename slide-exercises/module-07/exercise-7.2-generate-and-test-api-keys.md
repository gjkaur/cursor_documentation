# Exercise 7.2: Generate and Test API Keys

**Module 7:** Cursor API Foundations  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 7, Lesson 7.2)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Create Admin and User API keys and verify authentication.

---

## API basics (read this first)

**Windows:** PowerShell (``Ctrl+` ``) · **`curl.exe`** · store keys in `$env:` — **never** commit keys to git.

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"   # Admin labs (9–10)
```

More examples (Python, jq, bash): see **Detailed reference** below — optional for class.

---

## Steps from the training slides

**Environment:** Windows · PowerShell (``Ctrl+` ``) · **`curl.exe`** · keys in `$env:` only (never commit).

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"  # Modules 9–10
```

Follow each step in order. Confirm the **Expected result** before moving on.

### Step 1 — Create and store your User API key

**Do this:** Cursor **Settings** → **API Keys** → **Generate** → copy once, then:

```powershell
$env:CURSOR_USER_API_KEY = "cursor_paste_your_key_here"
```

**Expected result:** Key saved in `$env:` for this terminal only (not in git).

---

### Step 2 — Test the key with one curl call

**Do this:**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" https://api.cursor.com/v1/models
```

**Expected result:** JSON model list — not `401 Unauthorized`.

---

### Step 3 — Admin key (only if you have Enterprise Admin API)

**Do this:**

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_paste_here"
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" https://api.cursor.com/v1/teams/members
```

**Expected result:** `200` with team data, or your instructor explains your plan uses User key only.

**Success criteria:** User key works · keys stay in `$env:` only
---

## Success criteria

- [ ] Generated keys · tested curl, Python, OpenAI SDK · tested Admin key

---

> **Note:** The section below is optional deep dive — not required to finish the in-class steps.

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

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
    "composer-2.5",
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
    "composer-2.5",
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

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
