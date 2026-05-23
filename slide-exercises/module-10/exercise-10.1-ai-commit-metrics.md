# Exercise 10.1: AI Commit Metrics

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/module-10-marp.md` (Lesson 10.1)  
**Time:** 8 min  
**Difficulty:** Beginner

**Objective:** Fetch AI commit metrics and calculate contribution percentage.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
END=$(date +%Y-%m-%d)
START=$(date -d "30 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/commits?startDate=$START&endDate=$END&repo=https://github.com/YOUR_ORG/YOUR_REPO" \
  | jq '.'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---



```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/commits?startDate=$START&endDate=$END" \
  | jq '{
      total_commits: .summary.totalCommits,
      ai_commits: .summary.aiAuthoredCommits,
      ai_percentage: (.summary.aiAuthoredCommits / .summary.totalCommits * 100),
      lines_saved: .summary.aiGeneratedLines
    }'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Python `calculate_ai_roi()`:

```
AI-generated lines vs. human-written lines (%)
Estimated time saved (10 lines/min assumption)
Estimated cost saved ($100/hr developer cost)
AI usage cost → Net ROI
```

`contributor_breakdown()` — AI %, AI lines, commits per developer

---

## Success criteria

- [ ] Retrieved metrics · calculated AI % · generated ROI analysis

---

## Additional reference

## Expected Output

### Step 5 Output:
```
🚀 AI Commit Metrics
========================================

📊 AI Commit Metrics Report
Period: 30d to now
============================================================

📈 Overall Statistics
----------------------------------------
   Total commits: 156
   Total lines added: 15,234
   AI-generated lines: 9,876
   Human-written lines: 5,358

🤖 AI Contribution Breakdown
----------------------------------------
   Tab completions: 4,567 (30.0%)
   Agent edits: 5,309 (34.8%)
   Total AI: 64.8%

   AI vs Human: [████████████████████████████████░░░░░░░░░░░░░░░░░░░░]
   AI         64.8%                                    Human 35.2%

📝 Commit Source Breakdown
----------------------------------------
   ide: 142 (91.0%)
   cloud: 10 (6.4%)
   cli: 4 (2.6%)

👥 User Breakdown (Top 10 by AI usage)
----------------------------------------
   1. alice@company.com           78.2% AI (45 commits)
   2. bob@company.com             71.4% AI (38 commits)
   3. carol@company.com           65.3% AI (32 commits)
   4. dave@company.com            52.1% AI (28 commits)
```

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `commitHash` | Git commit hash |
| `userId` | Encoded user ID |
| `userEmail` | User's email address |
| `repoName` | Repository name |
| `commitSource` | Where commit originated (`ide`, `cli`, `cloud`) |
| `totalLinesAdded` | Total lines added in commit |
| `tabLinesAdded` | Lines added via Tab completions |
| `composerLinesAdded` | Lines added via Agent edits |
| `nonAiLinesAdded` | Human-written lines |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Availability** | Enterprise only, AI Code Tracking API |
| **Data collection** | On-device detection, only line counts stored |
| **Date range** | Maximum 30 days per request |
| **Pagination** | Use `page` and `pageSize` for large datasets |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key |
| 403 Forbidden | AI Code Tracking requires Enterprise plan |
| No data | No commits with AI tracking in date range |
| Empty items | Try longer date range or different repo |

---
