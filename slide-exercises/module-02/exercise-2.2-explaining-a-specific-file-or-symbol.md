# Exercise 2.2: Explaining a Specific File or Symbol

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.2)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Get targeted explanations of one file or symbol without reading the whole repo.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Step 1:** Open a specific file in your project

**Step 2:** Select a function or class you want explained

**Step 3:** Use the Agent with precise context:

```
Explain the function I have selected. For each major section, tell me:
- What it does
- Why it's designed that way (trade-offs)
- Potential edge cases or bugs
- How it could be improved
```

---

**Step 4:** Ask for a concrete example:

```
Give me a concrete example of inputs and outputs for this function.
Show me what happens in the normal case and one edge case.
```

---

**Step 5:** Ask about dependencies:

```
What other functions does this call? What calls this function?
Trace the call chain two levels in each direction.
```

---

## Additional reference

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
