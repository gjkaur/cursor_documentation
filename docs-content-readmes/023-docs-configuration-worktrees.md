This is the **Worktrees** documentation – it explains how Agent can work in **isolated Git checkouts**. Each task gets its own files, dependencies, and changes while your main project stays untouched.

Think of Worktrees as **separate sandboxes** where agents can work without messing up your main code. It's like having multiple copies of your project that all share the same Git history.

Let me break this down for a complete beginner.

---

## What Are Worktrees? (The 10-Second Summary)

**Worktrees let Agent work in isolated Git checkouts.** Each task gets its own files, dependencies, and changes while your main checkout stays untouched.

| Without Worktrees | With Worktrees |
|-------------------|----------------|
| One agent works at a time | Multiple agents work simultaneously |
| Changes mix together | Each agent has isolated changes |
| Risky experiments affect main code | Experiments are completely separate |
| Conflicts between agents | No conflicts |

> *"Use worktrees when you want to start several agents on the same repo without conflicts."*

---

## Important Note: Where Worktrees Are Available

| Interface | Worktrees Availability |
|-----------|----------------------|
| **Agents Window** | ✅ Full UI-native worktrees feature |
| **Editor Window** | ⚠️ Use Worktree Skills commands instead (`/worktree`, `/best-of-n`) |

**For beginners:** Worktrees are easiest to use in the **Agents Window**.

---

## Why Use Worktrees?

| Scenario | Why Worktrees Help |
|----------|---------------------|
| **Several agents on same repo** | No conflicts between agents |
| **Experimental edits** | Keep changes away from main checkout |
| **Run installs, builds, tests** | Don't disturb your current branch |
| **Risky refactors** | Simple cleanup path – just delete the worktree |
| **Compare different models** | Each model gets its own isolated worktree |

---

## Creating a Worktree in the Agents Window

When you start or move an agent into a worktree from the Agents Window:

1. **Cursor creates a separate checkout** for that agent
2. The agent continues the task **inside the worktree**
3. Changes stay **isolated** from your main checkout

### After the Agent Finishes:

| Option | What you can do |
|--------|-----------------|
| **Keep working** | Continue in the worktree |
| **Create commit/PR** | Push changes from that checkout |
| **Bring result back** | Merge into your main workspace |

---

## How Worktree Setup Works (Customization)

You can customize worktree setup with **`.cursor/worktrees.json`**.

### Where Cursor Looks:

| Order | Location |
|-------|----------|
| 1 | In the worktree path |
| 2 | In the root path of your project |

### Configuration Options (3 Setup Keys):

| Key | Platform | When used |
|-----|----------|-----------|
| `setup-worktree-unix` | macOS, Linux | Takes precedence on Unix systems |
| `setup-worktree-windows` | Windows | Takes precedence on Windows |
| `setup-worktree` | All | Generic fallback for all OS |

### What Each Key Accepts:

| Type | Description | Example |
|------|-------------|---------|
| **Array of shell commands** | Executed sequentially in the worktree | `["npm ci", "cp .env.example .env"]` |
| **String filepath** | Path to a script file | `"setup-worktree.sh"` |

---

## Example Setup Configurations

### Node.js Project

```json
{
  "setup-worktree": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env"
  ]
}
```

### Python Project with Virtual Environment

```json
{
  "setup-worktree": [
    "python -m venv venv",
    "source venv/bin/activate && pip install -r requirements.txt",
    "cp $ROOT_WORKTREE_PATH/.env .env"
  ]
}
```

### Project with Database Migrations

```json
{
  "setup-worktree": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env",
    "npm run db:migrate"
  ]
}
```

### Build and Link Dependencies

```json
{
  "setup-worktree": [
    "pnpm install",
    "pnpm run build",
    "cp $ROOT_WORKTREE_PATH/.env.local .env.local"
  ]
}
```

---

## Using Script Files (For Complex Setups)

Instead of inline commands, reference script files:

```json
{
  "setup-worktree-unix": "setup-worktree-unix.sh",
  "setup-worktree-windows": "setup-worktree-windows.ps1",
  "setup-worktree": [
    "echo 'Using generic fallback. For better support, define OS-specific scripts'"
  ]
}
```

**Place your scripts in the `.cursor/` directory** next to `worktrees.json`.

### Example: `setup-worktree-unix.sh` (macOS/Linux)

```bash
#!/bin/bash
set -e

# Install dependencies
npm ci

# Copy environment file
cp "$ROOT_WORKTREE_PATH/.env" .env

# Run database migrations
npm run db:migrate

echo "Worktree setup complete!"
```

### Example: `setup-worktree-windows.ps1` (Windows PowerShell)

```powershell
$ErrorActionPreference = 'Stop'

# Install dependencies
npm ci

# Copy environment file
Copy-Item "$env:ROOT_WORKTREE_PATH\.env" .env

# Run database migrations
npm run db:migrate

Write-Host "Worktree setup complete!"
```

---

## OS-Specific Configurations

You can provide different setup commands for different operating systems:

```json
{
  "setup-worktree-unix": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env",
    "chmod +x scripts/*.sh"
  ],
  "setup-worktree-windows": [
    "npm ci",
    "copy %ROOT_WORKTREE_PATH%\\.env .env"
  ]
}
```

---

## Important Warning About Symlinking

> *"We do not recommend symlinking dependencies into the worktree. This can cause issues in the main worktree. Use a fast package manager such as bun, pnpm, or uv instead."*

**What this means:** Don't create symbolic links from the worktree back to your main project. Use proper package managers that handle dependencies efficiently.

---

## Debugging Worktree Setup

If you want to debug worktree setup:
1. Open the **Output panel** in the editor
2. Select **Worktrees Setup**

This shows you what's happening during worktree creation.

---

## Worktrees Cleanup (Save Disk Space)

Cursor can **automatically clean up older worktrees** to limit disk usage.

### Configuration Settings:

| Setting | What it does | Example |
|---------|--------------|---------|
| `cursor.worktreeCleanupIntervalHours` | How often Cursor checks for old worktrees | `6` (every 6 hours) |
| `cursor.worktreeMaxCount` | Maximum worktrees before cleaning up older ones | `20` |

**Example settings:**
```json
{
  "cursor.worktreeCleanupIntervalHours": 6,
  "cursor.worktreeMaxCount": 20
}
```

**How it works:** Cleanup runs on an interval and keeps the newest worktrees up to the configured maximum count.

---

## Worktree Skills in Editor Window

In the **Editor Window** (not Agents Window), you use **commands** instead of UI.

### Two Main Commands:

| Command | What it does |
|---------|--------------|
| `/worktree` | Run a task in an isolated worktree (one run) |
| `/best-of-n` | Run same task across multiple models, each in its own worktree |

---

## Using `/worktree` for Isolated Runs

Start a task with `/worktree` when you want Cursor to do the rest of that chat in a separate checkout.

### Benefits:
- Keep experimental edits away from your main checkout
- Run installs, builds, and tests without disturbing your current branch
- Work on risky refactors with a simple cleanup path

### Example:

```
/worktree fix the failing auth tests and update the login copy
```

### After the Agent Finishes:

| Action | Command/Request |
|--------|-----------------|
| **Commit and push** | "Commit and push these changes, then open a PR" |
| **Bring changes to main** | Use `/apply-worktree` |
| **Delete worktree** | Use `/delete-worktree` |
| **See all worktrees** | `git worktree list` |

---

## Using `/best-of-n` to Compare Multiple Models

**`/best-of-n` runs the same task across multiple models at once.** Each run gets its own worktree, so candidates stay isolated.

### Example:

```
/best-of-n sonnet,gpt,composer fix the flaky logout test
```

This runs the same task on:
- Claude Sonnet (in its own worktree)
- GPT (in its own worktree)
- Composer (in its own worktree)

### When to use `/best-of-n`:

| Use Case | Why |
|----------|-----|
| **Compare different models** | See which produces better results |
| **Try multiple approaches** | Different models have different strengths |
| **Pick strongest result** | Choose winner before applying anything |

### Important Notes:

> *"`/best-of-n` compares runs only. It does not merge changes back into your main checkout for you."*

**After picking a winner:**
1. Commit and push directly from the worktree
2. OR use `/apply-worktree` to bring changes into your main checkout

---

## Real-World Examples

### Example 1: Multiple Agents on Same Repo

You have 3 features to build:
- Feature A: Dark mode
- Feature B: Search
- Feature C: User profiles

**Without Worktrees:** Agents would conflict, changes would mix.

**With Worktrees:**
- Agent 1 works on Feature A in Worktree A
- Agent 2 works on Feature B in Worktree B
- Agent 3 works on Feature C in Worktree C

**All work simultaneously, no conflicts!**

### Example 2: Risky Refactor

You want to refactor a core module. It might break things.

**Without Worktrees:** You risk breaking your main code.

**With Worktrees:**
- Create a worktree
- Agent does the risky refactor in isolation
- Test thoroughly
- If good → merge back
- If bad → delete the worktree (main code untouched!)

### Example 3: Comparing Models

You're not sure which model is best for a complex task.

**Use `/best-of-n`:**
```
/best-of-n claude-4.6-sonnet,gpt-5.3-codex,composer-2 refactor the payment service to use the new API
```

**Result:** Three worktrees, three implementations. Pick the best one.

---

## Common Beginner Questions

### Q: Do worktrees use more disk space?
**A:** Yes, each worktree is a separate checkout. But Cursor auto-cleans up old ones.

### Q: Can I have many worktrees at once?
**A:** Yes, up to the `cursor.worktreeMaxCount` setting (default 20).

### Q: Do I need to set up `.cursor/worktrees.json`?
**A:** No – it's optional. Only needed if you need custom setup commands.

### Q: Can I use worktrees without Git?
**A:** No – worktrees are a Git feature. Your project must be a Git repository.

### Q: What's the difference between Agents Window and Editor Window worktrees?
**A:** Agents Window has UI. Editor Window uses commands (`/worktree`, `/best-of-n`).

### Q: How do I clean up worktrees manually?
**A:** Use `/delete-worktree` in Editor Window, or delete from Agents Window UI.

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **What they are** | Isolated Git checkouts for agents |
| **Why use them** | Multiple agents, no conflicts, safe experiments |
| **Agents Window** | UI-native worktrees |
| **Editor Window** | `/worktree` and `/best-of-n` commands |
| **Configuration** | `.cursor/worktrees.json` (optional) |
| **Cleanup** | Automatic based on age and count |
| **Best for** | Parallel agents, risky refactors, model comparison |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Worktrees?** | Isolated copies of your Git repository |
| **Why use them?** | Multiple agents working without conflicts |
| **Where are they available?** | Agents Window (UI) or Editor Window (commands) |
| **Do I need to configure anything?** | No – optional for custom setup |
| **What's `/best-of-n`?** | Runs same task across multiple models to compare |
| **How to clean up?** | Automatic, or manual delete |

---

## The Bottom Line

**Worktrees are how you run multiple agents on the same repository without chaos.**

**Think of it as:**
- **Without Worktrees** = Multiple chefs in one kitchen 🍳👨‍🍳👩‍🍳 (chaos!)
- **With Worktrees** = Each chef has their own kitchen 🍳👨‍🍳 + 🍳👩‍🍳 + 🍳👨‍🍳 (organized!)

**For beginners:** Start with the Agents Window for worktrees (easier UI). Use them when you want to:
1. Run multiple agents simultaneously
2. Experiment safely without risking your main code
3. Compare different models on the same task

**The most powerful feature:** `/best-of-n` – let different models compete, then pick the winner. It's like having a coding competition between AI models!

