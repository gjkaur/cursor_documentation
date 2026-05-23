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

## Steps

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

---

## Success criteria

- [ ] Agent described project purpose
- [ ] Agent identified entry points and key modules
- [ ] Agent suggested first files to read

---

## Additional reference

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
