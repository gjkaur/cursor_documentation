# AI Code Tracking API – Complete Beginner's Guide

This document explains the **AI Code Tracking API** – how to programmatically track which lines of code were written by AI (Tab completions, Agent edits) versus humans, directly from your git commits.

Think of this as the **API version of Cursor Blame** – giving you data about AI contribution to your codebase.

Let me break this down for a complete beginner.

---

## What Is the AI Code Tracking API? (The 10-Second Summary)

**The AI Code Tracking API lets you programmatically track AI-generated code contributions across your team's repositories** – showing how many lines were added by Tab completions, Agent edits, or humans.

| Without AI Code Tracking | With AI Code Tracking |
|--------------------------|----------------------|
| Guess what AI contributed | Know exactly what AI wrote |
| Manual code review | Automated attribution |
| No visibility into AI adoption | Data-driven insights |

> *"Availability: Enterprise only. Status: Alpha (response shapes and fields may change)"*

**Important:** This is an **alpha** feature. APIs might change, so don't build critical systems that depend on exact behavior yet.

---

## How AI Code Tracking Works

When a user accepts AI suggestions (Tab completions or Agent edits), Cursor records signatures of those lines. Later, when the user commits code, Cursor compares the commit diff against those signatures to attribute lines.

**Key points:**
- All detection happens **on-device** – code never leaves the user's computer
- Only **line counts** (metadata) are stored and available via API
- Works for commits from IDE (`ide`), CLI (`cli`), and Cloud Agents (`cloud`)

---

## Authentication

All API requests use **Basic Authentication** with an API key (same method as Admin API).

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/analytics/ai-code/commits
```

**Note:** The colon after the API key is required (empty password).

### Where to Get an API Key:

1. Log into Cursor Dashboard
2. Go to **Settings → Advanced → Admin API Keys**
3. Generate an API key with `admin:*` scope

**Availability:** Enterprise only – contact sales to get access

---

## Endpoints Overview

| Endpoint | Method | Format | Description |
|----------|--------|--------|-------------|
| `/analytics/ai-code/commits` | GET | JSON (paginated) | Commit metrics with AI attribution |
| `/analytics/ai-code/commits.csv` | GET | CSV (streaming) | Commit metrics as CSV (large exports) |
| `/analytics/ai-code/changes` | GET | JSON (paginated) | Granular AI change events |
| `/analytics/ai-code/changes.csv` | GET | CSV (streaming) | AI change events as CSV |
| `/analytics/ai-code/commits/:commitHash` | GET | JSON | Detailed commit with blame (alpha, limited access) |

---

## 1. Get AI Commit Metrics (JSON)

### GET /analytics/ai-code/commits

Retrieve per-commit metrics with AI attribution – how many lines were added/deleted by Tab, Composer, or humans.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | string | now - 7 days | Start date (`7d`, `2025-01-01`, `now`) |
| `endDate` | string | now | End date (`0d`, `2025-01-31`, `now`) |
| `page` | number | 1 | Page number (1-based) |
| `pageSize` | number | 100 | Results per page (max 1000) |
| `user` | string | - | Filter by single user (email, encoded ID, or numeric ID) |

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `commitHash` | string | Git commit hash |
| `userId` | string | Encoded user ID (e.g., `user_abc123`) |
| `userEmail` | string | User's email address |
| `repoName` | string/null | Repository name |
| `branchName` | string/null | Branch name |
| `isPrimaryBranch` | boolean/null | Whether this is the default branch |
| `commitSource` | string | Where commit originated (`ide`, `cli`, `cloud`) |
| `totalLinesAdded` | number | Total lines added in commit |
| `totalLinesDeleted` | number | Total lines deleted in commit |
| `tabLinesAdded` | number | Lines added via Tab completions |
| `tabLinesDeleted` | number | Lines deleted via Tab completions |
| `composerLinesAdded` | number | Lines added via Composer/Agent |
| `composerLinesDeleted` | number | Lines deleted via Composer/Agent |
| `nonAiLinesAdded` | number/null | Non-AI lines added |
| `nonAiLinesDeleted` | number/null | Non-AI lines deleted |
| `message` | string/null | Commit message |
| `commitTs` | string/null | Commit timestamp (ISO format) |
| `createdAt` | string | Ingestion timestamp (ISO format) |

### Example Request

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100"
```

### Response Example

```json
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "commitSource": "ide",
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: extract analytics client",
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

### Understanding the Numbers

```
totalLinesAdded (120) = tabLinesAdded (50) + composerLinesAdded (40) + nonAiLinesAdded (30)
```

| Component | Meaning |
|-----------|---------|
| `tabLinesAdded` | Code written via Tab completions (inline suggestions) |
| `composerLinesAdded` | Code written via Agent (Composer) |
| `nonAiLinesAdded` | Code written manually by the developer |

---

## 2. Download AI Commit Metrics (CSV Streaming)

### GET /analytics/ai-code/commits.csv

Download commit metrics in CSV format – **streams data efficiently** for large exports (10,000 records at a time).

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | string | now - 7 days | Start date |
| `endDate` | string | now | End date |
| `user` | string | - | Filter by single user |

### CSV Columns

| Column | Description |
|--------|-------------|
| `commit_hash` | Git commit hash |
| `user_id` | Encoded user ID |
| `user_email` | User's email address |
| `repo_name` | Repository name |
| `branch_name` | Branch name |
| `is_primary_branch` | Whether this is the primary branch |
| `commit_source` | Where commit originated (`ide`, `cli`, `cloud`) |
| `total_lines_added` | Total lines added |
| `total_lines_deleted` | Total lines deleted |
| `tab_lines_added` | Lines added via Tab completions |
| `tab_lines_deleted` | Lines deleted via Tab completions |
| `composer_lines_added` | Lines added via Composer/Agent |
| `composer_lines_deleted` | Lines deleted via Composer/Agent |
| `non_ai_lines_added` | Non-AI lines added |
| `non_ai_lines_deleted` | Non-AI lines deleted |
| `message` | Commit message |
| `commit_ts` | Commit timestamp |
| `created_at` | Ingestion timestamp |

### Example Request

```bash
curl -L -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=30d&endDate=now" \
  -o commits.csv
```

### Sample CSV Output

```csv
commit_hash,commit_source,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,ide,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: extract analytics client",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,cloud,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Add error handling",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

---

## 3. Get AI Code Change Metrics (JSON)

### GET /analytics/ai-code/changes

Retrieve granular accepted AI changes – each change represents a single AI acceptance event (Tab completion or Agent edit). This is more detailed than commit-level aggregation.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | string | now - 7 days | Start date |
| `endDate` | string | now | End date |
| `page` | number | 1 | Page number (1-based) |
| `pageSize` | number | 100 | Results per page (max 1000) |
| `user` | string | - | Filter by single user |

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `changeId` | string | Deterministic ID for the change |
| `userId` | string | Encoded user ID |
| `userEmail` | string | User's email address |
| `source` | string | Source of AI change (`TAB` or `COMPOSER`) |
| `model` | string/null | AI model used (if available) |
| `totalLinesAdded` | number | Total lines added in this change |
| `totalLinesDeleted` | number | Total lines deleted in this change |
| `createdAt` | string | Ingestion timestamp (ISO format) |
| `metadata` | array | File metadata (may be omitted in privacy mode) |

### Example Request

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200"
```

### Response Example

```json
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        {
          "fileName": "src/analytics/report.ts",
          "fileExtension": "ts",
          "linesAdded": 12,
          "linesDeleted": 3
        },
        {
          "fileName": "src/analytics/ui.tsx",
          "fileExtension": "tsx",
          "linesAdded": 6,
          "linesDeleted": 1
        }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

### Change vs Commit: What's the Difference?

| Metric | Granularity | When to use |
|--------|-------------|-------------|
| **Commits** | Per git commit (aggregated) | Understanding overall AI contribution |
| **Changes** | Per AI acceptance event (granular) | Analyzing specific AI suggestions, debugging |

---

## 4. Download AI Code Change Metrics (CSV Streaming)

### GET /analytics/ai-code/changes.csv

Download change metrics in CSV format for large data extractions.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | string | now - 7 days | Start date |
| `endDate` | string | now | End date |
| `user` | string | - | Filter by single user |

### CSV Columns

| Column | Description |
|--------|-------------|
| `change_id` | Deterministic ID for the change |
| `user_id` | Encoded user ID |
| `user_email` | User's email address |
| `source` | Source of AI change (TAB or COMPOSER) |
| `model` | AI model used |
| `total_lines_added` | Total lines added |
| `total_lines_deleted` | Total lines deleted |
| `created_at` | Ingestion timestamp |
| `metadata_json` | JSON string of file metadata |

### Example Request

```bash
curl -L -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -o changes.csv
```

### Sample CSV Output

```csv
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

---

## 5. Get Commit Details (Alpha – Limited Access)

### GET /analytics/ai-code/commits/:commitHash

Retrieve detailed information for one or more commits, including **blame annotations** and referenced conversation metadata.

> *"This endpoint is in limited alpha and only available to select users. Response shapes may change."*

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `commitHash` | string (path) | Single commit hash or comma-separated list |
| `branch` | string (query) | Optional filter by branch name |

### Response Fields

| Field | Description |
|-------|-------------|
| `commits` | Array of commit objects with blame annotations |
| `commits[].rangeAnnotations[].filePath` | Path to the file |
| `commits[].rangeAnnotations[].groups[].conversationId` | ID of conversation that generated this code |
| `commits[].rangeAnnotations[].groups[].model` | AI model used |
| `commits[].rangeAnnotations[].groups[].ranges` | Line ranges (start/end) |
| `conversations` | Conversation metadata for referenced conversations |
| `conversations[].tldr` | Brief summary of the conversation |
| `conversations[].summaryBullets` | Key points from the conversation |

### Example Request (Single Commit)

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/commits/a1b2c3d4?branch=main"
```

### Example Request (Multiple Commits)

```bash
curl -u YOUR_API_KEY: \
  "https://api.cursor.com/analytics/ai-code/commits/abc123,def456,ghi789"
```

### Response Example

```json
{
  "commits": [
    {
      "commitHash": "0aabf603dc906e05bf5e4d9fd423fdd517f2e43f",
      "commitSource": "ide",
      "rangeAnnotations": [
        {
          "filePath": "src/analytics/report.ts",
          "groups": [
            {
              "conversationId": "conv_abc123",
              "model": "gpt-4o",
              "operationType": "insert",
              "ranges": [
                { "start": 10, "end": 25 },
                { "start": 42, "end": 58 }
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
      "title": "Refactor analytics module",
      "tldr": "Extracted report generation into separate functions",
      "overview": "Refactored the analytics module to improve maintainability...",
      "summaryBullets": [
        "Created dedicated report generator class",
        "Added unit tests for new functions",
        "Updated imports across affected files"
      ]
    }
  ]
}
```

**This endpoint tells you not just how many lines, but which lines (line numbers) and which conversation produced them!**

---

## Understanding the Data

### Commit Sources

| Source | Description |
|--------|-------------|
| `ide` | Commit made from Cursor IDE |
| `cli` | Commit made from Cursor CLI |
| `cloud` | Commit made by a Cloud Agent |

### AI Sources

| Source | Description |
|--------|-------------|
| `TAB` | Inline completions accepted by user |
| `COMPOSER` | Agent edits accepted by user |

### Lines Attribution Formula

```
totalLinesAdded = tabLinesAdded + composerLinesAdded + nonAiLinesAdded
totalLinesDeleted = tabLinesDeleted + composerLinesDeleted + nonAiLinesDeleted
```

### Privacy Mode

If privacy mode is enabled on the client, some metadata (like `fileName`) may be omitted from responses.

---

## Complete Example: Python Script

```python
#!/usr/bin/env python3
"""
AI Code Tracking API Examples
"""

import requests
import csv
import json
from datetime import datetime, timedelta

API_KEY = "your_api_key_here"
BASE_URL = "https://api.cursor.com"

def get_commit_metrics(start_date="7d", end_date="now", page=1, page_size=100):
    """Fetch AI commit metrics."""
    url = f"{BASE_URL}/analytics/ai-code/commits"
    auth = (API_KEY, "")
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "page": page,
        "pageSize": page_size
    }
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code == 429:
        print("Rate limit exceeded. Try again later.")
        return None
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    return response.json()

def download_commit_csv(start_date="7d", end_date="now", output_file="commits.csv"):
    """Download commit metrics as CSV."""
    url = f"{BASE_URL}/analytics/ai-code/commits.csv"
    auth = (API_KEY, "")
    params = {"startDate": start_date, "endDate": end_date}
    
    response = requests.get(url, auth=auth, params=params, stream=True)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Downloaded to {output_file}")
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_change_metrics(start_date="7d", end_date="now", page=1, page_size=100):
    """Fetch granular AI change events."""
    url = f"{BASE_URL}/analytics/ai-code/changes"
    auth = (API_KEY, "")
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "page": page,
        "pageSize": page_size
    }
    
    response = requests.get(url, auth=auth, params=params)
    
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    return response.json()

def calculate_ai_percentage(commits_data):
    """Calculate what percentage of code was AI-generated."""
    items = commits_data.get("items", [])
    if not items:
        return 0
    
    total_lines = sum(c.get("totalLinesAdded", 0) for c in items)
    ai_lines = sum(c.get("tabLinesAdded", 0) + c.get("composerLinesAdded", 0) for c in items)
    
    if total_lines == 0:
        return 0
    
    return (ai_lines / total_lines) * 100

def main():
    print("📊 AI Code Tracking API Demo")
    print("-" * 40)
    
    # 1. Get commit metrics for last 7 days
    print("\n1️⃣ Getting commit metrics (last 7 days)...")
    commits = get_commit_metrics(start_date="7d", end_date="now", page_size=10)
    
    if commits:
        print(f"   Found {commits.get('totalCount', 0)} commits")
        ai_percentage = calculate_ai_percentage(commits)
        print(f"   🤖 AI-generated code: {ai_percentage:.1f}%")
        
        # Show first commit
        first_commit = commits.get("items", [])[0] if commits.get("items") else None
        if first_commit:
            print(f"\n   📝 Sample commit:")
            print(f"      Hash: {first_commit.get('commitHash', 'N/A')[:8]}...")
            print(f"      Author: {first_commit.get('userEmail', 'N/A')}")
            print(f"      AI lines: +{first_commit.get('tabLinesAdded', 0) + first_commit.get('composerLinesAdded', 0)}")
            print(f"      Human lines: +{first_commit.get('nonAiLinesAdded', 0)}")
    
    # 2. Download CSV for deeper analysis
    print("\n2️⃣ Downloading CSV for last 30 days...")
    download_commit_csv(start_date="30d", end_date="now", output_file="commits_30d.csv")
    
    # 3. Get granular change metrics
    print("\n3️⃣ Getting granular change metrics (last 7 days)...")
    changes = get_change_metrics(start_date="7d", end_date="now", page_size=50)
    
    if changes:
        items = changes.get("items", [])
        tab_count = sum(1 for c in items if c.get("source") == "TAB")
        composer_count = sum(1 for c in items if c.get("source") == "COMPOSER")
        
        print(f"   Total AI changes: {len(items)}")
        print(f"   Tab completions: {tab_count}")
        print(f"   Agent edits: {composer_count}")
        
        # Show file extension breakdown
        extensions = {}
        for change in items[:20]:  # First 20 changes
            for meta in change.get("metadata", []):
                ext = meta.get("fileExtension", "unknown")
                extensions[ext] = extensions.get(ext, 0) + 1
        
        if extensions:
            print(f"\n   📁 Top file extensions:")
            for ext, count in sorted(extensions.items(), key=lambda x: -x[1])[:5]:
                print(f"      .{ext}: {count} changes")
    
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
```

---

## Complete Example: Bash Script

```bash
#!/bin/bash

API_KEY="your_api_key_here"
BASE_URL="https://api.cursor.com"

echo "📊 AI Code Tracking API Demo"
echo "============================"

# Get commit metrics (JSON)
echo -e "\n1️⃣ Getting commit metrics (last 7 days)..."
curl -s -u "$API_KEY:" \
  "$BASE_URL/analytics/ai-code/commits?startDate=7d&endDate=now&pageSize=10" | jq '.'

# Download commit metrics (CSV)
echo -e "\n2️⃣ Downloading commit metrics CSV..."
curl -L -s -u "$API_KEY:" \
  "$BASE_URL/analytics/ai-code/commits.csv?startDate=30d&endDate=now" \
  -o commits_30d.csv
echo "   Saved to commits_30d.csv"

# Get change metrics for a specific user
echo -e "\n3️⃣ Getting change metrics for user..."
curl -s -u "$API_KEY:" \
  "$BASE_URL/analytics/ai-code/changes?startDate=7d&endDate=now&pageSize=20&user=developer@company.com" | jq '.items[] | {source, totalLinesAdded, totalLinesDeleted}'

# Calculate AI percentage using jq
echo -e "\n4️⃣ Calculating AI percentage..."
curl -s -u "$API_KEY:" \
  "$BASE_URL/analytics/ai-code/commits?startDate=7d&endDate=now" | \
  jq '{
    total_lines: [.items[].totalLinesAdded] | add,
    ai_lines: ([.items[].tabLinesAdded] | add) + ([.items[].composerLinesAdded] | add),
    ai_percentage: ((([.items[].tabLinesAdded] | add) + ([.items[].composerLinesAdded] | add)) / ([.items[].totalLinesAdded] | add) * 100 | floor)
  }'
```

---

## Use Cases

| Use Case | How to Use |
|----------|------------|
| **Measure AI adoption** | Calculate % of code written by AI across your team |
| **Track model effectiveness** | See which models produce the most accepted code |
| **Team productivity analysis** | Compare AI usage across team members |
| **Cost attribution** | Understand which features drive AI usage |
| **Compliance reporting** | Document AI contribution to codebase |
| **Per-line attribution** | Use commit details endpoint to see exactly which lines came from AI |

---

## Tips

| Tip | Why |
|-----|-----|
| **Use CSV endpoints for large exports** | Streams 10,000 records at a time |
| **Use `user` parameter to filter** | Quickly analyze single developer |
| **Check `isPrimaryBranch`** | May be undefined if client couldn't resolve default branch |
| **`commitTs` vs `createdAt`** | `commitTs` is commit time; `createdAt` is ingestion time |
| **Commit hashes not unique** | Same commit may appear twice if amended |
| **Privacy mode affects fields** | Some metadata may be omitted |

---

## Limitations

| Limitation | Description |
|------------|-------------|
| **Alpha status** | Response shapes may change |
| **Enterprise only** | Requires Enterprise plan |
| **Multi-root workspaces** | Not supported (only top-level repo) |
| **Privacy mode** | Some metadata omitted |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Base URL** | `https://api.cursor.com/analytics/ai-code/` |
| **Authentication** | Basic Auth with admin-scoped API key |
| **Availability** | Enterprise only (contact sales) |
| **Status** | Alpha (may change) |
| **Date formats** | `7d`, `30d`, `2025-01-01`, `now` |
| **Commit sources** | `ide`, `cli`, `cloud` |
| **AI sources** | `TAB`, `COMPOSER` |
| **JSON pagination** | `page` (1-based), `pageSize` (max 1000) |
| **CSV streaming** | Use `-L` flag with curl |

---

## Common Beginner Questions

### Q: Is AI Code Tracking available on all plans?
**A:** No – only on **Enterprise plan**. Contact sales to get access.

### Q: Does this send my code to Cursor servers?
**A:** No – detection is **on-device**. Only line counts (metadata) are stored.

### Q: What's the difference between `/commits` and `/changes`?
**A:** `/commits` aggregates by git commit. `/changes` gives granular AI acceptance events.

### Q: Can I filter by a specific user?
**A:** Yes – use the `user` parameter with email, encoded ID, or numeric ID.

### Q: What does `isPrimaryBranch` mean?
**A:** True if branch equals the repo's default branch (e.g., `main`). May be undefined if info unavailable.

### Q: Why do I see the same commit twice?
**A:** Commit hashes aren't unique. Amending a commit creates a new hash but old data may remain.

### Q: What happens in privacy mode?
**A:** Some metadata (like `fileName`) may be omitted from responses.

### Q: What does the commit details endpoint show?
**A:** Line-by-line blame annotations – exactly which lines came from which AI conversation.

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is it?** | API to track AI-generated code in git commits |
| **Who can use it?** | Enterprise plan only (contact sales) |
| **What can I track?** | Lines added/deleted by Tab, Agent, or humans |
| **How is data collected?** | On-device detection, only line counts stored |
| **What formats?** | JSON (paginated) or CSV (streaming) |
| **Alpha status means?** | APIs may change – don't build critical systems yet |

---

## The Bottom Line

**The AI Code Tracking API gives enterprises visibility into how much AI contributes to their codebase – down to the line level.**

**Think of it as:**
- **Cursor Blame** = UI for AI attribution 👁️
- **AI Code Tracking API** = Data API for AI attribution 💻

**Use cases:**
- Measuring AI adoption across your team
- Tracking which models produce the most accepted code
- Generating compliance reports
- Understanding productivity gains from AI
- **Line-by-line attribution** (with commit details endpoint)

**Key features:**
- On-device detection – your code never leaves your machine
- CSV streaming for large exports
- Granular change-level data
- Commit-level aggregation
- **Blame annotations** – see exactly which lines came from which conversation (alpha)

**Limitations:**
- Enterprise plan only
- Alpha status – APIs may change
- Some metadata omitted in privacy mode
- Multi-root workspaces not supported
