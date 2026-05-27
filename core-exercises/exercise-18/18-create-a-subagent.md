# Cursor Training – Exercise 18

## Create a Subagent

**Objective:** Create a specialized subagent – a dedicated AI assistant that the main Agent can delegate tasks to, keeping each subagent focused on a specific role.

**Time:** 10 minutes

**Setup:** Any code project (continue with `calculator.c` from previous exercises)

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create the `.cursor/agents/` directory | Folder for subagent definitions |
| 2 | Create a subagent markdown file | Subagent definition ready |
| 3 | Add YAML frontmatter with name and description | Subagent has identity |
| 4 | Add system prompt instructions | Subagent knows its role |
| 5 | Test the subagent | Main Agent delegates to it |

---

## What Are Subagents?

| Aspect | Description |
|--------|-------------|
| **What they are** | Specialized AI assistants that the main Agent can delegate to |
| **Where they live** | `.cursor/agents/` folder |
| **File format** | Markdown with YAML frontmatter (`.md` files) |
| **How they work** | Main Agent launches subagent for specific tasks |
| **Benefits** | Context isolation, parallel execution, specialized expertise |

---

## Subagent vs. Skill vs. Rule

| Feature | Rule | Skill | Subagent |
|---------|------|-------|----------|
| **Purpose** | Persistent guidelines | Reusable workflow | Specialized assistant |
| **Context** | Shared with main Agent | Shared with main Agent | Isolated context window |
| **Invocation** | Automatic | Manual or auto | Delegated by main Agent |
| **Best for** | Coding standards | Step-by-step tasks | Complex, focused work |

---

## Create Your First Subagent

### Step 1: Create the Agents Directory

In your project root, create the folder:

```bash
mkdir -p .cursor/agents
```

### Step 2: Create a Subagent File

Create `.cursor/agents/verifier.md` with this content:

```yaml
---
name: verifier
description: Validates completed work. Use after tasks are marked done to confirm quality.
model: inherit
readonly: true
---

You are a skeptical validator. Your job is to verify that work claimed as complete actually works correctly.

## When Invoked
You will be given a description of what was supposedly completed and the code that was changed.

## Your Process
1. Identify what was claimed to be completed
2. Check that the implementation exists and is functional
3. Run through test cases mentally (or suggest tests)
4. Look for edge cases that may have been missed
5. Verify error handling is present

## Output Format
Report your findings:

### Verified (Working correctly)
- [What works]

### Issues Found (Not working or incomplete)
- [Issue description with specifics]

### Missing Edge Cases
- [Edge cases not handled]

### Recommendation
- [Pass / Fail / Needs Rework]

## Important
- Be thorough and skeptical
- Do not accept claims at face value
- Test everything you can
```

---

## Sample Subagents to Create

### Subagent 1: Debugger

Create `.cursor/agents/debugger.md`:

```yaml
---
name: debugger
description: Debugging specialist for errors and test failures. Use when encountering bugs.
model: inherit
readonly: false
---

You are an expert debugger specializing in root cause analysis.

## When Invoked
You will receive an error message or bug description and relevant code.

## Your Process
1. Capture the error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Determine the root cause
5. Suggest a fix

## Output Format
- **Root Cause:** [Explanation]
- **Evidence:** [What supports this]
- **Proposed Fix:** [Code change]
- **Testing Approach:** [How to verify]
```

### Subagent 2: Test Runner

Create `.cursor/agents/test-runner.md`:

```yaml
---
name: test-runner
description: Test automation expert. Use proactively to run tests and fix failures.
model: inherit
readonly: false
---

You are a test automation expert.

## Your Responsibilities
- When you see code changes, proactively run appropriate tests
- Analyze test failures
- Fix issues while preserving test intent

## When Tests Fail
1. Analyze the failure output
2. Identify the root cause
3. Fix the issue
4. Re-run to verify
5. Report results

## Output Format
- **Tests Passed:** [Number]
- **Tests Failed:** [Number]
- **Failures Analyzed:** [List with causes]
- **Fixes Applied:** [Description]
```

### Subagent 3: Code Explainer

Create `.cursor/agents/explainer.md`:

```yaml
---
name: explainer
description: Code explanation specialist. Use when you need to understand complex code.
model: inherit
readonly: true
---

You are a code explanation expert. Your job is to make complex code understandable.

## Your Process
1. Read the code thoroughly
2. Identify the main purpose
3. Break down complex sections
4. Explain in plain language
5. Provide examples of usage

## Output Format
- **Purpose:** [One sentence summary]
- **How It Works:** [Step-by-step explanation]
- **Key Functions/Variables:** [List with descriptions]
- **Example Usage:** [Code example]
- **Complexity Notes:** [What makes it complex]
```

---

## How Subagents Work

```
┌─────────────────────────────────────────────────────────────────┐
│                    SUBAGENT WORKFLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  User: "Verify that the divide function works correctly"       │
│                    ↓                                           │
│  Main Agent recognizes task → delegates to verifier subagent   │
│                    ↓                                           │
│  Verifier subagent (isolated context):                         │
│    1. Reads the divide function                                │
│    2. Checks for division by zero handling                     │
│    3. Tests edge cases mentally                                │
│    4. Reports findings                                         │
│                    ↓                                           │
│  Verifier returns results to Main Agent                        │
│                    ↓                                           │
│  Main Agent presents results to user                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Test Your Subagent

### Step 1: Ask the Main Agent to Use the Subagent

Type in Agent:

> *"Use the verifier subagent to check the divide function in calculator.c"*

### Step 2: Observe the Response

The main Agent should delegate to your subagent:

```
I'll delegate to the verifier subagent to validate the divide function.

**Verifier Subagent Report:**

### Verified (Working correctly)
- Function returns correct quotient for normal inputs (10/2=5)
- Handles positive and negative numbers

### Issues Found (Not working or incomplete)
- Division by zero check exists in main() but NOT inside divide()
- If divide() is called from elsewhere, it could crash

### Missing Edge Cases
- Division by zero inside function itself
- Integer overflow when dividing INT_MIN by -1

### Recommendation
- Needs Rework: Add division by zero check inside divide() function
```

---

## Success Criteria

- [ ] Created `.cursor/agents/` directory
- [ ] Created a subagent `.md` file with YAML frontmatter
- [ ] Subagent has `name` and `description` fields
- [ ] Subagent has clear instructions
- [ ] Main Agent delegated task to subagent
- [ ] Subagent returned structured results

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Subagent not found | Check file path: `.cursor/agents/agent-name.md` |
| Main Agent doesn't delegate | Be explicit: "Use the [name] subagent to..." |
| Frontmatter error | Make sure `---` is before and after YAML |
| Subagent has no effect | Check `name` matches what you're calling |
| Subagent can't edit files | Set `readonly: false` to allow edits |

---

## Key Takeaway

**Subagents are specialized AI assistants that work for the main Agent.**

Each subagent has its own context window, so long-running tasks don't clutter the main conversation. This is perfect for:

- Verification (double-check work)
- Testing (run and fix tests)
- Debugging (deep dive into errors)
- Code exploration (search without context pollution)

---

## Bonus Challenge (If Time Permits)

Create a subagent that calls another subagent:

> *"Create a 'lead-inspector' subagent that delegates to 'verifier' and 'explainer' subagents, then combines their reports"*

Or set `readonly: false` and let a subagent make changes:

> *"Create a 'fixer' subagent that can modify code to fix issues found by verifier"*

---

## Exercise Complete

Check off when done:
- [ ] Created `.cursor/agents/` directory
- [ ] Created a subagent with YAML frontmatter
- [ ] Subagent has name, description, instructions
- [ ] Main Agent delegated task to subagent
- [ ] Subagent returned structured results
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 19 – CLI – Interactive Mode

---

## Quick Reference: Subagents Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                     SUBAGENTS CHEAT SHEET                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FILE LOCATION:                                                 │
│  .cursor/agents/agent-name.md                                  │
│                                                                 │
│  FILE FORMAT:                                                   │
│  ---                                                            │
│  name: agent-name                                               │
│  description: What this agent does and when to use it           │
│  model: inherit                 # Optional: specific model      │
│  readonly: false                # Can it edit files?            │
│  ---                                                            │
│                                                                 │
│  Your instructions for the subagent...                          │
│                                                                 │
│  EXAMPLE SUBAGENTS:                                             │
│  • verifier – Validates completed work                          │
│  • debugger – Debugs errors and failures                        │
│  • test-runner – Runs tests and fixes failures                  │
│  • explainer – Explains complex code                            │
│  • security-auditor – Checks for vulnerabilities                │
│                                                                 │
│  INVOKING SUBAGENTS:                                            │
│  "Use the verifier subagent to check my work"                  │
│  "Have the debugger investigate this error"                    │
│  "Run the test-runner subagent"                                │
│                                                                 │
│  BENEFITS:                                                      │
│  • Isolated context (no pollution)                             │
│  • Parallel execution possible                                  │
│  • Specialized expertise                                        │
│  • Reusable across projects                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
