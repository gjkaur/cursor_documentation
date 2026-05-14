# Cursor Training – Exercise 11

## Terminal Tool – Run Tests

**Objective:** Use Cursor's terminal tool to run test suites, parse results, and let the Agent help fix failing tests.

**Time:** 10 minutes

**Setup:** A project with test files (use the sample test file provided below)

**This folder:** Open `core-exercises/exercise-11/` in Cursor. It already contains `test_calculator.c`, `run_tests.bat` (Windows), and `run_tests.sh` (Mac/Linux) so you can run the exercise as-is.

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Ask Agent to run the test command | Agent proposes the command |
| 4 | Approve the command | Tests run, output appears in chat |
| 5 | Ask Agent to analyze results | Agent identifies passed/failed tests |

---

## Setup: Create a Simple Test File

If you don't have existing tests, the `test_calculator.c` file in this folder already contains the example below. You can also recreate it from scratch.

### Create `test_calculator.c`

```c
#include <stdio.h>
#include <assert.h>

// Function to test (simple calculator functions)
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }
int divide(int a, int b) {
    if (b == 0) return 0;  // Simple error handling
    return a / b;
}

// Test functions
void test_add() {
    assert(add(2, 3) == 5);
    assert(add(-1, 1) == 0);
    assert(add(0, 0) == 0);
    printf("PASS: test_add passed\n");
}

void test_subtract() {
    assert(subtract(5, 3) == 2);
    assert(subtract(0, 5) == -5);
    assert(subtract(10, 10) == 0);
    printf("PASS: test_subtract passed\n");
}

void test_multiply() {
    assert(multiply(2, 3) == 6);
    assert(multiply(-2, 3) == -6);
    assert(multiply(0, 5) == 0);
    printf("PASS: test_multiply passed\n");
}

void test_divide() {
    assert(divide(6, 2) == 3);
    assert(divide(5, 2) == 2);  // Integer division
    assert(divide(10, 0) == 0); // Division by zero returns 0
    printf("PASS: test_divide passed\n");
}

int main() {
    printf("Running Calculator Tests...\n");
    printf("===========================\n");
    test_add();
    test_subtract();
    test_multiply();
    test_divide();
    printf("===========================\n");
    printf("All tests passed!\n");
    return 0;
}
```

### Create a Simple Test Runner Script

**Windows (`run_tests.bat`):**

```batch
@echo off
echo Running Tests...
gcc test_calculator.c -o test_calculator.exe
if %errorlevel% neq 0 (
    echo Compilation failed!
    exit /b 1
)
test_calculator.exe
```

**Mac/Linux (`run_tests.sh`):**

```bash
#!/bin/bash
echo "Running Tests..."
gcc test_calculator.c -o test_calculator
if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi
./test_calculator
```

Make the script executable (Mac/Linux):

```bash
chmod +x run_tests.sh
```

---

## Sample Prompts (Copy-Paste)

### Option A: Run Tests (Simple)

> *"Run the tests using `gcc test_calculator.c -o test_calculator && ./test_calculator` (Mac/Linux) or the appropriate command for your system"*

### Option B: Run with Test Runner

> *"Run `./run_tests.sh` (Mac/Linux) or `run_tests.bat` (Windows) to execute the test suite"*

### Option C: Analyze Test Results

> *"Run the tests and tell me how many passed and if any failed"*

### Option D: Fix a Failing Test (Intentional)

First, introduce an error in `test_calculator.c` – change `assert(add(2, 3) == 5)` to `assert(add(2, 3) == 6)`

Then ask:

> *"Run the tests. One test is failing. Identify which one and fix it."*

---

## Expected Agent Response (Example)

Using Option A with passing tests:

```
I'll compile and run the tests.

Command: gcc test_calculator.c -o test_calculator && ./test_calculator

Output:
Running Calculator Tests...
===========================
PASS: test_add passed
PASS: test_subtract passed
PASS: test_multiply passed
PASS: test_divide passed
===========================
All tests passed!

Results Summary:
- Total tests: 4
- Passed: 4
- Failed: 0
- Compilation: Successful

All tests are passing. The calculator functions work correctly.
```

---

## Expected Agent Response (With Failing Test)

Using Option D (after introducing the error):

```
I'll compile and run the tests.

Command: gcc test_calculator.c -o test_calculator && ./test_calculator

Output:
Running Calculator Tests...
===========================
test_calculator.c:16: test_add: Assertion `add(2, 3) == 6' failed.
Aborted

Results Summary:
- Total tests: 4
- Passed: 0 (process aborted on first failure)
- Failed: 1 (test_add)
- Compilation: Successful

Failing Test: test_add expects add(2, 3) to return 6, but it returns 5.

Analysis: The add() function is correct (2 + 3 = 5), but the test
expectation is wrong. The test should expect 5, not 6.

Fix: Change line 16 from
    assert(add(2, 3) == 6)
to
    assert(add(2, 3) == 5)

Do you want me to apply this fix?
```

---

## Success Criteria

- [ ] Agent ran the test command
- [ ] Test output appeared in chat
- [ ] Agent identified passing tests
- [ ] Agent identified failing tests (if any)
- [ ] Agent analyzed test results
- [ ] (Optional) Agent fixed a failing test

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `gcc: command not found` | Install GCC or use a different compiler. Ask: *"How do I install gcc on my system?"* |
| Compilation errors | The test file may have typos. Ask: *"Fix the compilation errors"* |
| Agent won't run the command | Approve by typing `y` or pressing Enter |
| Tests take too long | Add timeout: *"Run tests with 30 second timeout"* |
| No test framework | Use the simple test file provided above |

---

## Key Takeaway

**The Agent can run your entire test suite, parse results, and help fix failures – just like a CI pipeline, but interactive.**

This is especially useful for:

- Running tests after making changes
- Debugging flaky tests
- Understanding why a test failed
- Automating test-driven development workflows

---

## Bonus Challenge (If Time Permits)

Ask the Agent to add a new test:

> *"Add a new test called `test_modulo` that checks a modulo function. First write the test, then run all tests."*

Or run tests in a loop:

> *"Run the tests 3 times in a row. If any test fails, stop and tell me which one failed."*

---

## Exercise Complete

Check off when done:

- [ ] Agent ran test command
- [ ] Test output displayed
- [ ] Agent analyzed results
- [ ] Agent identified passed/failed tests
- [ ] (Optional) Agent fixed a failing test
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 12 – Terminal Tool (Fix Errors)

---

## Quick Reference: Running Tests Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                   RUNNING TESTS CHEAT SHEET                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  RUN TESTS:                                                     │
│  "Run `make test`"                                              │
│  "Run `npm test`"                                               │
│  "Run `pytest`"                                                 │
│  "Run `go test ./...`"                                          │
│  "Run `cargo test`"                                             │
│                                                                 │
│  ANALYZE RESULTS:                                               │
│  "How many tests passed?"                                       │
│  "Which tests failed?"                                          │
│  "Show me the error message for the failing test"               │
│                                                                 │
│  FIX FAILURES:                                                  │
│  "Fix the failing test"                                         │
│  "Why did test_divide fail?"                                    │
│  "Update the test expectation"                                  │
│                                                                 │
│  CONTINUOUS TESTING:                                            │
│  "Run tests, watch for failures, and fix them"                  │
│  "Run tests after each change I make"                           │
│                                                                 │
│  COMMON TEST COMMANDS:                                          │
│  Language/Framework    Command                                  │
│  C/C++ (simple)        gcc test.c -o test && ./test             │
│  Python (pytest)       pytest                                   │
│  JavaScript (npm)      npm test                                 │
│  Go                    go test ./...                            │
│  Rust                  cargo test                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Related in this repo

For the previous browser-tool exercise, see [Exercise 10 – Browser Tool (Read Console)](../exercise-10/10-browser-tool-read-console.md).
