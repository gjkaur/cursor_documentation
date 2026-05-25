# Exercise 2.1: Codebase Understanding

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.1)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Use the Cursor Agent to orient yourself in an unfamiliar repository.

---

## Cursor basics (read this first)

| Task | Windows / Linux | Mac | Where in Cursor |
|------|-----------------|-----|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.


---

## Steps from the training slides

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Step 1:** Open an unfamiliar repository in Cursor

Use **PowerShell**, **Git Bash**, or **CMD** in Cursor's integrated terminal (Ctrl+`):

```bash
git clone https://github.com/facebookresearch/detectron2
cd detectron2
cursor .
```

**Step 2:** Open the Agent (Ctrl+I on Windows/Linux · Cmd+I on Mac)

---

```
Explain this codebase to me as if I'm a new team member.

Specifically tell me:
1. What is the main purpose of this project?
2. What are the entry points (main scripts, CLI, API)?
3. What are the key modules and how do they relate?
4. What are the main dependencies?
5. What files should I read first to understand the architecture?
```

---

**Step 4:** Follow up — trace data flow:

```
Based on what you just told me, trace the flow of data from input
to output. What functions get called in order?
```

---

**Step 5:** Ask for a visual overview:

```
Create an ASCII diagram showing the module relationships in this codebase.
```

---

**Success Criteria:**
- Agent described project purpose
- Agent identified entry points and key modules
- Agent suggested first files to read

---

## Success criteria

- [ ] Agent described project purpose
- [ ] Agent identified entry points and key modules
- [ ] Agent suggested first files to read

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

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

A ready-to-use copy is included in this folder as [`calculator.c`](../../core-exercises/exercise-1/calculator.c). Open the `exercise-1` folder (under `core-exercises` in this repo) in Cursor and work from there.

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

Save this as `calculator.c` in an empty folder (or use [`calculator.c`](../../core-exercises/exercise-1/calculator.c)), then open that folder in Cursor.

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

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Terminal command fails on Windows | Use **PowerShell**; use `curl.exe` instead of `curl` |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
