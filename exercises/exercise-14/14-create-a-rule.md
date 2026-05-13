# Cursor Training – Exercise 14

## Create a Rule

**Objective:** Create a persistent rule that guides the Agent's behavior – ensuring it follows your coding standards and preferences automatically.

**Time:** 10 minutes

**Setup:** Any code project (continue with `calculator.c` from previous exercises)

**This folder:** Open `exercises/exercise-14/` in Cursor. It already contains a `sample-rules/` folder with three ready-to-use `.mdc` files (`coding-standards.mdc`, `naming-conventions.mdc`, `error-handling.mdc`) you can copy into your own project's `.cursor/rules/` directory.

---

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

> Tip: A ready-made copy of this file is available at `exercises/exercise-14/sample-rules/coding-standards.mdc` in this repo.

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
