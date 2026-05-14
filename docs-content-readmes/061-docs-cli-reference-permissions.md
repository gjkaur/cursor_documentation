This is the **CLI Permissions** reference documentation – it explains how to configure what the agent is **allowed or denied** to do using permission tokens.

Think of this as **setting up guardrails** for the CLI agent – you can control which shell commands, file reads/writes, web fetch domains, and MCP tools the agent can use.

Let me break this down.

---

## Where Permissions Are Stored

Permissions are set in a JSON configuration file:

| Location | Scope |
|----------|-------|
| `~/.cursor/cli-config.json` | Global (all projects) |
| `<project>/.cursor/cli.json` | Project-specific |

---

## Permission Types

| Type | Format | Controls |
|------|--------|----------|
| **Shell commands** | `Shell(commandBase)` | Which terminal commands can run |
| **File reads** | `Read(pathOrGlob)` | Which files can be read |
| **File writes** | `Write(pathOrGlob)` | Which files can be modified |
| **Web fetch** | `WebFetch(domainPattern)` | Which domains can be fetched |
| **MCP tools** | `Mcp(server:tool)` | Which MCP tools can run |

---

## 1. Shell Commands

**Format:** `Shell(commandBase)`

Controls access to shell commands. `commandBase` is the first token in the command line (the command name). Supports glob patterns.

| Example | Description |
|---------|-------------|
| `Shell(ls)` | Allow `ls` commands |
| `Shell(git)` | Allow any git subcommand |
| `Shell(npm)` | Allow npm package manager commands |
| `Shell(curl:*)` | Allow `curl` with any arguments |
| `Shell(rm)` | Deny destructive file removal (commonly in `deny`) |

---

## 2. File Reads

**Format:** `Read(pathOrGlob)`

Controls read access to files and directories. Supports glob patterns.

| Example | Description |
|---------|-------------|
| `Read(src/**/*.ts)` | Allow reading TypeScript files in `src` |
| `Read(**/*.md)` | Allow reading markdown files anywhere |
| `Read(.env*)` | Deny reading environment files |
| `Read(/etc/passwd)` | Deny reading system files |

---

## 3. File Writes

**Format:** `Write(pathOrGlob)`

Controls write access to files and directories. Supports glob patterns.

> *"When using in print mode, `--force` is required to write files."*

| Example | Description |
|---------|-------------|
| `Write(src/**)` | Allow writing to any file under `src` |
| `Write(package.json)` | Allow modifying `package.json` |
| `Write(**/*.key)` | Deny writing private key files |
| `Write(**/.env*)` | Deny writing environment files |

---

## 4. Web Fetch

**Format:** `WebFetch(domainPattern)`

Controls which domains the agent can fetch when using the web fetch tool.

> *"Without an allowlist entry, each fetch prompts for approval. Add domains to allow to auto-approve fetches from trusted sources."*

### Domain Pattern Matching:

| Pattern | Matches |
|---------|---------|
| `*` | All domains (use with caution) |
| `*.example.com` | Subdomains (docs.example.com, api.example.com) |
| `example.com` | Exact domain only |

| Example | Description |
|---------|-------------|
| `WebFetch(docs.github.com)` | Allow fetches from `docs.github.com` |
| `WebFetch(*.example.com)` | Allow fetches from any subdomain of `example.com` |
| `WebFetch(*)` | Allow fetches from any domain (use with caution) |

---

## 5. MCP Tools

**Format:** `Mcp(server:tool)`

Controls which MCP (Model Context Protocol) tools the agent can run. Use `server` (from `mcp.json`) and `tool` name, with `*` for wildcards.

| Example | Description |
|---------|-------------|
| `Mcp(datadog:*)` | Allow all tools from the Datadog MCP server |
| `Mcp(*:search)` | Allow any server's search tool |
| `Mcp(*:*)` | Allow all MCP tools (use with caution) |

---

## Configuration Example

Create a `cli.json` or `cli-config.json` file:

```json
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)",
      "Read(src/**/*.ts)",
      "Write(package.json)",
      "WebFetch(docs.github.com)",
      "WebFetch(*.github.com)",
      "Mcp(datadog:*)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)",
      "Write(**/.env*)",
      "WebFetch(malicious-site.com)"
    ]
  }
}
```

---

## Pattern Matching Rules

| Rule | Description |
|------|-------------|
| Glob patterns | Use `*`, `?`, and `**` wildcards |
| Relative paths | Expected to be within current workspace |
| Absolute paths | Can target files outside the project |
| **Deny takes precedence** | Deny rules override allow rules |
| `command:args` syntax | Use `curl:*` to match command + arguments with globs |

---

## Permission Types Summary

| Type | Format | Example Allow | Example Deny |
|------|--------|---------------|---------------|
| Shell | `Shell(cmd)` | `Shell(git)` | `Shell(rm)` |
| Read | `Read(path)` | `Read(src/**/*.ts)` | `Read(.env*)` |
| Write | `Write(path)` | `Write(package.json)` | `Write(**/*.key)` |
| WebFetch | `WebFetch(domain)` | `WebFetch(docs.github.com)` | `WebFetch(*)` |
| MCP | `Mcp(server:tool)` | `Mcp(datadog:*)` | `Mcp(*:*)` |

---

## Common Beginner Questions

### Q: Do I need to set up permissions?
**A:** Not for basic use. Default behavior asks for approval. Permissions let you auto-approve trusted commands.

### Q: What's the difference between `allow` and `deny`?
**A:** `allow` lists commands that can run automatically. `deny` lists commands that are never allowed. Deny takes precedence.

### Q: Can I use glob patterns for file paths?
**A:** Yes – `**/*.ts` matches all TypeScript files recursively.

### Q: How do I allow all git commands?
**A:** `Shell(git)` – this allows any git subcommand.

### Q: How do I block all web fetches?
**A:** Don't add any `WebFetch` entries to `allow`, or add `WebFetch(*)` to `deny`.

### Q: Do project-specific permissions override global ones?
**A:** Both are applied. Deny rules take precedence regardless of where they come from.

---

## The Bottom Line

**Permissions let you pre-approve or block specific actions the CLI agent can take – from shell commands to file access to web requests.**

**For most users:** You don't need to configure permissions. The default "ask for approval" behavior is safe.

**For power users and teams:** Permissions are powerful for:
- Automating trusted workflows (auto-approve `git status`, `npm test`)
- Blocking dangerous commands (`rm -rf`, writing to `.env` files)
- Restricting web access to trusted domains
- Controlling MCP tool usage

**Remember:** Deny rules take precedence over allow rules. Always put sensitive patterns in `deny`.

