# Cursor Training – Exercise 4

## Use Plan Mode

**Objective:** Use Plan Mode to design a change before implementing it – letting the Agent ask clarifying questions, create a detailed plan, and wait for your approval before writing any code.

**Time:** 10 minutes

**Setup:** Any code project (continue with `calculator.c` from previous exercises)

**This folder:** Open `core-exercises/exercise-4/` in Cursor. A matching [`calculator.c`](calculator.c) is included here so this exercise stays in its own subfolder.

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Press `Shift+Tab` to switch to Plan Mode | Mode indicator changes to "Plan" in the chat input |
| 2 | Type a request for a new feature or change | Agent recognizes Plan Mode |
| 3 | Press `Enter` to send | Agent asks clarifying questions instead of coding immediately |
| 4 | Answer the Agent's questions | Agent refines the plan based on your answers |
| 5 | Review the generated plan | Agent shows a detailed implementation plan |
| 6 | Type "Build it" or "Proceed" | Agent executes the plan and writes the code |

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

Choose ONE of these plan-mode requests:

### Option A: Add a New Feature (Modulo Operation)

> *"I want to add a new 'modulo' (remainder) operation to this calculator. Use Plan Mode. Ask me clarifying questions first."*

### Option B: Improve Error Handling

> *"I want to add better error handling for invalid inputs (like letters instead of numbers). Use Plan Mode. Ask me clarifying questions first."*

### Option C: Add Calculation History

> *"I want to add a feature that shows the last 5 calculations performed. Use Plan Mode. Ask me clarifying questions first."*

### Option D: Convert to Menu Loop

> *"I want to change the calculator so it keeps running until the user chooses to exit. Use Plan Mode. Ask me clarifying questions first."*

---

## Expected Agent Questions (Example)

Using Option A (Add modulo operation):

The Agent might ask:

| Question | Why It's Asked |
|----------|----------------|
| *"What key should represent modulo in the menu (e.g., option 5)?"* | Determines menu placement |
| *"How should modulo handle negative numbers?"* | Defines behavior edge cases |
| *"Should modulo be a separate function or handled inline?"* | Code organization preference |
| *"What should the output format look like?"* | User experience expectations |
| *"Should division by zero check be applied to modulo?"* | Safety considerations |

---

## Expected Plan Output (Example)

After answering the questions, the Agent will create a plan like this:

### Implementation Plan: Add Modulo Operation

**Summary:** Add a new modulo (remainder) operation as option 5 in the calculator menu.

**Files to Modify**
- `calculator.c` - Add modulo function and menu option

**Detailed Steps**

**Step 1: Add Function Prototype**

```c
int modulo(int a, int b);
```

**Step 2: Implement Modulo Function**

```c
int modulo(int a, int b) {
    if (b == 0) {
        printf("Error: Modulo by zero\n");
        return 0;
    }
    return a % b;
}
```

**Step 3: Update Menu Display**

Change menu to include:

```text
5. Modulo
```

**Step 4: Add Case in Switch Statement**

```c
case 5:
    result = modulo(x, y);
    printf("Result: %d\n", result);
    break;
```

**Estimated Changes**
- ~15 lines of code added
- No existing code removed

**Risks**
- Modulo by zero - handled with check
- Negative numbers - C's % operator works with negatives (implementation-defined behavior)

**Ready to build. Type 'Build it' to proceed.**

---

## Success Criteria

- [ ] Switched to Plan Mode (`Shift+Tab` or `/plan`)
- [ ] Mode indicator shows "Plan"
- [ ] Agent asked clarifying questions before planning
- [ ] You answered the questions
- [ ] Agent created a detailed implementation plan
- [ ] You reviewed and approved the plan
- [ ] Agent executed the plan and wrote the code

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Plan Mode not activating | Press `Shift+Tab` again. Check chat input shows "Plan" |
| Agent starts coding immediately | Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"* |
| Plan is too vague | Ask: *"Be more specific. What files will you change? What functions?"* |
| Forgot to answer a question | Scroll up and answer any unanswered questions |
| Don't like the plan | Ask: *"Change the plan to [your preference]"* |
| Agent won't build after approval | Type: *"Build it"* or *"Proceed with the plan"* |

---

## Plan Mode vs. Agent Mode Comparison

| Aspect | Agent Mode | Plan Mode |
|--------|-----------|-----------|
| **Starts coding immediately** | Yes | No |
| **Asks clarifying questions** | Rarely | Always |
| **Shows plan before coding** | No | Yes |
| **You approve before changes** | No | Yes |
| **Best for simple tasks** | Yes | Overkill |
| **Best for complex tasks** | Risky | Yes |
| **Best for unfamiliar code** | Risky | Yes |

---

## Key Takeaway

**Plan Mode = Measure twice, cut once.**

Use Plan Mode when:

- You're adding a new feature
- The change affects multiple files
- You're not 100% sure how to implement it
- Someone else needs to review the approach first
- The code is safety-critical (like industrial control systems)

Skip Plan Mode when:

- Fixing a typo
- Adding a comment
- Changing a constant value
- Any change you're 100% confident about

---

## Bonus Challenge (If Time Permits)

After executing the plan, ask the Agent to verify:

> *"Now that the code is written, test that the new modulo operation works correctly. Suggest 3 test cases with expected outputs."*

Or try a more complex plan:

> *"Switch back to Plan Mode. I want to add input validation that rejects non-numeric inputs. Plan first, then build."*

---

## Exercise Complete

Check off when done:

- [ ] Switched to Plan Mode successfully
- [ ] Agent asked clarifying questions
- [ ] Agent created a plan
- [ ] You approved the plan
- [ ] Agent executed the plan
- [ ] (Optional) Completed bonus challenge


---

## Quick Reference: Plan Mode Workflow

```text
┌─────────────────────────────────────────────────────────────────┐
│                     PLAN MODE WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Shift+Tab → Enter Plan Mode                                 │
│                    ↓                                            │
│  2. Describe what you want to build                             │
│                    ↓                                            │
│  3. Agent asks clarifying questions → You answer                │
│                    ↓                                            │
│  4. Agent creates detailed implementation plan                  │
│                    ↓                                            │
│  5. You review the plan                                         │
│                    ↓                                            │
│  6. Type "Build it" → Agent writes code                         │
│                    ↓                                            │
│  7. Review the result → Done or refine                          │
│                                                                 │
│  REMEMBER: The plan is a document you can edit.                 │
│  If you don't like something, ask the Agent to change the plan  │
│  before building.                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
