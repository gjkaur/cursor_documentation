---
name: doc-generator
description: Generates documentation comments for functions. Use when adding new functions.
---

# Documentation Generator Skill

When invoked, add documentation comments to functions.

## For C functions

```c
/**
 * Brief description of what the function does
 *
 * @param param1 Description of first parameter
 * @param param2 Description of second parameter
 * @return Description of return value
 */
```

## For Python functions

```python
def function_name(param1, param2):
    """
    Brief description of what the function does.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value
    """
```

## Rules
- Every function must have documentation
- Describe what, not how
- Include parameter descriptions
- Include return value description
