# Exercise 4.2: Repository Instructions

**Module 4:** Customizing Cursor for Your Team  
**Slides:** `slides/module-04-marp.md` (Lesson 4.2)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Add repository instructions the Agent reads automatically.

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

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Create `.cursor/repository-instructions.md`:

<img src="../../slides/assets/module-04/exercise-4-2-create-instructions.svg" alt="Exercise 4.2 — Create Instructions" />

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Step 2:** Ask the Agent:
**Where:** **Agent panel** — ``Ctrl+I``

```
What are the key technologies used in this project?
How do I run the tests?
```

---

**Step 3:** Update instructions when:
**Where:** **Agent panel** — ``Ctrl+I``
- New team members join → add contact info
- Architecture changes → update structure
- New dependencies or common issues discovered

**Success Criteria:** Created instructions · included purpose, stack, commands · verified agent access

---

## Success criteria

- [ ] New team members join → add contact info
- [ ] Architecture changes → update structure
- [ ] New dependencies or common issues discovered
- [ ] Created instructions · included purpose, stack, commands · verified agent access

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Create `AGENTS.md` in your project root | New markdown file created |
| 3 | Add project instructions to the file | File contains guidance for the Agent |
| 4 | Save the file | Instructions ready for Agent |
| 5 | Ask the Agent to perform a task | Agent follows instructions from AGENTS.md |

---

## What is AGENTS.md?

| Aspect | Description |
|--------|-------------|
| **What it is** | A simple markdown file that provides instructions to the Agent |
| **Where it goes** | Project root directory |
| **Format** | Plain markdown (no special frontmatter needed) |
| **When it applies** | Always (automatically read by Agent) |
| **Compared to Rules** | Simpler, no YAML frontmatter, good for basic instructions |

---

## Create AGENTS.md

In your project root, create a file named `AGENTS.md` with this content:

```markdown
# Project Instructions for Cursor Agent

## About This Project
This is a simple calculator program written in C. It supports basic arithmetic operations.

## Coding Standards
- Use 4 spaces for indentation (never tabs)
- Add comments before every function
- Use snake_case for variable names
- Keep functions under 30 lines

## Build Instructions
- Compile with: `gcc -o calculator calculator.c`
- Run with: `./calculator`

## Testing
- No automated tests yet
- Manually test with different inputs

## Common Tasks
- To add a new operation: add function in calculator.c, update menu, add case in switch
- To improve error handling: check for invalid inputs, division by zero, etc.

## Agent Behavior Preferences
- Explain your reasoning before writing code
- Show me the diff before making changes
- Suggest improvements even if not asked
```

---

## Alternative: Minimal AGENTS.md

If you want something simpler:

```markdown
# Project Rules

- Use 2 spaces for indentation
- Add comments to all functions
- Check for NULL pointers
- Use descriptive variable names
- Keep it simple and readable
```

---

## Sample Prompts to Test AGENTS.md

### Test Prompt 1: Code Generation

> *"Add a new function called `multiply` that multiplies two numbers"*

### Test Prompt 2: Code Review

> *"Review the `add` function for any issues"*

### Test Prompt 3: Refactoring

> *"Refactor the main function to be more readable"*

### Test Prompt 4: Documentation

> *"Add comments to the subtract function"*

---

## Expected Agent Response (With AGENTS.md)

Using Test Prompt 1:

Based on your AGENTS.md instructions:

**Reasoning (as requested):**
I'll add a `multiply` function to calculator.c. According to your coding standards, I'll use 4 spaces for indentation, snake_case for the function name, and add a comment before the function.

**Code to add:**

```c
// Multiplies two integers and returns the result
int multiply(int first_number, int second_number) {
    int product = first_number * second_number;
    return product;
}
```

**Diff:**

```diff
+ // Multiplies two integers and returns the result
+ int multiply(int first_number, int second_number) {
+     int product = first_number * second_number;
+     return product;
+ }
```

**Do you want me to add this function to calculator.c?**

---

## AGENTS.md vs. Rules (.mdc files)

| Feature | AGENTS.md | Rules (.mdc) |
|---------|-----------|--------------|
| **Format** | Plain markdown | YAML frontmatter + markdown |
| **Complexity** | Simple | More powerful |
| **File location** | Project root | `.cursor/rules/` |
| **Glob patterns** | No | Yes |
| **Always apply** | Yes | Configurable |
| **Best for** | Simple project instructions | Complex, file-specific rules |

---

## What You Can Put in AGENTS.md

| Category | Example |
|----------|---------|
| **Project overview** | "This is an embedded firmware project for ARM Cortex-M4" |
| **Coding standards** | "Use snake_case, 4 spaces, comments on all functions" |
| **Build instructions** | "Run `make` to build, `make flash` to deploy" |
| **Testing** | "Run `make test` to execute unit tests" |
| **Common tasks** | "To add a new feature: create file, update header, add to build" |
| **Agent preferences** | "Explain reasoning first, show diffs, suggest improvements" |
| **Safety rules** | "Never delete files, always check bounds" |

---

## Success Criteria

- [ ] Created `AGENTS.md` in project root
- [ ] Added at least 3 instructions to the file
- [ ] Saved the file
- [ ] Asked Agent to perform a task
- [ ] Agent referenced or followed instructions from AGENTS.md
- [ ] Verified the Agent's behavior changed based on your instructions

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent ignores AGENTS.md | Make sure file is named exactly `AGENTS.md` (case-sensitive) |
| File not found | Place it in the root of your project (same level as .cursor folder) |
| Instructions not followed | Be more specific. "Be concise" is vague; "Use 2-3 sentences maximum" is clear |
| Agent still does wrong thing | Add a rule in `.cursor/rules/` for enforcement |
| Multiple AGENTS.md files | Agent reads the one in project root. Subdirectory AGENTS.md files may not be read |

---

## Key Takeaway

**AGENTS.md is the simplest way to give the Agent project-specific instructions.**

No YAML, no special formatting – just plain markdown. The Agent reads it automatically and applies your guidance.

**When to use AGENTS.md:**
- Quick project setup
- Simple coding standards
- Build/test instructions
- Team onboarding

**When to use Rules (.mdc):**
- Need file-specific rules (globs)
- Need conditional application
- Complex rule structures

---

## Bonus Challenge (If Time Permits)

Add a section to AGENTS.md that asks the Agent to always suggest a simpler alternative:

```markdown
## Agent Behavior
- After writing any code, suggest a simpler or more efficient alternative
```

Then ask the Agent to implement a complex function and see if it suggests a simpler version.

Or create AGENTS.md for a different project type:

> *"Create an AGENTS.md file for a Python web application with Flask"*

---

## Exercise Complete

Check off when done:
- [ ] Created `AGENTS.md` in project root
- [ ] Added instructions to the file
- [ ] Agent followed at least one instruction
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 16 – Create a Skill

---

## Quick Reference: AGENTS.md Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                     AGENTS.md CHEAT SHEET                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FILE LOCATION:                                                 │
│  /your-project/AGENTS.md                                        │
│                                                                 │
│  BASIC TEMPLATE:                                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ # Project Instructions                                  │    │
│  │                                                         │    │
│  │ ## Coding Standards                                     │    │
│  │ - Use 4 spaces for indentation                          │    │
│  │ - Add comments before functions                         │    │
│  │                                                         │    │
│  │ ## Build                                                │    │
│  │ - Run `make` to build                                   │    │
│  │ - Run `make test` to test                               │    │
│  │                                                         │    │
│  │ ## Agent Behavior                                       │    │
│  │ - Explain reasoning first                               │    │
│  │ - Show diffs before applying                            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  WHAT YOU CAN INCLUDE:                                          │
│  - Project description                                          │
│  - Coding standards                                             │
│  - Build/test commands                                          │
│  - Common workflows                                             │
│  - Agent behavior preferences                                   │
│  - Safety rules                                                 │
│                                                                 │
│  TIPS:                                                          │
│  - Keep it concise (1-2 pages max)                              │
│  - Be specific, not vague                                       │
│  - Update as your project evolves                               │
│  - Commit to git for team sharing                               │
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
