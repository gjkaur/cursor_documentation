This is the **Agent Security** documentation – it explains how Cursor protects you from potential risks when using AI agents. Since AI can behave unexpectedly due to prompt injection, hallucinations, and other issues, Cursor has built-in **guardrails** that limit what agents can do.

Think of this as the **safety manual** for Cursor. By default, sensitive actions require your manual approval.

Let me break this down for a complete beginner.

---

## The Core Principle (Most Important!)

> *"By default, sensitive actions require your manual approval."*

**You are in control.** The Agent cannot do anything dangerous without asking you first.

| Action Type | Default Behavior |
|-------------|------------------|
| Reading files | ✅ No approval needed |
| Searching code | ✅ No approval needed |
| Editing workspace files | ⚠️ No approval (but use version control!) |
| Editing config files | 🔒 **Approval required** |
| Running terminal commands | 🔒 **Approval required** |
| Network requests | 🔒 Severely restricted |
| MCP connections | 🔒 **Approval required** |

> *"These controls and behaviors are our defaults. We recommend keeping them enabled."*

---

## Why Security Matters

AI can behave unexpectedly due to:

| Risk | What it means |
|------|---------------|
| **Prompt injection** | Someone could craft a prompt that tricks the AI into doing something bad |
| **Hallucinations** | AI might "imagine" things that aren't true or safe |
| **Unexpected behavior** | AI systems are complex and can act in surprising ways |

**Cursor's guardrails protect you from these risks.**

---

## First-Party Tool Calls (Cursor's Built-in Tools)

Cursor includes tools that help agents write code:
- Reading files
- Editing files
- Running terminal commands
- Searching the web
- And more...

### What Requires Approval vs. What Doesn't

| Tool Action | Approval Needed? | Notes |
|-------------|------------------|-------|
| **Reading files** | ❌ No | Use `.cursorignore` to block access to sensitive files |
| **Searching code** | ❌ No | |
| **Actions exposing sensitive data** | ✅ Yes | Requires explicit approval |
| **Modifying workspace files** | ⚠️ No (except config files) | Changes save immediately – **use version control!** |
| **Configuration files** (settings, etc.) | ✅ Yes | Needs approval first |
| **Terminal commands** | ✅ Yes | Review every command before running |

### ⚠️ Important Warning:

> *"If you have auto-reload enabled, agent changes might execute before you can review them."*

**For beginners:** Be careful with auto-reload. Consider turning it off when using agents.

---

## Terminal Command Security

**Terminal commands need your approval by default.** Review every command before letting the agent run it.

### Your Options:

| Option | What it does | Risk Level |
|--------|--------------|------------|
| **Manual approval (default)** | You approve each command | ✅ Safest |
| **Allowlist** | Pre-approved commands run automatically | ⚠️ Best-effort (bypasses possible) |
| **Auto-approval** | All commands run automatically | 🔴 **Not recommended** |
| **"Run Everything" mode** | Skips ALL safety checks | 🔴 **NEVER USE** |

### Critical Warning:

> *"Never use 'Run Everything' mode, which skips all safety checks."*

**This is non-negotiable.** "Run Everything" mode is dangerous.

### About Allowlists:

> *"The allowlist is best-effort – bypasses are possible."*

**What this means:** Even if you put a command on the allowlist, it's not a 100% security guarantee. Attackers might find ways around it.

### Managing Allowlists:

You can manage allowlists for:
- Terminal commands
- MCP tools

**Where:** Settings UI or `~/.cursor/permissions.json`

---

## Third-Party Tool Calls (MCP)

You can connect external tools using **MCP** (Model Context Protocol).

### Security Process:

| Step | What happens |
|------|--------------|
| **1** | You approve the MCP connection |
| **2** | Each tool call still needs individual approval |
| **3** | You can pre-approve specific tools with an MCP allowlist |

**For beginners:** Be very careful with third-party tools. Only connect tools you trust.

---

## Network Requests

**Attackers could use network requests to steal data.**

### Default Restrictions:

Cursor's tools only make network requests to:

| Allowed Destination | Purpose |
|---------------------|---------|
| **GitHub** | Pulling code, creating PRs |
| **Direct link retrieval** | Accessing specific URLs you provide |
| **Web search providers** | Searching the web (if enabled) |

> *"Agents cannot make arbitrary network requests with default settings."*

**This is a key security feature.** The Agent can't just call any website on the internet.

---

## Workspace Trust

Cursor supports **workspace trust**, but it's **disabled by default**.

### What It Does:

When enabled, Cursor prompts you to choose between:

| Mode | What it means | AI Features? |
|------|---------------|---------------|
| **Normal mode** | Full access | ✅ Works normally |
| **Restricted mode** | Limited access | ❌ Broken/slowed |

### Important Note:

> *"Restricted mode breaks AI features. For untrusted repos, use a basic text editor instead."*

**What this means:** If you don't trust a repository, don't use Cursor on it at all. Use a basic text editor.

### How to Enable Workspace Trust:

1. Open your `user settings.json` file
2. Add:

```json
{
  "security.workspace.trust.enabled": true
}
```

**Organizations** can enforce this setting through MDM solutions.

---

## Security Summary Table

| Feature | Default | Risk if changed | Recommendation |
|---------|---------|-----------------|----------------|
| **Terminal approval** | Manual approval | High | Keep default |
| **Config file edits** | Requires approval | High | Keep default |
| **Network requests** | Severely restricted | High | Keep default |
| **"Run Everything"** | Disabled | Critical | **Never enable** |
| **Workspace trust** | Disabled | Low | Optional |
| **Auto-reload** | (User choice) | Medium | Disable when using agents |

---

## What If You Find a Security Vulnerability?

Cursor has a **responsible disclosure** process.

### To report a vulnerability:

**Email:** `security-reports@cursor.com`

Include:
- Details of the issue
- Steps to reproduce

### What Happens Next:

| Timeline | Action |
|----------|--------|
| **Within 5 business days** | Acknowledgment of report |
| **For critical incidents** | All users notified via email |

---

## Common Beginner Questions

### Q: Why does the Agent need approval for terminal commands?
**A:** Terminal commands can delete files, install software, or access sensitive data. Approving each command keeps you safe.

### Q: Can I trust the allowlist completely?
**A:** No. The documentation says it's "best-effort" and bypasses are possible. Always be cautious.

### Q: What should I do with untrusted code?
**A:** Don't use Cursor on it. Use a basic text editor.

### Q: Can the Agent read my passwords?
**A:** The Agent can read files. Don't store passwords in plain text in your codebase. Use environment variables.

### Q: What's the most dangerous setting?
**A:** **"Run Everything" mode** – never enable it. It skips all safety checks.

### Q: Can the Agent make HTTP requests to any website?
**A:** No. Only to GitHub, direct links you provide, and search providers.

---

## Quick Reference Card

| Security Feature | What It Protects |
|------------------|------------------|
| **Manual approval** | Terminal commands, config edits, MCP tools |
| **Network restrictions** | Prevents data exfiltration |
| **`.cursorignore`** | Blocks access to sensitive files |
| **Allowlist (best-effort)** | Auto-approves trusted commands (use carefully) |
| **Workspace trust** | Warns about untrusted repos |
| **No "Run Everything"** | Most important rule – never enable |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **Is Cursor safe by default?** | Yes – sensitive actions require your approval |
| **What needs approval?** | Terminal commands, config files, MCP tools |
| **What doesn't need approval?** | Reading files, searching code |
| **What's the one rule to never break?** | Never enable "Run Everything" mode |
| **Can the Agent access the internet freely?** | No – only GitHub, direct links, search |
| **What if I find a security issue?** | Email security-reports@cursor.com |

---

## The Bottom Line

**Cursor is designed to be safe by default, but you are the ultimate safeguard.**

**The Golden Rules:**

1. **Keep default security settings** – they protect you
2. **Review every terminal command** before approving
3. **NEVER enable "Run Everything" mode** – this is critical
4. **Use version control** – so you can revert changes
5. **Don't use Cursor on untrusted repositories** – use a basic text editor instead

**Think of security as:**
- **Default Cursor** = Driving with seatbelt, airbags, and safe driving rules 🚗✅
- **"Run Everything" mode** = Driving without seatbelt, airbags, or brakes 🚗💀

**For beginners:** Trust the defaults. Don't change security settings until you fully understand the risks. When in doubt, approve manually.

Would you like me to explain any specific security feature in more detail, or move on to another document?