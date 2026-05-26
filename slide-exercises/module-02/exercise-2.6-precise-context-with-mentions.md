# Exercise 2.6: Precise Context with @mentions

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.6)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Use @mentions to point the Agent at exact files, symbols, and context.

---

## Cursor basics (read this first)

**Demonstration environment:** These exercises assume **Windows 10/11**. Open the integrated terminal with ``Ctrl+` `` and select **PowerShell** as the default profile.

| Task | Windows (demo) | Mac (optional) | Where in Cursor |
|------|----------------|----------------|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` → **PowerShell** | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Windows terminal commands (common in exercises):**

| Task | PowerShell command |
|------|-------------------|
| List files | `dir` or `Get-ChildItem` |
| Show file contents | `Get-Content .\file.txt` or `type file.txt` |
| Run a local `.bat` script | `.\run_tests.bat` |
| Run compiled program | `.\calculator.exe` or `calculator.exe` |
| Set env var (session) | `$env:MY_VAR = "value"` |
| Open HTML in browser | `start index.html` |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.


---

## Steps from the training slides

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Step 1:** Use @filename to point at a specific file:

```
@database.py What are the security vulnerabilities in this database connection?
```

**Step 2:** Use @symbol to reference a specific function:

```
@calculate_total This function is returning NaN sometimes. Why?
```

---

**Step 3:** Combine multiple @mentions:

```
@auth.py @UserModel @login_handler Review the authentication flow.
Are there any race conditions or timing attacks?
```

---

**Step 4:** Use @branch to reference a different branch:

```
Compare @main and @feature/payment branches.
What are the key differences in the payment handling code?
```

---

**Step 5:** Use @chat to refer to a previous conversation:

```
@chat(authentication-discussion) Based on that discussion,
implement the fix we agreed on.
```

---

**Step 6:** Use @folder for directory-level context:

```
@src/components Find all components that don't have loading states.
```

**Step 7:** Use @web for external documentation:

```
@web React 19 useTransition hook How do I use it?
```

---

**Success Criteria:**
- Used @filename to target a specific file
- Used @symbol to target a function or class
- Used multiple @mentions together
- Used @web for external search

---

## Success criteria

- [ ] Used @filename to target a specific file
- [ ] Used @symbol to target a function or class
- [ ] Used multiple @mentions together
- [ ] Used @web for external search

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Type `@` followed by a filename | Dropdown shows matching files |
| 4 | Select the file from dropdown | File name appears with @ prefix |
| 5 | Type your question after the @mention | Complete prompt ready to send |
| 6 | Press `Enter` | Agent reads that specific file and answers |

---

## Setup: Add a Second File

To see the full power of @mentions, create a second file in your project.

### Create `math_utils.h`

```c
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

// Basic arithmetic operations
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
int divide(int a, int b);

// Advanced operations
int power(int base, int exp);
int factorial(int n);
int modulo(int a, int b);

// Validation helpers
int is_valid_number(int n);
int is_in_range(int n, int min, int max);

#endif
```

### Create `math_utils.c`

```c
#include "math_utils.h"
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

int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int factorial(int n) {
    if (n < 0) return -1;
    if (n == 0 || n == 1) return 1;
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int modulo(int a, int b) {
    if (b == 0) {
        printf("Error: Modulo by zero\n");
        return 0;
    }
    return a % b;
}

int is_valid_number(int n) {
    return 1;  // Always valid in this simple implementation
}

int is_in_range(int n, int min, int max) {
    return (n >= min && n <= max);
}
```

> **Note:** In this repo, `math_utils.h` and `math_utils.c` are already in `core-exercises/exercise-6/`. If you are using your own project, add these files there (or equivalent) so @mentions have multiple targets.

---

## @mention Types

| Type | Syntax | What it does |
|------|--------|--------------|
| **File** | `@filename.c` | References a specific file |
| **Folder** | `@src/` | References all files in a folder |
| **Symbol** | `@function_name` | References a specific function (if indexed) |
| **Terminals** | `@Terminals` | Includes terminal output as context |
| **Docs** | `@Docs` | Searches documentation |
| **Past Chats** | `@Past Chats` | References previous conversations |
| **Git commit** | `@Commit` | Includes uncommitted changes |
| **Branch diff** | `@Branch (Diff with Main)` | Includes branch differences |

---

## Sample Prompts (Copy-Paste)

### Option A: Single File @mention

> *`@calculator.c` "Explain what the `main()` function does in this file"*

### Option B: Header File @mention

> *`@math_utils.h` "What functions are declared in this header? What do they do?"*

### Option C: Multiple File @mention

> *`@calculator.c` `@math_utils.c` "How do these two files work together? Which functions from math_utils.c are used in calculator.c?"*

### Option D: Specific Function @mention

> *`@divide` "Find the divide function. Does it handle division by zero correctly?"*

### Option E: With Terminal @mention (if you have test output)

> *`@Terminals` `@calculator.c` "The test shows an error. Look at the terminal output and the calculator.c file. What's wrong?"*

---

## Expected Agent Responses (Examples)

### Using Option A (Single File)

With `@calculator.c` "Explain what the `main()` function does":

```
In `calculator.c`, the `main()` function:

1. Displays a menu of operations (1-4)
2. Reads user's choice using `scanf`
3. Reads two numbers from the user
4. Uses a switch statement to call the appropriate math function
5. Prints the result
6. Includes a safety check for division by zero

The function returns 0 on successful execution.
```

### Using Option B (Header File)

With `@math_utils.h` "What functions are declared?":

```
The header `math_utils.h` declares 8 functions:

**Basic arithmetic:**
- `add(int a, int b)` - addition
- `subtract(int a, int b)` - subtraction
- `multiply(int a, int b)` - multiplication
- `divide(int a, int b)` - division

**Advanced operations:**
- `power(int base, int exp)` - exponentiation
- `factorial(int n)` - factorial calculation
- `modulo(int a, int b)` - remainder operation

**Validation helpers:**
- `is_valid_number(int n)` - validates input
- `is_in_range(int n, int min, int max)` - range checking
```

### Using Option C (Multiple Files)

With `@calculator.c` `@math_utils.c` "How do these files work together?":

```
**Relationship between files (this training folder):**

`math_utils.c` implements the functions declared in `math_utils.h`.

`calculator.c` includes `math_utils.h` and calls `add`, `subtract`, `multiply`, and `divide` from `math_utils.c` for the menu-driven calculator.

**Advanced helpers** (`power`, `factorial`, `modulo`, `is_valid_number`, `is_in_range`) are implemented in `math_utils.c` but not used by `main()` yet — good candidates for extending the menu.

**Command to compile both:**
`gcc -std=c99 -o calculator calculator.c math_utils.c`
```

---

## Without @mention vs. With @mention

| Without @mention | With @mention |
|------------------|---------------|
| Agent searches entire codebase | Agent reads exact file you specify |
| May miss the right file | Always references correct file |
| Response may be about wrong code | Response is about code you care about |
| Takes more time (searching) | Faster response (direct read) |
| May ignore irrelevant files | Focuses only on mentioned files |

**Try this comparison:**

First, ask without @mention:

> *"What does the divide function do?"*

Then, ask with @mention:

> *`@calculator.c` "What does the divide function do?"*

Notice the difference in precision and relevance.

---

## Success Criteria

- [ ] Typed `@` and saw file suggestions
- [ ] Selected a file from the dropdown
- [ ] Asked a question about that specific file
- [ ] Agent referenced the correct file in its response
- [ ] Used multiple @mentions in one prompt
- [ ] Compared response quality with and without @mention

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `@` doesn't show suggestions | Make sure you're in the Agent chat, not a code file |
| Wrong file appears | Type more letters to narrow down the suggestion |
| @mention not working | Put a space after the @mention before your question |
| Agent ignores the @mention | Put the @mention at the beginning of your prompt |
| Can't @mention a symbol | Symbol must be indexed first (Cursor does this automatically) |

---

## @mention Tips & Tricks

| Tip | Example |
|-----|---------|
| **Multiple files** | `@file1.c` `@file2.c` "Compare these files" |
| **Partial names** | Type `@calc` to match `calculator.c` |
| **Folders** | `@src/` "Explain the structure of this folder" |
| **With line numbers** | `@calculator.c:25-40` "Explain this section" (if supported) |
| **Recent files** | @ shows recently used files first |

---

## Key Takeaway

**@mentions are like pointing at code and saying "Look here!"**

Use them whenever you want the Agent to focus on specific files, functions, or folders. This is especially useful when:

- You have a large codebase (thousands of files)
- You know exactly which file contains the relevant code
- You want to compare multiple files
- The Agent seems confused about which file to look at

---

## Bonus Challenge (If Time Permits)

Try chaining multiple @mentions with a complex question:

> *`@math_utils.h` `@math_utils.c` "Compare the header file and implementation file. Are all declared functions implemented? Are there any extra functions in the .c file not in the .h?"*

Or use @mention with a specific request:

> *`@calculator.c` "Add a new menu option for the modulo function. First, show me where to add it, then write the code."*

---

## Exercise Complete ✓

Check off when done:

- [ ] Used @mention with a single file
- [ ] Agent answered correctly about that file
- [ ] Used @mention with multiple files
- [ ] Noticed the difference between with/without @mention
- [ ] (Optional) Completed bonus challenge

**Next:** [Exercise 7 – Use checkpoints](../../core-exercises/exercise-7/07-use-checkpoints.md)

---

## Quick Reference: @mention Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                      @MENTION CHEAT SHEET                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TYPES:                                                         │
│  @filename.c      → Specific file                               │
│  @folder/         → Entire folder                               │
│  @function_name   → Specific symbol (if indexed)                │
│  @Terminals       → Terminal output                             │
│  @Commit          → Uncommitted changes                         │
│  @Branch          → Branch differences                          │
│  @Docs            → Documentation search                        │
│  @Past Chats      → Previous conversations                      │
│                                                                 │
│  EXAMPLES:                                                      │
│  @main.c "What does this file do?"                             │
│  @src/ "Explain the project structure"                         │
│  @calculator.c @math_utils.c "How do these relate?"            │
│  @Terminals "Fix this compilation error"                       │
│                                                                 │
│  TIP: Start with @ then type first few letters of filename     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
