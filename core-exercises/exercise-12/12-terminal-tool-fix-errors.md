# Cursor Training – Exercise 12

## Terminal Tool – Fix Errors

**Objective:** Let the Agent compile code, detect compilation errors, and automatically fix them – simulating a real development workflow where builds fail and need correction.

**Time:** 10 minutes

**Setup:** A project with an intentionally broken code file (use the sample below)

**This folder:** Open `core-exercises/exercise-12/` in Cursor. It already contains `broken_calculator.c` (C version) and `broken_calculator.py` (Python alternative) so you can run the exercise as-is.

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Ask Agent to compile the broken code | Compilation fails with errors |
| 4 | Ask Agent to fix the errors | Agent identifies and fixes each error |
| 5 | Ask Agent to re-compile | Compilation succeeds |

---

## Setup: The Broken C File

The file `broken_calculator.c` in this folder has intentional errors. You can also recreate it from scratch using the snippet below.

```c
#include <stdio.h

// Missing semicolon after include
// Missing function return types
// Misspelled function names
// Missing closing braces

add(int a, int b)
    return a + b;
}

subtract(int a, int b) {
    return a - b
// Missing semicolon

multiply(int a, int b {
    return a * b;
}

divide(int a, int b)
    if (b == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }
    return a / b;
}

int main() {
    int x = 10, y = 5;

    printf("Addition: %d\n", add(x, y));
    printf("Subtraction: %d\n", subtract(x, y));
    printf("Multiplication: %d\n", multiply(x, y));
    printf("Division: %d\n", divide(x, y));

    return 0;
// Missing closing brace for main
```

This file has multiple intentional errors:

- Missing `>` in `#include <stdio.h`
- Missing return types on functions
- Missing semicolons
- Missing braces and parentheses

---

## Alternative: Broken Python File

If you prefer Python, use `broken_calculator.py` in this folder (or recreate it):

```python
# Broken Python Calculator

def add(a, b)
    return a + b  # Missing colon

def subtract(a, b)
    return a - b

def multiply(a, b)
    return a * b

def divide(a, b)
    if b = 0:  # Should be == not =
        print("Error: Division by zero")
        return None
    return a / b

def main(
    x = 10
    y = 5
    # Missing parentheses and commas

    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")
    print(f"Division: {divide(x, y)}")

# Missing closing parenthesis and incorrect indentation
```

---

## Sample Prompts (Copy-Paste)

### Option A: Compile and Show Errors

> *"Compile `broken_calculator.c` using `gcc -o broken broken_calculator.c` and show me all the compilation errors"*

### Option B: Fix All Errors

> *"Fix all compilation errors in `broken_calculator.c`. After fixing, compile again to verify."*

### Option C: Fix One Error at a Time

> *"Compile `broken_calculator.c`. Show me the first error only, then fix it. Then repeat for the next error."*

### Option D: Explain Each Error

> *"Compile `broken_calculator.c`. For each error, explain what caused it and how to fix it."*

---

## Expected Agent Response (Example)

Using Option A (Compile and show errors):

```
I'll compile broken_calculator.c and show the errors.

Command: gcc -o broken broken_calculator.c

Output:
broken_calculator.c:1:10: fatal error: stdio.h: No such file or directory
    1 | #include <stdio.h
      |          ^~~~~~
compilation terminated.

broken_calculator.c:3:1: error: unknown type name 'add'
    3 | add(int a, int b)
      | ^~~
broken_calculator.c:6:1: error: unknown type name 'subtract'
    6 | subtract(int a, int b) {
      | ^~~~~~~~
broken_calculator.c:11:1: error: unknown type name 'multiply'
   11 | multiply(int a, int b {
      | ^~~~~~~~
broken_calculator.c:16:1: error: unknown type name 'divide'
   16 | divide(int a, int b)
      | ^~~~~~
broken_calculator.c:27:5: error: expected ';' before '}' token
   27 |     return 0;
      |     ^~~~~~
      |     ;
   28 | }
      | ~

Summary of errors:
1. Line 1: Missing > after stdio.h - should be #include <stdio.h>
2. Lines 3, 6, 11, 16: Missing return type int before function names
3. Line 11: Missing closing ) after int b
4. Line 10: Missing semicolon after return a - b
5. Line 27-28: Missing closing brace for main() function

Do you want me to fix all these errors?
```

Using Option B (Fix all errors):

```
I'll fix all the compilation errors in broken_calculator.c.

Fixing errors:

1. Fixed #include <stdio  ->  #include <stdio.h>
2. Added int return type to all functions
3. Fixed multiply(int a, int b {  ->  multiply(int a, int b) {
4. Added missing semicolon after return a - b
5. Added missing closing brace for main() function

Here's the corrected code:

#include <stdio.h>

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
    if (b == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }
    return a / b;
}

int main() {
    int x = 10, y = 5;

    printf("Addition: %d\n", add(x, y));
    printf("Subtraction: %d\n", subtract(x, y));
    printf("Multiplication: %d\n", multiply(x, y));
    printf("Division: %d\n", divide(x, y));

    return 0;
}

Now re-compiling to verify...

Command: gcc -o broken broken_calculator.c

Output: (no errors)

Compilation successful! The program is ready to run.
```

---

## Common Compilation Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `fatal error: xxx.h: No such file` | Missing or incorrect include | Check include path and syntax |
| `expected ';' before '}'` | Missing semicolon | Add semicolon at end of statement |
| `unknown type name 'xxx'` | Missing return type or declaration | Add `int` or proper type |
| `expected ')' before '{'` | Missing parenthesis | Add closing `)` |
| `expected declaration specifiers` | Function defined incorrectly | Check function syntax |
| `stray '\xxx' in program` | Invalid character | Remove or replace the character |

---

## Success Criteria

- [ ] Agent attempted to compile broken code
- [ ] Compilation failed with errors
- [ ] Agent identified and listed errors
- [ ] Agent explained what caused each error
- [ ] Agent fixed the errors
- [ ] Re-compilation succeeded

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `gcc: command not found` | Install GCC or use a different compiler. Ask: *"How do I install gcc?"* |
| Agent fixes wrong things | Be specific: *"Only fix the missing semicolon errors first"* |
| Multiple errors overwhelm Agent | Ask: *"Fix one error at a time, starting with the first one"* |
| Python errors instead of C | Use the Python example or specify: *"For Python 3"* |

---

## Key Takeaway

**The Agent is a powerful debugging assistant – it can read compilation errors, understand what went wrong, and fix multiple issues automatically.**

This workflow mirrors real development:

1. Write code (or break it intentionally)
2. Compile / run tests
3. See errors
4. Fix errors
5. Repeat until success

The Agent accelerates steps 3-4 significantly.

---

## Bonus Challenge (If Time Permits)

Add a logical error (not a syntax error) and have the Agent find it:

> *"The code compiles but gives wrong answers for division. Find and fix the logical error."*

Or use a different language:

> *"Create a broken Python file, compile/run it, and fix all errors"*

---

## Exercise Complete

Check off when done:

- [ ] Compilation failed with errors
- [ ] Agent listed all errors
- [ ] Agent explained error causes
- [ ] Agent fixed errors
- [ ] Re-compilation succeeded
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 13 – Ask Mode vs Agent Mode

---

## Quick Reference: Fixing Errors Cheat Sheet

```
+-----------------------------------------------------------------+
|                   FIXING ERRORS CHEAT SHEET                     |
+-----------------------------------------------------------------+
|                                                                 |
|  COMPILE AND SHOW ERRORS:                                       |
|  "Compile mycode.c and show me all errors"                      |
|                                                                 |
|  FIX ERRORS:                                                    |
|  "Fix all compilation errors"                                   |
|  "Fix the syntax errors"                                        |
|  "Fix the missing semicolon errors"                             |
|                                                                 |
|  EXPLAIN ERRORS:                                                |
|  "What does 'expected declaration specifiers' mean?"            |
|  "Why am I getting 'implicit declaration' warnings?"            |
|                                                                 |
|  VERIFY FIXES:                                                  |
|  "Recompile and verify it works"                                |
|  "Run the program after fixing"                                 |
|                                                                 |
|  COMMON FIX PATTERNS:                                           |
|  - Missing include    -> add #include                           |
|  - Missing semicolon  -> add ;                                  |
|  - Wrong case         -> fix capitalization                     |
|  - Missing brace      -> add { or }                             |
|  - Wrong operator     -> = vs ==, & vs &&                       |
|                                                                 |
+-----------------------------------------------------------------+
```
