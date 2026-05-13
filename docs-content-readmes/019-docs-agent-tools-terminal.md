This is the **Terminal Tool** documentation – it explains how the Agent runs shell commands on your computer safely. This is one of the most powerful (and potentially scary) features of Cursor.

Think of the Terminal tool as giving the Agent **hands to type commands** in your terminal – but with a **safety cage** (sandbox) to prevent accidents.

Let me break this down for a complete beginner.

---

## What Is the Terminal Tool? (The 10-Second Summary)

**The Agent can run shell commands directly in your terminal**, with safe sandbox execution.

This means the Agent can:
- Install packages (`npm install`)
- Run tests (`npm test`)
- Start servers (`python app.py`)
- Check Git status (`git status`)
- And much more...

**But it does this safely** – by default, the Agent runs in a "sandbox" (restricted environment) that blocks unauthorized access to your files and network.

| Without Sandbox | With Sandbox |
|-----------------|--------------|
| Agent could delete anything | Agent limited to your workspace |
| Agent could access any website | Network blocked by default |
| Dangerous mistakes possible | Safe by default |

---

## What Is a Sandbox? (Simple Explanation)

A **sandbox** is like a playpen for the Agent. It can move around freely inside the playpen, but it can't get out and mess with things it shouldn't.

**Restrictions in the sandbox:**

| Access Type | Sandbox Behavior | What it means |
|-------------|------------------|----------------|
| **File access** | Read access only | Can read files, but can't write outside workspace |
| **Network access** | **Blocked by default** | Can't access internet unless you allow it |
| **Temporary files** | Full access to `/tmp/` | Can use temp files as needed |
| **Cursor config** | Protected | Your Cursor settings are safe |

**The .cursor configuration directory stays protected regardless of allowlist settings.**

---

## Platform Requirements

The sandbox works differently depending on your operating system:

### macOS 🍎
- **Cursor v2.0 or later**
- **Works out of the box** – no additional setup needed!

### Windows 🪟
- **WSL2 must be installed and configured**
- The sandbox runs inside WSL2 (Windows Subsystem for Linux)

**For beginners:** If you're on Windows and haven't set up WSL2, the Agent will ask for approval before running commands instead of using the sandbox.

### Linux 🐧
- **Kernel 6.2 or later** with Landlock support
- **Unprivileged user namespaces enabled** (usually on by default)

If your kernel doesn't meet requirements, Agent falls back to asking for approval before running commands.

---

## What Happens When a Command Needs Full Access?

Some commands need full system access and **bypass the sandbox**. The Agent will **ask for your approval** before running these.

**Example:** `sudo apt update` (needs admin privileges)

The Agent will show:
> *"This command needs to run outside the sandbox. Do you approve?"*

**You are always in control.** Nothing runs without your permission unless you configure it otherwise.

---

## The Allowlist: Your Safety Shortcut

Commands on the **allowlist** skip sandbox restrictions and run immediately.

### How to add to allowlist:

When a sandboxed command fails due to restrictions, you see this prompt:

| Option | What it does |
|--------|--------------|
| **Skip** | Cancel the command, let Agent try something else |
| **Run** | Execute this once without sandbox restrictions |
| **Add to allowlist** | Run without restrictions AND auto-approve for future use |

**Example:** You run `npm install` and it needs network access. You choose "Add to allowlist" – now all `npm` commands will run freely.

---

## Default Network Allowlist

When you **enable** network access for the sandbox, Cursor only allows connections to a **curated set of domains** by default.

**These include:**
- Common package registries (npm, PyPI, etc.)
- Cloud providers
- Language toolchains

**Why this matters:** Most development workflows work without extra configuration. You don't need to manually allow every single domain.

---

## Sandbox Configuration (Advanced)

For power users, you can customize sandbox behavior with a `sandbox.json` file.

**Two locations:**
| Location | Scope |
|----------|-------|
| `~/.cursor/sandbox.json` | Per-user (affects all your projects) |
| `<workspace>/.cursor/sandbox.json` | Per-repo (specific to one project) |

**What you can control:**
- Network access rules
- Filesystem paths
- Build caches
- And more...

**For beginners:** You don't need to worry about this file until you have specific security or access needs.

---

## Auto-Run Mode: How Much Control Do You Want?

Configure this at: **Settings → Cursor Settings → Agents → Auto-Run**

| Mode | Behavior | Best for |
|------|----------|----------|
| **Run in Sandbox** | Tools auto-run in sandbox where possible | **Most users (default)** |
| **Ask Every Time** | All tools require approval before running | Paranoid security, learning |
| **Run Everything** | All tools run automatically, no approval | Advanced users who trust Agent |

**For beginners:** Stick with **"Run in Sandbox"** (default). It's the best balance of safety and convenience.

---

## Auto-Run Network Access

Control how sandboxed commands access the network:

| Mode | Behavior |
|------|----------|
| **sandbox.json only** | Network limited to domains in your config (no defaults) |
| **sandbox.json + Defaults** | Your rules + Cursor's built-in defaults (default setting) |
| **Allow All** | All network access allowed (least secure) |

**For beginners:** Keep the default **"sandbox.json + Defaults"** unless you have a specific reason to change it.

---

## Protection Settings

| Setting | What it does |
|---------|--------------|
| **Command Allowlist** | Commands that can run automatically outside sandbox |
| **MCP Allowlist** | MCP tools that can run automatically outside sandbox |

**Enterprise only:** Some protection settings are only available for Enterprise subscriptions.

---

## Environment Variables (Advanced)

Cursor injects these variables into every sandboxed process. They help scripts understand they're running inside the sandbox.

| Variable | Platform | Description |
|----------|----------|-------------|
| `CURSOR_SANDBOX` | All | Set to "seatbelt" (macOS) or "native" (Linux/Windows) |
| `CURSOR_ORIG_UID` | macOS, Linux | Your real user ID before sandbox |
| `CURSOR_ORIG_GID` | macOS, Linux | Your real group ID before sandbox |

### Important Linux Note:

On Linux, the sandbox remaps the process to **UID 0 (root)** inside the sandbox. This means `id -u` returns `0`, not your real user ID.

**If your scripts need the real user ID**, use `CURSOR_ORIG_UID` instead.

### Docker Example:

```bash
docker run --rm \
  --user ${CURSOR_ORIG_UID:-$(id -u)}:${CURSOR_ORIG_GID:-$(id -g)} \
  -v "$PWD:/work" \
  -w /work \
  my-image build
```

The `${CURSOR_ORIG_UID:-$(id -u)}` fallback ensures the command works **both inside and outside** the sandbox.

---

## Troubleshooting: Shell Themes

**Problem:** Some shell themes (like Powerlevel9k, Powerlevel10k) can interfere with terminal output. Command output looks truncated or misformatted.

**Solution:** Disable the theme or switch to a simpler prompt when Agent runs.

### Detect Agent in your shell config:

**For zsh (`~/.zshrc`):**
```bash
# Disable Powerlevel10k when Cursor Agent runs
if [[ -n "$CURSOR_AGENT" ]]; then
  # Skip theme initialization for better compatibility
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

**For bash (`~/.bashrc`):**
```bash
# Fall back to a simple prompt in Agent sessions
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \w \$ '
fi
```

---

## Enterprise Settings (For Admins)

If you're an admin, you can control sandbox behavior for your entire team:

| Setting | Description |
|---------|-------------|
| **Auto-Run Controls** | Enable/disable auto-run controls |
| **Sandboxing Mode** | Control whether sandbox is available |
| **Sandbox Networking** | Choose network access level |
| **Delete File Protection** | Prevent Agent from deleting files automatically |
| **MCP Tool Protection** | Prevent automatic MCP tool execution |
| **Terminal Command Allowlist** | Commands that can run without sandboxing |
| **Enable Run Everything** | Allow users to enable "Run Everything" mode |

---

## Real-World Examples

### Example 1: Installing a package

**You say:** "Install express"
**Agent runs:** `npm install express`
**Sandbox behavior:** Needs network access. If not allowed, Agent will ask.

### Example 2: Running tests

**You say:** "Run the tests"
**Agent runs:** `npm test`
**Sandbox behavior:** Usually fine (no network needed)

### Example 3: Starting a server

**You say:** "Start the development server"
**Agent runs:** `python app.py`
**Sandbox behavior:** May need network access. Agent asks if not allowed.

### Example 4: Git operations

**You say:** "Check my Git status"
**Agent runs:** `git status`
**Sandbox behavior:** Works inside workspace, safe.

---

## Common Beginner Questions

### Q: Can the Agent delete my files?
**A:** By default, the sandbox limits file access. But some commands (like `rm -rf`) may still work. Use **Delete File Protection** (Enterprise) for extra safety.

### Q: Does the Agent have access to my passwords?
**A:** No. The sandbox blocks unauthorized access. Never type passwords into prompts anyway.

### Q: What if I don't want the Agent running commands at all?
**A:** Set Auto-Run mode to **"Ask Every Time"** – you'll approve every command.

### Q: Can I see what commands the Agent ran?
**A:** Yes! The terminal output shows everything. You can also check history.

### Q: Does the sandbox work on Windows without WSL2?
**A:** No. The sandbox requires WSL2 on Windows. Otherwise, commands ask for approval.

### Q: What happens if a command needs sudo?
**A:** The Agent will ask for approval. You may need to enter your password.

---

## Quick Reference Card

| Concept | What it means |
|---------|---------------|
| **Sandbox** | Restricted environment for safe command execution |
| **Allowlist** | Commands that bypass sandbox restrictions |
| **Auto-Run Mode** | How much approval you need (Sandbox/Ask/Run Everything) |
| **Network Access** | Blocked by default, can be configured |
| **CURSOR_AGENT** | Environment variable to detect Agent in scripts |
| **WSL2** | Required for Windows sandbox |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What does the Terminal tool do?** | Lets Agent run shell commands on your computer |
| **Is it safe?** | Yes – sandbox restricts access by default |
| **Do I need to set anything up?** | On macOS: no. On Windows: need WSL2. On Linux: kernel 6.2+ |
| **Can Agent access the internet?** | No, unless you allow it |
| **Can Agent delete files?** | Limited by sandbox. Enterprise has extra protection |
| **How do I control it?** | Settings → Agents → Auto-Run |

---

## The Bottom Line

**The Terminal tool is what makes the Agent truly autonomous** – it can not only suggest code but also run commands to test, build, and deploy.

**Think of the sandbox as:**
- **No sandbox** = Giving a toddler a permanent marker and no supervision 🖍️💥
- **With sandbox** = Giving the toddler crayons in a playpen 🖍️✅

**For beginners:** Leave the default settings. The sandbox protects you. Only add commands to the allowlist after you understand what they do. If you're ever unsure, choose "Ask Every Time" mode for maximum control.

**The most important safety feature:** You are always in control. Nothing runs without your permission unless you configure it otherwise.

Would you like me to explain any specific part of the sandbox configuration in more detail, or move on to another document?