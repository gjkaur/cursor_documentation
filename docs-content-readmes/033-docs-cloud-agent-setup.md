This is the **Cloud Agent Setup** documentation – it explains how to configure the environment that Cloud Agents run in. Since Cloud Agents run on isolated Ubuntu machines in the cloud, they need to be set up with the right tools, dependencies, and secrets to work with your code.

Think of this as **packing a suitcase for your cloud agent** – you need to include everything it will need to do its job.

Let me break this down for a beginner (note: this is an **advanced** feature).

---

## What Is Cloud Agent Setup? (The 10-Second Summary)

**Cloud agents run on an isolated Ubuntu machine. We recommend configuring this environment so the agent has access to the same tools a human developer would use.**

Go to `cursor.com/environment` to configure your environment.

| Without Setup | With Setup |
|---------------|------------|
| Agent has no dependencies | Agent has Node.js, Python, etc. |
| Can't build your project | Can run builds and tests |
| Missing API keys | Secrets available as environment variables |

---

## Two Ways to Configure the Environment

| Method | Best for | Difficulty |
|--------|----------|------------|
| **Agent-driven setup (recommended)** | Most users – let Cursor figure it out | Easy |
| **Manual setup with Dockerfile (advanced)** | Complex dependencies, specific requirements | Advanced |

Both options generate an environment and allow you to specify an **update command** (e.g., `npm install`, `pip install`) that runs before the agent starts to ensure dependencies are up to date.

---

## Environment Resolution Order

Cursor resolves environment configuration in this order, using the **first match**:

| Order | Source | Who can set it |
|-------|--------|----------------|
| 1 | `.cursor/environment.json` in the repository | Anyone (in code) |
| 2 | Personal environment configuration | Individual user |
| 3 | Team environment configuration | Team admin |

> *"This gives you predictable defaults at the team level while still letting individual users override with a personal environment when a repo-level `.cursor/environment.json` is not present."*

**User overrides** are useful for testing a new environment configuration before rolling it out to the entire team.

---

## Method 1: Agent-Driven Setup (Recommended)

This is the easiest way. Cursor figures out what your project needs.

### Step-by-step:

| Step | What happens |
|------|--------------|
| 1 | Connect your GitHub or GitLab account |
| 2 | Select the repository you want to work on |
| 3 | Provide environment variables and secrets (API keys, etc.) |
| 4 | Cursor installs dependencies and verifies the code is working |
| 5 | **Save a snapshot** of the virtual machine to reuse for future agents |

### The Snapshot Feature:

After Cursor sets up the environment, you can **save a snapshot** of the virtual machine. Future cloud agents can start from this snapshot, which is much faster than setting up from scratch.

---

## Method 2: Manual Setup with Dockerfile (Advanced)

For advanced cases, configure the environment with a **Dockerfile**.

### What you can do with a Dockerfile:

| Capability | Example |
|------------|---------|
| Install system-level dependencies | `apt-get install -y curl` |
| Use specific compiler versions | `gcc-11`, `clang-14` |
| Install debuggers | `gdb`, `lldb` |
| Switch base OS image | `FROM ubuntu:22.04` |

### Important Note:

> *"Do not COPY the full project; Cursor manages the workspace and checks out the correct commit."*

**Let Cursor handle the code checkout.** Your Dockerfile should focus on system dependencies, not copying your project.

### Example `.cursor/environment.json`:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": "."
  },
  "install": "pnpm install && ./custom_script.sh"
}
```

### Path Behavior:

> *"The `dockerfile` and `context` paths in `build` are relative to `.cursor`. The `install` command runs from your project root."*

---

## Computer Use Support for Dockerfile Repos

> *"Computer use is supported for repos with Dockerfiles based on Debian/Ubuntu-based Linux distributions. If you require support for a different Linux distribution, please contact support."*

**This is important for desktop control features** – only Debian/Ubuntu-based images are supported for remote desktop.

---

## Resource Limits

| Plan | Resource Limits |
|------|-----------------|
| **Default** | Limited memory and CPU (standard VM profile) |
| **Enterprise** | Can request increased limits (contact support) |

> *"Self-serve custom resource configuration is coming soon."*

---

## Update Command (The `install` Script)

When a new machine boots, Cursor starts from the base environment, then runs the **update command** (called `install` in `environment.json`).

### For most repos:

The update script is something like:
- `npm install`
- `bazel build`
- `pip install -r requirements.txt`

### Idempotency Requirement:

> *"The update script must be idempotent. It can run more than once, and it may run on partially cached state."*

**What "idempotent" means:** Running the script multiple times should have the same effect as running it once. It shouldn't break if run again.

---

## How Caching Works

| Step | What happens |
|------|--------------|
| 1 | Update command runs |
| 2 | If it takes more than a few seconds, Cursor takes an **internal checkpoint snapshot** |
| 3 | Future cloud agents start from this checkpoint |

> *"This is why update commands like `npm install` usually lead to fast startup – if dependencies changed, the command only needs to do incremental work."*

**Note:** Caching is best effort; you may see slower startup times on infrequently used repositories.

---

## What to Put in Your Update Script (Tradeoffs)

| Put in `update` script | Do on demand during run |
|------------------------|------------------------|
| Basic dependency updates (`npm install`) | Starting services |
| Commands that rarely change | Building Docker images |
| Fast operations | Expensive/infrequent operations |

> *"A practical pattern is to run basic cached dependency updates (such as `npm install`) in your `update` script, then adding instructions in AGENTS.md so the agent can figure out which commands it needs to run for each specific task."*

---

## Startup Commands

After `install`, the machine starts and runs the **start command**, then any configured terminals.

### Use `start` for:

- Starting processes that should stay alive while the agent runs
- Starting Docker services: `sudo service docker start`

### Use `terminals` for:

- App code processes (these run in a tmux session shared by you and the agent)

You can skip `start` in many repos.

---

## Add Cloud-Specific Instructions to AGENTS.md

> *"Cloud agents read AGENTS.md files. We recommend adding a dedicated section for Cloud-only setup and testing instructions, with a title such as 'Cursor Cloud specific instructions'."*

### Example:

```markdown
## Cursor Cloud specific instructions

### Running E2E tests
- Start the dev server: `npm run dev`
- Run tests: `npm run test:e2e`

### Database setup
- Run migrations: `npm run db:migrate`
- Seed data: `npm run db:seed`
```

---

## Environment Variables and Secrets

Cloud agents need environment variables and secrets such as API keys and database credentials.

### Recommended: Use the Secrets Tab

The easiest way to manage secrets is through `cursor.com`.

| Feature | What it does |
|---------|--------------|
| **Add secrets** | Key-value pairs |
| **Encryption** | Encrypted at rest with KMS |
| **Access** | Exposed to cloud agents as environment variables |
| **Sharing** | Shared across cloud agents for your workspace or team |

### Redacted Secrets (Extra Security)

You have the option to specify secrets as **redacted**:

| Protection | What it does |
|------------|--------------|
| **Commit scanning** | Scans commits the agent makes to prevent accidentally committing secrets |
| **Tool call redaction** | Redacted in tool call results so not exposed to agent |
| **Transcript redaction** | Not stored in chat transcript |

### Sign-in Credentials and 2FA

If your app requires login:

| What to add | How |
|-------------|-----|
| Username, email, password | Add as secrets |
| TOTP secret (for 2FA) | Add as secret; agent can generate 6-digit code with `oathtool --totp -b "TOTP_SECRET"` |

---

## Monorepos with Multiple `.env` Files

| Problem | Solution |
|---------|----------|
| Multiple `.env.local` files | Add values from all files to the same Secrets tab |
| Key name conflicts | Use unique variable names (e.g., `NEXTJS_API_KEY`, `CONVEX_API_KEY`) |
| Reference variables | Reference from each app as needed |

> *"If you include `.env.local` files while taking a snapshot, they can be saved and available to cloud agents. The Secrets tab remains the recommended approach for security and management."*

---

## Using AWS IAM Roles (Advanced)

Cursor supports assuming **customer-provided IAM roles** for deeper integration with AWS.

### Setup steps:

| Step | Action |
|------|--------|
| 1 | Create IAM role in AWS, note its ARN |
| 2 | Add secret `CURSOR_AWS_ASSUME_IAM_ROLE_ARN` = your role ARN |
| 3 | Generate external ID in Cursor Dashboard |
| 4 | Configure IAM role trust policy with Cursor's role assumer |

### Environment Variables Set Automatically:

| Variable | Value |
|----------|-------|
| `AWS_CONFIG_FILE` | Points to Cursor-managed AWS config |
| `AWS_PROFILE` | `cursor-cloud-agent` |
| `AWS_SDK_LOAD_CONFIG` | `1` |

> *"The AWS CLI and AWS SDKs that use the default credential chain pick up this profile automatically during setup commands and while the agent is running."*

**Credentials expire after 1 hour** and are automatically refreshed.

---

## Build Secrets (For Dockerfile Builds)

During builds of Dockerfiles set in `.cursor/environment.json`, build secrets can be set at the team level.

### Reference in Dockerfile:

```dockerfile
RUN --mount=type=secret,id=MY_TOKEN,env=MY_TOKEN,required=true \
    ./scripts/install-private-deps.sh
```

> *"Build secrets are scoped to the build step and aren't passed to the running agent's environment."*

---

## Configuration in Code with `environment.json`

If you prefer to keep your environment configuration defined in code, commit a `.cursor/environment.json` to your repository.

### Example using a snapshot:

```json
{
  "snapshot": "snapshot-20260212-00000000-0000-0000-0000-000000000000",
  "install": "npm install"
}
```

### Example using Dockerfile:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "install": "pnpm install && ./custom_script.sh"
}
```

> *"Cloud agents will use the configuration at the commit they start from, so to test a new configuration, you can commit and push the change to a new branch, and start a cloud agent from that branch."*

---

## Running Docker in Cloud Agents

Cloud agents support Docker workflows.

| Complexity | What works |
|------------|------------|
| **Simple** | `docker run hello-world` usually works once Docker is installed and daemon is running |
| **Complex** | May need `fuse-overlayfs` and `iptables-legacy` configuration |

> *"Docker has edge cases in Cloud Agents because it runs inside another container layer."*

---

## Running Tailscale in Cloud Agents

> *"Tailscale does not work in its default networking mode in Cloud agent VMs. Use userspace networking mode instead."*

### Startup command:

```bash
tailscaled --tun=userspace-networking \
  --outbound-http-proxy-listen=localhost:1054 \
  --socks5-server=localhost:1055
```

### Set proxy variables:

```bash
export ALL_PROXY=socks5h://localhost:1055/
export HTTP_PROXY=http://localhost:1054/
export HTTPS_PROXY=http://localhost:1054/
```

> *"Userspace networking does not let the VM appear as a tailnet exit node."*

---

## Common Beginner Questions

### Q: Do I need to set up Cloud Agents as a beginner?
**A:** No. This is for advanced users running cloud agents. Local agents don't need this setup.

### Q: What's a "snapshot"?
**A:** A saved state of the cloud agent's virtual machine. Future agents can start from this snapshot for faster startup.

### Q: How do I add secrets?
**A:** Through the Secrets tab at `cursor.com` (dashboard).

### Q: Can I use my own Dockerfile?
**A:** Yes, for advanced setups. Use Method 2 (manual setup with Dockerfile).

### Q: What if my repo needs more CPU/memory?
**A:** On Enterprise plans, contact support to increase limits.

### Q: How do I test a new environment configuration?
**A:** Commit your `.cursor/environment.json` to a new branch and start a cloud agent from that branch.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Setup URL** | `cursor.com/environment` |
| **Two methods** | Agent-driven (easy) or Dockerfile (advanced) |
| **Resolution order** | Repo config → Personal → Team |
| **Update command** | Runs before agent starts (e.g., `npm install`) |
| **Caching** | Automatic snapshots after long updates |
| **Secrets** | Via Secrets tab in dashboard |
| **Redacted secrets** | Extra security – scanned and redacted |
| **Resource limits** | Default VM; Enterprise can request more |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is Cloud Agent Setup?** | Configuring the environment Cloud Agents run in |
| **Do I need it?** | Only if you're using Cloud Agents |
| **What's the easiest way?** | Agent-driven setup (let Cursor figure it out) |
| **What's a snapshot?** | A saved VM state for faster startup |
| **How do I add API keys?** | Secrets tab in the dashboard |
| **Can I use Docker?** | Yes, with some caveats |

---

## The Bottom Line

**Cloud Agent Setup is like preparing a computer for a remote employee – you need to install the right software and give them the right keys.**

**Think of it as:**
- **Agent-driven setup** = IT department sets up the computer for you 🖥️
- **Dockerfile setup** = You write a configuration script 📝
- **Snapshots** = Saved computer images for quick setup 📸
- **Secrets** = Keys and passwords the agent needs 🔑

**For beginners:** You don't need to worry about this yet. Start with local agents. When you're ready to use Cloud Agents, start with the **agent-driven setup** – it's much easier.

**For advanced users:** The Dockerfile method gives you full control. Use it for complex dependencies, specific compiler versions, or custom base images.

**Security note:** Always use the Secrets tab for sensitive data. Never hardcode secrets in your Dockerfile or environment.json. Use redacted secrets for extra protection.

Would you like me to explain any specific part of Cloud Agent setup in more detail?