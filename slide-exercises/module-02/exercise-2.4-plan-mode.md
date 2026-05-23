# Exercise 2.4: Plan Mode

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.4)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Use Plan Mode to design a change before the Agent edits files.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Step 1:** Enable Plan Mode (Shift+Tab in the Agent input):

```bash
# Press Shift+Tab in the Agent input
# The input border changes color to indicate Plan Mode
```

---

**Step 2:** Describe a complex change:

```
Add user authentication to this web app.

Requirements:
- Email/password login · Session management
- Protected routes (dashboard, settings)
- Logout functionality · "Remember me" option

Don't write code yet – just give me a plan.
```

---

**Step 3:** Review the agent's plan — a good plan includes:

```
📋 IMPLEMENTATION PLAN

Step 1: Create User Model — models/user.js
Step 2: Auth Routes — routes/auth.js (login, logout, register)
Step 3: Session Management — middleware/session.js
Step 4: Protected Route Middleware — middleware/auth.js
Step 5: Update Frontend — pages/login.html, dashboard.html
Step 6: Environment Variables — .env (SESSION_SECRET, REDIS_URL)

Questions for you:
1. JWT or server-side sessions?
2. Existing user database?
3. Include email verification?

Ready to proceed? [Yes] [No] [Modify Plan]
```

---

**Step 4:** Answer questions and approve:

```
Use JWT for simplicity. No existing database yet – use SQLite for now.
Skip email verification for this version. Proceed.
```

**Step 5:** Watch the agent execute the plan step by step

---

---

## Success criteria

- [ ] Enabled Plan Mode (Shift+Tab)
- [ ] Agent created structured plan
- [ ] Agent asked clarifying questions
- [ ] Approved plan before code was written

---

## Additional reference

## Expected Agent Questions (Example)

Using Option A (Add modulo operation):

The Agent might ask:

| Question | Why It's Asked |
|----------|----------------|
| *"What key should represent modulo in the menu (e.g., option 5)?"* | Determines menu placement |
| *"How should modulo handle negative numbers?"* | Defines behavior edge cases |
| *"Should modulo be a separate function or handled inline?"* | Code organization preference |
| *"What should the output format look like?"* | User experience expectations |
| *"Should division by zero check be applied to modulo?"* | Safety considerations |

---

## Expected Plan Output (Example)

After answering the questions, the Agent will create a plan like this:

````markdown
# Implementation Plan: Add Modulo Operation

## Summary
Add a new modulo (remainder) operation as option 5 in the calculator menu.

## Files to Modify
- `calculator.c` - Add modulo function and menu option

## Detailed Steps

### Step 1: Add Function Prototype
```c
int modulo(int a, int b);
```

### Step 2: Implement Modulo Function
```c
int modulo(int a, int b) {
    if (b == 0) {
        printf("Error: Modulo by zero\n");
        return 0;
    }
    return a % b;
}
```

### Step 3: Update Menu Display
Change menu to include:
```
5. Modulo
```

### Step 4: Add Case in Switch Statement
```c
case 5:
    result = modulo(x, y);
    printf("Result: %d\n", result);
    break;
```

## Estimated Changes
- ~15 lines of code added
- No existing code removed

## Risks
- Modulo by zero - handled with check
- Negative numbers - C's % operator works with negatives (implementation-defined behavior)

**Ready to build. Type 'Build it' to proceed.**
````

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Plan Mode not activating | Press `Shift+Tab` again. Check chat input shows "Plan" |
| Agent starts coding immediately | Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"* |
| Plan is too vague | Ask: *"Be more specific. What files will you change? What functions?"* |
| Forgot to answer a question | Scroll up and answer any unanswered questions |
| Don't like the plan | Ask: *"Change the plan to [your preference]"* |
| Agent won't build after approval | Type: *"Build it"* or *"Proceed with the plan"* |

---

## Plan Mode vs. Agent Mode Comparison

| Aspect | Agent Mode | Plan Mode |
|--------|-----------|-----------|
| **Starts coding immediately** | Yes | No |
| **Asks clarifying questions** | Rarely | Always |
| **Shows plan before coding** | No | Yes |
| **You approve before changes** | No | Yes |
| **Best for simple tasks** | Yes | Overkill |
| **Best for complex tasks** | Risky | Yes |
| **Best for unfamiliar code** | Risky | Yes |

---

## Key Takeaway

**Plan Mode = Measure twice, cut once.**

Use Plan Mode when:

- You're adding a new feature
- The change affects multiple files
- You're not 100% sure how to implement it
- Someone else needs to review the approach first
- The code is safety-critical (like industrial control systems)

Skip Plan Mode when:

- Fixing a typo
- Adding a comment
- Changing a constant value
- Any change you're 100% confident about

---

## Bonus Challenge (If Time Permits)

After executing the plan, ask the Agent to verify:

> *"Now that the code is written, test that the new modulo operation works correctly. Suggest 3 test cases with expected outputs."*

Or try a more complex plan:

> *"Switch back to Plan Mode. I want to add input validation that rejects non-numeric inputs. Plan first, then build."*

---

## Quick Reference: Plan Mode Workflow

```text
┌─────────────────────────────────────────────────────────────────┐
│                     PLAN MODE WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Shift+Tab → Enter Plan Mode                                 │
│                    ↓                                            │
│  2. Describe what you want to build                             │
│                    ↓                                            │
│  3. Agent asks clarifying questions → You answer                │
│                    ↓                                            │
│  4. Agent creates detailed implementation plan                  │
│                    ↓                                            │
│  5. You review the plan                                         │
│                    ↓                                            │
│  6. Type "Build it" → Agent writes code                         │
│                    ↓                                            │
│  7. Review the result → Done or refine                          │
│                                                                 │
│  REMEMBER: The plan is a document you can edit.                 │
│  If you don't like something, ask the Agent to change the plan  │
│  before building.                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
