# Exercise 2.2: Explaining a Specific File or Symbol

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 2, Lesson 2.2)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Get targeted explanations of one file or symbol without reading the whole repo.

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

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

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

Use the same [`calculator.c`](../../core-exercises/exercise-1/calculator.c) file from Exercise 1 (open the `exercise-1` folder in Cursor so `@calculator.c` resolves), or any file in your project.

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
