This is the **Model and Integration Management** documentation – it explains how to control which AI models are available to your team, manage MCP server trust, and set up integrations with tools like Slack, GitHub, and Linear.

Think of this as the **governance guide** for enterprise teams – controlling costs, ensuring compliance, and managing third-party integrations.

Let me break this down.

---

## Model Access Control (Enterprise)

Enterprise teams can **control which AI models team members can use**. This helps:

| Objective | Description |
|-----------|-------------|
| **Manage costs** | Restrict expensive models |
| **Ensure appropriate usage** | Limit to approved models |
| **Comply with policies** | Meet organizational requirements |

> *"Model access controls are configured through the team dashboard. Navigate to Settings and look for 'Model Access Control' (Enterprise only)."*

### How Enterprise Model Rollout Works

When new models become available, Cursor **doesn't immediately enable them** for all enterprise teams. Instead, Enterprise teams can **opt in** to new models for their organization.

> *"See Models for the current list of available models."*

---

## Restrict Personal API Keys (BYOK Controls) – Enterprise

Enterprise teams can **prevent team members from using their own API keys** with third-party providers (OpenAI, Anthropic, Azure, AWS Bedrock) in Cursor.

| Effect |
|--------|
| All usage goes through Cursor's included models and usage pool |
| Prevents shadow AI usage |
| Ensures consistent cost tracking and security |

> *"Configure this in the team dashboard under Settings (Enterprise only)."*

---

## MCP Server Trust Management

The Model Context Protocol (MCP) lets you connect external tools and data sources to Cursor.

### MCP Servers Can:

| Capability |
|------------|
| Read files from external systems |
| Execute operations on your behalf |
| Access databases and APIs |
| Integrate with third-party services |

> *"MCP servers are designed and implemented by external vendors, not Cursor. We work with partners to provide a vetted marketplace of trusted servers, but you should review each server's capabilities and permissions before enabling it for your team."*

**Important:** Because MCP servers have significant capabilities, you need to manage which servers your team can use.

---

## MCP Allowlist (Enterprise)

Enterprise teams can control **which MCP servers team members are allowed to use**.

> *"Configure this in the team dashboard under 'MCP Configuration' (Enterprise only)."*

### Allowlist Entry Syntax

| Entry | Meaning |
|-------|---------|
| `server:tool` | One specific tool on one specific MCP server |
| `server:*` | All tools from one MCP server |
| `*:tool` | One tool from any MCP server |
| `*:*` | All MCP tools (use with caution) |

### Allowlist Resolution Order (Higher priority replaces lower)

| Priority | Source |
|----------|--------|
| 1 | Team dashboard or other admin-controlled settings |
| 2 | `~/.cursor/permissions.json` (via MDM) |
| 3 | Editor settings and inline "Add to allowlist" |

> *"Higher-priority sources replace lower-priority ones. They do not merge."*

### Behavior

| Rule | Description |
|------|-------------|
| **Blocking** | When allowlist active, only servers matching an allowlist entry can run |
| **Configuration** | Adding server to allowlist does NOT push it to users' machines – they still need to configure the server |
| **Wildcards** | All entries support `*` to match any sequence of characters |

---

### Command-Based Servers (stdio) – Allowlist Matching

For local MCP servers, the allowlist matches against the **full command string** (command + all args joined with spaces).

**Example `mcp.json`:**
```json
{
  "mcpServers": {
    "my-tool": {
      "command": "npx",
      "args": ["-y", "@acme/mcp-tool@latest"]
    }
  }
}
```

**Full command string:** `npx -y @acme/mcp-tool@latest`

**With path resolution:** On most systems, `npx` resolves to full path like `/usr/local/bin/npx` or `/opt/homebrew/bin/npx`

**Allowlist examples:**

| Allowlist entry | Matches |
|-----------------|---------|
| `*npx -y @acme/mcp-tool@latest` | npx at any path, exact arguments |
| `/usr/local/bin/npx -y @acme/mcp-tool@latest` | Only this exact path |
| `*npx -y @acme/*` | Any @acme-scoped MCP package |
| `*python */scripts/mcp-server.py*` | Python server at any matching path |

---

### URL-Based Servers (HTTP/SSE) – Allowlist Matching

For remote MCP servers, the allowlist matches against the **full URL**.

**Example `mcp.json`:**
```json
{
  "mcpServers": {
    "acme-tools": {
      "url": "https://mcp.acme.com/sse"
    }
  }
}
```

**Allowlist examples:**

| Allowlist entry | Matches |
|-----------------|---------|
| `https://mcp.acme.com/sse` | This exact URL |
| `https://*.acme.com/*` | Any subdomain and path under acme.com |
| `https://mcp.acme.com/*` | Any path on this host |

---

## Git Repository Blocklist (Enterprise)

Prevent Cursor from accessing specific repositories.

> *"Add repository URLs or patterns in the team dashboard under 'Repository Blocklist' (Enterprise only). Cursor will refuse to index or work with blocked repositories."*

---

## Integrations

### Slack Integration

| Feature | Description |
|---------|-------------|
| **Purpose** | Cloud Agents run directly from Slack |
| **Usage** | Team members mention `@cursor` with a prompt |
| **Output** | Automated code changes delivered as pull requests |
| **Permissions** | Read messages, post responses, access channel metadata |

> *"See Slack integration for detailed setup and usage instructions."*

### GitHub, GHES, and GitLab Integration

| Feature | Description |
|---------|-------------|
| **Purpose** | Connect Cursor to version control system |
| **Requirements** | Read access to repositories, write access to create PRs |
| **Control** | You control which repositories the Cursor app can access |

> *"See GitHub integration for setup."*

### Linear Integration

| Feature | Description |
|---------|-------------|
| **Purpose** | Start Cloud Agents from issues |
| **Requirements** | Read access to issues, write access to update issue status |

> *"See Linear integration for details."*

---

## Quick Reference Card

| Control | Availability | Configuration |
|---------|--------------|---------------|
| **Model Access Control** | Enterprise | Dashboard → Model Access Control |
| **BYOK Controls** | Enterprise | Dashboard → Settings |
| **MCP Allowlist** | Enterprise | Dashboard → MCP Configuration |
| **Repository Blocklist** | Enterprise | Dashboard → Repository Blocklist |
| **Slack Integration** | All plans | Integrations page |
| **GitHub/GitLab Integration** | All plans | Integrations page |
| **Linear Integration** | All plans | Integrations page |

---

## MCP Allowlist Summary

| Aspect | Details |
|--------|---------|
| **Syntax** | `server:tool`, `server:*`, `*:tool`, `*:*` |
| **Resolution** | Higher priority replaces lower (no merge) |
| **Command matching** | Full command string (including resolved path) |
| **URL matching** | Full URL |
| **Wildcards** | `*` supported |
| **Configuration** | Dashboard, `~/.cursor/permissions.json`, or editor settings |

---

## Common Beginner Questions

### Q: Can Enterprise teams restrict which models are available?
**A:** Yes – model access control is available for Enterprise teams.

### Q: Can I prevent team members from using their own API keys?
**A:** Yes – BYOK controls are available on Enterprise plans.

### Q: Are new models automatically enabled for Enterprise teams?
**A:** No – Enterprise teams opt in to new models.

### Q: How do I control which MCP servers my team can use?
**A:** Use MCP Allowlist in the team dashboard (Enterprise only).

### Q: Does adding a server to the allowlist push it to users?
**A:** No – users still need to configure the server in their own Cursor settings.

### Q: Can I block specific repositories?
**A:** Yes – repository blocklist is available on Enterprise plans.

---

## The Bottom Line

**Model and Integration Management gives enterprise teams control over AI models, MCP servers, and third-party integrations.**

**Key enterprise controls:**
1. **Model Access Control** – Restrict which models team members can use
2. **BYOK Controls** – Prevent personal API key usage
3. **MCP Allowlist** – Control which external MCP servers can run
4. **Repository Blocklist** – Prevent access to specific repos
5. **New model rollout** – Enterprise teams opt in to new models

**For security teams:** These controls help manage costs, ensure compliance, and prevent unauthorized AI usage.

**For integrations:** Slack, GitHub, GitLab, and Linear integrations are available for all plans with proper permission management.

Would you like me to explain any specific control or integration in more detail?