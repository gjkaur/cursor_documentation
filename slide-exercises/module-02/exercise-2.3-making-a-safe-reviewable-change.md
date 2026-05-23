# Exercise 2.3: Making a Safe, Reviewable Change

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.3)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Let the Agent propose a small change and review the diff before accepting.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Step 1:** Ask for a small, safe change:

```
Change the welcome message in index.html from "Hello World"
to "Welcome to My App"
```

**Step 2:** Watch the agent generate the diff:

```
📝 Changes to index.html:

  <h1>- Hello World</h1>
  <h1>+ Welcome to My App</h1>

Accept? [Yes] [No] [Edit]
```

---

Before accepting, ask yourself:

- Are the changes **only** what I asked for?
- Are there unexpected additions or deletions?
- Does the syntax look correct?
- Will this break anything else?

**Step 4:** Accept · **Step 5:** Test manually

---

```bash
# Windows (PowerShell)
start index.html          # web
python script.py          # Python
npm start                 # React

# Mac
open index.html
python script.py
npm start
```

---

```
That change didn't work. The button disappeared.
Please explain what happened and suggest a fix.
```

---

## Success criteria

- [ ] Agent proposed a change · Reviewed diff before accepting
- [ ] Accepted only after verification · Tested the change

---

## Additional reference

## Expected Agent Response (Example)

Using Option A (Add a comment), the Agent might reply in plain language, then show a diff like this:

```text
I'll add a comment at the top of calculator.c.

Proposed change: (see diff below)

Do you want me to apply this change?
Type 'yes' to apply, or describe any modifications.
```

**Example diff:**

```diff
+ // Created for Cursor Training - Basic Calculator
  #include <stdio.h>

  // Function prototypes
  int add(int a, int b);
```

After you approve, the Agent will apply the change.

---

## How to Review a Diff

When the Agent shows changes, look for:

| Symbol | Meaning |
|------|--------|
| `+` (green) | Line being ADDED |
| `-` (red) | Line being REMOVED |
| No color | Line unchanged (shown for context) |

**Example Diff Reading:**

```diff
-    printf("Result: %d\n", result);
+    printf("=== Result: %d ===\n", result);
```

This changes the output format from `Result: 5` to `=== Result: 5 ===`.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent makes changes without showing diff | Ask: *"Show me the diff before applying"* |
| Change breaks the code | Click a checkpoint (in chat timeline) to restore previous version |
| Agent changes the wrong place | Be more specific: *"In the `main()` function, right after the line that prints 'Simple Calculator'"* |
| Agent won't make the change | It may need approval – type 'yes' or 'apply' |
| Too many changes at once | Ask for one small change at a time |

---

## Understanding Safe vs. Unsafe Changes

| Safe Changes ✅ | Unsafe Changes ❌ |
|----------------|------------------|
| Adding comments | Deleting entire functions |
| Changing print messages | Modifying core logic |
| Adding whitespace/formatting | Changing function signatures |
| Adding input validation | Removing error handling |
| Renaming local variables | Changing data structures |
| Adding documentation | Modifying header files |

**Golden Rule:** If you're not sure, ask the Agent to explain the change first:

> *"Explain what you're going to change before you do it"*

---

## Key Takeaway

You are always in control. The Agent shows you exactly what it will change (the diff), and you decide whether to accept it. If something goes wrong, checkpoints let you undo everything instantly.

**Three Safety Nets:**

1. **Review the diff** – See changes before they happen
2. **Checkpoints** – Restore previous state with one click
3. **Ask for explanation** – "Explain what you'll change first"

---

## Bonus Challenge (If Time Permits)

After making a safe change, ask the Agent to verify it didn't break anything:

> *"Check that the code still compiles and the changes didn't introduce any syntax errors"*

Or try a slightly more complex safe change:

> *"Add a new function called `modulo(int a, int b)` that returns the remainder. Add it to the menu as option 5."*

---

## Quick Reference: Safe Change Checklist

```text
┌─────────────────────────────────────────────────────────────────┐
│                    SAFE CHANGE CHECKLIST                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BEFORE YOU ASK:                                                │
│  □ Is this change small (1-10 lines)?                          │
│  □ Does it add rather than delete?                             │
│  □ Is it isolated to one function?                             │
│                                                                 │
│  WHEN AGENT RESPONDS:                                          │
│  □ Read the diff (green +, red -)                              │
│  □ Do you understand each change?                              │
│  □ If unsure, ask: "Explain this change"                       │
│                                                                 │
│  AFTER APPROVING:                                              │
│  □ Look at the file – does it look right?                      │
│  □ Run the code to verify (if possible)                        │
│  □ If something's wrong → click previous checkpoint            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
