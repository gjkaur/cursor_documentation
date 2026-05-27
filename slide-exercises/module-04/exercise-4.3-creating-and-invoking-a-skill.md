# Exercise 4.3: Creating and Invoking a Skill

**Module 4:** Customizing Cursor for Your Team  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 4, Lesson 4.3)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Build and invoke reusable Agent skills for repeated workflows.

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

Create `.cursor/skills/pr-review/SKILL.md`:

```
name: pr-review
description: Review a PR for code quality, security, and team standards

Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD)
Step 2: Review — code quality, security, testing, docs, style
Step 3: Output formatted review with Critical / Warning / Suggestion
Verdict: APPROVE / REQUEST CHANGES / COMMENT
```

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Create `.cursor/skills/security-audit/SKILL.md`:

```
Scan for:
  Critical: hardcoded secrets, SQL injection, command injection, eval()
  Medium:   no input validation, weak crypto, missing CSRF
  Low:      debug endpoints, verbose errors, outdated deps

Output: report with line numbers, fix suggestions, overall risk rating
```

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Step 4:** Invoke via slash command:
**Where:** **Agent panel** — ``Ctrl+I``

```
/pr-review PR #42
/pr-review feature/payment-integration
```

---

**Step 5:** List available skills:
**Where:** **Agent panel** — ``Ctrl+I``

```
What skills are available in this project?
```

---

**Step 6:** Create **Onboarding** skill — generates setup checklist from repo instructions
**Where:** **Agent panel** — ``Ctrl+I``

**Success Criteria:** Created skills · built PR Review + Security Audit · invoked via slash command

---

## Success criteria

- [ ] Created skills · built PR Review + Security Audit · invoked via slash command

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create the `.cursor/skills/` directory | Folder for skills |
| 2 | Create a skill subfolder | Folder for your specific skill |
| 3 | Create `SKILL.md` with frontmatter | Skill file ready |
| 4 | Add skill instructions | Agent learns the workflow |
| 5 | Test the skill | Agent follows the skill instructions |

---

## What Are Skills?

| Aspect | Description |
|--------|-------------|
| **What they are** | Reusable packages that teach the Agent domain-specific tasks |
| **Where they live** | `.cursor/skills/` folder |
| **File format** | Markdown with YAML frontmatter (`SKILL.md`) |
| **How they work** | Agent reads the skill and follows its instructions |
| **Compared to Rules** | Skills are for specific workflows; Rules are for persistent guidelines |

---

## Skill vs. Rule vs. AGENTS.md

| Feature | AGENTS.md | Rules (.mdc) | Skills |
|---------|-----------|--------------|--------|
| **Purpose** | Project overview | Persistent guidelines | Specific workflows |
| **When used** | Always | Always or contextually | On demand or auto-detected |
| **Complexity** | Simple | Medium | Can include scripts |
| **Best for** | Basic instructions | Coding standards | Multi-step tasks |

---

## Create Your First Skill

### Step 1: Create the Skills Directory

In your project root, create the folder structure:

```bash
mkdir -p .cursor/skills/code-reviewer
```

### Step 2: Create SKILL.md

Create `.cursor/skills/code-reviewer/SKILL.md` with this content:

```yaml
---
name: code-reviewer
description: Reviews code for quality, bugs, and style issues. Use after writing or modifying code.
---

# Code Reviewer Skill

You are an expert code reviewer. When invoked, perform the following:

## Step 1: Understand the Code
- Read the file(s) being reviewed
- Identify the purpose of each function

## Step 2: Check for Issues
Look for these common problems:
- Missing or incorrect error handling
- Off-by-one errors in loops
- Uninitialized variables
- Memory leaks (if applicable)
- NULL pointer dereferences
- Buffer overflows
- Magic numbers (use constants instead)

## Step 3: Style and Readability
- Are variable names descriptive?
- Is there appropriate comments?
- Is the indentation consistent?
- Are functions too long (>30 lines)?

## Step 4: Provide Feedback
Format your response as:

### Critical Issues (Must Fix)
- [Issue description with line number]

### Suggestions (Should Consider)
- [Suggestion with explanation]

### Nice to Have (Optional)
- [Minor improvement idea]

## Step 5: Summary
- Overall assessment (Excellent / Good / Needs Improvement)
- 1-2 sentences on the most important change
```

A ready-to-copy version of this file lives at `core-exercises/exercise-16/sample-skills/code-reviewer/SKILL.md`.

---

## Sample Skills to Create

### Skill 1: Documentation Generator

```yaml
---
name: doc-generator
description: Generates documentation comments for functions. Use when adding new functions.
---

# Documentation Generator Skill

When invoked, add documentation comments to functions:

## For C functions:

/**
 * Brief description of what the function does
 *
 * @param param1 Description of first parameter
 * @param param2 Description of second parameter
 * @return Description of return value
 */

## For Python functions:

def function_name(param1, param2):
    """
    Brief description of what the function does.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value
    """

## Rules:
- Every function must have documentation
- Describe what, not how
- Include parameter descriptions
- Include return value description
```

Ready-to-copy version: `core-exercises/exercise-16/sample-skills/doc-generator/SKILL.md`.

### Skill 2: Test Generator

```yaml
---
name: test-generator
description: Generates unit tests for functions. Use when adding new functions or fixing bugs.
---

# Test Generator Skill

When invoked, generate unit tests for the specified function.

## Test Structure:
1. Normal case – typical inputs
2. Edge case – boundary values
3. Error case – invalid inputs
4. Corner case – empty/zero values

## For C (using assert):

void test_function_name(void) {
    // Normal case
    assert(function(input) == expected);

    // Edge case
    assert(function(edge) == expected_edge);

    printf("test_function_name passed\n");
}

## For Python (using assert):

def test_function_name():
    # Normal case
    assert function(input) == expected

    # Edge case
    assert function(edge) == expected_edge

    print("test_function_name passed")

## Guidelines:
- One test function per function being tested
- Test names should describe what is being tested
- Each test should be independent
```

Ready-to-copy version: `core-exercises/exercise-16/sample-skills/test-generator/SKILL.md`.

### Skill 3: Bug Hunter

```yaml
---
name: bug-hunter
description: Actively searches for bugs in the codebase. Use when something isn't working correctly.
---

# Bug Hunter Skill

You are a bug hunting specialist. Your goal is to find the root cause of issues.

## Investigation Process:
1. Ask for the symptoms (what's not working?)
2. Read the relevant code sections
3. Look for common bug patterns:
   - Off-by-one errors
   - Uninitialized variables
   - Race conditions (if multithreaded)
   - Resource leaks
   - Logic errors in conditionals

4. Form hypotheses about the cause
5. Suggest debugging steps (adding logs, assertions)
6. Propose fixes with explanations

## Output Format:
- **Symptoms observed:** [restate]
- **Suspected cause:** [hypothesis]
- **Evidence:** [what supports this]
- **Suggested fix:** [code change]
- **Verification:** [how to test the fix]
```

Ready-to-copy version: `core-exercises/exercise-16/sample-skills/bug-hunter/SKILL.md`.

---

## How to Invoke a Skill

| Method | Example |
|--------|---------|
| **Auto-detection** | Agent detects relevant task and uses skill automatically |
| **Manual invocation** | Type `/code-reviewer` to invoke the skill |
| **Natural language** | "Use the code-reviewer skill to review my changes" |

---

## Test Your Skill

### Step 1: Invoke the Skill

Type in Agent:

> *"Use the code-reviewer skill to review the `divide` function in calculator.c"*

### Step 2: Observe the Response

The Agent should follow the skill's structure:

```
## Code Reviewer Skill - Review of divide() function

### Step 1: Understand the Code
The divide() function takes two integers and returns their quotient...

### Step 2: Check for Issues

**Critical Issues (Must Fix):**
- No check for NULL pointer (though ints can't be NULL)
- Division by zero check only in main(), not in function itself

**Suggestions (Should Consider):**
- Add division by zero check inside divide() for safety
- Consider returning an error code instead of 0

**Nice to Have (Optional):**
- Add comment explaining integer division behavior

### Step 3: Style and Readability
- Variable names are clear
- Function is appropriately short

### Summary
Good - Needs Improvement: Add division by zero check inside the function.
```

---

## Success Criteria

- [ ] Created `.cursor/skills/` directory
- [ ] Created a skill subfolder with `SKILL.md`
- [ ] Skill has proper YAML frontmatter (name, description)
- [ ] Skill has clear step-by-step instructions
- [ ] Invoked the skill successfully
- [ ] Agent followed the skill's structure

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Skill not recognized | Check file path: `.cursor/skills/skill-name/SKILL.md` |
| Agent ignores skill | Invoke manually: `/skill-name` or "Use the [name] skill" |
| Frontmatter error | Make sure `---` is before and after YAML |
| Description not working | Keep description concise and action-oriented |
| Skill too verbose | Skills work best with 5-10 clear steps |

---

## Key Takeaway

**Skills are reusable workflows that teach the Agent how to perform specific tasks.**

Once you create a skill, you (and your team) can invoke it anytime – the Agent will follow the same proven process every time.

**When to create a skill:**
- You find yourself giving the same instructions repeatedly
- You have a multi-step process (code review, testing, deployment)
- You want to standardize a workflow across your team

---

## Bonus Challenge (If Time Permits)

Create a skill for your team's specific workflow:

> *"Create a skill called 'firmware-deploy' that guides the Agent through building, flashing, and testing firmware on a target device"*

Or combine multiple skills:

> *"Create a skill called 'pre-commit-checklist' that runs the code-reviewer skill, then the test-generator skill, then the doc-generator skill in sequence"*

---

## Exercise Complete

Check off when done:
- [ ] Created `.cursor/skills/` directory
- [ ] Created a skill with SKILL.md
- [ ] Skill has name and description in frontmatter
- [ ] Skill has step-by-step instructions
- [ ] Invoked the skill successfully
- [ ] Agent followed the skill's structure
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 17 – Invoke a Skill

---

## Quick Reference: Skills Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                       SKILLS CHEAT SHEET                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FILE STRUCTURE:                                                │
│  .cursor/skills/                                                │
│  └── skill-name/                                                │
│      └── SKILL.md                                               │
│                                                                 │
│  SKILL.MD FORMAT:                                               │
│  ---                                                            │
│  name: skill-name                                               │
│  description: What this skill does and when to use it           │
│  ---                                                            │
│                                                                 │
│  # Skill Title                                                  │
│                                                                 │
│  Step-by-step instructions for the Agent...                     │
│                                                                 │
│  EXAMPLE SKILLS:                                                │
│  • code-reviewer – Review code for issues                       │
│  • test-generator – Generate unit tests                         │
│  • doc-generator – Add documentation comments                   │
│  • bug-hunter – Find and fix bugs                               │
│  • refactor-assistant – Suggest refactoring                     │
│                                                                 │
│  INVOKING SKILLS:                                               │
│  • Auto: Agent detects relevant task                            │
│  • Manual: "/skill-name"                                        │
│  • Natural: "Use the [name] skill to..."                        │
│                                                                 │
│  BEST PRACTICES:                                                │
│  • Keep skills focused (one job per skill)                      │
│  • Use clear, numbered steps                                    │
│  • Provide examples in the skill                                │
│  • Test the skill before sharing                                │
│  • Commit skills to git for team use                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files and skills are available |
| 2 | Use natural language to invoke a skill | Agent recognizes and uses the skill |
| 3 | Use slash command to invoke a skill | Skill runs immediately |
| 4 | Let Agent auto-detect skill need | Agent invokes skill automatically |
| 5 | Compare results with/without skill | See the difference skill makes |

---

## Three Ways to Invoke a Skill

| Method | How to Use | Example |
|--------|------------|---------|
| **Natural Language** | Say "Use the [skill-name] skill" | *"Use the code-reviewer skill to review my code"* |
| **Slash Command** | Type `/skill-name` | `/code-reviewer` |
| **Auto-Detection** | Agent recognizes the task | Asking for code review triggers the skill |

---

## Prerequisite: Skills from Exercise 16

Make sure you have at least one skill created:

```
.cursor/skills/
├── code-reviewer/
│   └── SKILL.md
├── test-generator/
│   └── SKILL.md
└── doc-generator/
│   └── SKILL.md
```

---

## Method 1: Natural Language Invocation

### Sample Prompts

> *"Use the code-reviewer skill to review the `add` function in calculator.c"*

> *"Invoke the test-generator skill to create tests for the `multiply` function"*

> *"Run the doc-generator skill on all functions in calculator.c"*

### Expected Response

```
I'll use the **code-reviewer skill** to review the `add` function.

## Step 1: Understand the Code
The `add` function takes two integers and returns their sum...

## Step 2: Check for Issues

**Critical Issues (Must Fix):**
- No overflow checking (if a and b are very large, sum may overflow)

**Suggestions (Should Consider):**
- Add comment explaining the function
- Consider using long long for larger numbers

**Nice to Have (Optional):**
- Could be a macro for performance

## Step 3: Style and Readability
- Variable names are clear
- Function is appropriately short

## Summary
Good - Consider adding overflow protection.
```

---

## Method 2: Slash Command Invocation

### How to Use

In the Agent chat, type:

```
/code-reviewer
```

Then follow up with what you want reviewed:

> *"Review the divide function"*

### Complete Example

```
User: /code-reviewer

Agent: Code Reviewer skill activated. What code would you like me to review?

User: Review the divide function in calculator.c

Agent: [Follows skill structure to review the function]
```

---

## Method 3: Auto-Detection

The Agent automatically detects when a skill might be useful based on your request.

### Example Prompts That May Trigger Auto-Detection

| Prompt | Likely Skill Triggered |
|--------|------------------------|
| *"Review this code for bugs"* | code-reviewer |
| *"Check my code quality"* | code-reviewer |
| *"Write tests for this function"* | test-generator |
| *"Add documentation comments"* | doc-generator |

### How Auto-Detection Works

```
User: "Review this code for bugs"

Agent recognizes this matches the code-reviewer skill's description
→ Automatically invokes the skill
→ Follows the skill's step-by-step process
```

---

## Compare: Without Skill vs. With Skill

### Without Skill (Generic Response)

> *"Review the add function"*

**Typical response:**
```
The add function adds two numbers. It looks fine. It returns a+b.
```

### With Skill (Using code-reviewer)

> *"Use the code-reviewer skill to review the add function"*

**Typical response:**
```
## Code Reviewer Skill - Review of add() function

### Step 1: Understand the Code
The function takes two ints and returns their sum...

### Step 2: Check for Issues

**Critical Issues:**
- None found

**Suggestions:**
- Consider adding overflow detection
- Add documentation comment

### Step 3: Style
- Good: short and focused
- Could improve: variable names are fine but minimal

### Summary
Good - ready for use in production.
```

**The skill provides a structured, thorough review – not just a quick opinion.**

---

## Listing Available Skills

To see what skills are available, ask:

> *"What skills do I have available?"*

Or check the `.cursor/skills/` directory.

**Expected response:**
```
Available skills in this project:

1. code-reviewer - Reviews code for quality, bugs, and style issues
2. test-generator - Generates unit tests for functions
3. doc-generator - Adds documentation comments to functions

To invoke a skill, type /skill-name or say "Use the [skill-name] skill"
```

---

## Success Criteria

- [ ] Invoked a skill using natural language
- [ ] Invoked a skill using slash command (`/skill-name`)
- [ ] Observed Agent following skill structure
- [ ] (Optional) Observed auto-detection of skill
- [ ] Compared response quality with and without skill

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Skill not found | Make sure SKILL.md is in `.cursor/skills/skill-name/` |
| Slash command not working | Type `/` then start typing skill name – should autocomplete |
| Agent doesn't use skill | Be explicit: "Use the [name] skill" |
| Auto-detection not working | Check skill description – make it clear when to use |
| Multiple skills triggered | Be specific about which skill you want |

---

## Key Takeaway

**Skills give the Agent a structured playbook for specific tasks.**

- **Natural language** = Most flexible, easy to remember
- **Slash command** = Fastest, works well for repeated use
- **Auto-detection** = Most seamless, Agent figures it out

**Best practice:** Start with explicit invocation until you trust the auto-detection.

---

## Bonus Challenge (If Time Permits)

Create a composite workflow:

> *"First, use the code-reviewer skill on calculator.c, then use the doc-generator skill to add comments to any functions missing documentation"*

Or create a custom slash command that chains skills:

> *"Create a slash command called `/full-review` that runs code-reviewer, then test-generator, then doc-generator in sequence"*

---

## Exercise Complete ✓

Check off when done:
- [ ] Invoked skill using natural language
- [ ] Invoked skill using slash command
- [ ] Agent followed skill structure
- [ ] Observed difference between skill and non-skill responses
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 18 – Create a Subagent

---

## Quick Reference: Invoking Skills Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                    INVOKING SKILLS CHEAT SHEET                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  THREE WAYS TO INVOKE:                                          │
│                                                                 │
│  1. NATURAL LANGUAGE                                            │
│     "Use the code-reviewer skill to review my code"            │
│     "Run the test-generator skill"                             │
│                                                                 │
│  2. SLASH COMMAND                                               │
│     /code-reviewer                                              │
│     /test-generator                                             │
│     /doc-generator                                              │
│                                                                 │
│  3. AUTO-DETECTION                                              │
│     Agent recognizes the task and uses the skill automatically │
│     "Review this function" → triggers code-reviewer            │
│     "Write tests" → triggers test-generator                    │
│                                                                 │
│  CHECK AVAILABLE SKILLS:                                        │
│     "What skills do I have?"                                   │
│     "List available skills"                                    │
│                                                                 │
│  SKILL NAMING TIPS:                                             │
│     • Use hyphens for multi-word names                          │
│     • Keep names short and descriptive                          │
│     • Match the skill to what users will type                   │
│                                                                 │
│  EXAMPLE SESSION:                                               │
│     User: /code-reviewer                                        │
│     Agent: Code Reviewer skill activated. What code?           │
│     User: Review calculator.c                                  │
│     Agent: [Follows skill's step-by-step review]               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Next:** [`Exercise 17 – Invoke a Skill`](../../core-exercises/exercise-17/17-invoke-a-skill.md)

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
