# Exercise 9.4: Model Usage Analytics

**Module 9:** Admin and Analytics APIs  
**Slides:** `slides/module-09-marp.md` (Lesson 9.4)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Analyze model usage and identify optimization opportunities.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/models?startDate=$START&endDate=$END" \
  | jq '.models[] | {model: .modelId, cost: .cost, requests: .requestCount}'

# Find Opus overuse per user
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/users?startDate=$START&endDate=$END" \
  | jq '.users[] | select(.modelBreakdown."claude-4.7-opus" != null)'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

`generate_optimization_report()`:

- Model cost breakdown (% of total)
- Users on Claude Opus → suggest Sonnet for non-critical tasks
- High Sonnet usage → suggest GPT-5.3 Codex (40% savings)
- Estimated monthly savings if guidelines applied

---

## Success criteria

- [ ] Model cost breakdown (% of total)
- [ ] Users on Claude Opus → suggest Sonnet for non-critical tasks
- [ ] High Sonnet usage → suggest GPT-5.3 Codex (40% savings)
- [ ] Estimated monthly savings if guidelines applied
- [ ] Retrieved model breakdown · identified expensive users · generated recommendations

---

## Additional reference

## Expected Output

### Step 5 Output:
```
🚀 Model Usage Analytics
========================================

📊 Model Usage Report
Period: 30d to today
==================================================

📈 Model Usage Summary
--------------------------------------------------
Model                          Messages    Users   Avg/User
--------------------------------------------------
claude-4.5-sonnet                 8,520       28        304
gpt-5-mini                        5,600       18        311
composer-2                        4,500       22        204
gpt-5.2                           3,100       15        206
claude-4.7-opus                   2,100       12        175

📊 Market Share
--------------------------------------------------
claude-4.5-sonnet                 35.5% █████████████████
gpt-5-mini                        23.3% ███████████
composer-2                        18.8% █████████
gpt-5.2                           12.9% ██████
claude-4.7-opus                    8.8% ████

💰 Estimated Cost (approximate)
--------------------------------------------------
   claude-4.7-opus                  $52.50
   claude-4.5-sonnet                $25.56
   gpt-5.2                           $7.75
   composer-2                       $11.25
--------------------------------------------------
   Estimated total                 $101.31

💡 Tip: Use composer-2 or gpt-5-mini for cost savings
```

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /analytics/team/models` |
| **Authentication** | Admin API key (Enterprise) |
| **Response** | Daily breakdown by model |
| **Per-user** | `GET /analytics/by-user/models` |
| **Date range** | Maximum 30 days |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Use Admin API key |
| 403 Forbidden | Enterprise plan required |
| No data | Check date range and team activity |

---
