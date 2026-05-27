# Exercise 4.1: Creating a Rule

**Module 4:** Customizing Cursor for Your Team  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 4, Lesson 4.1)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Create Cursor rules that persist coding standards for your team.

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

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

```bash
mkdir -p .cursor/rules
```

Create **coding standards** rule at `.cursor/rules/coding-standards.mdc`:

```
globs: **/*.{js,ts,py}  |  alwaysApply: true

Python: type hints, Black (88 chars), Google docstrings
JS/TS: const over let, arrow functions, optional chaining
General: no commented-out code, no console.log in prod
```

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Create `.cursor/rules/build-and-test.mdc`:

```
Before changes: git status, git diff
After changes:  make test / pytest / npm test → make lint
Do NOT suggest changes that break tests or need undocumented API keys
```

Create `.cursor/rules/security.mdc`:

```
Never: hardcoded secrets, eval() on user input, SQL concatenation
Always: input validation, rate limiting, HTTPS, safe error messages
Flag: exec/eval with user input, password/secret in variable names
```

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Step 5:** Verify rules are applied:
**Where:** **Agent panel** — ``Ctrl+I``

```
Based on the project rules, what are the coding standards I should follow?
What are the security guardrails?
```

---

**Step 6:** Create `.cursor/rules/react-components.mdc` for `**/*.jsx, **/*.tsx`:
**Where:** **Agent panel** — ``Ctrl+I``
- Component structure, naming (PascalCase, handleSubmit)
- Performance: React.memo, useCallback, useMemo
- Accessibility: keyboard nav, alt text, semantic HTML

**Success Criteria:** Created rules directory · coding, build, security rules · verified application

---

## Success criteria

- [ ] Component structure, naming (PascalCase, handleSubmit)
- [ ] Performance: React.memo, useCallback, useMemo
- [ ] Accessibility: keyboard nav, alt text, semantic HTML
- [ ] Created rules directory · coding, build, security rules · verified application

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Create the `.cursor/rules/` directory | Folder for rule files |
| 3 | Create a new rule file with `.mdc` extension | Rule file ready for content |
| 4 | Add frontmatter and rule content | Properly formatted rule |
| 5 | Test the rule by asking the Agent | Agent follows the rule |

---

## What Are Rules?

Rules are persistent instructions that the Agent follows in every conversation.

| Aspect | Description |
|--------|-------------|
| **What they do** | Guide Agent behavior, coding style, preferences |
| **Where they live** | `.cursor/rules/` folder in your project |
| **File format** | Markdown with YAML frontmatter (`.mdc` files) |
| **When they apply** | Always (if `alwaysApply: true`) or contextually |
| **Scope** | Project-level (shared via git) or user-level |

---

## Rule File Structure

```yaml
---
description: "Brief description of what this rule does"
globs: "**/*.c"  # Optional: only apply to certain files
alwaysApply: true  # Apply to every conversation
---

Your rule content goes here.
Write instructions for the Agent in plain English.
Be specific and actionable.
```

---

## Create Your First Rule

### Step 1: Create the Rules Directory

In your project root, create the folder:

```bash
mkdir -p .cursor/rules
```

### Step 2: Create a Rule File

Create `.cursor/rules/coding-standards.mdc` with this content:

```yaml
---
description: "Basic coding standards for C programming"
globs: "**/*.c"
alwaysApply: true
---

## Coding Standards

Follow these standards when writing or modifying C code:

1. Use 4 spaces for indentation (not tabs)
2. Add comments before every function explaining what it does
3. Use descriptive variable names (not single letters except loop counters)
4. Always check for NULL pointers before dereferencing
5. Use `//` for single-line comments, `/* */` for multi-line
6. Keep functions under 30 lines when possible
```

> Tip: A ready-made copy of this file is available at `core-exercises/exercise-14/sample-rules/coding-standards.mdc` in this repo.

### Step 3: Save the File

Save `.cursor/rules/coding-standards.mdc` in your project.

---

## Sample Rules to Try

### Rule 1: Comment Style

```yaml
---
description: "Require function comments"
alwaysApply: true
---

Always add a comment before each function that describes:
- What the function does
- What parameters it takes
- What it returns
- Any side effects
```

### Rule 2: Naming Conventions

```yaml
---
description: "Variable naming conventions"
alwaysApply: true
---

Follow these naming rules:
- Variables: snake_case (e.g., `user_count`)
- Functions: snake_case (e.g., `calculate_total`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_BUFFER_SIZE`)
- Struct names: PascalCase (e.g., `UserProfile`)
```

### Rule 3: Error Handling

```yaml
---
description: "Error handling requirements"
globs: "**/*.c"
alwaysApply: true
---

Always check return values for error conditions:
- Check if pointers are NULL before using them
- Validate user input before processing
- Handle edge cases (empty arrays, zero values)
- Print meaningful error messages
```

---

## Test That the Rule Works

### Step 1: Ask the Agent to Write Code

After saving the rule, ask the Agent:

> *"Write a function that calculates the average of an array of integers"*

### Step 2: Verify the Rule Was Followed

Check if the Agent's response follows your rule:

| Rule Requirement | Check |
|-----------------|-------|
| 4 spaces for indentation | ✅ / ❌ |
| Comment before function | ✅ / ❌ |
| Descriptive variable names | ✅ / ❌ |
| NULL pointer check | ✅ / ❌ |

---

## Expected Agent Response (With Rule)

Based on your coding standards rule, the Agent should produce something like:

```c
// Calculates the average of an integer array
// Parameters:
//   arr - pointer to integer array
//   size - number of elements in the array
// Returns:
//   double - average value, or 0.0 if array is NULL or empty
double calculate_average(int* arr, int size) {
    // Check for NULL pointer (rule #4)
    if (arr == NULL || size <= 0) {
        return 0.0;
    }

    int sum = 0;  // descriptive variable name (rule #3)

    for (int i = 0; i < size; i++) {  // loop counter can be single letter
        sum = sum + arr[i];
    }

    double average = (double)sum / size;
    return average;
}
```

The function includes:
- Comment before function (rule #2)
- 4-space indentation (rule #1)
- NULL pointer check (rule #4)
- Descriptive variable names (rule #3)

---

## Without vs. With Rules

| Without Rules | With Rules |
|---------------|------------|
| `int avg(int *a, int n){int s=0;for(int i=0;i<n;i++)s+=a[i];return s/n;}` | Function with comments, checks, proper formatting |
| Inconsistent style | Consistent across all code |
| You must repeat instructions every time | Rules apply automatically |

---

## Success Criteria

- [ ] Created `.cursor/rules/` directory
- [ ] Created a `.mdc` rule file with proper frontmatter
- [ ] Rule has `alwaysApply: true`
- [ ] Saved the file in the correct location
- [ ] Asked Agent to write code
- [ ] Agent followed the rule
- [ ] Verified rule compliance

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Rule not being applied | Check that `alwaysApply: true` is set correctly |
| Agent ignores the rule | Restart Cursor to reload rules |
| Rule applies to wrong files | Check the `globs` pattern |
| Rule syntax error | Make sure frontmatter has `---` before and after |
| Can't find `.cursor` folder | Create it in your project root |

---

## Rule File Location

```
your-project/
├── .cursor/
│   └── rules/
│       ├── coding-standards.mdc
│       ├── naming-conventions.mdc
│       └── error-handling.mdc
├── calculator.c
└── ...
```

---

## Key Takeaway

**Rules are like a style guide the Agent actually follows.**

Once you create a rule, you never have to repeat those instructions again. The Agent reads them before every response.

**Best practices:**
- Start with 1-2 simple rules
- Add rules when you notice the Agent making the same mistake repeatedly
- Keep rules focused and specific
- Share `.cursor/rules/` via git so your whole team benefits

---

## Bonus Challenge (If Time Permits)

Create a second rule that conflicts with the first, then see which one wins:

> *Create a rule that says "Use tabs for indentation" and another that says "Use spaces". Which one does the Agent follow?*

Or create a language-specific rule:

> *Create a rule with `globs: "**/*.py"` that applies only to Python files*

---

## Exercise Complete ✓

Check off when done:
- [ ] Created `.cursor/rules/` directory
- [ ] Created a rule file with frontmatter
- [ ] Rule has `alwaysApply: true`
- [ ] Agent followed the rule when writing code
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 15 – Use AGENTS.md

---

## Quick Reference: Rules Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                       RULES CHEAT SHEET                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FILE LOCATION:                                                 │
│  .cursor/rules/your-rule-name.mdc                               │
│                                                                 │
│  FILE FORMAT:                                                   │
│  ---                                                            │
│  description: "What this rule does"                             │
│  globs: "**/*.c"           # Optional: file pattern             │
│  alwaysApply: true         # Apply to every conversation        │
│  ---                                                            │
│                                                                 │
│  Your instructions here in plain English.                       │
│                                                                 │
│  EXAMPLE RULES:                                                 │
│                                                                 │
│  Naming:                                                        │
│  "Use snake_case for variables and functions"                   │
│                                                                 │
│  Comments:                                                      │
│  "Add a comment before every function explaining what it does"  │
│                                                                 │
│  Safety:                                                        │
│  "Always check for NULL pointers before dereferencing"          │
│                                                                 │
│  Style:                                                         │
│  "Use 4 spaces for indentation, not tabs"                       │
│                                                                 │
│  TIPS:                                                          │
│  • Start with 1-2 simple rules                                  │
│  • Add rules when Agent repeats mistakes                        │
│  • Be specific and actionable                                   │
│  • Share .cursor/rules/ via git                                 │
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
