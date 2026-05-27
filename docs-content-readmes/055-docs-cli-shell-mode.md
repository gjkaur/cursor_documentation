This is the **Shell Mode** documentation – it explains how to run shell commands directly from the Cursor CLI without leaving your conversation.

Think of Shell Mode as **running terminal commands inside your AI chat** – you can check Git status, run builds, or inspect files, and the output appears right in the conversation.

Let me break this down.

---

## What Is Shell Mode? (The 10-Second Summary)

**Shell Mode runs shell commands directly from the CLI without leaving your conversation.** Use it for quick, non-interactive commands with safety checks and output displayed in the conversation.

| Without Shell Mode | With Shell Mode |
|--------------------|-----------------|
| Exit chat to run commands | Run commands inside the conversation |
| Context lost when you exit | Output stays in chat history |
| Manual copy-paste | Seamless integration |

> *"Use it for quick, non-interactive commands with safety checks and output displayed in the conversation."*

---

## Command Execution

Commands run in your **login shell** (`$SHELL`) with the CLI's working directory and environment.

### Run a command:

```
$ git status
```

### Chain commands (run in different directories):

```
cd subdir && npm test
```

> *"Each command runs independently – use `cd <dir> && ...` to run commands in other directories."*

---

## Output

| Feature | Behavior |
|---------|----------|
| **Large outputs** | Truncated automatically |
| **Long-running processes** | Timeout to maintain performance |
| **Expand output** | Press `Ctrl+O` to see full output |

---

## Limitations

| Limitation | Details |
|------------|---------|
| **Timeout** | Commands timeout after **30 seconds** |
| **No long-running processes** | Servers, daemons not supported |
| **No interactive prompts** | Commands that ask for input won't work |

> *"Use short, non-interactive commands for best results."*

---

## Permissions

> *"Commands are checked against your permissions and team settings before execution."*

| Security Feature | Description |
|------------------|-------------|
| **Permission checks** | Commands validated before execution |
| **Admin policies** | May block certain commands |
| **Inline allowlist** | Commands with redirection cannot be allowed inline |

---

## Usage Guidelines

### ✅ Works Well For:

| Use Case | Example |
|----------|---------|
| **Status checks** | `git status`, `ls -la` |
| **Quick builds** | `npm run build` |
| **File operations** | `cat file.txt`, `grep pattern` |
| **Environment inspection** | `echo $PATH`, `pwd` |

### ❌ Avoid:

| Use Case | Why |
|----------|-----|
| **Long-running servers** | Timeout after 30 seconds |
| **Interactive applications** | Can't respond to prompts |
| **Commands requiring input** | No stdin support |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Command hangs** | Press `Ctrl+C` and add non-interactive flags |
| **Permission prompted** | Approve once or `Tab` to add to allowlist |
| **Output truncated** | Press `Ctrl+O` to expand |
| **Wrong directory** | Use `cd <dir> && ...` – changes don't persist between commands |

> *"Shell Mode supports zsh and bash from your `$SHELL` variable."*

---

## FAQ (From Documentation)

The documentation lists these FAQs (answers not shown):

| Question |
|----------|
| Does `cd` persist across runs? |
| Can I change the timeout? |
| Where are permissions configured? |
| How do I exit Shell Mode? |

### Likely Answers:

| Question | Answer |
|----------|--------|
| **Does `cd` persist?** | No – each command runs independently. Use `cd <dir> && ...` |
| **Can I change timeout?** | Not currently – fixed at 30 seconds |
| **Where are permissions?** | Cursor Settings or team dashboard |
| **How to exit Shell Mode?** | Likely `Ctrl+D` or `/exit` |

---

## Real-World Examples

### Check Git Status:

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.
Changes not staged for commit:
  modified: src/app/page.tsx
```

### Run Tests:

```
$ cd backend && npm test
```

### Inspect Environment:

```
$ echo $NODE_ENV
production
```

### List Files:

```
$ ls -la src/components/
total 48
drwxr-xr-x  12 user  staff   384 May 9 10:00 .
...
```

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **What it does** | Run shell commands inside CLI conversation |
| **Timeout** | 30 seconds |
| **Output truncation** | Automatic; `Ctrl+O` to expand |
| **Directory persistence** | ❌ No – use `cd <dir> && ...` |
| **Interactive commands** | ❌ Not supported |
| **Long-running processes** | ❌ Not supported |
| **Permissions** | Checked before execution |

### Keyboard Shortcuts:

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel hanging command |
| `Ctrl+O` | Expand truncated output |
| `Tab` | Add to allowlist when prompted |

---

## Common Beginner Questions

### Q: When should I use Shell Mode?
**A:** For quick checks – Git status, running tests, inspecting files. Not for starting servers.

### Q: Can I run `npm run dev`?
**A:** Not recommended – it's a long-running server that will timeout.

### Q: Does `cd` change my directory for the next command?
**A:** No – each command is independent. Use `cd subdir && your-command` to run in a different directory.

### Q: What happens if a command takes more than 30 seconds?
**A:** It times out. Use shorter commands or add non-interactive flags.

### Q: How do I see the full output if it's truncated?
**A:** Press `Ctrl+O` to expand.

### Q: Is Shell Mode safe?
**A:** Yes – commands are checked against your permissions and team settings before execution.

---

## The Bottom Line

**Shell Mode is a convenient way to run quick shell commands without leaving your Cursor CLI conversation.**

**Think of it as:**
- **Without Shell Mode** = Exit chat → run command → restart chat 🔄
- **With Shell Mode** = Run command directly in chat 💬

**Best for:**
- `git status`, `git diff`
- `ls`, `cat`, `grep`
- `npm test`, `go test`
- `echo`, `pwd`, `which`

**Not for:**
- `npm run dev` (server)
- `vim` (interactive)
- `top` (long-running)
- `curl` with no timeout

**Pro tip:** Use `cd <dir> && <command>` to run commands in other directories since `cd` doesn't persist between commands.

