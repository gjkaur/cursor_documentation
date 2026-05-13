This is the **My Machines** documentation – it explains how to run Cloud Agents on **your own machines** (laptop, devbox, remote VM) instead of on Cursor's cloud infrastructure.

Think of My Machines as **bringing the cloud to your hardware** – you get all the power of Cloud Agents (parallel execution, remote desktop, artifacts), but the work happens on your computer with your network, your secrets, and your build cache.

Let me break this down for a beginner.

---

## What Is My Machines? (The 10-Second Summary)

**My Machines lets you run Cloud Agents on a machine you already use: your laptop, a devbox, or a remote VM.** It is the fastest way to give Cloud Agents access to your local repo, dependencies, build cache, and private network.

| Cursor-Hosted Cloud Agents | My Machines |
|---------------------------|-------------|
| Run on Cursor's computers | Run on YOUR computer |
| Need to set up environment | Use your existing setup |
| Don't have your private network access | Can access your internal services |
| Fresh build cache every time | Keep your build cache |

> *"A worker on your machine opens an outbound connection to Cursor. The agent loop runs in Cursor's cloud, but terminal commands, file edits, browser actions, and other tool calls execute on your machine. No inbound ports or firewall changes are required."*

---

## Why Use My Machines?

| Use Case | Why |
|----------|-----|
| **Use a devbox or remote workstation** | Already has your repo and tools set up |
| **Run against private network services** | Agents can access internal APIs and databases |
| **Keep build caches and secrets on your machine** | Faster builds, no need to re-enter secrets |
| **Try self-hosted Cloud Agents quickly** | Fastest way to get started |

---

## How It Works

```
Your Machine                     Cursor Cloud
     │                                │
     │──── outbound connection ──────→│
     │                                │
     │←─── agent loop runs here ──────│
     │                                │
     │──── tool calls execute here ──→│ (terminal, files, browser)
     │                                │
```

**Key points:**
- Worker opens an **outbound connection** to Cursor (no inbound ports needed)
- Agent **logic runs in Cursor's cloud**
- **Tool calls** (terminal commands, file edits, browser actions) run on YOUR machine
- **No firewall changes** required

---

## Quickstart (4 Steps)

### Step 1: Install the CLI

**macOS, Linux, and WSL2:**
```bash
curl https://cursor.com/install -fs | bash
```

**Windows PowerShell:**
```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

**Verify installation:**
```bash
agent --version
```

### Step 2: Sign In

For a personal machine, browser login is the easiest:

```bash
agent login
```

### Step 3: Start the Worker

```bash
agent worker start
```

> *"Keep this process running while you use the machine. By default, a My Machines worker is long-lived: it stays connected until you stop it and can be reused for future Cloud Agent sessions."*

### Step 4: Run an Agent

1. Go to `cursor.com/agents`
2. The machine should show up in the environment dropdown
3. Send a task

**That's it!** Your machine is now ready to run Cloud Agents.

---

## Common Options

### Name the Machine

Use a friendly name when you have multiple machines for the same repo:

```bash
agent worker start --name "my-devbox"
```

### Run from a Different Repo Directory

```bash
agent worker start --worker-dir /path/to/repo
```

### Use an API Key (For Shared Devboxes or Automation)

```bash
agent worker start --api-key "your-api-key"
```

### Use a User-Scoped Token (For Self-Managed Per-User Workers)

```bash
agent worker start --auth-token "your-user-scoped-token"
```

**For long-lived workers in Kubernetes:**
```bash
agent worker start --auth-token-file /var/run/cursor/token
```

> *"This is useful in Kubernetes because environment variables from Secrets are fixed when the pod starts. Secret volumes update while the pod runs, while mounted token paths can be live updated within the pod."*

---

## Triggering from Chat Surfaces (Slack, GitHub, Linear)

Use `worker=` or `machine=` when you want Slack, GitHub, or Linear requests to run on one of your named machines.

### Start the machine with a name:

```bash
agent worker start --name "my-devbox"
```

### Then trigger from:

| Platform | Syntax |
|----------|--------|
| **Slack** | `@Cursor worker=my-devbox fix the flaky test` |
| **GitHub** | `@cursoragent worker=my-devbox fix the flaky test` |
| **Linear** | Add `worker=my-devbox` to the issue body |

> *"You must be a trusted repo commenter, and the target machine must belong to the Cursor user linked to your GitHub account."*

---

## How Cursor Picks Your Machine

A `worker=<name>` request runs on a machine **only when all three are true**:

| Condition | Description |
|-----------|-------------|
| **1** | The machine belongs to the Cursor user who triggered the request |
| **2** | The machine's `--name` matches the requested `<name>` |
| **3** | The machine's registered repo matches the trigger's target repo |

### Where the target repo comes from:

| Surface | Source |
|---------|--------|
| **Slack** | `repo=` in message → channel default → user default → team default |
| **Linear** | `[repo=]` in issue → issue labels → project labels → dashboard default |
| **GitHub** | Repo of the issue/PR where `@cursoragent` was mentioned |

> *"Each machine's registered repo comes from the git remote in the directory where you started the worker. To serve more than one repo, start a worker in each repo's checkout."*

---

## When a Worker Request Can't Run

If you have a machine with that name but it's registered for a **different repo**, Cursor rejects the request:

> *"worker=<name> is registered on your machine but for a different repository. Start the worker in a checkout of the target repo first."*

**The error appears as:**
- Ephemeral reply in Slack
- Agent activity error in Linear
- `@cursoragent` reply on GitHub

> *"The behavior is intentional: a request for repo A should never run on a machine checkout for repo B."*

---

## Artifacts (Screenshots, Videos, Logs)

> *"Artifact behavior is identical on self-hosted workers and Cursor-hosted agents."*

| What happens |
|--------------|
| Agent produces artifact inside the worker |
| Worker uploads artifact to Cursor-managed storage over HTTPS |
| Downstream (PR embeds, dashboard previews, notifications) handled by Cursor |

### Disabling Artifacts:

To disable artifact uploads, block outbound traffic to:
```
cloud-agent-artifacts.s3.us-east-1.amazonaws.com
```

> *"The agent session keeps working; artifacts produced during the session fail to upload."*

---

## Networking Requirements

Workers need **outbound HTTPS access** to:

| Host | Purpose |
|------|---------|
| `api2.cursor.sh` and `api2direct.cursor.sh` | Agent session |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` | Artifact uploads |

> *"No inbound ports, public IPs, or VPN tunnels are required. If you use a proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment."*

---

## Failure Modes

| If you block... | Effect |
|-----------------|--------|
| `api2.cursor.sh` or `api2direct.cursor.sh` | Worker can't start or continue agent session |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` | Artifact uploads fail (agent session keeps working) |
| An outbound host a specific tool needs | Only that tool/integration fails |

---

## MCP Servers on My Machines

MCP servers are routed by transport type:

| Transport | Runs on | Use case |
|-----------|---------|----------|
| **Command (stdio)** | Your machine | Can reach private networks, internal APIs, local services |
| **HTTP/SSE (url)** | Cursor backend | Cursor handles OAuth, session caching, auth |

> *"If your MCP server needs to reach endpoints on your private network, use the command (stdio) transport. The process runs directly on your machine and shares its network."*

---

## Troubleshooting

Run a preflight debug report:

```bash
agent worker start --debug
```

This checks:
- Authentication
- Privacy routing
- Repo labels
- Whether Cursor can see matching workers

---

## Related Pages

- **Self-Hosted Pool** – For org-wide worker fleets
- **Cloud Agent security and network**
- **Service accounts**

---

## Common Beginner Questions

### Q: Do I need My Machines as a beginner?
**A:** No. You can use Cursor-hosted Cloud Agents. My Machines is for advanced users who want agents to run on their own infrastructure.

### Q: Does My Machines work on Windows?
**A:** Yes – Windows PowerShell is supported. WSL2 is also supported.

### Q: Do I need to open firewall ports?
**A:** No – workers open an outbound connection. No inbound ports required.

### Q: Can I run multiple workers on the same machine?
**A:** Yes – start workers in different repo directories with different names.

### Q: What happens if my machine goes offline?
**A:** The agent session will fail. Workers need to stay running.

### Q: Can I use My Machines with Slack/GitHub/Linear?
**A:** Yes – use `worker=` or `machine=` in your commands.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Run Cloud Agents on your own machines |
| **Install CLI** | `curl https://cursor.com/install -fs \| bash` |
| **Start worker** | `agent worker start` |
| **Name a machine** | `agent worker start --name "my-name"` |
| **Trigger from Slack** | `@Cursor worker=my-name fix the test` |
| **Networking** | Outbound HTTPS only, no inbound ports |
| **Artifacts** | Uploaded to Cursor storage |
| **MCP stdio** | Runs on your machine (can access private network) |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is My Machines?** | Run Cloud Agents on your own computer |
| **Why use it?** | Access private network, keep build cache, use existing setup |
| **Do I need to open ports?** | No – outbound connection only |
| **How do I start?** | Install CLI → `agent login` → `agent worker start` |
| **Can I name my machine?** | Yes – `--name "my-devbox"` |
| **Can I trigger from Slack?** | Yes – `@Cursor worker=my-name` |

---

## The Bottom Line

**My Machines is the bridge between Cloud Agents and your local infrastructure.**

**Think of it as:**
- **Cursor-hosted agents** = Rented computers in the cloud 🏢
- **My Machines** = Your own computer working for you in the cloud 🏠

**For beginners:** You don't need this. Use Cursor-hosted Cloud Agents first.

**For advanced users:** My Machines is powerful when you need:
- Access to private networks (internal APIs, databases)
- Your existing build cache (faster builds)
- Your secrets already on the machine
- To test Cloud Agents without setting up new environments

**The best part:** No firewall changes needed. The worker opens an outbound connection, so you don't need to configure inbound ports or VPNs.

Would you like me to explain any specific part of My Machines in more detail?