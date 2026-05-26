# Cursor Training – Exercise 26

## Effective Prompting in Practice

**Objective:** Write clear, bounded prompts so the Agent stays focused. Practice constrained prompts, plan-first requests, DO NOT lists, and reusable templates.

**Time:** 22 minutes

**Setup:** Open `core-exercises/exercise-3/` in Cursor. You will prompt against `calculator.c` — the same file from earlier exercises.

---

## What You Will Practice

| Step | Technique | Why it helps |
|------|-----------|--------------|
| 1 | **Constrained prompt** | Agent changes only what you specify |
| 2 | **Vague vs. constrained** | See how missing boundaries cause scope creep |
| 3 | **Plan first** | Review approach before any diff |
| 4 | **DO NOT list** | Explicitly forbid unwanted edits |
| 5 | **One change at a time** | Two messages: propose, then apply |
| 6 | **Prompt templates** | Reuse patterns on real tasks |

---

## Before You Start

1. **File → Open Folder** → select `core-exercises/exercise-3/` in this repo.
2. Press **`Ctrl+I`** to open the **Agent** panel.
3. Confirm the mode footer shows **Agent** (use `/agent` if needed).
4. Use **PowerShell** as your terminal (``Ctrl+` `` → **PowerShell**).
5. In prompts, type **`@calculator.c`** so the Agent reads the correct file.

---

## Step 1: Write a Constrained Prompt

**Goal:** Give the Agent a task, boundaries, output format, and success criteria.

Copy and send:

```
@calculator.c

Task: Improve divide() so it handles division by zero safely inside the function itself.

Constraints:
- Do NOT change any function signatures
- Do NOT add new #include lines
- Do NOT modify main() or other functions
- Change ONLY the divide() function body

Output format: Show the exact diff and explain the root cause in 2–3 sentences.

Success criteria: divide(10, 0) returns safely without crashing; divide(10, 2) still returns 5.
```

**What to look for:**
- The diff touches **`divide()` only** — not `main()`, not other functions.
- The Agent explains *why* the change is needed, not just *what* changed.
- If the diff is too large, reply: *"Scope is too wide. Change ONLY divide(). Try again."*

---

## Step 2: Compare Vague vs. Constrained

**Goal:** See what happens when you drop the boundaries.

### Part A — vague prompt

Start a fresh message (or type `/clear` to reset context). Send:

```
@calculator.c Fix the divide function.
```

**Write down:** Did the Agent change only `divide()`? Did it explain the cause? Did it refactor `main()` too?

### Part B — constrained prompt

Send the **Step 1 prompt** again (full constrained version).

**Compare:** The constrained prompt should produce a **smaller, reviewable diff** and a clearer explanation.

| | Vague prompt | Constrained prompt |
|---|--------------|-------------------|
| Scope | Often spreads to other code | Stays in `divide()` |
| Explanation | May skip root cause | Should explain cause |
| Review | Harder to approve safely | Easier to accept or reject |

---

## Step 3: Plan Before Editing

**Goal:** Get a plan you approve **before** any file changes.

**Option A — Ask Mode:** Switch to Ask Mode (`/ask`), then send:

```
@calculator.c

Before making any changes, answer:
1. What is the smallest change needed for divide()?
2. Which lines would you change?
3. What could go wrong?
4. What will you NOT change?

Do not edit files yet — I will review first.
```

**Option B — Agent Mode:** Send the same prompt. If the Agent starts editing, add: *"Stop — plan only, no diffs yet."*

**What to look for:**
- A numbered plan with files and line areas mentioned.
- **No diff applied** until you say to proceed.

When satisfied, you can send: *"Proceed with that plan. Show the diff before I accept."*

---

## Step 4: Negative Constraints (DO NOT List)

**Goal:** Tell the Agent what **not** to touch.

```
@calculator.c

Add a one-line comment above divide() explaining it performs integer division.

DO NOT:
- Change any function bodies
- Rename functions
- Add new functions
- Modify main()
- Change printf messages elsewhere
```

**What to look for:**
- Only a **comment** is added — no logic changes, no refactors.

If the Agent changes code anyway, reject the diff and resend with: *"You changed function bodies. Follow the DO NOT list."*

---

## Step 5: One Change at a Time (Two Messages)

**Goal:** Separate "show me the idea" from "apply the change."

### Message 1 — propose only

```
@calculator.c

Show me the validation you would add inside divide() for division by zero.
Do not edit the file yet.
```

Read the response. Confirm you agree with the approach.

### Message 2 — apply only

```
Now add only that validation to divide(). Show the diff before I accept.
Do not change main() or other functions.
```

**What to look for:**
- Message 1: explanation or pseudocode — **no file edit**.
- Message 2: small diff — **only** what you approved.

This is the same pattern as Plan Mode and Ask-then-Agent workflows from earlier exercises.

---

## Step 6: Save Reusable Prompt Templates

**Goal:** Create prompts you can copy on real projects.

1. In the project root, create a folder **`.cursor/`** if it does not exist.
2. Create **`.cursor/prompt-templates.md`** with:

```markdown
## Bug Fix Template
@{{file}}

Task: [Describe the bug]
Constraints: Do NOT change [signatures / imports / other files]
Output: Show diff + root cause
Success: [How to verify]

## Plan-First Template
@{{file}}

Before editing, list: files to change, risks, and what you will NOT touch.
Wait for my approval before changing code.

## Small Change Template
@{{file}}

Change ONLY: [function or line range]
DO NOT: [list forbidden changes]
Show diff before applying.
```

3. Open the file and replace `{{file}}` with a real path when you use a template (e.g. `@calculator.c`).

---

## Prompt Anatomy Checklist

Use this mental checklist for every non-trivial prompt:

1. **Context** — `@file` or brief project note
2. **Task** — one clear goal
3. **Constraints / DO NOT** — what to leave alone
4. **Output format** — diff, plan, explanation, etc.
5. **Success criteria** — how you will verify the result

---

## Success Criteria

- [ ] Sent a constrained prompt with Task, Constraints, Output, and Success criteria
- [ ] Compared a vague prompt vs. a constrained prompt on the same task
- [ ] Got a plan before any file was edited
- [ ] Used a DO NOT list and kept the change minimal
- [ ] Split work into two messages (propose, then apply)
- [ ] Created `.cursor/prompt-templates.md` with at least three templates

---

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| Agent changes too many files | Add *"Change ONLY [function/file]."* Reject the diff and retry. |
| Agent edits when you wanted a plan | Switch to `/ask` or add *"Do not edit files yet."* |
| Agent ignores DO NOT list | Reject diff; paste the DO NOT list again at the top of the prompt. |
| `@calculator.c` not found | Open **Folder** `exercise-3`, not a single file. |
| Prompt feels too long | Keep Task + DO NOT + Success criteria; drop optional prose. |

---

## Key Takeaway

**Boundaries prevent scope creep.** A few extra lines in your prompt (constraints, DO NOT, success criteria) save time reviewing large unexpected diffs.

**Next:** Module 4 — Rules, AGENTS.md, and Skills for team-wide prompting defaults.
