# Exercise 10.3: Granular AI Change Events

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/module-10-marp.md` (Lesson 10.3)  
**Time:** 7 min  
**Difficulty:** Beginner

**Objective:** Query per-change AI events for compliance reporting.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/events?startDate=$START&endDate=$END&limit=100" \
  | jq '.events[] | {user: .user.email, file: .filePath, model: .modelId, accepted: .accepted}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Acceptance rate by model: group events → total vs. accepted per model

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

`generate_compliance_report()` for last 90 days:

- Acceptance rate by model (table)
- Top 10 files with most AI changes (needs review)
- Export `compliance_export.csv` for auditors:
  - timestamp, user_email, model_id, file_path, line_start, line_end, accepted

---

## Success criteria

- [ ] Acceptance rate by model (table)
- [ ] Top 10 files with most AI changes (needs review)
- [ ] Export `compliance_export.csv` for auditors:
- [ ] timestamp, user_email, model_id, file_path, line_start, line_end, accepted
- [ ] Retrieved events · calculated acceptance rates · compliance export

---

## Additional reference

## Expected Output

### Step 5 Output:
```
🚀 Granular AI Change Metrics
========================================

📊 Granular AI Change Metrics Report
Period: 30d to now
============================================================

📈 Overall Statistics
----------------------------------------
   Total AI changes: 1,250
   Total lines added: 15,500
   Average lines/change: 12.4

🔧 Breakdown by Source
----------------------------------------
   COMPOSER (Agent): 456 changes (61.2% lines)
   TAB (Completions): 794 changes (38.8% lines)
   Avg COMPOSER size: 24.8 lines
   Avg TAB size: 4.2 lines

📁 Top File Extensions by Lines Added
----------------------------------------
   .ts        12,500 lines ( 450 changes)
   .tsx        8,900 lines ( 320 changes)
   .py         5,600 lines ( 210 changes)
   .js         3,400 lines ( 150 changes)
   .c          2,100 lines (  80 changes)

🧠 Model Distribution (COMPOSER changes only)
----------------------------------------
   claude-4.5-sonnet          234 (51.3%)
   composer-2                 123 (27.0%)
   gpt-5.2                     67 (14.7%)
   claude-4.7-opus             32 ( 7.0%)

📅 Daily AI Acceptance (Last 7 days)
----------------------------------------
   2025-01-25 ████████ 845 lines
   2025-01-26 ███████ 723 lines
   2025-01-27 ██████████ 1,023 lines
   2025-01-28 ███████ 698 lines
   2025-01-29 ████████ 812 lines
   2025-01-30 ██████ 567 lines
   2025-01-31 █████████ 945 lines
```

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `changeId` | Unique ID for this acceptance event |
| `userId` | Encoded user ID |
| `userEmail` | User's email address |
| `source` | Source of AI change (`TAB` or `COMPOSER`) |
| `model` | AI model used (COMPOSER only) |
| `totalLinesAdded` | Lines added in this change |
| `metadata` | File-level details (fileName, fileExtension, linesAdded, linesDeleted) |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Granularity** | Each change is a single AI acceptance event |
| **vs Commits** | Changes can span multiple files (unlike commits) |
| **Metadata** | May be omitted in privacy mode |
| **Pagination** | Use `page` and `pageSize` for large datasets |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data | No AI acceptances in date range |
| Empty metadata | Privacy mode may be enabled |
| 403 Forbidden | Enterprise plan required |

---
