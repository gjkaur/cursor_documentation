# API Exercise 11: Remove Team Member

**Objective:** Programmatically remove a team member from your Cursor organization, useful for automating offboarding workflows.

**Time:** 10 minutes

**Difficulty:** Intermediate

**Real-World Scenario:** Your company uses an HR system that automatically disables employee accounts upon departure. You want to integrate Cursor offboarding into this workflow so departing employees lose access immediately without manual dashboard intervention.

---

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] Team member email or user ID to remove
- [ ] At least one admin and one paid member must remain

---

## Step-by-Step Instructions

### Step 1: List Team Members to Find Target User (2 minutes)

First, identify the user you want to remove.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/teams/members" | jq '.teamMembers[] | {id, email, name, role}'
```

**Expected output:**
```json
{
  "id": 12345,
  "email": "alice@company.com",
  "name": "Alice Developer",
  "role": "member"
}
{
  "id": 12346,
  "email": "bob@company.com",
  "name": "Bob Engineer",
  "role": "member"
}
{
  "id": 12347,
  "email": "charlie@company.com",
  "name": "Charlie Tester",
  "role": "member"
}
```

---

### Step 2: Remove Member by Email (2 minutes)

Remove a team member using their email address.

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/remove-member \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "charlie@company.com"
  }' | jq '.'
```

**Expected response:**
```json
{
  "success": true,
  "userId": "user_abc123def456",
  "hasBillingCycleUsage": true
}
```

---

### Step 3: Remove Member by User ID (2 minutes)

Remove a team member using their encoded user ID.

**Command:**
```bash
curl -s -X POST https://api.cursor.com/teams/remove-member \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "user_abc123def456"
  }' | jq '.'
```

**Expected response:**
```json
{
  "success": true,
  "userId": "user_abc123def456",
  "hasBillingCycleUsage": true
}
```

---

### Step 4: Handle Error Cases (2 minutes)

Test error scenarios to understand the responses.

**Error: User not a member**
```bash
curl -s -X POST https://api.cursor.com/teams/remove-member \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nonexistent@company.com"
  }' | jq '.'
```

**Expected response:**
```json
{
  "error": "User is not a member of this team"
}
```

**Error: No identifier provided**
```bash
curl -s -X POST https://api.cursor.com/teams/remove-member \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{}' | jq '.'
```

**Expected response:**
```json
{
  "error": "Either userId or email must be provided"
}
```

**Error: Both identifiers provided**
```bash
curl -s -X POST https://api.cursor.com/teams/remove-member \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@company.com",
    "userId": "user_abc123def456"
  }' | jq '.'
```

**Expected response:**
```json
{
  "error": "Only one of userId or email should be provided, not both"
}
```

---

### Step 5: Create an Offboarding Script (2 minutes)

**Create `offboard_user.py`:**
```python
#!/usr/bin/env python3
"""
Automated user offboarding script
"""

import requests
import os
import sys
import json
import argparse
from datetime import datetime

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class OffboardingManager:
    """Manage user offboarding"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_team_members(self):
        """Get all team members."""
        url = f"{self.base_url}/teams/members"
        response = requests.get(url, auth=self.auth)
        
        if response.status_code == 200:
            return response.json().get("teamMembers", [])
        return []
    
    def find_user(self, identifier):
        """Find user by email or user ID."""
        members = self.get_team_members()
        
        for member in members:
            if member.get("email") == identifier or str(member.get("id")) == identifier:
                return member
            # Also check encoded user ID if available
            if f"user_{member.get('id')}" == identifier:
                return member
        
        return None
    
    def remove_by_email(self, email):
        """Remove user by email."""
        url = f"{self.base_url}/teams/remove-member"
        payload = {"email": email}
        
        response = requests.post(url, auth=self.auth, json=payload)
        return response.json()
    
    def remove_by_user_id(self, user_id):
        """Remove user by encoded user ID."""
        url = f"{self.base_url}/teams/remove-member"
        payload = {"userId": user_id}
        
        response = requests.post(url, auth=self.auth, json=payload)
        return response.json()
    
    def offboard_user(self, identifier):
        """
        Offboard a user by email or user ID.
        
        Args:
            identifier: Email address or encoded user ID
        
        Returns:
            Tuple of (success, message, user_info)
        """
        # Find user first
        user = self.find_user(identifier)
        
        if not user:
            return False, f"User not found: {identifier}", None
        
        print(f"\n📋 Found user:")
        print(f"   Name: {user.get('name', 'N/A')}")
        print(f"   Email: {user.get('email')}")
        print(f"   Role: {user.get('role')}")
        print(f"   Active: {not user.get('isRemoved', False)}")
        
        # Confirm removal
        print(f"\n⚠️  Are you sure you want to remove {user.get('email')}?")
        confirm = input("   Type 'yes' to confirm: ")
        
        if confirm.lower() != 'yes':
            return False, "Removal cancelled", user
        
        # Perform removal
        if '@' in identifier:
            result = self.remove_by_email(identifier)
        else:
            result = self.remove_by_user_id(identifier)
        
        if result.get("success"):
            return True, f"Successfully removed {user.get('email')}", user
        else:
            return False, result.get("error", "Unknown error"), user
    
    def offboard_batch(self, identifiers):
        """Offboard multiple users."""
        results = []
        
        for identifier in identifiers:
            success, message, user = self.offboard_user(identifier)
            results.append({
                "identifier": identifier,
                "success": success,
                "message": message,
                "user_email": user.get("email") if user else None
            })
        
        return results

def main():
    parser = argparse.ArgumentParser(description="Offboard Cursor team members")
    parser.add_argument("identifier", nargs="?", help="Email or user ID to remove")
    parser.add_argument("--batch", help="CSV file with list of users to remove")
    parser.add_argument("--dry-run", action="store_true", help="Preview without removing")
    
    args = parser.parse_args()
    
    manager = OffboardingManager()
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print("=" * 40)
        
        if args.identifier:
            user = manager.find_user(args.identifier)
            if user:
                print(f"\nWould remove: {user.get('email')} ({user.get('role')})")
            else:
                print(f"\nUser not found: {args.identifier}")
        elif args.batch:
            with open(args.batch, 'r') as f:
                import csv
                reader = csv.DictReader(f)
                for row in reader:
                    email = row.get('email')
                    user = manager.find_user(email)
                    if user:
                        print(f"Would remove: {user.get('email')}")
                    else:
                        print(f"User not found: {email}")
        return
    
    if args.identifier:
        # Single user offboard
        success, message, user = manager.offboard_user(args.identifier)
        print(f"\n{'✅' if success else '❌'} {message}")
        
        if success and user:
            print(f"\n📊 Removal summary:")
            print(f"   User: {user.get('email')}")
            print(f"   Role: {user.get('role')}")
            print(f"   Had billing usage: Check dashboard")
    
    elif args.batch:
        # Batch offboard
        import csv
        identifiers = []
        
        with open(args.batch, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('email'):
                    identifiers.append(row['email'])
                elif row.get('user_id'):
                    identifiers.append(row['user_id'])
        
        print(f"\n📋 Found {len(identifiers)} users to offboard")
        
        results = manager.offboard_batch(identifiers)
        
        print("\n📊 Offboarding Results")
        print("=" * 40)
        for result in results:
            status = "✅" if result["success"] else "❌"
            print(f"{status} {result['identifier']}: {result['message']}")
    
    else:
        print("❌ Please provide an email, user ID, or --batch CSV file")
        print("   Example: python offboard_user.py alice@company.com")
        print("   Example: python offboard_user.py --batch users_to_remove.csv")
        print("   Example: python offboard_user.py --dry-run alice@company.com")

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 2 Output:
```json
{
  "success": true,
  "userId": "user_abc123def456",
  "hasBillingCycleUsage": true
}
```

### Step 5 Output (Success):
```
📋 Found user:
   Name: Charlie Tester
   Email: charlie@company.com
   Role: member
   Active: True

⚠️  Are you sure you want to remove charlie@company.com?
   Type 'yes' to confirm: yes

✅ Successfully removed charlie@company.com

📊 Removal summary:
   User: charlie@company.com
   Role: member
   Had billing usage: Check dashboard
```

---

## Important Constraints

| Constraint | Description |
|------------|-------------|
| **At least one paid member** | Cannot remove the last paid member |
| **At least one admin** | Cannot remove the last admin (owner) |
| **Enterprise only** | Feature only available on Enterprise plan |
| **Rate limit** | 50 requests per minute per team |

---

## Response Fields

| Field | Description |
|-------|-------------|
| `success` | Whether removal was successful |
| `userId` | Encoded user ID of removed user |
| `hasBillingCycleUsage` | Whether user had usage in current billing cycle |

---

## Success Criteria

- [ ] Listed team members to find target user
- [ ] Removed member by email
- [ ] Removed member by user ID
- [ ] Handled error cases (user not found, no identifier, both identifiers)
- [ ] Created offboarding script with dry-run option
- [ ] Batch offboard from CSV file

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key, not User API key |
| 403 Forbidden | Member removal requires Enterprise plan |
| "User is not a member" | Verify email or ID is correct |
| "At least one paid member must remain" | Cannot remove last paid user |
| "At least one admin must remain" | Cannot remove last admin |

---

## Best Practices

| Practice | Why |
|----------|-----|
| **Always dry-run first** | Preview changes before executing |
| **Log all removals** | Audit trail for compliance |
| **Integrate with HR system** | Automate offboarding |
| **Check billing usage** | May need to handle remaining credits |
| **Remove spend limits first** | Optional: clear limits before removal |

---

## Bonus Challenge

Create an HR system integration that automatically offboards users:

```python
def sync_with_hr_system():
    """Fetch terminated employees from HR system and offboard"""
    
    # Fetch terminated employees from HR API
    hr_response = requests.get(
        "https://hr.company.com/api/terminations",
        headers={"Authorization": f"Bearer {HR_API_KEY}"}
    )
    terminated_employees = hr_response.json()
    
    manager = OffboardingManager()
    
    for employee in terminated_employees:
        email = employee.get("email")
        termination_date = employee.get("termination_date")
        
        print(f"Processing: {email} (terminated {termination_date})")
        
        # Optional: Only offboard after certain date
        if should_offboard(termination_date):
            success, message, _ = manager.offboard_user(email)
            log_offboarding(email, success, message)
    
    print("✅ HR sync complete")
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Removed member by email
- [ ] Removed member by user ID
- [ ] Handled error cases
- [ ] Created offboarding script with dry-run
- [ ] Batch offboard from CSV
- [ ] (Bonus) Integrated with HR system
