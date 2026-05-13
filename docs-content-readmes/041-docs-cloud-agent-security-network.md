This is the **Security & Network** documentation for Cloud Agents – it explains how Cursor protects your data and how you can control network access when using Cloud Agents.

Think of this as the **security guard** for your Cloud Agents – controlling what they can access, protecting secrets, and ensuring commits are verified.

Let me break this down.

---

## Privacy Mode (The Foundation)

**Cloud Agents are available in Privacy Mode.**

| What Privacy Mode Means |
|-------------------------|
| We **never train on your code** |
| We only retain code for **running the agent** |
| Your code is not used to improve Cursor (unless you opt out) |

> *"Learn more about Privacy mode."*

### Important Note:

> *"If privacy mode is disabled, we collect prompts and dev environments to improve the product."*

> *"If you disable privacy mode when starting a cloud agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes."*

---

## Secret Protection 🔑

Secrets provided to Cloud Agents are **encrypted at rest and in transit**. They are **not visible** to anyone other than the Cloud Agent user.

### Redacted Secrets (Extra Protection)

You can classify secrets as **"Redacted"** for additional protection:

| Protection | What it does |
|------------|--------------|
| **Commit scanning** | Scans commit messages and files – rejects if they contain the secret |
| **Model tool call redaction** | Redacted from model tool calls – not shown to models |
| **Transcript redaction** | Not stored in chat transcripts |

> *"This prevents accidental exposure of credentials in version control and model context."*

---

## Signed Commits (Verified Badge) ✅

Cloud Agents **sign every commit** with a **HSM-backed Ed25519 key**.

| Platform | Effect |
|----------|--------|
| **GitHub** | Displays "Verified" badge |
| **GitLab** | Displays "Verified" badge |

> *"This works automatically for all Cloud Agents. No setup is required."*

### Branch Protection:

> *"If your repository enforces branch protection rules that require signed commits, Cloud Agent PRs satisfy those rules without extra configuration."*

---

## What You Should Know (6 Important Facts)

| # | Fact |
|---|------|
| **1** | Grant read-write privileges to our GitHub app for repos you want to edit. We use this to clone the repo and make changes. |
| **2** | Your code runs inside our AWS infrastructure in **isolated VMs** and is stored on VM disks while the agent is accessible. |
| **3** | The agent has **internet access by default**. You can configure network egress controls to restrict domains. |
| **4** | The agent **auto-runs all terminal commands**, letting it iterate on tests. This differs from foreground agent (requires approval). Auto-running introduces **data exfiltration risk** – attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites. |
| **5** | If privacy mode is disabled, we collect prompts and dev environments to improve the product. |
| **6** | If you disable privacy mode when starting a cloud agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes. |

### ⚠️ Important Security Warning:

> *"Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites."*

**This is a real risk** – be careful what contexts you run Cloud Agents in.

---

## Network Access (Egress Controls)

Control which network resources your Cloud Agents can reach. Settings available in the Cloud Agents dashboard.

### Three Access Modes:

| Mode | Behavior |
|------|----------|
| **Allow all network access** | Cloud Agents can reach any external host. No domain restrictions. |
| **Default + allowlist** | Can reach default domains + any domains you add to allowlist |
| **Allowlist only** | Can ONLY reach domains you explicitly add to allowlist |

> *"Even in Allowlist only mode, a small set of domains remain accessible so Cloud Agents can function. These include Cursor's own services and source control management (SCM) providers."*

---

## Artifact Uploads (Important!)

Cloud Agents upload artifacts (screenshots, videos, log references) to:
```
cloud-agent-artifacts.s3.us-east-1.amazonaws.com
```

### Security Warning:

> *"Don't broaden the entry to `*.s3.us-east-1.amazonaws.com`: the wildcard opens egress to every bucket in the region and creates an exfiltration path for a prompt-injected agent."*

| Correct | Incorrect (Dangerous) |
|---------|----------------------|
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` | `*.s3.us-east-1.amazonaws.com` |

> *"Blocking the host disables uploads; agent sessions and other tool calls keep working."*

---

## User-Level Settings

Individual users can configure network access mode from the Cloud Agents dashboard under the **Security** header.

| Setting | Scope |
|---------|-------|
| **User-level setting** | Applies to all Cloud Agents YOU create |

When you select a mode with an allowlist, an allowlist configuration section appears to add custom domains.

---

## Team-Level Settings

Team admins can set a **default network access mode** for the entire team.

> *"The team-level allowlist is the same allowlist that admins configure for the sandbox default network allowlist. There is no separate allowlist to manage; one allowlist controls both Cloud Agent network access and the sandbox defaults."*

### Precedence:

| If user has... | Setting used |
|----------------|--------------|
| **Their own setting** | User setting takes precedence |
| **No setting configured** | Team default applies |

---

## Locking the Setting (Enterprise Only)

Enterprise team admins can **lock** the network access setting using the **Lock Network Access Policy** option.

| When locked... |
|----------------|
| Team-level setting applies to EVERY member |
| Users cannot override from their dashboard |

> *"This gives admins full control over Cloud Agent network access across the organization."*

---

## Relationship to Sandbox Network Policy

| Feature | Relationship |
|---------|--------------|
| **"Default" domains** | Same as desktop Agent's sandbox |
| **Team-level allowlist** | Shared between Cloud Agents and sandbox |

> *"When an admin configures an allowlist on the dashboard, it applies to both Cloud Agent network access and the sandbox network policy."*

---

## Egress IP Ranges

Cloud Agents make network connections from **specific IP address ranges**.

### API Endpoint:

```
https://cursor.com/docs/ips.json
```

### Response Format:

```json
{
  "version": 1,
  "modified": "2025-09-24T16:00:00.000Z",
  "cloudAgents": {
    "us3p": ["100.26.13.169/32", "34.195.201.10/32", "..."],
    "us4p": ["54.184.235.255/32", "35.167.37.158/32", "..."],
    "us5p": ["3.12.82.200/32", "52.14.104.140/32", "..."]
  },
  "gitEgressProxy": ["184.73.225.134/32", "3.209.66.12/32", "52.44.113.131/32"]
}
```

### Using the IP Ranges:

These IP ranges may be used by Cloud Agents to:

| Action |
|--------|
| Clone and push to remote repositories |
| Download packages and dependencies |
| Make API calls to external services |
| Access web resources during execution |

### Important Considerations:

> *"We make changes to our IP addresses from time to time for scaling and operational needs. We do not recommend allowlisting by IP address as your primary security mechanism. If you must use these IP ranges, we strongly encourage regular monitoring of the JSON API endpoint."*

---

## Git Egress Proxy

For git hosts specifically, Cursor supports a **git egress proxy** that routes all git traffic through a narrower set of IPs.

### Proxy IP Addresses:

| IP |
|----|
| `184.73.225.134` |
| `3.209.66.12` |
| `52.44.113.131` |

> *"For git hosts specifically, we recommend the IP allow list configuration described in the link above, as it integrates directly with the Cursor GitHub app."*

---

## Summary of Security Features

| Feature | What it does |
|---------|--------------|
| **Privacy Mode** | Never train on your code |
| **Secret encryption** | Encrypted at rest and in transit |
| **Redacted secrets** | Scanned from commits + hidden from models |
| **Signed commits** | "Verified" badge on GitHub/GitLab |
| **Network egress controls** | Restrict which domains agents can reach |
| **Egress IP ranges** | Publish IPs for firewall allowlisting |

---

## Network Access Modes Summary

| Mode | Behavior | Risk Level |
|------|----------|------------|
| **Allow all** | Agent can reach any host | Highest |
| **Default + allowlist** | Default domains + your additions | Medium |
| **Allowlist only** | Only your explicitly added domains | Lowest |

---

## Common Beginner Questions

### Q: Is my code safe in Cloud Agents?
**A:** Yes – Privacy Mode ensures no training on your code. Code runs in isolated VMs.

### Q: Can my secrets be exposed?
**A:** Secrets are encrypted. Redacted secrets add extra protection (scanned from commits, hidden from models).

### Q: Do Cloud Agent commits show as verified?
**A:** Yes – automatically on GitHub and GitLab.

### Q: Can I restrict what websites Cloud Agents can access?
**A:** Yes – use network egress controls (Allowlist only or Default + allowlist).

### Q: What's the risk with auto-running terminal commands?
**A:** Prompt injection attacks could trick the agent into uploading code to malicious sites. Use network restrictions to mitigate.

### Q: Can I set network policies for my whole team?
**A:** Yes – team admins can set defaults and Enterprise can lock them.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Privacy Mode** | No training on code |
| **Secret protection** | Encrypted + optional redaction |
| **Signed commits** | Automatic "Verified" badge |
| **Network modes** | Allow all, Default+allowlist, Allowlist only |
| **Artifact upload host** | `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` |
| **IP ranges API** | `cursor.com/docs/ips.json` |
| **Git proxy IPs** | 184.73.225.134, 3.209.66.12, 52.44.113.131 |

---

## The Bottom Line

**Cloud Agent security is built on Privacy Mode, encrypted secrets, signed commits, and configurable network controls.**

**Think of it as:**
- **Privacy Mode** = Your code is not used for training 🔒
- **Redacted secrets** = Extra protection against accidental exposure 🛡️
- **Signed commits** = Proof commits came from Cursor ✅
- **Network allowlists** = Control where agents can go 🌐

**For security-conscious teams:**
1. Use **Privacy Mode** (default)
2. Mark sensitive secrets as **Redacted**
3. Use **Allowlist only** mode for network access
4. Add **exact artifact host** (not wildcard) to allowlist
5. Consider **locking** policies for Enterprise

**Most important warning:** Auto-running commands introduces data exfiltration risk. Use network restrictions to limit blast radius if prompt injection occurs.

Would you like me to explain any specific security feature in more detail?