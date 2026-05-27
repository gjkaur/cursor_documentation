# Cursor Training – Exercise 13

## Ask Mode vs Agent Mode

**Objective:** Understand the difference between Ask Mode (read-only, safe exploration) and Agent Mode (full tool access, can make changes). Learn when to use each.

**Time:** 10 minutes

**Setup:** Any code project (continue with `calculator.c` from previous exercises)

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Switch to Ask Mode using `/ask` | Mode indicator changes to "Ask" |
| 4 | Ask a question that requires code changes | Agent explains but does NOT modify files |
| 5 | Switch to Agent Mode using `/agent` | Mode indicator changes to "Agent" |
| 6 | Ask the same question | Agent makes the actual code change |

---

## Understanding the Two Modes

| Feature | Ask Mode | Agent Mode |
|---------|----------|------------|
| **Read files** | ✅ Yes | ✅ Yes |
| **Search codebase** | ✅ Yes | ✅ Yes |
| **Explain code** | ✅ Yes | ✅ Yes |
| **Answer questions** | ✅ Yes | ✅ Yes |
| **Edit files** | ❌ No | ✅ Yes |
| **Create files** | ❌ No | ✅ Yes |
| **Delete files** | ❌ No | ✅ Yes |
| **Run terminal commands** | ❌ No | ✅ Yes |
| **Best for** | Exploration, learning, code review | Building, debugging, refactoring |

---

## How to Switch Modes

| Method | Action |
|--------|--------|
| **Slash command** | Type `/ask`, `/agent`, or `/plan` |
| **Keyboard shortcut** | Press `Shift+Tab` to rotate through modes |
| **Dropdown** | Click the mode selector in the chat input |

---

## Sample Prompts to Compare

### Test Prompt 1: Code Change Request

> *"Add a comment at the top of `calculator.c` saying 'Created with Cursor'"*

### Test Prompt 2: Code Generation

> *"Create a new function called `greeting()` that prints 'Hello, World!'"*

### Test Prompt 3: Code Modification

> *"Change all `printf` statements to add an exclamation mark at the end"*

### Test Prompt 4: File Creation

> *"Create a new file called `README.md` with basic project documentation"*

---

## Expected Behavior: Ask Mode

Using Test Prompt 1 in Ask Mode:

I'm in Ask Mode, so I cannot make changes to your files.

**What I would do in Agent Mode:**
Add this comment at the top of `calculator.c`:

```c
// Created with Cursor
#include <stdio.h>
...
```

**To make this change:**
1. Switch to Agent Mode by typing `/agent`
2. Then ask me again to add the comment

**Alternative:** You can make the change manually by editing the file yourself.

**Key observation:** Ask Mode explains WHAT would change but does NOT actually change anything.

---

## Expected Behavior: Agent Mode

Using the same prompt after switching to Agent Mode:

I'll add a comment at the top of `calculator.c`.

**Change made:**

```diff
+ // Created with Cursor
  #include <stdio.h>
```

✅ Comment added successfully.

**Updated file:** `calculator.c` now has the comment at the top.

**Key observation:** Agent Mode actually makes the change.

---

## Comparison Table: Same Prompt, Different Modes

| Aspect | Ask Mode | Agent Mode |
|--------|----------|------------|
| **File modified?** | ❌ No | ✅ Yes |
| **Shows what would change?** | ✅ Yes | ✅ Yes (as diff) |
| **Requires approval?** | N/A | ✅ Yes (for changes) |
| **Time to complete** | Faster | Slower (does actual work) |
| **Risk level** | None (read-only) | Low to medium (changes files) |

---

## When to Use Each Mode

### Use Ask Mode when:

| Scenario | Example |
|----------|---------|
| Exploring unfamiliar code | *"What does this function do?"* |
| Getting code review | *"Are there any bugs in this function?"* |
| Planning changes | *"How would you refactor this?"* |
| Learning the codebase | *"Explain the project structure"* |
| Before making changes | *"If I change X, what will break?"* |

### Use Agent Mode when:

| Scenario | Example |
|----------|---------|
| Making actual changes | *"Add error handling here"* |
| Creating new files | *"Create a new utility file"* |
| Refactoring code | *"Rename this variable throughout the project"* |
| Running commands | *"Run the tests"* |
| Fixing bugs | *"Fix the off-by-one error"* |

---

## Workflow: Ask First, Then Agent

**Best practice workflow:**

```
1. Start in Ask Mode
2. Ask: "How would I add input validation to this function?"
3. Agent explains the approach (no changes)
4. Review the plan
5. Switch to Agent Mode: `/agent`
6. Ask: "Now implement the input validation you described"
7. Agent makes the actual changes
```

**Why this is effective:**
- You get a plan before committing to changes
- No risk of unwanted modifications
- You can approve the approach before implementation

---

## Success Criteria

- [ ] Switched to Ask Mode (`/ask`)
- [ ] Asked a change-making request in Ask Mode
- [ ] Agent explained what would change but didn't modify files
- [ ] Switched to Agent Mode (`/agent`)
- [ ] Asked the same request in Agent Mode
- [ ] Agent actually made the change
- [ ] Verified the difference in behavior

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't switch modes | Type `/ask` or `/agent` exactly. Use `Shift+Tab` as alternative |
| Agent still makes changes in Ask Mode | You might not be in Ask Mode. Check the mode indicator |
| Don't see mode indicator | Look near the chat input – it shows "Ask", "Agent", or "Plan" |
| Agent asks for approval in Ask Mode | This shouldn't happen. Stay in Ask Mode for read-only |
| Forgot which mode you're in | Type `/mode` or check the indicator |

---

## Key Takeaway

**Ask Mode = "Tell me what you would do" (read-only)**
**Agent Mode = "Do it" (full access)**

**Golden Rule:** When in doubt, start in Ask Mode. You can always switch to Agent Mode when you're ready to make changes.

---

## Bonus Challenge (If Time Permits)

Try this multi-step workflow:

1. In Ask Mode: *"Plan adding a modulo operation to this calculator"*
2. Review the plan
3. Switch to Agent Mode: *"Now implement the plan you just described"*
4. Verify the change works

This mimics a safe, review-before-implement workflow.

---

## Exercise Complete ✓

Check off when done:
- [ ] Switched to Ask Mode
- [ ] Asked change-making request in Ask Mode – no changes made
- [ ] Switched to Agent Mode
- [ ] Asked same request – changes made
- [ ] Understood the difference between modes
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 14 – Create a Rule

---

## Quick Reference: Modes Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│                    MODES COMPARISON CHEAT SHEET                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┬─────────────┬─────────────┐                   │
│  │   Feature   │   Ask Mode  │  Agent Mode │                   │
│  ├─────────────┼─────────────┼─────────────┤                   │
│  │ Read files  │     ✅      │     ✅      │                   │
│  │ Search code │     ✅      │     ✅      │                   │
│  │ Explain     │     ✅      │     ✅      │                   │
│  │ Edit files  │     ❌      │     ✅      │                   │
│  │ Create files│     ❌      │     ✅      │                   │
│  │ Run commands│     ❌      │     ✅      │                   │
│  │ Risk level  │    None     │   Low-Med   │                   │
│  └─────────────┴─────────────┴─────────────┘                   │
│                                                                 │
│  SWITCH MODES:                                                  │
│  • /ask        → Ask Mode (read-only)                          │
│  • /agent      → Agent Mode (full access)                      │
│  • /plan       → Plan Mode (design first)                      │
│  • Shift+Tab   → Rotate through modes                          │
│                                                                 │
│  RECOMMENDED WORKFLOW:                                          │
│  1. Start in Ask Mode - "How would I...?"                      │
│  2. Review the plan                                            │
│  3. Switch to Agent Mode - "Now do it"                         │
│  4. Verify the change                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
