# Cursor API Training – Optional Exercises Guide

Based on your audience (experienced engineers, platform/admin focus, hands-on API training), here is a breakdown of which API exercises are **essential**, **recommended**, and **optional**.

These 23 exercises cover the five Cursor APIs: **Cloud Agents** (all plans, Beta), **Admin** (Enterprise), **Analytics** (Enterprise), **AI Code Tracking** (Enterprise, alpha), and shared concepts like auth, rate limits, ETag caching, and webhooks.

---

## Quick Summary

| Category | Exercises | Count |
|----------|-----------|-------|
| **Essential (Must Do)** | 1, 2, 4, 5, 8, 9, 12, 13, 16, 20 | 10 |
| **Recommended (If Time Permits)** | 3, 6, 7, 10, 14, 17, 18, 21, 22 | 9 |
| **Optional (Skip or Demo Only)** | 11, 15, 19, 23 | 4 |

---

## Detailed Breakdown

### Track 1: Foundations (Exercises 1-4)

| Exercise | Essential | Recommended | Optional | Reason |
|----------|-----------|-------------|----------|--------|
| 1: Generate and Test API Keys | ✅ | | | Required for every API call – do this first |
| 2: Rate Limits and Error Handling | ✅ | | | Production reliability – every integration needs it |
| 3: ETag Caching | | ✅ | | Important for analytics, but skippable on day 1 |
| 4: List Available Models | ✅ | | | 5-min auth smoke test, useful for Cloud Agents |

**Track 1: 3 essential / 1 recommended**

---

### Track 2: Cloud Agents API (Exercises 5-7)

Cloud Agents is the only Cursor API available on **all plans**, so this track is the most universally relevant.

| Exercise | Essential | Recommended | Optional | Reason |
|----------|-----------|-------------|----------|--------|
| 5: Create a Cloud Agent | ✅ | | | Core agent launch flow – foundation for automation |
| 6: Stream Agent Responses | | ✅ | | SSE streaming is powerful but conceptually heavier |
| 7: List and Download Artifacts | | ✅ | | Important for CI integration, can follow Exercise 5 |

**Track 2: 1 essential / 2 recommended**

---

### Track 3: Admin API (Exercises 8-11)

Enterprise plan only. Skip this track entirely if your audience is on Pro/Business plans.

| Exercise | Essential | Recommended | Optional | Reason |
|----------|-----------|-------------|----------|--------|
| 8: List Team Members | ✅ | | | Simplest Admin API call – good entry point |
| 9: Get Daily Usage Data | ✅ | | | Most-asked-for admin report |
| 10: Set User Spend Limits | | ✅ | | Important for cost governance |
| 11: Remove Team Member | | | ✅ | Destructive – demo only to avoid accidents |

**Track 3: 2 essential / 1 recommended / 1 optional**

---

### Track 4: Analytics API (Exercises 12-15)

Enterprise plan only. Most commonly used for dashboards and adoption reporting.

| Exercise | Essential | Recommended | Optional | Reason |
|----------|-----------|-------------|----------|--------|
| 12: Get Model Usage Analytics | ✅ | | | Direct cost/usage insight – highly demanded |
| 13: Get Daily Active Users (DAU) | ✅ | | | Core adoption metric for leadership |
| 14: Get Leaderboard | | ✅ | | Useful but politically sensitive – cover briefly |
| 15: Get Conversation Insights | | | ✅ | Enterprise-only, narrow use case |

**Track 4: 2 essential / 1 recommended / 1 optional**

---

### Track 5: AI Code Tracking API (Exercises 16-19)

Enterprise plan, alpha. Skip or demo if AI attribution is not a goal.

| Exercise | Essential | Recommended | Optional | Reason |
|----------|-----------|-------------|----------|--------|
| 16: Get AI Commit Metrics | ✅ | | | Headline AI-attribution metric |
| 17: Download AI Commit Metrics CSV | | ✅ | | CSV streaming for BI tools – great for reporting |
| 18: Get Granular AI Change Metrics | | ✅ | | Per-event detail for compliance |
| 19: Get Commit Details (Alpha) | | | ✅ | Alpha endpoint – demo only, may change |

**Track 5: 1 essential / 2 recommended / 1 optional**

---

### Track 6: Webhooks & Workflows (Exercises 20-23)

Cross-cutting integration exercises that build on earlier tracks.

| Exercise | Essential | Recommended | Optional | Reason |
|----------|-----------|-------------|----------|--------|
| 20: Create a Webhook Endpoint | ✅ | | | HMAC verification is critical for production |
| 21: Test Webhooks with ngrok | | ✅ | | Practical local-dev pattern, follows Exercise 20 |
| 22: Build Automated Agent Workflow | | ✅ | | Capstone for Cloud Agents track |
| 23: Build a Complete Dashboard | | | ✅ | Long (25 min), advanced – great take-home project |

**Track 6: 1 essential / 2 recommended / 1 optional**

---

## Summary Table

| Track | Essential | Recommended | Optional | Total |
|-------|-----------|-------------|----------|-------|
| 1: Foundations | 3 | 1 | 0 | 4 |
| 2: Cloud Agents API | 1 | 2 | 0 | 3 |
| 3: Admin API | 2 | 1 | 1 | 4 |
| 4: Analytics API | 2 | 1 | 1 | 4 |
| 5: AI Code Tracking API | 1 | 2 | 1 | 4 |
| 6: Webhooks & Workflows | 1 | 2 | 1 | 4 |
| **Total** | **10** | **9** | **4** | **23** |

---

## 2-Day Training Plan (Using Essential + Recommended)

### Day 1 (Foundations + Cloud Agents + Webhooks)

| Time | Exercise | Type |
|------|----------|------|
| 9:00-9:15 | Setup & welcome | |
| 9:15-9:25 | 1: Generate and Test API Keys | Essential |
| 9:25-9:35 | 2: Rate Limits and Error Handling | Essential |
| 9:35-9:45 | 3: ETag Caching | Recommended |
| 9:45-9:50 | 4: List Available Models | Essential |
| 9:50-10:00 | 5: Create a Cloud Agent | Essential |
| 10:00-10:15 | Break | |
| 10:15-10:30 | 6: Stream Agent Responses | Recommended |
| 10:30-10:45 | 7: List and Download Artifacts | Recommended |
| 10:45-11:00 | 20: Create a Webhook Endpoint | Essential |
| 11:00-11:10 | 21: Test Webhooks with ngrok | Recommended |
| 11:10-11:20 | 22: Build Automated Agent Workflow | Recommended |
| 11:20-12:00 | Open lab / repeat exercises | |
| 12:00-1:00 | Lunch | |
| 1:00-2:00 | Free integration time / Q&A | |
| 2:00-2:30 | Day 1 wrap-up | |

**Day 1: 5 essential + 5 recommended = 10 exercises**

---

### Day 2 (Admin + Analytics + AI Code Tracking)

| Time | Exercise | Type |
|------|----------|------|
| 9:00-9:15 | Day 1 recap | |
| 9:15-9:20 | 8: List Team Members | Essential |
| 9:20-9:30 | 9: Get Daily Usage Data | Essential |
| 9:30-9:40 | 10: Set User Spend Limits | Recommended |
| 9:40-9:50 | 11: Remove Team Member (Demo) | Optional |
| 9:50-10:00 | 12: Get Model Usage Analytics | Essential |
| 10:00-10:10 | 13: Get Daily Active Users | Essential |
| 10:10-10:25 | Break | |
| 10:25-10:35 | 14: Get Leaderboard | Recommended |
| 10:35-10:45 | 15: Conversation Insights (Demo) | Optional |
| 10:45-10:55 | 16: Get AI Commit Metrics | Essential |
| 10:55-11:05 | 17: Download AI Commit Metrics CSV | Recommended |
| 11:05-11:15 | 18: Granular AI Change Metrics | Recommended |
| 11:15-11:25 | 19: Commit Details (Demo) | Optional |
| 11:25-11:50 | 23: Complete Dashboard (Demo / take-home) | Optional |
| 11:50-12:00 | Wrap-up & certificates | |
| 12:00-1:00 | Lunch | |
| 1:00-2:30 | Open lab / capstone work | |

**Day 2: 5 essential + 4 recommended + 4 demo-only = 13 exercises**

---

## Optional Exercises – What to Skip

| Exercise | Skip? | Alternative |
|----------|-------|-------------|
| **11: Remove Team Member** | ✅ Demo only | Destructive – show payload but don't execute against real team |
| **15: Get Conversation Insights** | ✅ Demo only | Show sample response; Enterprise-only and narrow |
| **19: Get Commit Details (Alpha)** | ✅ Demo only | Alpha endpoint – mention as preview, link to docs |
| **23: Build a Complete Dashboard** | ✅ Take-home | Walk through architecture; assign as post-training project |

---

## Time Savings

| Scenario | Exercises | Total Time |
|----------|-----------|------------|
| All 23 exercises | 23 | ~4.2 hours instruction |
| Essential only (10) | 10 | ~1.6 hours instruction |
| Essential + Recommended (19) | 19 | ~3.3 hours instruction |
| Essential + Recommended + Demo (23) | 19 + 4 demo | ~3.3 hours + demos |

---

## Recommendations by Audience

### For Platform / Admin Engineers (Enterprise)

| Priority | Exercises |
|----------|-----------|
| **Must Do** | 1, 2, 4, 8, 9, 12, 13, 16, 20 |
| **Should Do** | 3, 10, 14, 17, 18, 21 |
| **Can Demo** | 5, 6, 7, 11, 15, 19, 22, 23 |

### For Automation / Backend Engineers (Cloud Agents focus)

| Priority | Exercises |
|----------|-----------|
| **Must Do** | 1, 2, 4, 5, 20 |
| **Should Do** | 3, 6, 7, 21, 22 |
| **Can Skip** | 8-19, 23 (Admin/Analytics/AI tracking not in scope) |

### For Pro / Business Plan Teams (No Admin / Analytics)

| Priority | Exercises |
|----------|-----------|
| **Must Do** | 1, 2, 4, 5, 20 |
| **Should Do** | 3, 6, 7, 21, 22 |
| **Cannot Do** | 8-19, 23 (require Enterprise) |

### For Data / BI Engineers (Analytics + Reporting)

| Priority | Exercises |
|----------|-----------|
| **Must Do** | 1, 2, 3, 9, 12, 13, 16, 17 |
| **Should Do** | 14, 18, 23 |
| **Can Skip** | 5-7, 10, 11, 15, 19, 20-22 |

---

## Quick Decision Matrix

```
┌─────────────────────────────────────────────────────────────────┐
│                 WHICH API EXERCISES TO RUN                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SHORT ON TIME (½ day / 2 hours)?                              │
│  → Exercises: 1, 2, 4, 5, 8, 9, 12, 13, 16, 20                 │
│  → Total: 10 essential exercises (~95 min)                     │
│                                                                 │
│  HAVE 1 DAY (4 hours)?                                          │
│  → Essential (10) + Cloud Agents track recommended (6, 7)      │
│  → + Webhooks recommended (21, 22)                             │
│  → Total: ~14 exercises                                        │
│                                                                 │
│  HAVE 2 FULL DAYS (8 hours)?                                    │
│  → All essential + recommended (19 exercises)                  │
│  → Demo the 4 optional exercises                               │
│  → Total: 19 hands-on + 4 demos                                │
│                                                                 │
│  PRO / BUSINESS PLAN AUDIENCE?                                  │
│  → Only run Tracks 1, 2, and 6 (Cloud Agents + Webhooks)       │
│  → Skip Tracks 3, 4, 5 (Enterprise-only)                       │
│                                                                 │
│  ENTERPRISE ADMIN AUDIENCE?                                     │
│  → Emphasize Tracks 3, 4, 5 (Admin / Analytics / AI Tracking)  │
│  → Skim Tracks 1, 2 (foundations + Cloud Agents demo)          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Plan-Availability Cheat Sheet

| Track | Plan Required | Notes |
|-------|---------------|-------|
| 1: Foundations | All plans | Auth, rate limits, caching work everywhere |
| 2: Cloud Agents | All plans (Beta) | The only universally available Cursor API |
| 3: Admin API | Enterprise | Requires Admin API key |
| 4: Analytics API | Enterprise | Admin-scoped key, 30-day max range |
| 5: AI Code Tracking | Enterprise (alpha) | Endpoints may change |
| 6: Webhooks & Workflows | Depends on referenced API | Cloud Agents webhooks work on all plans |
