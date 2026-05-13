# Cursor Training – Exercise 17

## Invoke a Skill

**Objective:** Learn how to invoke skills – both automatically (Agent detects the need) and manually (using slash commands or natural language).

**Time:** 10 minutes

**Setup:** Use the skills created in Exercise 16 (code-reviewer, test-generator, etc.)

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
