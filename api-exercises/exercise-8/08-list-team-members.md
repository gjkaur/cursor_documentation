# API Exercise 8: List Team Members

**Objective:** Retrieve all team members programmatically using the Admin API, including their names, emails, roles, and status.

**Time:** 5 minutes

**Difficulty:** Beginner

**Real-World Scenario:** Your team needs to sync Cursor user data with your internal HR system. Instead of manually exporting user lists from the dashboard, you want to programmatically fetch all team members and their roles for automated provisioning.

---

## Prerequisites

- [ ] Admin API key from Exercise 1 (Admin API key required)
- [ ] Cursor Enterprise plan
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: List All Team Members (2 minutes)

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/teams/members" | jq '.'
```

**Expected response:**
```json
{
  "teamMembers": [
    {
      "id": 12345,
      "name": "Alex Developer",
      "email": "alex@company.com",
      "role": "owner",
      "isRemoved": false
    },
    {
      "id": 12346,
      "name": "Sam Engineer",
      "email": "sam@company.com",
      "role": "member",
      "isRemoved": false
    },
    {
      "id": 12347,
      "name": "Jordan Tester",
      "email": "jordan@company.com",
      "role": "member",
      "isRemoved": true
    }
  ]
}
```

---

### Step 2: Format Output for Readability (1 minute)

**List members with formatted output:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/teams/members" | \
  jq -r '.teamMembers[] | "\(.id) | \(.email) | \(.role) | Active: \(.isRemoved | not)"'
```

**Expected output:**
```
12345 | alex@company.com | owner | Active: true
12346 | sam@company.com | member | Active: true
12347 | jordan@company.com | member | Active: false
```

---

### Step 3: Filter Active Members Only (1 minute)

**Get only active members (not removed):**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/teams/members" | \
  jq '.teamMembers[] | select(.isRemoved == false) | {name, email, role}'
```

**Expected output:**
```json
{
  "name": "Alex Developer",
  "email": "alex@company.com",
  "role": "owner"
}
{
  "name": "Sam Engineer",
  "email": "sam@company.com",
  "role": "member"
}
```

---

### Step 4: Count Members by Role (1 minute)

**Get count of owners vs members:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/teams/members" | \
  jq '{owners: [.teamMembers[] | select(.role == "owner")] | length, members: [.teamMembers[] | select(.role == "member")] | length}'
```

**Expected output:**
```json
{
  "owners": 1,
  "members": 5
}
```

---

## Expected Output

### Step 1 Output:
```json
{
  "teamMembers": [
    {
      "id": 12345,
      "name": "Alex Developer",
      "email": "alex@company.com",
      "role": "owner",
      "isRemoved": false
    },
    {
      "id": 12346,
      "name": "Sam Engineer",
      "email": "sam@company.com",
      "role": "member",
      "isRemoved": false
    }
  ]
}
```

### Step 2 Output:
```
12345 | alex@company.com | owner | Active: true
12346 | sam@company.com | member | Active: true
```

---

## Response Fields Reference

| Field | Type | Description |
|-------|------|-------------|
| `id` | number | Unique identifier for the team member |
| `name` | string | Display name of the team member |
| `email` | string | Email address of the team member |
| `role` | string | Role in the team (`owner` or `member`) |
| `isRemoved` | boolean | Whether the member has been removed from the team |

---

## Success Criteria

- [ ] Retrieved all team members
- [ ] Filtered active members only
- [ ] Counted members by role
- [ ] Formatted output for readability
- [ ] Identified owners vs regular members

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key, not User API key |
| 403 Forbidden | Admin API requires Enterprise plan |
| Empty response | Team may have no members (at least one owner should exist) |
| Missing name field | Some users may not have set a display name |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /teams/members` |
| **Authentication** | Admin API key (Enterprise) |
| **Response** | Array of team member objects |
| **Active filter** | `select(.isRemoved == false)` |
| **Role types** | `owner` (admin), `member` (regular user) |

---

## Bonus Challenge

Create a Python script to export team members to CSV:

```python
#!/usr/bin/env python3
"""
Export team members to CSV
"""

import requests
import csv
import os
import sys

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

def get_team_members():
    """Fetch all team members."""
    url = "https://api.cursor.com/teams/members"
    auth = (API_KEY, "")

    response = requests.get(url, auth=auth)

    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        return []

    return response.json().get("teamMembers", [])

def export_to_csv(members, filename="team_members.csv"):
    """Export team members to CSV."""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'email', 'role', 'active']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for member in members:
            writer.writerow({
                'id': member.get('id'),
                'name': member.get('name', ''),
                'email': member.get('email'),
                'role': member.get('role'),
                'active': not member.get('isRemoved', False)
            })

    print(f"✅ Exported {len(members)} members to {filename}")

if __name__ == "__main__":
    members = get_team_members()
    if members:
        export_to_csv(members)
        print(f"\n📊 Summary:")
        active = sum(1 for m in members if not m.get('isRemoved', False))
        print(f"   Total members: {len(members)}")
        print(f"   Active: {active}")
        print(f"   Inactive: {len(members) - active}")
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved all team members
- [ ] Filtered active members only
- [ ] Counted members by role
- [ ] Formatted output for readability
- [ ] (Bonus) Exported to CSV
