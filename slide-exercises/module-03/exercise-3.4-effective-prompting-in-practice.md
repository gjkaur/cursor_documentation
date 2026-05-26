# Exercise 3.4: Effective Prompting in Practice

**Module 3:** Agent Modes and Tools  
**Slides:** `slides/module-03-marp.md` (Lesson 3.4)  
**Time:** 22 min  
**Difficulty:** Beginner

**Objective:** Write constrained prompts and reusable templates for real tasks.

---

## Cursor basics (read this first)

**Demonstration environment:** These exercises assume **Windows 10/11**. Open the integrated terminal with ``Ctrl+` `` and select **PowerShell** as the default profile.

| Task | Windows (demo) | Mac (optional) | Where in Cursor |
|------|----------------|----------------|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` → **PowerShell** | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Windows terminal commands (common in exercises):**

| Task | PowerShell command |
|------|-------------------|
| List files | `dir` or `Get-ChildItem` |
| Show file contents | `Get-Content .\file.txt` or `type file.txt` |
| Run a local `.bat` script | `.\run_tests.bat` |
| Run compiled program | `.\calculator.exe` or `calculator.exe` |
| Set env var (session) | `$env:MY_VAR = "value"` |
| Open HTML in browser | `start index.html` |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.


---

## Steps from the training slides

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Before you start**

**Goal:** Practice six prompting techniques on `calculator.c` from earlier exercises.

**Do this first:**
1. **File → Open Folder** → `core-exercises/exercise-3/`
2. Open **Agent panel** — ``Ctrl+I``
3. Confirm **Agent Mode** (footer shows Agent, or type `/agent`)

Use **`@calculator.c`** in every prompt below.

---

**Step 1 — Constrained prompt**

**Goal:** Task + boundaries + output format + success criteria.

**Where:** **Agent panel** — ``Ctrl+I``

```
@calculator.c

Task: Improve divide() so it handles division by zero safely inside the function itself.

Constraints:
- Do NOT change any function signatures
- Do NOT add new #include lines
- Do NOT modify main() or other functions
- Change ONLY the divide() function body

Output format: Show the exact diff and explain the root cause in 2–3 sentences.

Success criteria: divide(10, 0) returns safely; divide(10, 2) still returns 5.
```

**Look for:** Diff limited to `divide()` — not a full refactor.

---

**Step 2 — Vague vs. constrained**

**Goal:** See why boundaries matter.

**Part A — vague** (new message or `/clear`):

```
@calculator.c Fix the divide function.
```

Note: Did the Agent change more than `divide()`?

**Part B — constrained:** Re-send the **Step 1** prompt.

**Look for:** Constrained prompt → smaller, reviewable diff.

---

**Step 3 — Plan before editing**

**Goal:** Approve a plan before any file changes.

**Where:** Ask Mode (`/ask`) or Agent with *"do not edit yet"*

```
@calculator.c

Before making any changes, answer:
1. What is the smallest change needed for divide()?
2. Which lines would you change?
3. What could go wrong?
4. What will you NOT change?

Do not edit files yet — I will review first.
```

**Look for:** Written plan, **no diff** until you approve.

---

**Step 4 — DO NOT list**

**Goal:** Forbid scope creep explicitly.

```
@calculator.c

Add a one-line comment above divide() explaining it performs integer division.

DO NOT:
- Change any function bodies
- Rename functions
- Add new functions
- Modify main()
```

**Look for:** Comment only — no logic changes.

---

**Step 5 — One change at a time**

**Goal:** Two messages — propose, then apply.

**Message 1:**
```
@calculator.c

Show me the validation you would add inside divide() for division by zero.
Do not edit the file yet.
```

**Message 2** (after you review Message 1):
```
Now add only that validation to divide(). Show the diff before I accept.
Do not change main() or other functions.
```

**Look for:** Message 1 = no edit · Message 2 = small diff.

---

**Step 6 — Prompt templates**

**Goal:** Reusable prompts for real projects.

Create **`.cursor/prompt-templates.md`**:

```
## Bug Fix Template
@{{file}}
Task: [Describe bug]
Constraints: Do NOT change [signatures / other files]
Output: Show diff + root cause
Success: [How to verify]

## Plan-First Template
@{{file}}
Before editing: list files, risks, and what you will NOT touch.
Wait for my approval.

## Small Change Template
@{{file}}
Change ONLY: [function or lines]
DO NOT: [forbidden changes]
Show diff before applying.
```

**Success Criteria:**
- Constrained prompt sent · Vague vs. constrained compared
- Plan before edit · DO NOT list used · Two-message flow tried
- `.cursor/prompt-templates.md` created

---

## Success criteria

- [ ] Constrained prompt sent · Vague vs. constrained compared
- [ ] Plan before edit · DO NOT list used · Two-message flow tried
- [ ] `.cursor/prompt-templates.md` created

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

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

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
