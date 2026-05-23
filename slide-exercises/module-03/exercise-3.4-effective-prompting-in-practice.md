# Exercise 3.4: Effective Prompting in Practice

**Module 3:** Agent Modes and Tools  
**Slides:** `slides/module-03-marp.md` (Lesson 3.4)  
**Time:** 22 min  
**Difficulty:** Beginner

**Objective:** Write constrained prompts and reusable templates for real tasks.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

```
Task: Fix the bug where get_user_email(user_id) returns None for valid users.

Constraints:
- Do NOT change the function signature
- Do NOT add new imports
- Do NOT modify other functions
- Do NOT add print statements (use existing logger)

Output format: Show exact diff and explain root cause.
Success criteria: Function returns email string for valid user IDs.
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 2:** Compare constrained vs. unconstrained:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
Fix get_user_email - it's returning None sometimes.
```

---

**Step 3:** Plan first:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Before making any changes, answer:
1. What files would need to change?
2. What is the root cause you suspect?
3. What are the risks?
4. Are there alternative approaches?

I will review before approving any code changes.
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 4:** Negative constraints:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Add error handling to the file parser.

But DO NOT:
- Change the return type (must remain dict)
- Add external dependencies
- Swallow exceptions silently (always log them)
- Change the existing test file
```

---

**Step 5:** One change at a time:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
First, add input validation. Just show me what you'd add — don't modify yet.
[Review] Now add the validation. Show the diff before I accept.
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Save as `.cursor/prompt-templates.md`:

```
## Bug Fix Template
Task: [Describe bug]  File: [path]  Lines: [range]
Constraints: Do NOT change [signatures, imports]
Success criteria: [How to verify]

## Feature Addition Template
Plan first: Yes/No  Constraints: Do NOT break [existing functionality]

## Code Review Template
Focus: [Security, Performance, Edge cases]
Ignore: [Style, formatting]
```

---

## Success criteria

- [ ] Constrained prompt · Plan first · Negative constraints · Template created

---

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch to **Agent Mode** in the panel footer |
| Agent can't see files | **File → Open Folder** (not a single file) |
