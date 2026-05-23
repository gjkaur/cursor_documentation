# Exercise 4.3: Creating and Invoking a Skill

**Module 4:** Customizing Cursor for Your Team  
**Slides:** `slides/module-04-marp.md` (Lesson 4.3)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Build and invoke reusable Agent skills for repeated workflows.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

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

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Create `.cursor/skills/security-audit/SKILL.md`:

```
Scan for:
  Critical: hardcoded secrets, SQL injection, command injection, eval()
  Medium:   no input validation, weak crypto, missing CSRF
  Low:      debug endpoints, verbose errors, outdated deps

Output: report with line numbers, fix suggestions, overall risk rating
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 4:** Invoke via slash command:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
/pr-review PR #42
/pr-review feature/payment-integration
```

---

**Step 5:** List available skills:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
What skills are available in this project?
```

---

**Step 6:** Create **Onboarding** skill — generates setup checklist from repo instructions
**Where:** **Cursor Agent panel** — ``Ctrl+L``

---

## Success criteria

- [ ] Created skills · built PR Review + Security Audit · invoked via slash command

---

## Additional reference

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
