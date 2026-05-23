# Exercise 2.7: Checkpoints

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.7)  
**Time:** 8 min  
**Difficulty:** Beginner

**Objective:** Create and restore checkpoints before risky Agent experiments.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

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

## Additional reference

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
