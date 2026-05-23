# Exercise 2.3: Making a Safe, Reviewable Change

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.3)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Let the Agent propose a small change and review the diff before accepting.

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

**Success Criteria:**
- Agent proposed a change · Reviewed diff before accepting
- Accepted only after verification · Tested the change

---

## Success criteria

- [ ] Agent proposed a change · Reviewed diff before accepting
- [ ] Accepted only after verification · Tested the change

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Type a request for a small, safe change | Prompt ready to send |
| 4 | Press `Enter` to send | Agent proposes changes or asks for approval |
| 5 | Review the diff (green = added, red = removed) | You see exactly what will change |
| 6 | If you approve, let the Agent proceed | Changes are applied to your file |

---

## Code Example to Use

Continue with `calculator.c` in **this** folder (same directory as this doc):

```c
#include <stdio.h>

// Function prototypes
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
int divide(int a, int b);

int main() {
    int choice, x, y, result;

    printf("Simple Calculator\n");
    printf("1. Add\n");
    printf("2. Subtract\n");
    printf("3. Multiply\n");
    printf("4. Divide\n");
    printf("Enter choice: ");
    scanf("%d", &choice);

    printf("Enter two numbers: ");
    scanf("%d %d", &x, &y);

    switch(choice) {
        case 1:
            result = add(x, y);
            printf("Result: %d\n", result);
            break;
        case 2:
            result = subtract(x, y);
            printf("Result: %d\n", result);
            break;
        case 3:
            result = multiply(x, y);
            printf("Result: %d\n", result);
            break;
        case 4:
            if (y != 0) {
                result = divide(x, y);
                printf("Result: %d\n", result);
            } else {
                printf("Error: Division by zero\n");
            }
            break;
        default:
            printf("Invalid choice\n");
    }

    return 0;
}

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    return a / b;
}
```

---

## Sample Prompts (Copy-Paste)

Choose ONE of these safe change requests:

### Option A: Add a Comment (Safest)

> *"Add a comment at the very top of `calculator.c` that says: 'Created for Cursor Training - Basic Calculator' "*

### Option B: Add a Welcome Message

> *"In the `main()` function, right after the `printf("Simple Calculator\n");` line, add a new line that prints: 'Welcome to the calculator!' "*

### Option C: Add Input Confirmation

> *"After reading the two numbers with `scanf`, add a line that prints: 'You entered: x and y' (replace x and y with the actual values)"*

### Option D: Improve Output Formatting

> *"Change all result print statements from 'Result: %d\n' to '=== Result: %d ===\n' (with the === before and after)"*

---

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

## Success Criteria

- [ ] Agent understood your request
- [ ] Agent showed a diff (changes highlighted)
- [ ] You reviewed the changes before approving
- [ ] Changes were applied to the file
- [ ] The file still works (no syntax errors)

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

## Exercise Complete ✓

Check off when done:

- [ ] Requested a small, safe change
- [ ] Reviewed the diff before approving
- [ ] Changes applied successfully
- [ ] File still works (if applicable)
- [ ] (Optional) Completed bonus challenge



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
