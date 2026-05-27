# Cursor Training – Exercise 2

## Explain a Specific File

**Objective:** Use the Agent to read and explain a specific file in your codebase – understanding its purpose, functions, and how it fits into the larger project.

**Time:** 10 minutes

**Setup:** Any code project with at least 2–3 files (use the same project from [Exercise 1](../exercise-1/01-open-agent-first-prompt.md), or any codebase you have access to).

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Type `@` followed by a filename from your project (e.g., `@calculator.c`) | Agent shows file suggestions; select the file |
| 4 | After the file name appears, type your question | Complete prompt ready to send |
| 5 | Press `Enter` to send | Agent reads the file and provides explanation |

---

## Code Example to Use

Use the same [`calculator.c`](../exercise-1/calculator.c) file from Exercise 1 (open the `exercise-1` folder in Cursor so `@calculator.c` resolves), or any file in your project.

To practice on a larger codebase, open any multi-file project you have locally and use `@` on a real source file (for example `@README.md` plus a file under `src/`).

### Reference: `calculator.c`

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

## Sample Prompt (Copy-Paste)

**Option A (if using `calculator.c`):**

> `@calculator.c` *Explain this file line by line. What does each function do? What are the inputs and outputs of each function?*

**Option B (generic – works with any file):**

> `@[YOUR_FILENAME]` *Explain this file in detail. What is its purpose? List all functions and what each one does. Identify any potential bugs or improvements.*

**Option C (deeper analysis – for header files):**

> `@[HEADER_FILE.h]` *Explain the purpose of this header file. What constants, types, and function prototypes are defined here? How should this be used by other files?*

---

## Expected Agent Response (Example)

Using `calculator.c`:

```text
I've analyzed `calculator.c`. This file implements a simple command-line calculator.

## File Purpose
Provides basic arithmetic operations (add, subtract, multiply, divide) through an interactive menu.

## Function Breakdown

| Function | Inputs | Output | Purpose |
|----------|--------|--------|---------|
| `main()` | None (reads from stdin) | int (0 on success) | Displays menu, gets user input, calls appropriate math function |
| `add(a, b)` | int a, int b | int (sum) | Returns a + b |
| `subtract(a, b)` | int a, int b | int (difference) | Returns a - b |
| `multiply(a, b)` | int a, int b | int (product) | Returns a * b |
| `divide(a, b)` | int a, int b | int (quotient) | Returns a / b (caller must check b != 0) |

## Key Observations

1. The `divide()` function does NOT check for division by zero – that check is done in `main()` before calling it
2. All functions use integer arithmetic (no floating point support)
3. The switch statement handles user menu choices 1-4

## Potential Improvements

- Add input validation (non-integer inputs cause issues)
- Add floating-point support for division
- Move math functions to a separate `math_ops.c` file for reusability
```

---

## Success Criteria

- [ ] Used `@filename` to reference a specific file
- [ ] Agent identified the file correctly
- [ ] Agent explained the file's purpose
- [ ] Agent listed the main functions and what they do
- [ ] Agent identified at least one potential issue or improvement

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `@filename` doesn't autocomplete | Start typing the full filename. Make sure the file exists in your project |
| Agent says "File not found" | Check the exact filename including extension. Use `@` then browse the dropdown |
| Response is too brief | Ask a more specific question: *"Explain the `divide()` function in detail"* |
| Agent ignores the `@` mention | Make sure there's a space between the `@filename` and your question |
| Wrong file is selected | Delete the `@mention` and re-type it, selecting the correct file from dropdown |

---

## Try It With Different File Types

| File Type | Example Question |
|-----------|------------------|
| **C/C++ (.c, .cpp)** | `@main.c` *Explain the memory allocation in this file* |
| **Python (.py)** | `@app.py` *What are the class hierarchies in this file?* |
| **JavaScript (.js)** | `@index.js` *Explain the async/await patterns here* |
| **Header (.h)** | `@config.h` *What constants and macros are defined?* |
| **Makefile** | `@Makefile` *Explain the build targets and dependencies* |
| **JSON/YAML** | `@config.json` *Explain the configuration structure* |

---

## Key Takeaway

The `@filename` mention is one of the most powerful Cursor features. It tells the Agent exactly which file to read – no guessing, no searching. Use it whenever you want to discuss, debug, or refactor a specific file.

**Pro Tip:** You can `@mention` multiple files at once:

> `@main.c` `@utils.c` `@math.h` *Explain how these three files work together*

---

## Bonus Challenge (If Time Permits)

Ask the Agent to compare two files:

> `@calculator.c` `@math_ops.c` *(if you have it)* *How are these files different? Could one reuse code from the other?*

Or ask for a refactoring suggestion:

> `@calculator.c` *Suggest how to split this file into smaller, more focused files*

---

## Exercise Complete ✓

Check off when done:

- [ ] Used `@filename` to reference a specific file
- [ ] Agent explained the file's purpose and functions
- [ ] Agent identified at least one improvement
- [ ] (Optional) Completed bonus challenge


