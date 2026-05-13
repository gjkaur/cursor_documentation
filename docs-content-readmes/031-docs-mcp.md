This is the **Model Context Protocol (MCP)** documentation – it explains how Cursor can connect to **external tools and data sources**. MCP is like a **universal adapter** that lets Cursor talk to anything – databases, APIs, local files, custom scripts – regardless of what language they're written in.

Think of MCP as **plugging Cursor directly into your tools** – instead of describing your database schema, you just connect to it and the Agent can query it directly.

Let me break this down for a beginner.

---

## What Is MCP? (The 10-Second Summary)

**Model Context Protocol (MCP) enables Cursor to connect to external tools and data sources.**

Instead of explaining your project structure repeatedly, integrate directly with your tools. Write MCP servers in **any language** – Python, JavaScript, Go, etc.

| Without MCP | With MCP |
|-------------|----------|
| You describe your database schema to Agent | Agent queries database directly |
| You copy-paste error logs | Agent reads logs from your monitoring system |
| You explain your API structure | Agent calls your API directly |

> *"Write MCP servers in any language that can print to stdout or serve an HTTP endpoint – Python, JavaScript, Go, etc."*

---

## Why Use MCP?

| Benefit | Example |
|---------|---------|
| **Direct integration** | Agent queries your database instead of you describing schemas |
| **Any language** | Write servers in Python, JS, Go, Rust, etc. |
| **Reusable** | Share MCP servers across your team |
| **Rich interactions** | Return images, structured data, even interactive UI |

**Browse official plugins** in the Cursor Marketplace.  
**For community MCP servers**, browse `cursor.directory`.

---

## How MCP Works

MCP servers expose **capabilities** (tools, prompts, resources) through the protocol, connecting Cursor to external tools or data sources.

### Supported Transports (3 Ways to Connect)

| Transport | Execution Environment | Best for |
|-----------|----------------------|----------|
| **STDIO (Local)** | Cursor manages the process | Local tools, command-line servers |
| **SSE (Remote)** | Deploy as a server | Multiple users, remote access |
| **Streamable HTTP (Remote)** | Deploy as a server | Multiple users, modern APIs |

---

## Supported MCP Capabilities

Cursor supports these MCP protocol capabilities:

| Feature | What it does |
|---------|--------------|
| **Tools** | Functions the AI model can execute (most common) |
| **Prompts** | Templated messages and workflows for users |
| **Resources** | Structured data sources that can be read and referenced |
| **Roots** | Server-initiated inquiries into URI or filesystem boundaries |
| **Elicitation** | Server requests for additional info from users |
| **Apps (extension)** | Interactive UI views returned by MCP tools |

### MCP Apps (Special Feature)

Cursor supports the **MCP App extension** – MCP tools can return interactive UI along with standard tool output.

> *"MCP Apps follow progressive enhancement. If a host cannot render app UI, the same tool still works through normal MCP responses."*

---

## Installing MCP Servers

### One-Click Installation

Browse the **Cursor Marketplace** for official plugins with one-click install. Click "Add to Cursor" on a marketplace entry to install and authenticate with OAuth.

### Manual Configuration with `mcp.json`

Configure custom MCP servers with a JSON file.

---

## Configuration File Locations

| Location | Scope |
|----------|-------|
| `.cursor/mcp.json` | Project-level (in your repository) |
| `~/.cursor/mcp.json` | User-level (global, all projects) |

---

## STDIO Server Configuration (Local)

For local command-line servers:

```json
{
  "mcpServers": {
    "my-python-server": {
      "type": "stdio",
      "command": "python",
      "args": ["mcp-server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      },
      "envFile": ".env"
    }
  }
}
```

### STDIO Configuration Fields:

| Field | Required | Description |
|-------|----------|-------------|
| `type` | Yes | Must be `"stdio"` |
| `command` | Yes | Command to start server (e.g., `"python"`, `"node"`, `"docker"`) |
| `args` | No | Array of arguments (e.g., `["server.py"]`) |
| `env` | No | Environment variables for the server |
| `envFile` | No | Path to `.env` file to load variables |

> *"The `envFile` option is only available for STDIO servers. Remote servers (HTTP/SSE) do not support `envFile`."*

---

## Remote Server Configuration (HTTP/SSE)

For remote servers (deployed as web services):

```json
{
  "mcpServers": {
    "remote-tool": {
      "url": "https://api.example.com/mcp"
    }
  }
}
```

---

## Static OAuth for Remote Servers

For MCP servers that use OAuth, you can provide static credentials. Use this when:

- The MCP provider gives you a fixed Client ID
- The provider requires whitelisting a redirect URL (e.g., Figma, Linear)
- The provider doesn't support OAuth Dynamic Client Registration

### Example:

```json
{
  "mcpServers": {
    "oauth-server": {
      "url": "https://api.example.com/mcp",
      "auth": {
        "CLIENT_ID": "your-oauth-client-id",
        "CLIENT_SECRET": "your-client-secret",
        "scopes": ["read", "write"]
      }
    }
  }
}
```

### Static Redirect URL:

Cursor uses a **fixed OAuth redirect URL** for all MCP servers:

```
cursor://anysphere.cursor-mcp/oauth/callback
```

> *"When configuring the MCP provider's OAuth app, register this URL as an allowed redirect URL."*

### Combining with Interpolation:

```json
{
  "mcpServers": {
    "oauth-server": {
      "url": "https://api.example.com/mcp",
      "auth": {
        "CLIENT_ID": "${env:MCP_CLIENT_ID}",
        "CLIENT_SECRET": "${env:MCP_CLIENT_SECRET}"
      }
    }
  }
}
```

---

## Config Interpolation (Variables)

Use variables in `mcp.json` values. Supported syntax:

| Variable | What it resolves to |
|----------|---------------------|
| `${env:NAME}` | Environment variable |
| `${userHome}` | Your home folder path |
| `${workspaceFolder}` | Project root (folder containing `.cursor/mcp.json`) |
| `${workspaceFolderBasename}` | Name of the project root |
| `${pathSeparator}` or `${/}` | OS path separator (`/` or `\`) |

### Example:

```json
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

---

## Using MCP in Chat

Agent **automatically uses MCP tools** listed under "Available Tools" when relevant. This includes Plan Mode.

**Ask for a specific tool by name** or just describe what you need.

### Tool Approval (Security)

Agent asks for approval before using MCP tools by default. Click the arrow next to the tool name to see arguments.

**Enable auto-run** for Agent to use MCP tools without asking (works like terminal commands). Read more about auto-run settings.

### Pre-configuring auto-run:

To pre-configure which MCP tools can auto-run without using the settings UI, add them to `~/.cursor/permissions.json`.

---

## Tool Response

Cursor shows the response in chat with **expandable views** of arguments and responses:

```
Calling list_schemas → Result: [{'schema_name': 'information_schema'}, ...]
```

---

## Images as Context 🖼️

MCP servers can return images – screenshots, diagrams, etc. Return them as **base64 encoded strings**:

```javascript
const RED_CIRCLE_BASE64 = "/9j/4AAQSKZ..."; // full base64

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      }
    ]
  };
});
```

> *"Cursor attaches returned images to the chat. If the model supports images, it analyzes them."*

---

## Using the Extension API (For Developers)

For programmatic MCP server registration, Cursor provides an extension API that allows dynamic configuration without modifying `mcp.json` files. Useful for enterprise environments and automated setup workflows.

**API method:** `vscode.cursor.mcp.registerServer()`

---

## Security Considerations ⚠️

When installing MCP servers, follow these security practices:

| Practice | Why |
|----------|-----|
| **Verify the source** | Only install from trusted developers and repositories |
| **Review permissions** | Check what data and APIs the server will access |
| **Limit API keys** | Use restricted API keys with minimal required permissions |
| **Audit code** | For critical integrations, review the server's source code |

> *"Remember that MCP servers can access external services and execute code on your behalf. Always understand what a server does before installation."*

---

## Real-World Examples

| Integration | What it does |
|-------------|--------------|
| **Xcode integration** | Connect Cursor to Xcode 26.3+ for builds, tests, SwiftUI previews, Apple documentation search |
| **Web Development guide** | Integrate Linear, Figma, and browser tools into your development workflow |

---

## Common Beginner Questions

### Q: What's the point of MCP servers?
**A:** They let Cursor directly access external data and tools – databases, APIs, local files, etc.

### Q: How do I debug MCP server issues?
**A:** Check the Cursor output panel for MCP-related logs.

### Q: Can I temporarily disable an MCP server?
**A:** Yes – toggle it off in Cursor Settings under MCP configuration.

### Q: What happens if an MCP server crashes or times out?
**A:** The tool call will fail. Cursor may retry depending on configuration.

### Q: How do I update an MCP server?
**A:** Depends on the server. For local STDIO servers, update the code. For remote servers, the provider updates it.

### Q: Can I use MCP servers with sensitive data?
**A:** Yes, but take precautions – use local STDIO servers when possible, limit API keys, audit code.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What is MCP?** | Protocol to connect Cursor to external tools and data sources |
| **Transports** | STDIO (local), SSE (remote), Streamable HTTP (remote) |
| **Configuration** | `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (user) |
| **Supported capabilities** | Tools, Prompts, Resources, Roots, Elicitation, Apps |
| **Languages** | Any – Python, JavaScript, Go, Rust, etc. |
| **Security** | Approval required by default, configurable auto-run |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is MCP?** | A way for Cursor to connect directly to external tools |
| **Why use it?** | Agent can query databases, call APIs, read from systems directly |
| **Do I need to use MCP?** | Not as a beginner – it's for advanced integrations |
| **What languages can I use?** | Any language that can print to stdout or serve HTTP |
| **Is it secure?** | Approval required by default – you control what runs |
| **Where do I find MCP servers?** | Cursor Marketplace or cursor.directory |

---

## The Bottom Line

**MCP is the "USB-C" of AI integrations – a universal protocol for connecting Cursor to anything.**

**Think of it as:**
- **Without MCP** = Describing your tools to the AI 🗣️
- **With MCP** = Plugging your tools directly into the AI 🔌

**For beginners:** You don't need to build MCP servers. But you might enjoy **installing** them from the marketplace. Look for integrations with your favorite tools (GitHub, Slack, databases, etc.).

**For advanced users:** MCP is incredibly powerful. Write servers in any language. Connect to your internal APIs. Let the Agent query your data warehouse directly. The possibilities are endless.

**Security reminder:** MCP servers can execute code on your behalf. Only install from trusted sources. Use approval mode by default.

Would you like me to explain how to build a simple MCP server, or move on to another document?