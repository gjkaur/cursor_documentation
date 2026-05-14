This is the **Self-Hosted Pool** documentation – it explains how Enterprise teams can run Cloud Agents on **company-managed infrastructure** instead of Cursor's cloud or individual developer machines.

Think of Self-Hosted Pool as **running a private fleet of agent workers** – like having your own data center of AI workers that your whole organization can use.

Let me break this down. (Note: This is an **Enterprise-only, advanced feature**.)

---

## What Is Self-Hosted Pool? (The 10-Second Summary)

**Self-Hosted Pool is for Enterprise teams that want Cloud Agents to run inside company-managed infrastructure.** Instead of each developer starting a worker on a personal machine, admins operate a pool of workers that can be assigned to agents across the organization.

| My Machines (Personal) | Self-Hosted Pool (Enterprise) |
|------------------------|-------------------------------|
| Individual developers | Entire team/organization |
| Personal authentication | Service account API keys |
| Run on your laptop | Run on company infrastructure |
| Manual start/stop | Fleet management, autoscaling |
| No labeling/routing | Labels to route work to right workers |

> *"Use a pool when you need: Centrally managed workers for a team or organization, Service account authentication instead of individual browser logins, Kubernetes or autoscaling, Labels that route work to the right environment, Enterprise controls around network access and monitoring."*

---

## How It Works

```
Your Infrastructure                    Cursor Cloud
     │                                      │
     │── outbound HTTPS connection ────────→│
     │                                      │
     │←──── agent loop runs here ───────────│
     │                                      │
     │──── tool calls execute here ────────→│ (terminal, files, browser)
     │                                      │
     │──── artifacts uploaded ─────────────→│
```

| Component | Where it runs |
|-----------|---------------|
| **Agent loop** (inference + planning) | Cursor's cloud |
| **Tool calls** (terminal, file edits, browser) | Your infrastructure |
| **Repos, build caches, secrets** | Your infrastructure |
| **Artifacts** (screenshots, videos) | Uploaded to Cursor |

> *"Workers only need outbound access. No inbound ports, public IPs, or VPN tunnels are required."*

---

## Limits

| Limit | Value |
|-------|-------|
| Workers per user | Up to 10 |
| Workers per team | Up to 50 |

> *"For larger company-wide deployments, contact us to discuss scaling."*

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **Cursor Enterprise plan** | Required |
| **Self-hosted settings configured** | By team admin in Cloud Agents dashboard |
| **Service account API key** | For pool worker authentication |
| **Worker machine** | With CLI, git, cloned repo, build tools, secrets, internal services |

### Admin Settings (Dashboard)

| Setting | Effect |
|---------|--------|
| **Allow Self-Hosted Agents** | Users can opt in to self-hosted runs |
| **Require Self-Hosted Agents** | Every Cloud Agent run routes to self-hosted workers |

---

## Install the CLI

**macOS, Linux, and WSL2:**
```bash
curl https://cursor.com/install -fs | bash
```

**Windows PowerShell:**
```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

**Verify:**
```bash
agent --version
```

---

## Authenticate Workers

Pool workers must authenticate with a **service account API key** (personal/user API keys won't work).

```bash
export CURSOR_API_KEY="your-service-account-api-key"
```

Or pass directly:
```bash
agent worker start --api-key "your-service-account-api-key"
```

> *"User, personal, team, and organization API keys can't start pool workers. Use personal or user API keys with personal workers on My Machines."*

---

## Start a Pool Worker

Run the worker from the git repo it should serve:

```bash
cd /path/to/repo
agent worker start --pool
```

### With Idle Release Timeout

For orchestrated environments, add timeout so the process exits cleanly after work completes:

```bash
agent worker start --pool --idle-release-timeout 600
```

> *"`--idle-release-timeout` keeps the worker alive for a window (in seconds) after a session ends to handle follow-up messages. If a follow-up arrives, the timer resets. Once the timeout fires, the CLI exits with code 0."*

---

## Pool Names (Routing)

Group pool workers under a name to route sessions to specific subsets (GPU machines, staging fleet, team's dedicated build boxes).

```bash
agent worker start --pool --pool-name gpu
```

| Without `--pool-name` | With `--pool-name` |
|-----------------------|---------------------|
| Joins "default" pool | Joins named pool (e.g., "gpu") |

### Set from environment:

```bash
export CURSOR_WORKER_POOL_NAME=gpu
agent worker start --pool
```

---

## Labels (Advanced Routing)

Add custom labels to workers for fine-grained routing:

```bash
agent worker start --pool \
  --label team=backend \
  --label env=production
```

**Reserved labels (cannot set manually):**
- `repo` – comes from worker directory's git remote
- `pool` – set by `--pool-name`

---

## MCP Servers on Self-Hosted Workers

| Transport | Runs on | Use case |
|-----------|---------|----------|
| **Command (stdio)** | Worker | Can reach private networks, internal APIs, services behind firewall |
| **HTTP/SSE (url)** | Cursor backend | Cursor handles OAuth, session caching, auth |

> *"If your MCP server needs to access private-network endpoints, use the command (stdio) transport. The process runs directly on the worker and shares its network."*

---

## Artifacts

> *"Artifact behavior is identical on self-hosted workers and Cursor-hosted agents."*

| What happens |
|--------------|
| Agent produces artifact inside worker |
| Worker uploads artifact to Cursor-managed storage over HTTPS |
| Downstream handled by Cursor's backend |

**To disable artifact uploads:** Block outbound traffic to:
```
cloud-agent-artifacts.s3.us-east-1.amazonaws.com
```

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
| `api2.cursor.sh` or `api2direct.cursor.sh` | Worker can't start or continue session |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` | Artifact uploads fail (session keeps working) |
| Host a tool needs | Only that tool fails |

---

## Kubernetes Support

> *"We provide a Helm chart and Kubernetes operator for managing worker pools at scale."*

See the Kubernetes deployment guide for setup instructions.

---

## Fleet Management API

For non-Kubernetes environments, use the fleet management API to monitor utilization and build autoscaling.

### List Workers

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers?status=idle&limit=50" \
  --u "$CURSOR_API_KEY:"
```

### Get Summary (for Autoscaling)

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  --u "$CURSOR_API_KEY:"
```

Returns connected and in-use counts. Use to trigger scaling:

```javascript
const summary = await response.json();
const team = summary.teamSummary;
if (team && team.totalConnected > 0) {
  const utilization = team.inUse / team.totalConnected;
  if (utilization >= 0.9) {
    // Scale up: provision additional workers
  }
}
```

### Get Worker by ID

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pw_123" \
  --u "$CURSOR_API_KEY:"
```

---

## Monitoring (Prometheus Metrics)

Start worker with management address:

```bash
agent worker start --pool --management-addr ":8080"
```

Exposes endpoints:
- `GET /healthz` – liveness probe
- `GET /readyz` – readiness probe
- `GET /metrics` – Prometheus metrics

### Metrics:

| Metric | Type | Description |
|--------|------|-------------|
| `cursor_self_hosted_worker_connected` | Gauge | 1 if connected, 0 otherwise |
| `cursor_self_hosted_worker_session_active` | Gauge | 1 if session active, 0 otherwise |
| `cursor_self_hosted_worker_last_activity_unix_seconds` | Gauge | Timestamp of last activity |
| `cursor_self_hosted_worker_connect_attempts_total` | Counter | Total connection attempts |
| `cursor_self_hosted_worker_connect_retry_total` | Counter | Total retries |
| `cursor_self_hosted_worker_session_ends_total` | Counter | Session ends (with reason label) |

### Session End Reasons:

| Reason | Meaning |
|--------|---------|
| `stream_end` | Normal completion |
| `stream_error` | Stream error |
| `session_closed` | Session closed |
| `session_error` | Session error |
| `connection_timeout` | Timeout |
| `session_aborted` | Aborted |

---

## Security

| Feature | What it does |
|---------|--------------|
| **Data flow** | Only file chunks (for inference) and artifacts leave your network. Repos, caches, secrets stay with you. |
| **Outbound-only** | No inbound ports or firewall changes required |
| **Privacy mode** | Zero data retention across all model providers. No code stored or used for training. |
| **Isolation** | Each session gets its own dedicated worker |
| **Authentication** | Service account API keys only |
| **Dashboard visibility** | Admins see all workers; team members see only theirs |

---

## CLI Reference: `agent worker start`

| Flag | Env var | Description |
|------|---------|-------------|
| `--worker-dir <path>` | | Working directory (must be git repo) |
| `--management-addr <addr>` | | Address for /healthz, /readyz, /metrics |
| `--label <key=value>` | | Add label (repeatable) |
| `--labels-file <path>` | `CURSOR_WORKER_LABELS_FILE` | Path to JSON/TOML labels file |
| `--idle-release-timeout <sec>` | `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT` | Seconds to stay connected after session ends |
| `--pool` | | Register for pool assignment |
| `--pool-name <name>` | `CURSOR_WORKER_POOL_NAME` | Pool label (requires `--pool`) |
| `--api-key <key>` | `CURSOR_API_KEY` | Service account API key |
| `--auth-token <token>` | | Pre-minted access token |
| `--auth-token-file <path>` | | File containing access token (refreshed on reconnection) |
| `--endpoint <url>` | | API endpoint (default: `https://api2.cursor.sh`) |

---

## Common Beginner Questions

### Q: Is this for me as a beginner?
**A:** No. This is for Enterprise teams with dedicated infrastructure teams.

### Q: How is this different from My Machines?
**A:** My Machines = personal workers on your laptop. Self-Hosted Pool = shared workers for entire organization.

### Q: Do I need Kubernetes?
**A:** No, but Kubernetes is supported for large-scale deployments. You can also run workers on VMs.

### Q: What if I need more than 50 workers?
**A:** Contact Cursor support to discuss scaling.

### Q: Can I use personal API keys?
**A:** No. Pool workers require service account API keys.

### Q: Do workers need inbound ports?
**A:** No – outbound HTTPS only.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it is** | Enterprise fleet of Cloud Agent workers |
| **Authentication** | Service account API keys only |
| **Start worker** | `agent worker start --pool` |
| **Pool name** | `--pool-name gpu` for routing |
| **Labels** | `--label team=backend` for fine routing |
| **Idle timeout** | `--idle-release-timeout 600` |
| **Monitoring** | Prometheus metrics on `--management-addr` |
| **Kubernetes** | Helm chart + operator available |
| **Limits** | 10 workers/user, 50 workers/team default |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is Self-Hosted Pool?** | Enterprise fleet of Cloud Agent workers on your infrastructure |
| **Who is it for?** | Enterprise teams with dedicated infrastructure |
| **How is it different from My Machines?** | Centralized vs. personal |
| **Do I need Kubernetes?** | No – works on VMs too |
| **How do I start?** | `agent worker start --pool` |
| **Can I autoscale?** | Yes – via fleet management API |

---

## The Bottom Line

**Self-Hosted Pool is how Enterprises run Cloud Agents on their own infrastructure at scale.**

**Think of it as:**
- **Cursor-hosted agents** = Rented computers in Cursor's cloud 🏢
- **My Machines** = Your personal computer ☁️
- **Self-Hosted Pool** = Your company's private fleet of workers 🏭

**For Enterprise teams:** This gives you:
- Centralized management
- Service account authentication (no individual logins)
- Network isolation (agents run inside your firewall)
- Access to internal services and databases
- Full control over data and secrets
- Kubernetes and autoscaling support

**For beginners:** This is not something you need to worry about. Your organization's infrastructure team would set this up.

