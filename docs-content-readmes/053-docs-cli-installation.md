This is the **CLI Installation** documentation – it explains how to install and set up the Cursor CLI on different operating systems. The CLI lets you interact with Cursor's AI agents directly from your terminal.

Think of this as the **setup guide** for using Cursor from the command line.

Let me break this down.

---

## Installation Commands

### macOS, Linux, and Windows (WSL)

Install with a single command:

```bash
curl https://cursor.com/install -fsS | bash
```

This works on:
- macOS
- Linux
- WSL (Windows Subsystem for Linux)

### Windows (Native PowerShell)

Install using PowerShell:

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

> `irm` = Invoke-RestMethod (PowerShell's version of curl)  
> `iex` = Invoke-Expression (executes the downloaded script)

---

## Verification

After installation, verify the CLI is working correctly:

```bash
agent --version
```

This should output the installed version number.

---

## Post-Installation Setup (PATH Configuration)

The CLI installs to `~/.local/bin`. You may need to add this to your `PATH` so your terminal can find the `agent` command.

### For bash users:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### For zsh users (macOS default):

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## Start Using Cursor Agent

Once installed and configured:

```bash
agent
```

This starts an interactive session with the AI agent in your terminal.

---

## Updates

### Auto-Updates (Default)

> *"Cursor CLI will try to auto-update by default to ensure you always have the latest version."*

No action needed – it updates itself automatically.

### Manual Update

To manually update to the latest version:

```bash
agent update
```

---

## Installation Summary Table

| Platform | Command |
|----------|---------|
| macOS, Linux, WSL | `curl https://cursor.com/install -fsS \| bash` |
| Windows (PowerShell) | `irm 'https://cursor.com/install?win32=true' \| iex` |

### Post-Installation:

| Shell | Command |
|-------|---------|
| bash | `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc` |
| zsh | `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |

### Verify:

```bash
agent --version
```

### Update:

```bash
agent update
```

---

## Common Beginner Questions

### Q: What is WSL?
**A:** Windows Subsystem for Linux – lets you run Linux on Windows. The Linux install command works inside WSL.

### Q: What if `agent` command is not found after installation?
**A:** You likely need to add `~/.local/bin` to your PATH (see post-installation setup above).

### Q: Do I need an internet connection to use the CLI?
**A:** Yes – the CLI connects to Cursor's cloud services.

### Q: Does the CLI require a paid Cursor plan?
**A:** Yes – the CLI uses your existing Cursor subscription and usage-based pricing.

### Q: Can I use the CLI without installing the desktop app?
**A:** Yes – the CLI is standalone.

### Q: How do I know if auto-update worked?
**A:** Run `agent --version` to check your current version.

---

## The Bottom Line

**The Cursor CLI is easy to install – one command on Mac/Linux/WSL, one command on Windows PowerShell.**

**After installation:**
1. Add `~/.local/bin` to your PATH (if needed)
2. Run `agent` to start
3. The CLI auto-updates itself

**The CLI works alongside (or instead of) the desktop app – same account, same billing, same models.**

Would you like me to explain any other CLI commands or features?