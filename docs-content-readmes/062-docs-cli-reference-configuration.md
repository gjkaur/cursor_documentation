This is the **CLI Configuration** reference documentation – it explains how to configure the Agent CLI using the `cli-config.json` file.

Think of this as the **settings file** for the `agent` command – where you set preferences like Vim mode, permissions, proxy settings, and attribution.

Let me break this down.

---

## File Locations

| Type | Platform | Path |
|------|----------|------|
| **Global** | macOS/Linux | `~/.cursor/cli-config.json` |
| **Global** | Windows | `$env:USERPROFILE\.cursor\cli-config.json` |
| **Project** | All | `<project>/.cursor/cli.json` |

> *"Only permissions can be configured at the project level. All other CLI settings must be set globally."*

---

## Override with Environment Variables

| Variable | Purpose |
|----------|---------|
| `CURSOR_CONFIG_DIR` | Custom directory path |
| `XDG_CONFIG_HOME` (Linux/BSD) | Uses `$XDG_CONFIG_HOME/cursor/cli-config.json` |

---

## Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `version` | number | Config schema version (current: `1`) |
| `editor.vimMode` | boolean | Enable Vim keybindings (default: `false`) |
| `permissions.allow` | string[] | Permitted operations (see Permissions) |
| `permissions.deny` | string[] | Forbidden operations (see Permissions) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `model` | object | Selected model configuration |
| `hasChangedDefaultModel` | boolean | CLI-managed model override flag |
| `network.useHttp1ForAgent` | boolean | Use HTTP/1.1 instead of HTTP/2 (default: `false`) |
| `attribution.attributeCommitsToAgent` | boolean | Add "Made with Cursor" trailer to Agent commits (default: `true`) |
| `attribution.attributePRsToAgent` | boolean | Add "Made with Cursor" footer to Agent PRs (default: `true`) |

---

## Example Configurations

### Minimal Configuration

```json
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

### Enable Vim Mode

```json
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

### Configure Permissions

```json
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

> *"See Permissions for available permission types and examples."*

---

## HTTP/1.1 Fallback (For Corporate Proxies)

Some enterprise proxies (like Zscaler) don't support HTTP/2 bidirectional streaming. Enable HTTP/1.1 mode:

```json
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": [], "deny": [] },
  "network": {
    "useHttp1ForAgent": true
  }
}
```

> *"This switches agent connections to HTTP/1.1 with Server-Sent Events (SSE), which works with most corporate proxies."*

---

## Proxy Configuration (Environment Variables)

If you're behind a corporate proxy:

```bash
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
export NODE_USE_ENV_PROXY=1
```

### SSL Inspection (Corporate CA Certificate):

If your proxy performs SSL inspection (man-in-the-middle):

```bash
export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca-cert.pem
```

---

## Model Selection

You can select a model using the `/model` slash command in the CLI:

```
/model auto
/model gpt-5.2
/model sonnet-4.5-thinking
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Config errors** | Move file aside and restart: `mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad` |
| **Changes don't persist** | Ensure valid JSON and write permissions. Some fields are CLI-managed and may be overwritten. |

---

## Important Notes

| Note | Description |
|------|-------------|
| **Pure JSON format** | No comments allowed |
| **Self-repair** | CLI performs self-repair for missing fields |
| **Backup** | Corrupted files are backed up as `.bad` and recreated |
| **Exact strings** | Permission entries are exact strings (see Permissions for details) |

---

## Complete Example

```json
{
  "version": 1,
  "editor": {
    "vimMode": true
  },
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)",
      "Shell(npm)",
      "Read(src/**/*.ts)",
      "Write(package.json)",
      "WebFetch(docs.github.com)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  },
  "network": {
    "useHttp1ForAgent": false
  },
  "attribution": {
    "attributeCommitsToAgent": true,
    "attributePRsToAgent": true
  }
}
```

---

## Configuration Summary Table

| Setting | Location | Scope |
|---------|----------|-------|
| `version` | Global only | Required |
| `editor.vimMode` | Global only | Optional |
| `permissions` | Global or Project | Optional |
| `network.useHttp1ForAgent` | Global only | Optional |
| `attribution.*` | Global only | Optional |
| `model` | Global only | CLI-managed |

---

## Common Beginner Questions

### Q: Do I need to create this file?
**A:** No – defaults work fine. Only create it if you need custom permissions or settings.

### Q: Where is the global config file on Windows?
**A:** `%USERPROFILE%\.cursor\cli-config.json`

### Q: Can I have different permissions for different projects?
**A:** Yes – put a `cli.json` file in the project's `.cursor/` directory.

### Q: How do I enable Vim mode permanently?
**A:** Set `"editor.vimMode": true` in `~/.cursor/cli-config.json`.

### Q: Can I add comments to the JSON file?
**A:** No – pure JSON format only. No comments allowed.

### Q: What happens if my config file is corrupted?
**A:** CLI backs it up as `.bad` and recreates it.

---

## The Bottom Line

**The CLI configuration file lets you customize the behavior of the `agent` command – from Vim keybindings to permissions to proxy settings.**

**For most users:** You don't need to create this file. Defaults work fine.

**For power users:** You can:
- Enable Vim mode permanently
- Pre-approve trusted shell commands
- Block dangerous commands globally
- Configure HTTP/1.1 for corporate proxies
- Set attribution preferences

**Remember:** Only permissions can be set at the project level. All other settings are global only.

Would you like me to explain any specific configuration option in more detail?