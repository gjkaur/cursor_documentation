# Exercise 9.3: Set User Spend Limits

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 9, Lesson 9.3)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Set and bulk-update per-user spending limits.

---

## API basics (read this first)

**Demonstration (Windows):** Use **PowerShell** in Cursor's terminal (``Ctrl+` ``).

1. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

2. Use **`curl.exe`** (not the `curl` alias) or Python `requests`.
3. Install **jq** for JSON parsing: `winget install jqlang.jq` or use Python instead.
4. Bash `curl` examples below each have a **PowerShell** equivalent — use those on Windows.
5. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps from the training slides

**Environment:** Windows 10/11 · **PowerShell** · use **`curl.exe`** (not the `curl` alias)

**Before API calls:** set your key (replace with your real key):

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_your_key_here"
# Admin exercises use:
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"
```

Follow each step in order. Confirm the **Expected result** before moving on.

### Step 1 — Get a user ID

**Do this:** From 9.1 member list, copy one `userId` or email identifier.

```powershell
$env:TARGET_USER_ID = "paste_user_id"
```

**Expected result:** ID stored in a variable.

---

### Step 2 — Set spend limit

**Do this:** Call the spend-limit endpoint from the lab guide (POST/PATCH per current API docs), e.g. monthly cap in dollars.

**Expected result:** `200`/`204` or clear validation message.

---

### Step 3 — Verify in dashboard

**Do this:** Open team admin UI → member → spending limit.

**Expected result:** UI matches the limit you set (may take a minute).

---

### Step 4 — Bulk CSV format (discussion)

**Do this:** Review CSV columns: `email, monthly_limit_usd` from slides.

**Expected result:** You could automate onboarding limits from HR export.

**Success criteria:** Set one limit · verified · understand bulk pattern
---

## Success criteria

- [ ] Retrieved user ID · set limit · verified · bulk setting implemented

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] `curl` and `jq` installed
- [ ] Team member email addresses

---

## Step-by-Step Instructions

### Step 1: Set a Spend Limit for a User (2 minutes)

Set a $100 monthly spend limit for a team member.

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/user-spend-limit \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }' | jq '.'
```

**Expected response:**
```json
{
  "outcome": "success",
  "message": "Spend limit set to $100 for user developer@company.com"
}
```

---

### Step 2: Remove a Spend Limit (2 minutes)

Remove the spend limit (set to unlimited).

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/user-spend-limit \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": null
  }' | jq '.'
```

**Expected response:**
```json
{
  "outcome": "success",
  "message": "Spend limit removed for user developer@company.com"
}
```

---

### Step 3: Set Different Limits for Multiple Users (2 minutes)

Create a batch script to set limits for multiple users.

**Command:**
```bash
# Create a CSV file
cat > user_limits.csv << EOF
email,limit_dollars
alice@company.com,200
bob@company.com,100
charlie@company.com,50
diana@company.com,25
EOF

# Batch set limits
tail -n +2 user_limits.csv | while IFS=, read -r email limit; do
  echo "Setting $email to \$$limit"
  curl -s -X POST https://api.cursor.com/teams/user-spend-limit \
    -u "$CURSOR_ADMIN_API_KEY:" \
    -H "Content-Type: application/json" \
    -d "{\"userEmail\": \"$email\", \"spendLimitDollars\": $limit}" | jq -r '.message'
done
```

---

### Step 4: Handle Error Cases (2 minutes)

Test error scenarios to understand the responses.

**Invalid email:**
```bash
curl -s -X POST https://api.cursor.com/teams/user-spend-limit \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "nonexistent@company.com",
    "spendLimitDollars": 100
  }' | jq '.'
```

**Expected error response:**
```json
{
  "outcome": "error",
  "message": "User is not a member of this team"
}
```

**Invalid limit (decimal not allowed):**
```bash
curl -s -X POST https://api.cursor.com/teams/user-spend-limit \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 50.50
  }' | jq '.'
```

**Expected error response:**
```json
{
  "outcome": "error",
  "message": "Only integer values are accepted for spend limit"
}
```

---

### Step 5: Create a Python Script for Spend Limit Management (2 minutes)

**Create `spend_limit_manager.py`:**
```python
#!/usr/bin/env python3
"""
Manage team member spend limits
"""

import requests
import csv
import os
import sys
import json

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class SpendLimitManager:
    """Manage user spend limits"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def set_limit(self, email, limit_dollars):
        """
        Set spend limit for a user.
        
        Args:
            email: User's email address
            limit_dollars: Limit in dollars (integer) or None to remove
        """
        url = f"{self.base_url}/teams/user-spend-limit"
        payload = {
            "userEmail": email,
            "spendLimitDollars": limit_dollars
        }
        
        response = requests.post(url, auth=self.auth, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if result.get("outcome") == "success":
                if limit_dollars is None:
                    print(f"✅ Removed limit for {email}")
                else:
                    print(f"✅ Set ${limit_dollars} limit for {email}")
            else:
                print(f"❌ Error: {result.get('message')}")
        else:
            print(f"❌ HTTP {response.status_code}: {response.text}")
        
        return response.status_code == 200
    
    def set_limits_from_csv(self, csv_file):
        """Set limits for multiple users from CSV file."""
        print(f"\n📋 Processing {csv_file}...")
        print("-" * 40)
        
        success_count = 0
        fail_count = 0
        
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                email = row.get('email')
                limit = row.get('limit_dollars')
                
                if not email:
                    continue
                
                # Convert to int or None
                limit_dollars = int(limit) if limit and limit.strip() else None
                
                if self.set_limit(email, limit_dollars):
                    success_count += 1
                else:
                    fail_count += 1
        
        print("-" * 40)
        print(f"✅ Successful: {success_count}")
        print(f"❌ Failed: {fail_count}")
    
    def get_team_members(self):
        """Get list of team members with their current limits."""
        url = f"{self.base_url}/teams/members"
        response = requests.get(url, auth=self.auth)
        
        if response.status_code == 200:
            return response.json().get("teamMembers", [])
        return []
    
    def show_limits_summary(self):
        """Show current spend limits for all team members."""
        members = self.get_team_members()
        
        if not members:
            print("No team members found")
            return
        
        print("\n📊 Current Spend Limits")
        print("=" * 50)
        print(f"{'Email':<30} {'Role':<10} {'Limit':<10}")
        print("-" * 50)
        
        # Note: This only shows limits you've set.
        # The API doesn't directly return current limits per user.
        # Track limits separately in your own database.
        for member in members:
            email = member.get('email')
            role = member.get('role', 'member')
            # In a real implementation, you'd store limits in a database
            print(f"{email:<30} {role:<10} {'?':<10}")
        
        print("=" * 50)
        print("Note: Track limits separately; API doesn't retrieve current limits")

def main():
    print("🚀 Spend Limit Manager")
    print("=" * 40)
    
    manager = SpendLimitManager()
    
    # Example: Set a single limit
    manager.set_limit("test@company.com", 100)
    
    # Example: Remove a limit
    # manager.set_limit("test@company.com", None)
    
    # Example: Set limits from CSV
    # manager.set_limits_from_csv("user_limits.csv")
    
    # Show current team members
    manager.show_limits_summary()

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 1 Output:
```json
{
  "outcome": "success",
  "message": "Spend limit set to $100 for user developer@company.com"
}
```

### Step 2 Output:
```json
{
  "outcome": "success",
  "message": "Spend limit removed for user developer@company.com"
}
```

### Step 3 Output:
```
Setting alice@company.com to $200
✅ Set $200 limit for alice@company.com
Setting bob@company.com to $100
✅ Set $100 limit for bob@company.com
Setting charlie@company.com to $50
✅ Set $50 limit for charlie@company.com
Setting diana@company.com to $25
✅ Set $25 limit for diana@company.com
```

---

## Important Notes

| Note | Description |
|------|-------------|
| **Availability** | Enterprise only |
| **Rate limit** | 250 requests per minute per team |
| **Integer only** | No decimal values (e.g., 100, not 100.50) |
| **Null removes** | Set to `null` to remove limit completely |
| **Zero is valid** | Setting to `0` prevents any usage-based spend |

---

## Success Criteria

- [ ] Set spend limit for a user
- [ ] Removed spend limit for a user
- [ ] Batch set limits from CSV
- [ ] Handled error cases (invalid email, decimal values)
- [ ] Created Python management script

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key, not User API key |
| 403 Forbidden | Spend limits require Enterprise plan |
| "User is not a member" | Verify email is in your team |
| Decimal not allowed | Use integer values only (e.g., 100, not 100.50) |

---

## Best Practices

| Practice | Why |
|----------|-----|
| **Track limits in your own DB** | API doesn't retrieve current limits |
| **Set limits on team join** | Automate via SSO/SCIM integration |
| **Remove on departure** | Revoke access when users leave |
| **Use CSV for bulk updates** | Efficient for large teams |
| **Integrate with HR system** | Automate based on role/department |

---

## Bonus Challenge

Create a script that syncs spend limits from your HR system:

```python
def sync_from_hr_system():
    """Fetch limits from HR system and sync to Cursor"""
    
    # Example: Fetch from HR API
    # hr_response = requests.get("https://hr.company.com/api/employees")
    # employees = hr_response.json()
    
    # Mock data
    employees = [
        {"email": "engineer@company.com", "department": "engineering", "budget": 200},
        {"email": "qa@company.com", "department": "quality", "budget": 50},
        {"email": "manager@company.com", "department": "management", "budget": 300},
    ]
    
    manager = SpendLimitManager()
    
    for emp in employees:
        manager.set_limit(emp["email"], emp["budget"])
    
    print("✅ Synced limits from HR system")
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Set spend limit for a user
- [ ] Removed spend limit for a user
- [ ] Batch set limits from CSV
- [ ] Handled error cases
- [ ] Created Python management script
- [ ] (Bonus) Integrated with HR system

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
