# Exercise 10.2: Bulk Export via CSV Streaming

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/module-10-marp.md` (Lesson 10.2)  
**Time:** 7 min  
**Difficulty:** Beginner

**Objective:** Stream large CSV exports for BI tools.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -N -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/export/csv?startDate=$START&endDate=$END&type=commits" \
  -o cursor_commits_export.csv

head -10 cursor_commits_export.csv
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---



Python `stream_to_dataframe()` → pandas DataFrame:

```python
export_for_bi():
  bi_commits.csv   # commit data
  bi_events.csv    # event data
  bi_usage.csv     # usage data
```

Upload to Metabase, PowerBI, or Tableau via CSV import

---

## Success criteria

- [ ] Streamed CSV · loaded into DataFrame · created BI-ready files

---

## Additional reference

## Expected Output

### Step 4 Output:
```
📊 Analyzing ai_commits_30d.csv
==================================================

📈 Basic Statistics
------------------------------
   Total commits: 1,234
   Date range: 2025-01-01 to 2025-01-31
   Unique users: 25
   Unique repos: 8

🤖 AI Contribution
------------------------------
   Total lines added: 45,678
   AI-generated lines: 29,876
   AI percentage: 65.4%

   Tab completions: 12,345 (27.0%)
   Agent edits: 17,531 (38.4%)

👥 Top Users by AI Percentage
-----------------------------------
   alice@company.com           78.2% (45 commits)
   bob@company.com             71.4% (38 commits)
   carol@company.com           65.3% (32 commits)

📁 Top Repositories by AI Lines
-----------------------------------
   main-app                     15,234 lines (68% AI)
   backend-api                  8,456 lines (72% AI)
   mobile-app                   6,123 lines (55% AI)

📅 Daily AI Percentage Trend (Last 7 days)
-------------------------------------------
   2025-01-25 ████████████████████ 78%
   2025-01-26 ██████████████████ 72%
   2025-01-27 ████████████████████ 76%
   2025-01-28 █████████████████ 68%
   2025-01-29 ████████████████████ 80%
   2025-01-30 ██████████████████ 74%
   2025-01-31 ████████████████████ 79%
```

---

## CSV Columns Reference

| Column | Description |
|--------|-------------|
| `commit_hash` | Git commit hash |
| `user_id` | Encoded user ID |
| `user_email` | User's email address |
| `repo_name` | Repository name |
| `branch_name` | Branch name |
| `is_primary_branch` | Whether this is the primary branch |
| `commit_source` | Where commit originated (`ide`, `cli`, `cloud`) |
| `total_lines_added` | Total lines added in commit |
| `total_lines_deleted` | Total lines deleted in commit |
| `tab_lines_added` | Lines added via Tab completions |
| `tab_lines_deleted` | Lines deleted via Tab completions |
| `composer_lines_added` | Lines added via Agent edits |
| `composer_lines_deleted` | Lines deleted via Agent edits |
| `non_ai_lines_added` | Human-written lines added |
| `non_ai_lines_deleted` | Human-written lines deleted |
| `message` | Commit message |
| `commit_ts` | Commit timestamp |
| `created_at` | Ingestion timestamp |

---

## Important Notes

| Note | Description |
|------|-------------|
| **CSV streaming** | Streams in pages of 10,000 records |
| **No pagination params** | Use `startDate` and `endDate` only |
| **Large exports** | CSV is more efficient than JSON for large datasets |
| **Filtering** | Only `startDate`, `endDate`, and `user` parameters |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Empty CSV | No data in date range; try longer range |
| Partial download | Use `-L` flag with curl to follow redirects |
| Memory issues | CSV streams; shouldn't cause memory problems |
| Unicode errors | CSV is UTF-8 encoded |

---
