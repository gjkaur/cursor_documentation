# Exercise 10.4: Reporting Dashboard Architecture

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/module-10-marp.md` (Lesson 10.4)  
**Time:** Take-home  
**Difficulty:** Beginner

**Objective:** Design a leadership dashboard combining analytics APIs.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

_No slide steps extracted — use the additional reference below if present._

---

## Additional reference

## Expected Dashboard View

```
┌─────────────────────────────────────────────────────────────────┐
│  📊 Cursor Analytics Dashboard                                  │
│  Team AI Usage & Adoption Metrics                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────┐│
│  │Active    │ │Total     │ │AI Lines  │ │AI %     │ │Top    ││
│  │Members:25│ │Commits:  │ │Added:    │ │64.8%    │ │Model: ││
│  │          │ │1,234     │ │29,876    │ │         │ │claude ││
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └───────┘│
├─────────────────────────────────────────────────────────────────┤
│  📈 Daily Active Users (Last 7 Days)                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Line Chart                            │   │
│  └─────────────────────────────────────────────────────────┘   │
├──────────────────────────────┬──────────────────────────────────┤
│  🤖 Model Usage              │  🏆 Top Users by Tab Accepts     │
│  ┌────────────────────────┐  │  ┌─────┬─────────┬────────┬─────┐│
│  │      Bar Chart         │  │  │Rank │ User    │Accepts │Lines││
│  └────────────────────────┘  │  │ 1   │ alice   │ 1,334  │3,455││
│                              │  │ 2   │ bob     │ 796    │2,090││
│                              │  │ 3   │ carol   │ 654    │1,890││
│                              │  └─────────────────────────────┘│
├──────────────────────────────┴──────────────────────────────────┤
│  💚 AI vs Human Code Contribution                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Doughnut Chart                          │   │
│  │            AI 64.8%  │  Human 35.2%                     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Check Admin API key |
| Empty charts | No data in selected date range |
| CORS error | Flask-CORS should handle this |
| Port in use | Change port number |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Multi-API integration** | Combine data from 4+ Cursor APIs |
| **Real-time updates** | 5-minute auto-refresh |
| **Visual analytics** | Charts for all key metrics |
| **Team insights** | Usage, adoption, contribution |

---

## 🎉 Congratulations! You've Completed All 23 API Exercises! 🎉

You can now:
- ✅ Authenticate and use all Cursor APIs
- ✅ Create and manage Cloud Agents programmatically
- ✅ Stream real-time agent responses
- ✅ Track team usage and analytics
- ✅ Analyze AI code contribution
- ✅ Set spending limits and manage users
- ✅ Handle webhooks and notifications
- ✅ Build custom dashboards and automation
