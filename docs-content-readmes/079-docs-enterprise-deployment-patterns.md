This is the **Deployment Patterns** documentation – it explains how to deploy the Cursor editor and CLI tools to developer machines in your organization.

Think of this as the **IT deployment guide** – covering MDM, Group Policy, configuration profiles, silent installers, and policy enforcement across Windows, macOS, and Linux.

Let me break this down.

---

## Overview

**This guide covers how to deploy the Cursor editor and CLI tools to developer machines in your organization.** Most organizations deploy both the editor (for daily development work) and the CLI (for automation, CI/CD, and scripting).

---

## Editor Deployment with MDM

Deploy the Cursor editor and agent to user workstations and enforce policies through **Mobile Device Management (MDM)** systems.

### How It Works

| Step | Action |
|------|--------|
| 1 | Your IT team packages the Cursor application for deployment |
| 2 | Push to user machines via MDM (Jamf, Intune, Kandji, etc.) |
| 3 | Users receive Cursor on their primary development machines |

**MDM allows you to enforce policies for Cursor** – allowed team IDs, extensions, workspace trust, auto-updates, and new versions.

---

## MDM Configuration

Cursor supports policies on:

| Platform | Method |
|----------|--------|
| **Windows** | Group Policy |
| **macOS** | Configuration profiles |
| **Linux** | JSON policy files (version 2.0+) |

### Available Policies

| Policy | Description | Cursor setting |
|--------|-------------|----------------|
| `AllowedExtensions` | Controls which extensions can be installed | `extensions.allowed` |
| `AllowedTeamId` | Controls which team IDs are allowed to log in. Users with unauthorized IDs are forcefully logged out. | `cursorAuth.allowedTeamId` |
| `ExtensionGalleryServiceUrl` | Configures a custom extension marketplace URL | `extensions.gallery.serviceUrl` |
| `NetworkDisableHttp2` | Disables HTTP/2, uses HTTP/1.1 instead | `cursor.general.disableHttp2` |
| `UpdateMode` | Controls automatic update behavior. Set to `none` to disable updates. | `update.mode` |
| `WorkspaceTrustEnabled` | Controls whether Workspace Trust is enabled | `security.workspace.trust.enabled` |

---

## Managing Auto-Run Allowlists with MDM

Deploy Cursor's permissions file through MDM to manage which terminal commands and MCP tools auto-run without prompting.

**File path:** `~/.cursor/permissions.json`

### File Format

```json
{
  "terminalAllowlist": ["npm install", "pnpm test", "python -m pytest"],
  "mcpAllowlist": ["linear:*", "github:create_pull_request", "*:search"]
}
```

### `mcpAllowlist` Entry Syntax

| Entry | Meaning |
|-------|---------|
| `server:tool` | One specific tool on one specific MCP server |
| `server:*` | All tools from one MCP server |
| `*:tool` | One tool name from any MCP server |
| `*:*` | All MCP tools |

### Allowlist Precedence (Higher priority replaces lower)

| Priority | Source |
|----------|--------|
| 1 | Team dashboard or other admin-controlled settings |
| 2 | Managed `~/.cursor/permissions.json` |
| 3 | Editor settings and inline "Add to allowlist" |

> *"Higher-priority sources replace lower-priority allowlists for that category. They do not merge."*

> *"Cursor watches `permissions.json`, so updates apply automatically without requiring a restart."*

---

## Windows Group Policy

Cursor has support for Windows Registry-based Group Policy.

### To Add a Policy

| Step | Action |
|------|--------|
| 1 | Copy the Policy ADMX and ADML files from `AppData\Local\Programs\cursor\policies` |
| 2 | Paste ADMX into `C:\Windows\PolicyDefinitions`, ADML into `C:\Windows\PolicyDefinitions\<your-locale>\` |
| 3 | Restart Local Group Policy Editor |
| 4 | Set policy values in Local Group Policy Editor |

> *"Policies can be set at both Computer level and User level. If both are set, Computer level takes precedence."*

### Important

> *"When a policy value is set, it overrides the Cursor setting value configured at any level (default, user, workspace, etc.). This is a global override that prevents users from changing these settings."*

> *"In Cursor 2.1, we renamed the category name to Cursor in the Group Policy Editor. Old keys still work."*

---

## Windows Installer

The Windows installer is based on **Inno Setup**.

### Fresh Installation (Silent)

```bash
CursorSetup-x64-2.0.exe /SILENT /VERYSILENT /SUPPRESSMSGBOXES /NORESTART /CLOSEAPP
```

### Updating Existing Installation

Create a temporary flag file and pass its path:

```bash
CursorSetup-x64-2.0.exe /VERYSILENT /update="%TEMP%\cursor-update.flag" /CLOSEAPP
```

> *"Installers pre-2.0 may incorrectly not respect `/SILENT` flags."*

---

## macOS Configuration Profiles

Configuration profiles manage settings on macOS devices. A profile is an XML file with key/value pairs for policies.

### Bundle IDs per Channel

| Channel | Bundle ID |
|---------|-----------|
| **Production** | `com.todesktop.230313mz14w4u92` |
| **Nightly** | `co.anysphere.cursor.nightly` |

> *"For most enterprise deployments, use the production bundle ID."*

### Example Policy Values

**AllowedExtensions (string policy):**
```xml
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

**AllowedTeamId (string policy):**
```xml
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**NetworkDisableHttp2 (boolean policy):**
```xml
<key>NetworkDisableHttp2</key>
<true/>
```

**WorkspaceTrustEnabled (boolean policy):**
```xml
<key>WorkspaceTrustEnabled</key>
<false/>
```

**UpdateMode (string policy):**
```xml
<key>UpdateMode</key>
<string>none</string>
```

**ExtensionGalleryServiceUrl (string policy):**
```xml
<key>ExtensionGalleryServiceUrl</key>
<string>https://marketplace.example.com</string>
```

### UpdateMode Values

| Value | Behavior |
|-------|----------|
| `none` | Disables all automatic updates |
| `manual` | Users can manually check for updates |
| `start` | Check for updates when Cursor starts |
| `default` | Same as `start` |
| `silentlyApplyOnQuit` | Download updates in background, apply when Cursor quits |

### Deploying with MDM Solutions

| MDM | Method |
|-----|--------|
| **Jamf** | Upload as custom configuration profile |
| **Kandji** | Add as custom profile in Library |
| **Microsoft Intune** | Deploy as custom profile with correct payload domain |

### Reference Configuration File

Located at:
- **Production:** `/Applications/Cursor.app/Contents/Resources/app/policies/com.todesktop.230313m...`
- **Nightly:** `/Applications/Cursor Nightly.app/Contents/Resources/app/policies/co.anysphere...`

### Important Security Considerations

| Consideration |
|---------------|
| The provided `.mobileconfig` file initializes **all** policies available in that version |
| Delete any policies not needed to avoid unintentionally restrictive defaults |
| If you don't edit or remove a policy, it will be enforced with its default value |
| Policy values override all user and workspace settings globally |

---

## Linux Policy File

Linux distributions don't have a standardized enterprise policy system. Cursor reads policies from a JSON file.

> *"Linux policy file support is available in Cursor version 2.0 and later."*

**File location:** `~/.cursor/policy.json`

### Example `policy.json`

```json
{
  "AllowedExtensions": "{\"anysphere\": true, \"github\": true}",
  "AllowedTeamId": "1,3,7",
  "WorkspaceTrustEnabled": true
}
```

> *"The `AllowedExtensions` value must be a JSON string (escaped quotes), not a JSON object."*

### Deploying Policies

| Method |
|--------|
| Ansible, Puppet, or Chef for automated deployment |
| NFS or shared network storage |
| Package managers with post-install scripts |
| Container base images |

> *"Changes to the policy file take effect when Cursor restarts. The file is monitored for changes, so updates propagate automatically."*

> *"If the policy file doesn't exist, Cursor runs without policy restrictions."*

---

## Automatic Updates for Non-Admin Users (macOS)

Due to Electron framework limitations, Cursor updates require **administrator privileges** on macOS.

### Recommended Approaches

| Approach | Description |
|----------|-------------|
| **MDM deployment** | Use Jamf, Kandji, Intune to deploy updates centrally |
| **Automated deployment tools** | Consider Installomator for scripted updates |
| **Disable update prompts** | Set `UpdateMode` policy to `none` |

> *"For organizations with non-admin users, the most reliable approach is to manage Cursor updates through your existing software deployment pipeline and disable automatic updates via MDM policy."*

---

## CLI Deployment

Run Cursor agents as a headless CLI tool on your infrastructure.

### How It Works

| Step | Action |
|------|--------|
| 1 | Deploy the CLI to your environment (on-prem, cloud, Kubernetes, CI/CD) |
| 2 | CLI is scripted or run in the background |
| 3 | CLI can access whatever the user can access from their machine (VPN, internal APIs, private package registries) |

### Installation

```bash
# macOS, Linux, WSL
curl https://cursor.com/install -fsS | bash

# Windows PowerShell
irm 'https://cursor.com/install?win32=true' | iex

# Set API key for scripts
export CURSOR_API_KEY=your_api_key_here
agent -p "Analyze this code"
```

### GitHub Actions Integration

Cursor CLI works in GitHub Actions and other CI systems.

---

## Cursor CLI Considerations

Whether running in the desktop app or as a standalone CLI, Cursor agents have the **same security controls**:

| Feature | Available |
|---------|-----------|
| Privacy Mode | ✅ |
| Hooks | ✅ |
| Model access controls | ✅ |
| Audit logging | ✅ |
| Usage tracking | ✅ |

| Requirement | Needed |
|-------------|--------|
| Network access to Cursor services | ✅ |
| Send code to LLMs (with Privacy Mode) | ✅ |
| Appropriate authentication | ✅ |

> *"The CLI is the same agent with a different interface."*

---

## Network Considerations

User machines need access to the following endpoints:

| Endpoint | Purpose |
|----------|---------|
| `*.cursor.sh` | Backend services and API endpoints |
| `*.cursor-cdn.com` | Application downloads and updates |
| `marketplace.cursorapi.com` | Extension marketplace |
| Third-party AI provider endpoints | OpenAI, Anthropic, Google, etc. |

> *"When using the `UpdateMode` policy set to `none`, you can restrict access to update endpoints while maintaining access to other services."*

> *"The Cursor editor inherits the machine's network configuration, including VPN access, internal service endpoints, and private package registries."*

---

## Minimum Versions

| Version difference | Action |
|-------------------|--------|
| Within 1 version of latest | Recommended |
| 3+ versions behind | Warning to update |
| 4+ versions behind | Error forcing update |

> *"For example, if the latest release is 1.7, users on 1.4 or below see a warning. Users on 1.3 or below see an error forcing them to update."*

---

## Troubleshooting

| Issue | Where to look |
|-------|---------------|
| Proxy configuration problems | Network Configuration |
| Model access issues | Model and Integration Management or team dashboard |
| Spending limit reached | Spend Limits |

---

## FAQ

### Does Cursor support policies on Linux?

**Yes**, starting with version 2.0. Linux uses a file-based policy system at `~/.cursor/policy.json`.

### Can I use environment variables in the policy file?

**No.** The policy file must be a valid JSON file with static values. Use configuration management tools to generate dynamically.

### What happens if the policy file has invalid JSON?

Cursor logs an error and runs without policy restrictions. Check main process logs for parsing errors.

### What is my team ID?

Find your team ID by clicking on your team name from `https://cursor.com/dashboard`.

---

## Quick Reference Card

| Platform | Policy Method | File/Location |
|----------|---------------|---------------|
| **Windows** | Group Policy | ADMX/ADML in PolicyDefinitions |
| **macOS** | Configuration Profile | `.mobileconfig` via MDM |
| **Linux** | JSON policy file | `~/.cursor/policy.json` |
| **Auto-run allowlists** | JSON file | `~/.cursor/permissions.json` |

| Policy | Purpose |
|--------|---------|
| `AllowedExtensions` | Control which extensions can be installed |
| `AllowedTeamId` | Prevent personal account logins |
| `UpdateMode` | Control automatic updates |
| `WorkspaceTrustEnabled` | Enable/disable workspace trust prompts |
| `NetworkDisableHttp2` | Fallback to HTTP/1.1 for proxies |

---

## The Bottom Line

**Deployment Patterns gives IT teams the tools to deploy and manage Cursor across their organization.**

**Key deployment methods:**
- **MDM** (Jamf, Intune, Kandji) – deploy editor and enforce policies
- **Group Policy** (Windows) – registry-based policy enforcement
- **Configuration Profiles** (macOS) – XML-based policies
- **JSON policy files** (Linux) – file-based policies
- **Silent installer** (Windows) – unattended installation
- **CLI deployment** – headless automation

**Key policies to enforce:**
1. **AllowedTeamId** – prevent personal account usage (most important)
2. **AllowedExtensions** – control which extensions can run
3. **UpdateMode** – manage automatic updates
4. **WorkspaceTrustEnabled** – security for untrusted workspaces
5. **NetworkDisableHttp2** – work around proxy limitations

**For IT teams:** The reference configuration files are included with Cursor. Delete unused policies to avoid unintentionally restrictive defaults.

Would you like me to explain any specific deployment pattern in more detail?