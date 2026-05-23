# Exercise 3.1: Ask Mode vs. Agent Mode

**Module 3:** Agent Modes and Tools  
**Slides:** `slides/module-03-marp.md` (Lesson 3.1)  
**Time:** 18 min  
**Difficulty:** Beginner

**Objective:** Learn when Ask Mode is read-only and when Agent Mode can edit files.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 1:** Open Agent panel (`Cmd+I` / `Ctrl+I`) — note mode indicator at bottom
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

---

**Step 2:** Try to make a change in **Ask Mode**:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
Change the variable name 'temp' to 'temperature' in the current file.
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 3:** Ask a question Ask Mode handles well:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
Explain the purpose of the main() function in this file.
What edge cases does it handle?
```

---

**Step 4:** Switch to **Agent Mode** via the dropdown
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Step 5:** Repeat the rename request — agent shows diff for approval
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 6:** Practice mode-switching mid-conversation:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
# Start in Ask Mode: What does this function return?
# Then: "Switch to Agent Mode and fix the off-by-one error"
```

---

## Success criteria

- [ ] Used Ask Mode for questions · Observed Ask Mode cannot make changes
- [ ] Switched to Agent Mode · Made a change with diff review

---

## Additional reference

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

## Expected Behavior: Ask Mode

Using Test Prompt 1 in Ask Mode:

```
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
```

**Key observation:** Ask Mode explains WHAT would change but does NOT actually change anything.

---

## Expected Behavior: Agent Mode

Using the same prompt after switching to Agent Mode:

```
I'll add a comment at the top of `calculator.c`.

**Change made:**
```diff
+ // Created with Cursor
  #include <stdio.h>
```

✅ Comment added successfully.

**Updated file:** `calculator.c` now has the comment at the top.
```

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
