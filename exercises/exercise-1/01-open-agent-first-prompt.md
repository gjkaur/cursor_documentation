# Cursor Training – Exercise 1

## Open Agent & First Prompt

**Objective:** Open the Cursor Agent and ask your first question to understand a codebase.

**Time:** 10 minutes

**Setup:** Any code project (can be your own work, an open-source repo, or the sample codebase provided)

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and open a project folder (File → Open Folder) | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac) | The Agent panel opens on the right side of the screen |
| 3 | Type or copy-paste the sample prompt below into the Agent input box | The prompt appears in the input area |
| 4 | Press `Enter` to send | Agent starts responding, showing its thinking process |
| 5 | Read the Agent's response | Agent explains the codebase purpose, entry point, and key files |

---

## Code Example to Use

You can use **any codebase** you have access to. If you don't have one, create a simple test file:

### Sample File: `calculator.c`

A ready-to-use copy is included in this folder as [`calculator.c`](calculator.c). Open the `exercise-1` folder (under `exercises` in this repo) in Cursor and work from there.

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

Save this as `calculator.c` in an empty folder (or use the file in this folder), then open that folder in Cursor.

---

## Sample Prompt (Copy-Paste)

> *"Explain this codebase in 3-5 sentences. What is the main purpose? Where is the entry point (where does execution start)? List 2-3 key functions and what they do."*

---

## Expected Agent Response (Example)

```
This codebase implements a simple command-line calculator program.

The entry point is the `main()` function, which:
- Displays a menu of operations (add, subtract, multiply, divide)
- Takes user input for choice and numbers
- Calls the appropriate math function based on user choice

Key functions:
- `add(a, b)` - Returns the sum of two integers
- `divide(a, b)` - Returns the quotient, with safety check for division by zero
- `subtract(a, b)` - Returns the difference between two integers

The program includes error handling for invalid menu choices and division by zero.
```

---

## Success Criteria

- [ ] Agent panel opened successfully (`Ctrl+I` or `Cmd+I`)
- [ ] Agent responded to your prompt
- [ ] Response identified the main entry point (e.g., `main()`, `main.c`, `app.js`)
- [ ] Response listed at least 2 key functions with their purposes
- [ ] You understood the codebase better after reading the response

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent panel doesn't open | Make sure Cursor is the active window. Try `Ctrl+Shift+I` or click the Agent icon in the left sidebar |
| Agent not responding | Check your internet connection. The Agent requires an internet connection to access AI models |
| "No codebase found" error | Make sure you opened a folder (File → Open Folder), not just a single file |
| Response is too generic | Try a more specific prompt: *"What does the `main()` function do line by line?"* |
| Agent takes too long | Switch to a faster model: `/model gpt-5-mini` then ask again |

---

## Key Takeaway

You can ask the Agent to explain **any** codebase – even one you've never seen – and get a clear summary in seconds. This works for:

- Legacy code you inherited
- Open-source projects you want to contribute to
- Your own code from months ago that you've forgotten
- Team codebases you're new to

---

## Bonus Challenge (If Time Permits)

After completing the exercise, try this follow-up prompt:

> *"Now explain the most complex function in this codebase. What makes it complex? How could it be simplified?"*

This helps you identify areas of technical debt or candidates for refactoring.

---

## Exercise Complete ✓

Check off when done:

- [ ] Opened Agent panel
- [ ] Asked for codebase explanation
- [ ] Received and understood response
- [ ] (Optional) Completed bonus challenge


