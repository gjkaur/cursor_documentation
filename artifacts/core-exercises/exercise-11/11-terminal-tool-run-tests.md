# Cursor Training – Exercise 11

## Terminal Tool – Run Tests

**Objective:** Use the Agent's terminal tool to run commands, read output, diagnose failures, and verify fixes.

**Time:** 20 minutes

**Setup:** Open **`core-exercises/exercise-11/`** in Cursor. This folder includes `test_calculator.c`, `run_tests.bat` (Windows), and `run_tests.sh` (Mac/Linux).

---

## What You Will Practice

| Step | Technique | Why it helps |
|------|-----------|--------------|
| 1 | **Setup + safe command** | Confirm the Agent can run read-only terminal commands |
| 2 | **Run passing tests** | See compile + test output in chat |
| 3 | **Introduce a failure** | You control the bug — predictable exercise |
| 4 | **Diagnose from output** | Agent reads stderr/assert messages |
| 5 | **Fix and re-run** | Close the loop: reproduce → fix → verify |
| 6 | **Approval rules** | Know which commands need extra caution |

---

## Before You Start

1. **File → Open Folder** → `core-exercises/exercise-11/` in this repo.
2. Press **`Ctrl+I`** to open the **Agent** panel.
3. Confirm **Agent Mode** (`/agent`).
4. Set integrated terminal to **PowerShell**: ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell**.
5. Install **`gcc`** if needed (MinGW-w64 or MSVC). Ask the Agent: *"How do I install gcc on Windows?"*

---

## Step 1: Run a Safe Read-Only Command

**Goal:** Practice approving a low-risk terminal command.

```
Check whether gcc and git are available in this project.

Run:
- gcc --version
- git --version

Summarize the output. Do not modify any files.
```

**What to look for:**
- Agent proposes commands and shows stdout.
- You may need to click **Allow** / **Run** when prompted.
- No file edits.

---

## Step 2: Run the Test Suite (All Tests Should Pass)

**Goal:** Compile and run `test_calculator.c` using the Windows batch runner.

```
Run the test suite with .\run_tests.bat in this folder.

Show the full terminal output and tell me:
- Did compilation succeed?
- How many tests passed?
- Did any test fail?
```

**Alternative (manual compile in PowerShell):**

```
Compile and run test_calculator.c with gcc.
Use: gcc test_calculator.c -o test_calculator.exe ; .\test_calculator.exe
Show me the full output.
```

**Other platforms (optional):** Mac/Linux — `./run_tests.sh` (run `chmod +x run_tests.sh` if needed).

**What to look for:**

```text
Running Calculator Tests...
===========================
PASS: test_add passed
PASS: test_subtract passed
PASS: test_multiply passed
PASS: test_divide passed
===========================
All tests passed!
```

---

## Step 3: Introduce a Failing Test (You Do This Manually)

**Goal:** Create a known failure before asking the Agent to debug.

1. Open **`test_calculator.c`** in the editor.
2. Find `assert(add(2, 3) == 5);` in `test_add()`.
3. Change it to **`assert(add(2, 3) == 6);`**
4. Save the file.

**Do not ask the Agent to edit yet** — you introduced the bug on purpose.

---

## Step 4: Diagnose the Failure

**Goal:** Agent reads terminal output and explains the failure.

```
@test_calculator.c

Run the test suite again with .\run_tests.bat.

One test is failing. From the terminal output:
1. Which test failed?
2. What assertion failed?
3. Is the bug in the test or in the add() function?
Do not fix anything yet — explain only.
```

**What to look for:**
- Agent cites the assertion line (expects 6, got 5).
- Correct diagnosis: **the test expectation is wrong**, not `add()`.

---

## Step 5: Fix and Verify (Debug Workflow)

**Goal:** Reproduce → diagnose → fix → re-run (same pattern as real debugging).

```
@test_calculator.c

Follow this workflow:
1. Run the tests and confirm the failure
2. Fix the incorrect assertion in test_add() only
3. Re-run the tests
4. Confirm all tests pass

Show me the diff before I accept file changes.
```

**What to look for:**
- Agent runs terminal commands at least twice (fail, then pass).
- Diff changes **one assertion** back to `== 5`.
- Final output shows **All tests passed!**

---

## Step 6: Command Approval — Safe vs. Risky

**Goal:** Learn which commands usually need careful review.

| Usually review carefully | Usually lower risk |
|--------------------------|-------------------|
| Deletes files, `sudo`, `git push --force` | `gcc --version`, `git status`, `ls`, `dir` |
| Installs packages globally | Running project test scripts |
| Starts servers, changes system config | Reading files, compiling local `.c` files |

**Optional prompt:**

```
Run git status in this folder and summarize what you see.
Do not commit or push anything.
```

**What to look for:** Read-only git output — no writes to the repo.

---

## Sample Prompts (Quick Reference)

| Situation | Prompt |
|-----------|--------|
| Run tests | *"Run run_tests.bat and show full output"* |
| Count results | *"How many tests passed vs failed?"* |
| Explain failure | *"What does the assertion error mean?"* |
| Fix + verify | *"Fix the failing assertion and re-run tests"* |

---

## Expected Agent Response (Passing Tests)

Using Step 2:

I'll compile and run the tests using the test runner in this folder.

**Command:** `.\run_tests.bat` (Windows PowerShell)

**Output:**

```text
Running Calculator Tests...
===========================
PASS: test_add passed
PASS: test_subtract passed
PASS: test_multiply passed
PASS: test_divide passed
===========================
All tests passed!
```

**Summary:** Compilation succeeded. 4 tests passed, 0 failed.

---

## Expected Agent Response (Failing Test)

Using Step 4 after you changed the assertion to `== 6`:

**Command:** same test runner as Step 2

**Output:**

```text
Running Calculator Tests...
===========================
test_calculator.c:16: test_add: Assertion `add(2, 3) == 6' failed.
```

**Analysis:**
- **Failed test:** `test_add`
- **Cause:** Test expects `add(2, 3)` to be 6, but `add()` correctly returns 5.
- **Fix:** Change the assertion back to `assert(add(2, 3) == 5);`

---

## Success Criteria

- [ ] Agent ran a read-only command (gcc/git version or `git status`)
- [ ] Agent ran the test suite and showed terminal output
- [ ] You introduced a failing assertion manually
- [ ] Agent diagnosed the failure from output
- [ ] Agent fixed the test and re-ran — all tests passed
- [ ] You understand safe vs. risky terminal commands

---

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| `gcc: command not found` | Install GCC, or ask Agent for install steps for your OS |
| Agent won't run command | Click **Allow** / **Run** when the approval dialog appears |
| `run_tests.sh: Permission denied` | Run `chmod +x run_tests.sh` first (Mac/Linux) |
| Agent edits wrong file | Add *"Change ONLY test_calculator.c line with the assertion"* |
| Tests pass when they should fail | Confirm you saved the edited `assert(add(2, 3) == 6)` |

---

## Key Takeaway

**The terminal tool lets the Agent run your commands, read stdout/stderr, and act on results** — like an interactive CI job. Always review proposed commands before approving destructive or global installs.

**Next in this course:** Module 3, Exercise 3.4 — Effective Prompting in Practice.

---

## Bonus Challenge (Optional)

> *"Add a `test_modulo` function and a modulo implementation, then run the full suite."*

Or:

> *"Run the tests twice in a row. If the second run fails, explain why."*

---

## Quick Reference: Running Tests

| Stack | Command |
|-------|---------|
| This exercise (Windows demo) | `.\run_tests.bat` |
| This exercise (Mac/Linux) | `./run_tests.sh` |
| C (manual) | `gcc test_calculator.c -o test_calculator && ./test_calculator` |
| Python | `pytest` |
| JavaScript | `npm test` |

---

## Related in this repo

Previous exercise: [Exercise 10 – Browser Tool (Read Console)](../exercise-10/10-browser-tool-read-console.md).
