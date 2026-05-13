---
name: test-generator
description: Generates unit tests for functions. Use when adding new functions or fixing bugs.
---

# Test Generator Skill

When invoked, generate unit tests for the specified function.

## Test Structure
1. Normal case – typical inputs
2. Edge case – boundary values
3. Error case – invalid inputs
4. Corner case – empty/zero values

## For C (using assert)

```c
void test_function_name(void) {
    // Normal case
    assert(function(input) == expected);

    // Edge case
    assert(function(edge) == expected_edge);

    printf("test_function_name passed\n");
}
```

## For Python (using assert)

```python
def test_function_name():
    # Normal case
    assert function(input) == expected

    # Edge case
    assert function(edge) == expected_edge

    print("test_function_name passed")
```

## Guidelines
- One test function per function being tested
- Test names should describe what is being tested
- Each test should be independent
