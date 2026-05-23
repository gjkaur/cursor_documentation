# Exercise 9.6: Leaderboards

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.6)  
**Time:** 11 min  
**Difficulty:** Beginner

**Objective:** Build leaderboards for tabs, AI lines, and agent runs.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**1. Engagement leaderboard** — rank by request count (anonymized emails)

**2. Efficiency leaderboard** — tokens per dollar spent

**3. Savings leaderboard** — users who saved by choosing efficient models over Opus

```python
def anonymize_email(email):
    local = email.split('@')[0]
    return local[:2] + "..." + local[-2:]
```

---

## Success criteria

- [ ] Anonymized · efficiency-focused · savings-focused leaderboards

---

## Additional reference

## Expected Output

### Step 5 Output:
```
🚀 Leaderboard Report Generator
========================================

🏆 Cursor Leaderboard Report
Period: 30d to today
============================================================

📋 TAB COMPLETIONS LEADERBOARD
Total users: 142
------------------------------------------------------------
Rank   User                           Accepts      Lines   Accept %
------------------------------------------------------------
1      alice@company.com                 1,334      3,455      23.3%
2      bob@company.com                     796      2,090      27.3%
3      carol@company.com                   654      1,890      24.1%
4      dave@company.com                    521      1,234      22.8%
5      eve@company.com                     498      1,102      21.5%

🤖 AGENT EDITS LEADERBOARD
Total users: 142
------------------------------------------------------------
Rank   User                           Accepts      Lines   Line Accept %
------------------------------------------------------------
1      alice@company.com                   914     65,947        32.7%
2      bob@company.com                     843     61,709       120.8%
3      carol@company.com                   712     54,321        34.2%
4      dave@company.com                    598     43,210        29.8%
5      eve@company.com                     445     32,109        27.6%

📄 Page 1 of 15
   Showing top 10 of 142 users

🏅 Top Performers (by lines accepted)
----------------------------------------
   1. alice@company.com: 3,455 lines
   2. bob@company.com: 2,090 lines
   3. carol@company.com: 1,890 lines
   4. dave@company.com: 1,234 lines
   5. eve@company.com: 1,102 lines
```

---

## Response Fields Reference

### Tab Leaderboard Fields

| Field | Description |
|-------|-------------|
| `email` | User's email address |
| `user_id` | Encoded user ID |
| `total_accepts` | Number of Tab completions accepted |
| `total_lines_accepted` | Lines accepted via Tab |
| `total_lines_suggested` | Lines suggested by Tab |
| `accept_ratio` | Acceptance rate (accepts / suggestions) |
| `line_acceptance_ratio` | Lines accepted / lines suggested |
| `rank` | User's rank (1 = best) |

### Agent Leaderboard Fields

| Field | Description |
|-------|-------------|
| `total_accepts` | Number of Agent edits accepted |
| `total_lines_accepted` | Lines accepted via Agent |
| `line_acceptance_ratio` | Lines accepted / lines suggested |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Filtered users show actual rank** | They appear with team-wide rank, not filtered rank |
| **Two separate leaderboards** | Tab completions and Agent edits are separate |
| **Pagination** | Use `page` and `pageSize` for large teams |
| **Default pageSize** | 10 users per page |
| **Max pageSize** | 500 users per page |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data | Team may have no activity in date range |
| 403 Forbidden | Enterprise plan required |
| User not found in filter | Check email spelling or user ID format |

---
