# API Exercise 19: Get Commit Details (Alpha)

**Objective:** Retrieve detailed commit information including line-by-line blame annotations and conversation metadata – showing exactly which lines came from which AI conversation.

**Time:** 10 minutes

**Difficulty:** Advanced

**Real-World Scenario:** Your compliance team needs to trace specific lines of code back to the AI conversations that generated them. The commit details endpoint provides line-level attribution with conversation summaries.

---

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan (AI Code Tracking API)
- [ ] Git repository with Cursor-tracked commits
- [ ] A commit hash from a Cursor-generated commit
- [ ] **Note:** This endpoint is in limited alpha and may not be available to all users

---

## Step-by-Step Instructions

### Step 1: Get a Commit Hash (2 minutes)

First, get a commit hash from the AI commits endpoint.

**Command:**
```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&pageSize=5" | \
  jq '.items[] | {commitHash, userEmail, message, commitSource}'
```

**Expected output:**
```json
{
  "commitHash": "0aabf603dc906e05bf5e4d9fd423fdd517f2e43f",
  "userEmail": "alice@company.com",
  "message": "Refactor authentication module",
  "commitSource": "ide"
}
{
  "commitHash": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1",
  "userEmail": "bob@company.com",
  "message": "Add error handling",
  "commitSource": "cloud"
}
```

---

### Step 2: Get Commit Details for a Single Commit (3 minutes)

Retrieve detailed information for a specific commit.

**Command:**
```bash
COMMIT_HASH="0aabf603dc906e05bf5e4d9fd423fdd517f2e43f"

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits/$COMMIT_HASH?branch=main" | jq '.'
```

**Expected response:**
```json
{
  "commits": [
    {
      "commitHash": "0aabf603dc906e05bf5e4d9fd423fdd517f2e43f",
      "commitSource": "ide",
      "rangeAnnotations": [
        {
          "filePath": "src/auth/login.ts",
          "groups": [
            {
              "conversationId": "conv_abc123",
              "model": "claude-4.5-sonnet",
              "operationType": "insert",
              "ranges": [
                { "start": 10, "end": 25 },
                { "start": 42, "end": 58 }
              ]
            }
          ]
        },
        {
          "filePath": "src/auth/validation.ts",
          "groups": [
            {
              "conversationId": "conv_abc123",
              "model": "claude-4.5-sonnet",
              "operationType": "modify",
              "ranges": [
                { "start": 5, "end": 20 }
              ]
            }
          ]
        }
      ]
    }
  ],
  "conversations": [
    {
      "id": "conv_abc123",
      "title": "Refactor authentication module",
      "tldr": "Extracted login and validation into separate functions",
      "overview": "Refactored the authentication module to improve maintainability. Created dedicated login handler and validation service.",
      "summaryBullets": [
        "Created AuthService class with login method",
        "Added input validation for email and password",
        "Updated error handling to use custom exceptions",
        "Added unit tests for new functions"
      ]
    }
  ]
}
```

---

### Step 3: Get Multiple Commits at Once (2 minutes)

Retrieve details for multiple commits in a single request.

**Command:**
```bash
COMMIT_HASHES="0aabf603dc906e05bf5e4d9fd423fdd517f2e43f,b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1"

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits/$COMMIT_HASHES" | jq '{commit_count: (.commits | length), conversation_count: (.conversations | length)}'
```

**Expected output:**
```json
{
  "commit_count": 2,
  "conversation_count": 3
}
```

---

### Step 4: Parse Line Annotations (2 minutes)

Extract which lines were AI-generated and which conversation produced them.

**Command:**
```bash
COMMIT_HASH="0aabf603dc906e05bf5e4d9fd423fdd517f2e43f"

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits/$COMMIT_HASH" | \
  jq '.commits[0].rangeAnnotations[] | {filePath, lines: [.groups[].ranges[]]}'
```

**Expected output:**
```json
{
  "filePath": "src/auth/login.ts",
  "lines": [
    {"start": 10, "end": 25},
    {"start": 42, "end": 58}
  ]
}
{
  "filePath": "src/auth/validation.ts",
  "lines": [
    {"start": 5, "end": 20}
  ]
}
```

---

### Step 5: Create Commit Details Report (1 minute)

**Create `commit_details_report.py`:**
```python
#!/usr/bin/env python3
"""
Commit Details Report - Line-by-line AI attribution
"""

import requests
import os
import sys
from datetime import datetime

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class CommitDetails:
    """Commit Details with Blame Annotations"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com"
        self.auth = (API_KEY, "")
    
    def get_commit_details(self, commit_hash, branch=None):
        """Get detailed commit information."""
        url = f"{self.base_url}/analytics/ai-code/commits/{commit_hash}"
        
        if branch:
            url += f"?branch={branch}"
        
        response = requests.get(url, auth=self.auth)
        
        if response.status_code == 404:
            print(f"❌ Commit not found: {commit_hash}")
            return None
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            return None
        
        return response.json()
    
    def print_commit_summary(self, commit_hash, branch=None):
        """Print a human-readable commit summary."""
        data = self.get_commit_details(commit_hash, branch)
        
        if not data:
            return
        
        commits = data.get("commits", [])
        conversations = data.get("conversations", [])
        
        if not commits:
            print("No commit data found")
            return
        
        commit = commits[0]
        print(f"\n📝 Commit: {commit_hash[:8]}...")
        print(f"   Source: {commit.get('commitSource', 'unknown')}")
        print("=" * 50)
        
        # Build file to conversation mapping
        file_conversations = {}
        for annotation in commit.get("rangeAnnotations", []):
            file_path = annotation.get("filePath", "unknown")
            for group in annotation.get("groups", []):
                conv_id = group.get("conversationId")
                if conv_id:
                    if file_path not in file_conversations:
                        file_conversations[file_path] = []
                    file_conversations[file_path].append({
                        "conversationId": conv_id,
                        "model": group.get("model"),
                        "ranges": group.get("ranges", []),
                        "operationType": group.get("operationType")
                    })
        
        # Print file information
        print(f"\n📁 Files Modified ({len(file_conversations)})")
        print("-" * 30)
        
        for file_path, groups in file_conversations.items():
            total_lines = sum(
                sum(r.get("end", 0) - r.get("start", 0) + 1 for r in group["ranges"])
                for group in groups
            )
            print(f"\n   📄 {file_path}")
            print(f"      AI-generated lines: ~{total_lines}")
            
            for group in groups:
                conv_id = group["conversationId"]
                model = group.get("model", "unknown")
                op_type = group.get("operationType", "unknown")
                
                # Find conversation details
                conv = next((c for c in conversations if c.get("id") == conv_id), None)
                
                if conv:
                    print(f"      💬 Conversation: {conv.get('title', 'Untitled')}")
                    print(f"         Model: {model}")
                    print(f"         Operation: {op_type}")
                    print(f"         Summary: {conv.get('tldr', 'No summary')[:80]}...")
                
                # Print line ranges
                ranges_str = ", ".join([f"{r['start']}-{r['end']}" for r in group["ranges"]])
                print(f"         Lines: {ranges_str}")
        
        # Print conversation details
        if conversations:
            print(f"\n💬 Conversations ({len(conversations)})")
            print("-" * 30)
            for conv in conversations:
                print(f"\n   📋 {conv.get('title', 'Untitled')}")
                print(f"      ID: {conv.get('id')}")
                print(f"      TLDR: {conv.get('tldr', 'No summary')}")
                if conv.get('summaryBullets'):
                    print(f"      Key points:")
                    for bullet in conv.get('summaryBullets', [])[:3]:
                        print(f"         • {bullet}")

def main():
    print("🚀 Commit Details Report (Alpha)")
    print("=" * 40)
    print("Note: This endpoint is in limited alpha")
    
    if len(sys.argv) < 2:
        print("\nUsage: python commit_details_report.py <commit_hash> [branch]")
        print("Example: python commit_details_report.py 0aabf603")
        print("\nTo get a commit hash, run:")
        print("  python ai_commit_report.py")
        sys.exit(1)
    
    commit_hash = sys.argv[1]
    branch = sys.argv[2] if len(sys.argv) > 2 else None
    
    details = CommitDetails()
    details.print_commit_summary(commit_hash, branch)

if __name__ == "__main__":
    main()
```

---

## Expected Output

### Step 5 Output:
```
🚀 Commit Details Report (Alpha)
========================================

📝 Commit: 0aabf603...
   Source: ide
==================================================

📁 Files Modified (2)
------------------------------

   📄 src/auth/login.ts
      AI-generated lines: ~33
      💬 Conversation: Refactor authentication module
         Model: claude-4.5-sonnet
         Operation: insert
         Summary: Extracted login and validation into separate functions...
         Lines: 10-25, 42-58

   📄 src/auth/validation.ts
      AI-generated lines: ~16
      💬 Conversation: Refactor authentication module
         Model: claude-4.5-sonnet
         Operation: modify
         Summary: Extracted login and validation into separate functions...
         Lines: 5-20

💬 Conversations (1)
------------------------------

   📋 Refactor authentication module
      ID: conv_abc123
      TLDR: Extracted login and validation into separate functions
      Key points:
         • Created AuthService class with login method
         • Added input validation for email and password
         • Updated error handling to use custom exceptions
```

---

## Response Fields Reference

### Commit Object Fields

| Field | Description |
|-------|-------------|
| `commitHash` | Git commit hash |
| `commitSource` | Where commit originated (`ide`, `cli`, `cloud`) |
| `rangeAnnotations` | File-level blame data |
| `rangeAnnotations[].filePath` | Path to the file |
| `rangeAnnotations[].groups[].conversationId` | ID of conversation that generated this code |
| `rangeAnnotations[].groups[].model` | AI model used |
| `rangeAnnotations[].groups[].operationType` | Type of operation (`insert`, `modify`, `delete`) |
| `rangeAnnotations[].groups[].ranges[].start` | Starting line number |
| `rangeAnnotations[].groups[].ranges[].end` | Ending line number |

### Conversation Object Fields

| Field | Description |
|-------|-------------|
| `id` | Unique conversation identifier |
| `title` | Conversation title |
| `tldr` | Brief summary (Too Long; Didn't Read) |
| `overview` | Detailed overview |
| `summaryBullets` | Array of key points |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Alpha status** | Endpoint in limited alpha, may not be available |
| **Conversation tracking** | Requires conversation insights enabled |
| **Line numbers** | 1-indexed line numbers |
| **Multiple commits** | Up to 10 commit hashes can be requested at once |

---

## Success Criteria

- [ ] Retrieved commit hash from AI commits endpoint
- [ ] Got detailed commit information
- [ ] Retrieved multiple commits at once
- [ ] Parsed line annotations
- [ ] Created commit details report script

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 404 Not Found | Commit may not exist or not tracked by Cursor |
| 403 Forbidden | Endpoint in alpha; may not be available to your team |
| No conversations | Conversation insights may be disabled |
| Empty annotations | Commit may have no AI-generated code |

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved commit hash from AI commits endpoint
- [ ] Got detailed commit information
- [ ] Retrieved multiple commits at once
- [ ] Parsed line annotations
- [ ] Created commit details report script
