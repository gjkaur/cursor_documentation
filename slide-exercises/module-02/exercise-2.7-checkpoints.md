# Exercise 2.7: Checkpoints

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.7)  
**Time:** 8 min  
**Difficulty:** Beginner

**Objective:** Create and restore checkpoints before risky Agent experiments.

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

**Step 1:** Create a checkpoint before making a change

```bash
# Click checkpoint icon in Agent panel
# Windows/Linux: Ctrl+Shift+S · Mac: Cmd+Shift+S
```

---

**Step 2:** Name it descriptively: `"Before auth refactor - safe point"`

**Step 3:** Let the agent make changes:

```
Add input validation to all form handlers.
```

---

**Step 4:** If something goes wrong → **Restore to checkpoint**

**Step 5:** View history via the clock icon in Agent panel

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and your project folder | Your code files appear in the Explorer sidebar |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Make a small change and note the checkpoint appears | Checkpoint marker shows in chat timeline |
| 4 | Make another change | Second checkpoint appears |
| 5 | Click a previous checkpoint | Preview shows file state at that point |
| 6 | Click "Restore" | Files revert to that checkpoint state |

---

## Code Example to Use

Continue with `calculator.c` in **this** folder (same directory as this doc):

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

## Understanding Checkpoints

| What | Description |
|------|-------------|
| **What are they?** | Automatic snapshots taken before Agent makes significant changes |
| **Where to find them?** | In the chat timeline – each checkpoint has a marker |
| **What do they capture?** | State of ALL modified files |
| **How to use?** | Click any checkpoint → Preview → Restore |
| **Storage?** | Local only (not in Git) |
| **Purpose?** | Undo Agent mistakes, experiment safely |

---

## Sample Prompts (Make Changes to Create Checkpoints)

Use these prompts in sequence to create multiple checkpoints:

### Change 1: Add a Comment

> *"Add a comment at the top of `calculator.c` that says: 'Version 2.0 - Enhanced Calculator'"*

**After this change, note the checkpoint appears in chat.**

### Change 2: Add a Welcome Message

> *"In the `main()` function, right after the first `printf`, add: `printf("Welcome to the Enhanced Calculator!\\n");`"*

**Second checkpoint appears.**

### Change 3: Add Input Validation (Risky Change)

> *"Add input validation to check if the user enters a number between 1 and 4 for the menu choice. If not, print 'Invalid choice' and exit."*

**Third checkpoint appears.**

---

## How to Preview a Checkpoint

| Step | Action |
|------|--------|
| 1 | Look at the chat timeline – find a previous checkpoint marker |
| 2 | Click on the checkpoint |
| 3 | A preview panel opens showing file state at that point |
| 4 | Scroll through the preview to see what the file looked like |
| 5 | Files are NOT actually changed yet – just previewing |

---

## How to Restore a Checkpoint

| Step | Action |
|------|--------|
| 1 | Click on a checkpoint in the chat timeline |
| 2 | In the preview panel, click **"Restore"** button |
| 3 | Confirm if prompted |
| 4 | All files revert to the state at that checkpoint |

**Result:** Your code is back to exactly how it was when that checkpoint was created.

---

## Expected Checkpoint Timeline (Example)

```
┌─────────────────────────────────────────────────────────────────┐
│                    CHAT TIMELINE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [10:00] User: Add a comment at the top                        │
│     ● Checkpoint: calculator.c - 10:00:01                      │
│  [10:01] Agent: Comment added successfully                     │
│                                                                 │
│  [10:02] User: Add a welcome message                           │
│     ● Checkpoint: calculator.c - 10:02:15                      │
│  [10:03] Agent: Welcome message added                          │
│                                                                 │
│  [10:04] User: Add input validation                            │
│     ● Checkpoint: calculator.c - 10:04:30                      │
│  [10:05] Agent: Input validation added                         │
│                                                                 │
│  [10:06] User clicks first checkpoint → Restores to 10:00 state│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Experiment: Make a Change That Breaks Something

### Step 1: Make a Risky Change

Ask the Agent:

> *"Change the `divide()` function to ALWAYS return 0, ignoring the division logic"*

### Step 2: Test or Review

Ask the Agent:

> *"Check if the divide function still works correctly"*

### Step 3: If Broken, Restore

Click the previous checkpoint to restore the working version.

### Step 4: Verify

Ask the Agent:

> *"Show me the divide function now"*

It should be back to the original, working version.

---

## Checkpoints vs. Git

| Feature | Checkpoints | Git |
|---------|-------------|-----|
| **Automatic** | Yes | No (manual commit) |
| **Per-change snapshots** | Yes | No (batch commits) |
| **Instant restore** | Yes (one click) | Yes (multiple commands) |
| **Permanent history** | No (temporary) | Yes |
| **Share with team** | No | Yes |
| **Branch support** | No | Yes |

**Best practice:** Use checkpoints for undoing Agent mistakes during a session. Use Git for permanent, shareable history.

---

## Success Criteria

- [ ] Made a change and saw checkpoint appear in chat
- [ ] Made multiple changes – saw multiple checkpoints
- [ ] Clicked a checkpoint to preview previous state
- [ ] Restored to a previous checkpoint
- [ ] Verified files reverted correctly
- [ ] Experimented with a risky change and restored when needed

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No checkpoint appears | Make sure you're in Agent mode (not Ask mode). Agent mode creates checkpoints automatically |
| Can't find checkpoint | Scroll up in chat – checkpoints are marked with a dot or icon |
| Restore didn't revert everything | Checkpoints only capture files the Agent modified. Manually changed files aren't included |
| Don't see preview panel | Click the checkpoint again. It should open on the right or bottom |
| Want to revert but no checkpoint | Ask Agent to make a small safe change first – that creates a checkpoint |

---

## Key Takeaway

**Checkpoints = Fearless experimentation.**

You can try any change – no matter how risky – because you're always one click away from restoring to a working state.

**Three things to remember:**

1. Checkpoints are **automatic** – you don't need to create them
2. Checkpoints are **local** – they don't affect your Git history
3. Checkpoints are **temporary** – use Git for permanent history

---

## Bonus Challenge (If Time Permits)

Try this experiment:

1. Ask Agent to make 3-4 consecutive changes to your file
2. Each change creates a checkpoint
3. Restore to the very first checkpoint (before any changes)
4. Observe that ALL changes are undone
5. Then restore back to the last checkpoint
6. Observe that changes come back

**What you learn:** Checkpoints save complete state, not just incremental diffs.

---

## Exercise Complete ✓

Check off when done:

- [ ] Observed checkpoint creation after a change
- [ ] Made multiple changes with multiple checkpoints
- [ ] Previewed a previous checkpoint
- [ ] Restored to a checkpoint
- [ ] Verified files reverted correctly
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 8 – Run a Terminal Command

---

## Quick Reference: Checkpoint Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                     CHECKPOINT CHEAT SHEET                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  WHAT ARE THEY?                                                 │
│  Automatic snapshots before Agent makes significant changes     │
│                                                                 │
│  WHERE TO FIND?                                                 │
│  Chat timeline – look for checkpoint markers                    │
│                                                                 │
│  HOW TO USE:                                                    │
│  1. Click any checkpoint                                        │
│  2. Preview the state                                           │
│  3. Click "Restore" to revert                                   │
│                                                                 │
│  WHEN TO USE:                                                    │
│  • Experimenting with new approach                              │
│  • Before risky changes                                         │
│  • Multi-file refactoring                                       │
│  • Any time you might want to undo                              │
│                                                                 │
│  CHECKPOINTS vs GIT:                                            │
│  • Checkpoints = Undo button for Agent (temporary)             │
│  • Git = Permanent history (commit, push, share)               │
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
| Terminal command fails on Windows | Use **PowerShell**; use `curl.exe` instead of `curl` |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
