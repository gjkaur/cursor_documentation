# Exercise 9.5: Daily Active Users (DAU)

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.5)  
**Time:** 10 min  
**Difficulty:** Beginner

**Objective:** Report daily active users over a date range.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '{avg_weekly: ([.daily[-7:] | .[].activeUsers] | add / length),
         peak: ([.daily[] | .activeUsers] | max)}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

**Python leadership report:**
- Average/median/peak DAU · adoption rate (% of team)
- WoW growth rate · weekly averages
- Health assessment: >80% excellent · >50% good · <30% investigate

---

## Success criteria

- [ ] Average/median/peak DAU · adoption rate (% of team)
- [ ] WoW growth rate · weekly averages
- [ ] Health assessment: >80% excellent · >50% good · <30% investigate
- [ ] Calculated DAU · adoption metrics · leadership-ready report

---

## Additional reference

## Expected Output

### Step 5 Output:
```
🚀 DAU Dashboard
========================================

📊 DAU Dashboard
Period: Last 30 days
==================================================

📅 Latest Day (2025-01-16)
   Total DAU: 38
   CLI: 4
   Cloud Agents: 34
   Bugbot: 12

📈 Averages (Last 30 days)
   DAU: 38.5
   CLI: 4.2
   Cloud Agents: 35.1
   Bugbot: 11.3

📈 Trend: Moderate growth (+8.2%)

🎯 Product Adoption (Last 30 days)
------------------------------
   CLI: 10.9% of DAU
   Cloud Agents: 91.2% of DAU
   Bugbot: 29.4% of DAU

📊 Weekly DAU Trend (Last 7 days)
----------------------------------------
   01-10 ████████████████████████████████ 42
   01-11 ██████████████████████████████ 40
   01-12 ████████████████████████████████ 41
   01-13 ████████████████████████████ 37
   01-14 ████████████████████████████ 36
   01-15 ████████████████████████████████ 42
   01-16 ██████████████████████████████ 38

✅ Exported to dau_export.csv
```

---

## Response Fields Reference

| Field | Description |
|-------|-------------|
| `date` | Date in YYYY-MM-DD format |
| `dau` | Total daily active users |
| `cli_dau` | Users who used CLI |
| `cloud_agent_dau` | Users who used Cloud Agents |
| `bugbot_dau` | Users who used Bugbot |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /analytics/team/dau` |
| **Active user definition** | Used at least one AI feature |
| **Date range** | Maximum 30 days |
| **Default** | Last 7 days if not specified |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data | Team may have no activity in date range |
| 403 Forbidden | Enterprise plan required |

---
