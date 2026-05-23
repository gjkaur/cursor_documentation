# Exercise 2.5: Comparing Two Models

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.5)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Run the same prompt on two models and compare quality, speed, and cost.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Step 1:** Set model to Claude Sonnet, ask:

```
Explain what a closure is in JavaScript with a practical example.
```

**Step 2:** Copy the response

**Step 3:** Switch to GPT-5 Mini — ask the **same question**

**Step 4:** Compare responses side by side

---

| Comparison Point | Claude Sonnet | GPT-5 Mini |
|-----------------|---------------|------------|
| Length | | |
| Code example quality | | |
| Explanation clarity | | |
| Speed | | |

---

**Step 5:** Check token usage at bottom of chat after each request

**Step 6:** Create a personal decision matrix:

<img src="assets/module-02/exercise-2-5-cost-decision-matrix.svg" alt="Exercise 2.5 — Cost & Decision Matrix" />

---

---

## Success criteria

- [ ] Same question to two models
- [ ] Compared quality and speed
- [ ] Created personal model-selection guide

---

## Additional reference

## Available Models in Cursor

| Model | Provider | Speed | Cost | Best For |
|-------|----------|-------|------|----------|
| **GPT-5 Mini** | OpenAI | Fast | $ | Quick answers, simple tasks |
| **Composer 2** | Cursor | Fast | $$ | Everyday coding (best value) |
| **Grok 4.3** | xAI | Fastest | $$ | Interactive, speed-critical |
| **GPT-5.3 Codex** | OpenAI | Medium | $$ | Coding specialized |
| **Claude 4.6 Sonnet** | Anthropic | Medium | $$$ | Balanced daily driver |
| **Claude 4.7 Opus** | Anthropic | Slow | $$$$ | Maximum quality |

---

## Step-by-Step Comparison Process

### Step 1: Run with GPT-5 Mini (Fast & Cheap)

**Switch to GPT-5 Mini:**

Type in Agent: `/model gpt-5-mini`

**Ask the prompt (e.g., Prompt A):**

> *"Explain the `divide()` function in `calculator.c`. What happens if someone tries to divide by zero? Suggest an improvement."*

**Record:**

- Time to first response: _____ seconds
- Response length: _____ lines
- Quality (1-5): _____
- Detail level (Basic / Medium / Detailed): _____

---

### Step 2: Run with Composer 2 (Cursor's Default)

**Switch to Composer 2:**

Type in Agent: `/model composer-2`

**Ask the EXACT SAME prompt:**

> *"Explain the `divide()` function in `calculator.c`. What happens if someone tries to divide by zero? Suggest an improvement."*

**Record:**

- Time to first response: _____ seconds
- Response length: _____ lines
- Quality (1-5): _____
- Detail level (Basic / Medium / Detailed): _____

---

### Step 3: Run with Grok 4.3 (Fastest)

**Switch to Grok 4.3:**

Type in Agent: `/model grok-4.3`

**Ask the EXACT SAME prompt:**

> *"Explain the `divide()` function in `calculator.c`. What happens if someone tries to divide by zero? Suggest an improvement."*

**Record:**

- Time to first response: _____ seconds
- Response length: _____ lines
- Quality (1-5): _____
- Detail level (Basic / Medium / Detailed): _____

---

### Step 4: Run with Claude 4.6 Sonnet (Balanced)

**Switch to Claude 4.6 Sonnet:**

Type in Agent: `/model claude-4.6-sonnet`

**Ask the EXACT SAME prompt:**

> *"Explain the `divide()` function in `calculator.c`. What happens if someone tries to divide by zero? Suggest an improvement."*

**Record:**

- Time to first response: _____ seconds
- Response length: _____ lines
- Quality (1-5): _____
- Detail level (Basic / Medium / Detailed): _____

---

### Step 5: Run with Claude 4.7 Opus (Quality)

**Switch to Claude 4.7 Opus:**

Type in Agent: `/model claude-4.7-opus`

**Ask the EXACT SAME prompt:**

> *"Explain the `divide()` function in `calculator.c`. What happens if someone tries to divide by zero? Suggest an improvement."*

**Record:**

- Time to first response: _____ seconds
- Response length: _____ lines
- Quality (1-5): _____
- Detail level (Basic / Medium / Detailed): _____

---

## Comparison Recording Sheet

Copy this table to record your observations:

| Model | Speed (1-5) | Quality (1-5) | Detail Level | Best For |
|-------|-------------|---------------|--------------|----------|
| GPT-5 Mini | | | | |
| Composer 2 | | | | |
| Grok 4.3 | | | | |
| Claude 4.6 Sonnet | | | | |
| Claude 4.7 Opus | | | | |

**Speed Rating:**

- 1 = Very Slow (>20 seconds)
- 3 = Medium (5-10 seconds)
- 5 = Very Fast (<2 seconds)

**Quality Rating:**

- 1 = Poor (wrong or confusing)
- 3 = Good (accurate but basic)
- 5 = Excellent (detailed, insightful, thorough)

---

## Expected Observations

| Model | Typical Speed | Typical Quality | Best Use Case |
|-------|---------------|-----------------|---------------|
| **GPT-5 Mini** | Very Fast | Basic | Quick answers, simple explanations |
| **Composer 2** | Fast | Good | Everyday coding, best value |
| **Grok 4.3** | Fastest | Good | Interactive debugging, speed-critical |
| **Claude 4.6 Sonnet** | Medium | Very Good | Code review, refactoring |
| **Claude 4.7 Opus** | Slow | Excellent | Complex analysis, safety-critical |

---

## Expected Response Examples

### GPT-5 Mini Response (Fast, Basic)

```text
The divide() function returns a / b. If b is 0, division by zero occurs which causes undefined behavior (program crash).

Improvement: Add a check in divide() itself, not just in main():
if (b == 0) { printf("Error"); return 0; }
```

### Claude 4.6 Sonnet Response (Medium, Detailed)

Prose (illustrative):

```text
The divide() function performs integer division. Currently, it does NOT check for division by zero – that check happens in main() before calling divide().

**What happens on division by zero?**
If divide(10, 0) were called directly, integer division by zero causes undefined behavior (typically program crash).

**Improvement suggestions:**

1. Add guard in divide() itself.
2. Consider floating-point division for non-integer results.
```

Suggested `divide()` guard:

```c
int divide(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }
    return a / b;
}
```

Optional `double` helper (requires `#include <math.h>` for `NAN`):

```c
double divide_double(double a, double b) {
    if (b == 0.0) return NAN;
    return a / b;
}
```

### Claude 4.7 Opus Response (Slower, Most Thorough)

Illustrative structure:

```text

## Analysis of the divide() Function

**Current Implementation:** performs integer division (truncates toward zero).

**Division by Zero Behavior:** undefined behavior per the C standard; may SIGFPE, crash, or behave unpredictably on embedded targets.

**Current Protection:** main() checks y != 0 before calling divide(), but divide() is still unsafe if called elsewhere.

**Improvement:** defensive checks in divide() and/or an error-code API for ambiguous return values like 0.
```

Example defensive `divide()`:

```c
int divide(int a, int b) {
    if (b == 0) {
        fprintf(stderr, "Error: Division by zero in divide()\n");
        return 0;  /* or use an error-code convention */
    }
    return a / b;
}
```

Example status API:

```c
typedef enum {
    MATH_OK = 0,
    MATH_DIVIDE_BY_ZERO,
    MATH_OVERFLOW
} math_status_t;

math_status_t divide_safe(int a, int b, int* result) {
    if (b == 0) return MATH_DIVIDE_BY_ZERO;
    *result = a / b;
    return MATH_OK;
}
```

**Note:** On two's complement systems, `INT_MIN / -1` can overflow; safety-critical code may need an explicit check.

---

## How to Switch Models (Quick Reference)

| Method | Command |
|--------|---------|
| **Slash command in chat** | `/model gpt-5-mini` |
| **Slash command in chat** | `/model composer-2` |
| **Slash command in chat** | `/model claude-4.6-sonnet` |
| **Slash command in chat** | `/model claude-4.7-opus` |
| **CLI flag** | `agent --model gpt-5-mini "prompt"` |
| **Dropdown** | Click model name in chat input |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Model not available | Check your plan – some models require Pro or higher |
| `/model` command not working | Type it in the Agent chat, not in terminal |
| Can't tell which model is active | Look at the model name in the chat input dropdown |
| Switch doesn't seem to apply | Type `/model` alone to see current model |
| Responses are too similar | Try a more complex prompt (code generation or debugging) |

---

## Model Selection Decision Guide

```
┌─────────────────────────────────────────────────────────────────┐
│                 WHEN TO USE EACH MODEL                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SIMPLE TASKS (typo fixes, comments, quick questions)          │
│  → GPT-5 Mini or Grok 4.3 (fastest, cheapest)                  │
│                                                                 │
│  EVERYDAY CODING (80% of your work)                            │
│  → Composer 2 or GPT-5.3 Codex (best value)                    │
│                                                                 │
│  CODE REVIEW & REFACTORING                                     │
│  → Claude 4.6 Sonnet (good balance)                            │
│                                                                 │
│  COMPLEX ANALYSIS (architecture, safety-critical)              │
│  → Claude 4.7 Opus (maximum quality)                           │
│                                                                 │
│  INTERACTIVE DEBUGGING (need fast responses)                   │
│  → Grok 4.3 (fastest)                                          │
│                                                                 │
│  WHEN UNSURE → Start with Composer 2, upgrade if needed        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaway

**Different models for different tasks.**

- Use **cheap/fast models** (GPT-5 Mini, Grok) for simple questions
- Use **balanced models** (Composer 2, Claude Sonnet) for daily coding
- Use **premium models** (Claude Opus) for complex, safety-critical work

**Cost-saving tip:** Start with a cheaper model. If the response isn't good enough, switch to a smarter model for just that task.

---

## Bonus Challenge (If Time Permits)

Compare two models on a code generation task:

**Prompt:** *"Write a function that validates if a string is a valid email address"*

Compare:

- GPT-5 Mini (fast, cheap)
- Claude Opus (slower, expensive)

Does the extra cost justify the quality difference for this task?

---
