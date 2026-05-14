# Coding Agents – Finding and Fixing Bugs

## Complete Beginner's Guide

This document explains the **Finding and Fixing Bugs** lesson from the Coding Agents course. It covers debugging fundamentals, two approaches to debugging (quick fixes vs. evidence-first), using multiple models in parallel, bringing runtime data into the agent loop, and common pitfalls.

Let me break this down for a complete beginner.

---

## The Big Picture

> *"As coding agents write more code, engineers spend more time reviewing that code and tracking down bugs. Even with help from coding agents, it's worth brushing up on the fundamentals of effective debugging."*

| Traditional Debugging | Agent-Assisted Debugging |
|---------------------|-------------------------|
| You do all the investigation | Agent helps find root cause |
| Manual log insertion | Agent instruments code |
| You analyze logs | Agent analyzes runtime evidence |
| You propose fixes | Agent makes targeted fixes |

---

## Debugging Fundamentals (Human or Agent)

Good debugging follows the same principles whether a human or an agent does the work:

| Principle | What It Means | Why Important |
|-----------|---------------|---------------|
| **Create a reliable reproduction** | Write down exact steps, inputs, conditions | Can't verify fix without reproducing |
| **Reduce to a minimal case** | Strip away everything not related | Smaller case = easier to find root cause |
| **Isolate variables** | Change one thing at a time | Know which change fixed it |
| **Form specific hypotheses** | "The bug occurs because calculateTotal() doesn't account for negative discounts" | Specific enough to test |
| **Instrument your code** | Add logging at inputs and outputs | Compare expected vs. actual |
| **Prevent regressions with tests** | Write test that would have caught it | Bug doesn't come back |

---

## Two Approaches to Debugging

| Approach | Best For | Method |
|----------|----------|--------|
| **Quick fix** | Simple errors with clear messages | Paste error, agent fixes directly |
| **Debug Mode** | Tricky bugs, no clear error | Evidence-first, systematic investigation |

---

## Approach 1: Quick Fix (Simple Errors)

For bugs with clear error messages or straightforward causes, the agent can often find and fix the problem directly.

### Example Prompt:

> *"This test is failing:*
> *TypeError: Cannot read properties of undefined (reading 'profile')*
> *at getProfile (src/services/UserService.ts:45)*
> *at UserController.show (src/controllers/UserController.ts:23)*
>
> *The error happens when a user created before we added the profile onboarding flow tries to view their profile. Find the root cause and fix it."*

> *"This works well when the cause is visible in the error message. The agent can read the stack trace, find the code, and patch it."*

---

## Approach 2: Debug Mode (Evidence First)

> *"For trickier bugs, Debug Mode takes a different approach. Instead of guessing at fixes, it collects runtime evidence first."*

### Debug Mode Steps:

| Step | What Happens |
|------|--------------|
| **1** | Generates hypotheses about what could go wrong |
| **2** | Instruments your code with targeted logging |
| **3** | Asks you to reproduce the bug while it collects data |
| **4** | Analyzes the logs to identify the root cause |
| **5** | Makes a targeted fix based on evidence |

### Example Prompt:

> *"Checkout is failing intermittently for some users. No consistent error message. Sometimes the order goes through, sometimes it silently fails and the user sees a blank confirmation page."*

> *"Debug Mode can help you find and fix your trickiest bugs. It takes the fundamentals we covered earlier and teaches the agent to be an effective debugger, automating the investigation you'd otherwise do manually."*

---

## Interactive Quiz

The course includes this quiz question:

> *"You have a bug that only appears when two users edit the same document simultaneously. Which approach is more likely to find the root cause?"*

| Option | Correct? | Why |
|--------|----------|-----|
| Paste the error and ask the agent to fix it | ❌ No | No clear error message, intermittent |
| **Use Debug Mode to instrument the code, reproduce the race condition, and analyze the runtime logs** | ✅ **Yes** | Evidence-first approach for tricky bugs |
| Read through the code manually until you spot the issue | ❌ No | Inefficient for race conditions |

---

## Run Multiple Models in Parallel

> *"For hard bugs, different models sometimes find different things. Cursor lets you run the same debugging prompt across multiple models simultaneously."*

### The Workflow:

| Step | Action |
|------|--------|
| 1 | Write a clear debugging brief with reproduction steps and hypotheses |
| 2 | Select multiple models from the agent dropdown |
| 3 | Submit the prompt; each model works independently |
| 4 | Compare the proposed fixes from each model |
| 5 | Keep the approach with the strongest evidence |

> *"Cursor will suggest which solution it believes is best, but you should evaluate the reasoning, not only the final solution."*

---

## Bring Runtime Data into the Agent Loop

> *"The agent can spot performance problems and common bugs by reading code alone. But the more runtime evidence you give it, the deeper it can go."*

### Level 1: Start with a Question

**Example:**
> *"The order history page takes 4 seconds to load for users with lots of orders. Why is this slow?"*

> *"In the example above, the agent found a slow query by reading through the code. No logging or performance profiling needed."*

### Level 2: Feed It Runtime Evidence

When code analysis alone isn't enough, give the agent real data:

| Data Source | Example |
|-------------|---------|
| Terminal output | Error logs, build output |
| Query logs | `EXPLAIN ANALYZE` output |
| Application logs | Runtime behavior |
| Profiling data | Performance metrics |

### Example: EXPLAIN ANALYZE Debugging

> *"This query is taking 1.2 seconds in production. Here's the EXPLAIN ANALYZE output:*
> *Seq Scan on orders (cost=0.00..45892.00 rows=47 width=244) (actual time=0.423..1203.112 rows=47 loops=1)*
> *Filter: (user_id = 'usr_abc123')*
> *Rows Removed by Filter: 2341856*
>
> *Find why it's doing a sequential scan and fix it."*

> *"The same pattern works for application logs, profiling data, or build and test output."*

---

## Use the Browser for Frontend Debugging

> *"For frontend issues, Cursor's integrated browser gives the agent direct access to your web application. It can read console logs, inspect network requests, and observe the DOM without you needing to copy anything."*

| Capability | What Agent Can Do |
|------------|-------------------|
| **Open pages** | Navigate to your app |
| **Reproduce issues** | Click through UI |
| **Check console** | Read JavaScript errors |
| **Inspect network** | See API calls, slow requests |
| **Observe DOM** | Check rendered output |

> *"The agent sees what you'd see in DevTools and can trace problems back to your source code."*

---

## Connect Monitoring Tools with MCP

> *"MCP servers give your agent new capabilities and connect it to production observability tools. Instead of pasting data manually, the agent pulls what it needs on demand."*

### Example Prompt:

> *"We're getting a spike in checkout errors since yesterday's deploy. Can you pull the details from Sentry and check the Datadog logs to figure out what's going on?"*

> *"In the example above, the agent queries Sentry through MCP and pulls in the relevant error details. It correlates the error with logs, finds the offending code, and proposes a fix."*

### Useful MCP Servers for Debugging:

| MCP Server | What It Provides |
|------------|------------------|
| **Sentry** | Error details, stack traces, breadcrumbs |
| **Datadog** | Production logs, APM traces |
| **Databases** | Query production data to verify hypotheses |
| **Linear/GitHub Issues** | Pull bug reports, reproduction steps |

### Automated Workflows:

> *"You can set up workflows where monitoring alerts on your production application trigger agent investigations automatically. If an error rate spikes, a ticket gets created in Linear, and an agent starts diagnosing the issue before a human even looks."*

---

## Common Failure Pattern: Accepting Fixes You Don't Understand

> *"If you don't understand the fix, you can't validate whether it's correct. The agent might add a null check that makes the error go away, but the underlying data inconsistency remains."*

### Wrong Approach:

```
Agent proposes fix → You accept → Error gone (maybe) → Underlying problem remains
```

### Right Approach:

```
Agent proposes fix → Ask questions until you understand → Verify root cause → Accept fix
```

### Questions to Ask:

| Question | Why |
|----------|-----|
| "Why is that value null?" | Find the real cause |
| "What changed to cause this?" | Understand the regression |
| "Is this the root cause or a symptom?" | Avoid masking issues |

> *"As we covered in foundations, agents can hallucinate plausible-sounding explanations. You need to develop your own understanding and use the data from your investigation to confirm the agent has identified the real root cause."*

---

## Debugging Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                      DEBUGGING WORKFLOW                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. REPRODUCE THE BUG                                          │
│     • Write down exact steps                                   │
│     • Create reliable reproduction                             │
│                    ↓                                           │
│  2. CHOOSE APPROACH                                            │
│     • Clear error? → Quick fix                                 │
│     • Tricky/no error? → Debug Mode                            │
│                    ↓                                           │
│  3. GATHER EVIDENCE                                            │
│     • Code analysis                                            │
│     • Runtime data (logs, EXPLAIN ANALYZE)                     │
│     • Browser console/network                                  │
│     • MCP-connected tools (Sentry, Datadog)                    │
│                    ↓                                           │
│  4. FORM HYPOTHESES                                            │
│     • Specific, testable                                       │
│     • Multiple possibilities                                    │
│                    ↓                                           │
│  5. TEST & FIX                                                 │
│     • Run multiple models in parallel (optional)               │
│     • Verify fix                                               │
│     • Write regression test                                    │
│                    ↓                                           │
│  6. UNDERSTAND THE FIX                                         │
│     • Ask questions until you understand                       │
│     • Confirm root cause                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Insight |
|---------|-------------|
| **Debugging fundamentals** | Same whether human or agent |
| **Quick fix** | Clear error messages |
| **Debug Mode** | Evidence-first for tricky bugs |
| **Multiple models** | Run in parallel, compare fixes |
| **Runtime evidence** | More data = deeper investigation |
| **Browser tool** | Frontend debugging |
| **MCP servers** | Connect to production observability |
| **Understand fixes** | Don't accept what you don't understand |

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What are debugging fundamentals?** | Reproduce, reduce, isolate, hypothesize, instrument, test |
| **When to use quick fix?** | Clear error messages, straightforward causes |
| **When to use Debug Mode?** | Tricky bugs, no clear error, intermittent issues |
| **Why run multiple models?** | Different models find different things |
| **How to bring runtime data?** | Paste logs, use browser, connect MCP |
| **What MCP servers help debugging?** | Sentry, Datadog, Databases, Linear |
| **What's the common failure?** | Accepting fixes you don't understand |

---

## The Bottom Line

**Debugging with agents is about giving them the right evidence – error messages, logs, runtime data – and letting them investigate systematically.**

**Think of it as:**
- **Quick fix** = Urgent care for obvious issues 🏥
- **Debug Mode** = Full diagnostic workup for tricky cases 🔬
- **Multiple models** = Get second (and third) opinions 👨‍⚕️👩‍⚕️
- **MCP tools** = Connect to production monitoring 📊

**For your engineers:**
- Master the fundamentals first
- Use quick fix for clear errors
- Use Debug Mode for tricky bugs
- Run multiple models for hard problems
- Connect monitoring tools via MCP
- Never accept a fix you don't understand
