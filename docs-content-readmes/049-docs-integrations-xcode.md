This is the **Xcode Integration** documentation – it explains how Cursor can directly interact with **Xcode 26.3+** projects through a built-in MCP server.

Think of this as **Cursor talking directly to Xcode** – your agent can read files, run builds, execute tests, capture SwiftUI previews, and search Apple's documentation, all without leaving Cursor.

Let me break this down for a beginner.

---

## What Is the Xcode Integration? (The 10-Second Summary)

**Xcode 26.3+ exposes a built-in MCP server that gives Cursor direct access to your Xcode projects.** Cursor's agent can read and edit files, trigger builds, run tests, capture SwiftUI previews, and search Apple's documentation – all without leaving your editor.

| Without Xcode Integration | With Xcode Integration |
|--------------------------|----------------------|
| Manually switch between Cursor and Xcode | Cursor talks directly to Xcode |
| Build/test manually in Xcode | Agent can trigger builds and tests |
| Can't see SwiftUI previews in Cursor | Agent captures previews as images |

> *"This works through `xcrun mcpbridge`, a binary Apple ships with Xcode that translates MCP protocol messages into Xcode's internal XPC layer."*

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **macOS** | Required (Xcode only runs on Mac) |
| **Xcode 26.3 or later** | Must be installed |
| **Paid Cursor plan** | Active subscription |
| **Xcode project open** | Xcode must be running with your project open |

---

## Step 1: Enable MCP in Xcode

Before Cursor can connect, turn on Xcode's MCP bridge:

| Step | Action |
|------|--------|
| **1** | Open Xcode settings: **Xcode > Settings > Intelligence** |
| **2** | Under **Model Context Protocol**, toggle **Xcode Tools ON** |

---

## Step 2: Set Up Cursor (3 Ways)

Pick whichever method suits your workflow.

### Option 1: MCP Settings UI (Easiest)

| Step | Action |
|------|--------|
| 1 | Open **Cursor Settings > Features > MCP** |
| 2 | Click **Add New MCP Server** |
| 3 | Set transport to **stdio** |
| 4 | Name it **xcode-tools** |
| 5 | Enter command: `xcrun mcpbridge` |

### Option 2: `mcp.json` (Manual Config)

Add an entry to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "xcode-tools": {
      "command": "xcrun",
      "args": ["mcpbridge"]
    }
  }
}
```

### Option 3: Cursor CLI (Terminal)

```bash
agent mcp add xcode-tools -- xcrun mcpbridge
```

> *"The CLI shares the same MCP config as the editor, so the server appears in both."*

---

## Available Tools (20 MCP Tools)

Xcode exposes **20 MCP tools** across five categories:

### 1. File Operations

| Tool | What it does |
|------|--------------|
| `XcodeRead` | Read file contents (up to 600 lines per call) |
| `XcodeWrite` | Create or overwrite files |
| `XcodeUpdate` | Apply targeted edits to existing files |
| `XcodeGrep` | Search file contents with regex |
| `XcodeGlob` | Find files by pattern |
| `XcodeLS` | List directory contents |
| `XcodeMakeDir` | Create directories |
| `XcodeRM` | Remove files or directories |
| `XcodeMV` | Move or rename files |

### 2. Build and Test

| Tool | What it does |
|------|--------------|
| `BuildProject` | Build the active scheme |
| `GetBuildLog` | Retrieve build logs (filterable by severity, regex, or file glob) |
| `RunAllTests` | Run the full test suite |
| `RunSomeTests` | Run specific test classes or methods |
| `GetTestList` | List available tests |

### 3. Diagnostics

| Tool | What it does |
|------|--------------|
| `XcodeListNavigatorIssues` | Show warnings and errors from Issue Navigator |
| `XcodeRefreshCodeIssuesInFile` | Re-check a file for code issues |

### 4. Intelligence

| Tool | What it does |
|------|--------------|
| `RenderPreview` | Capture a screenshot of a SwiftUI preview |
| `DocumentationSearch` | Semantic search across Apple's documentation and WWDC transcripts |
| `ExecuteSnippet` | Run a Swift code snippet |

### 5. Workspace

| Tool | What it does |
|------|--------------|
| `XcodeListWindows` | List open Xcode windows and tabs |

---

## Example Workflow (Cursor + Xcode)

A typical workflow looks like this:

| Step | What happens |
|------|--------------|
| 1 | Open your project in **both Cursor and Xcode** |
| 2 | Ask Cursor's agent to add a feature or fix a bug |
| 3 | Agent uses `XcodeRead` and `XcodeGrep` to understand your code |
| 4 | Agent edits files with `XcodeWrite` or `XcodeUpdate` |
| 5 | Agent runs `BuildProject` to check for errors, reads results with `GetBuildLog` |
| 6 | Agent runs tests with `RunSomeTests` to verify the change |
| 7 | Agent captures a SwiftUI preview with `RenderPreview` to confirm the UI |

> *"You stay in Cursor the whole time. Xcode handles compilation, testing, and previews in the background."*

---

## Cursor CLI with Xcode

The Cursor CLI also works with Xcode's MCP tools – useful for headless workflows, CI pipelines, or terminal-first developers.

```bash
agent "Add unit tests for the NetworkManager class"
```

> *"The agent picks up the `xcode-tools` MCP server from your config and uses the same tools available in the editor."*

---

## Troubleshooting

| Issue | What to check |
|-------|---------------|
| **Cursor can't find xcode-tools server** | Verify MCP is enabled in Xcode Settings → Intelligence |
| **Tools show errors about missing identifiers** | Check that Xcode has your project open |
| **Build or test tools time out** | Large projects may take time; ensure Xcode isn't busy |
| **MCP toggle missing in Xcode settings** | You need Xcode 26.3 or later |
| **`xcrun: error: unable to find utility 'mcpbridge'`** | Xcode version is too old (need 26.3+) |

---

## Related Documentation

| Topic | What it covers |
|-------|----------------|
| **MCP overview** | Complete MCP guide with setup, configuration, authentication |
| **iOS & macOS (Swift)** | Swift development workflow with Cursor, Sweetpad, and Xcode Build Server |
| **Cursor CLI** | Use Cursor's agent from the terminal, manage MCP servers |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Cursor agent interacts directly with Xcode |
| **Requirement** | macOS + Xcode 26.3+ + paid Cursor plan |
| **Enable in Xcode** | Settings → Intelligence → Toggle Xcode Tools |
| **Setup in Cursor** | MCP settings UI, mcp.json, or CLI |
| **Number of tools** | 20 MCP tools |
| **Key capabilities** | Read/write files, build, test, preview SwiftUI, search docs |
| **Workflow** | Stay in Cursor; Xcode handles compilation/testing |

---

## Common Beginner Questions

### Q: Do I need to stop using Xcode?
**A:** No – you keep Xcode open. Cursor's agent talks to Xcode while you stay in Cursor.

### Q: Does this work with older Xcode versions?
**A:** No – you need **Xcode 26.3 or later**.

### Q: Does this work on Windows or Linux?
**A:** No – Xcode only runs on macOS.

### Q: Can the agent run SwiftUI previews?
**A:** Yes – `RenderPreview` captures screenshots of SwiftUI previews.

### Q: Can the agent search Apple's documentation?
**A:** Yes – `DocumentationSearch` provides semantic search across Apple docs and WWDC transcripts.

### Q: Do I need to configure anything else?
**A:** Just enable MCP in Xcode and add the server in Cursor. Xcode must be running with your project open.

---

## The Bottom Line

**The Xcode integration lets Cursor's agent work directly with your Xcode projects – reading files, running builds, executing tests, and capturing SwiftUI previews.**

**Think of it as:**
- **Without integration** = You manually build, test, and preview in Xcode 🖱️
- **With integration** = Agent does it all while you stay in Cursor 🤖

**For iOS/macOS developers:** This is a game-changer. You can:
1. Stay in Cursor for all your coding
2. Let the agent trigger builds and tests
3. See SwiftUI previews without switching to Xcode
4. Search Apple's documentation directly from Cursor

**The setup is simple:**
1. Enable MCP in Xcode (Settings → Intelligence)
2. Add `xcode-tools` MCP server in Cursor
3. Keep Xcode open with your project
4. Start coding in Cursor – the agent does the rest

