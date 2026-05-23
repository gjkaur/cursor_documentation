# Exercise 9.3: Set User Spend Limits

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.3)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Set and bulk-update per-user spending limits.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
USER_ID=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?email=developer@company.com" \
  | jq -r '.members[0].id')

curl -X PATCH ".../policies/users/$USER_ID/limits" \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -d '{"monthlyLimit": 50.00, "exceedanceAction": "block"}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Check current limit: `GET .../policies/users/{userId}/limits`

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**CSV bulk set:** `email, monthly_limit, action`

```csv
intern@company.com,20,block
contractor@company.com,50,alert
lead@company.com,200,alert
```

**Find heavy users:** query `/analytics/usage/users` for current month → filter cost > threshold

---

## Success criteria

- [ ] Retrieved user ID · set limit · verified · bulk setting implemented

---

## Additional reference

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
