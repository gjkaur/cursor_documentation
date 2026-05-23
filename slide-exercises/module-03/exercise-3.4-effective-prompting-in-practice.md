# Exercise 3.4: Effective Prompting in Practice

**Module 3:** Agent Modes and Tools  
**Slides:** `slides/module-03-marp.md` (Lesson 3.4)  
**Time:** 22 min  
**Difficulty:** Beginner

**Objective:** Write constrained prompts and reusable templates for real tasks.

---

## Cursor basics (read this first)

| Task | Windows / Linux | Mac | Where in Cursor |
|------|-----------------|-----|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.


---

## Steps from the training slides

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

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

**Success Criteria:** Constrained prompt · Plan first · Negative constraints · Template created

---

## Success criteria

- [ ] Constrained prompt · Plan first · Negative constraints · Template created

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Terminal command fails on Windows | Use **PowerShell**; use `curl.exe` instead of `curl` |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
