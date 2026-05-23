# Exercise 7.2: Generate and Test API Keys

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.2)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Create Admin and User API keys and verify authentication.

---

## API basics (read this first)

1. Use **PowerShell** or **Git Bash** in Cursor's terminal (``Ctrl+` ``).
2. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

3. Prefer `curl.exe` on Windows (not the `curl` alias) or Python `requests`.
4. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Step 1:** Generate User API Key — **Where:** **Cursor app** → **Settings** → **API Keys** → **Generate New Key** (copy the key; you will not see it again)

---

**Step 2:** Set environment variable — **Terminal:** **PowerShell** (``Ctrl+` ``)

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
$env:CURSOR_USER_API_KEY
```

---

**Step 3:** Test with curl — **Terminal:** **PowerShell**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  https://api.cursor.com/v1/models | Select-Object -First 20
```

---



**Step 4:** Test with Python requests:
**Terminal:** **PowerShell** — save as `test_models.py`, then `python test_models.py` — ``Ctrl+L``

```python
response = requests.get(
    "https://api.cursor.com/v1/models",
    auth=(API_KEY, "")  # Empty password
)
```

---

**Step 5:** Test with OpenAI SDK:
**Terminal:** **PowerShell** — `python test_openai_sdk.py` — ``Ctrl+L``

```python
client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY)
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "Say 'API works!'"}],
    max_tokens=10
)
```

---



**Step 6:** Generate and test Admin API Key:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx"
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/organization | jq '.'
```

---

**Step 7:** Revoke compromised keys via API or Settings → API Keys → Revoke
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

---

## Success criteria

- [ ] Generated keys · tested curl, Python, OpenAI SDK · tested Admin key

---

## Additional reference

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
