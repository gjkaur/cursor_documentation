This is the **GitHub Integration** documentation – it explains how to connect your GitHub repositories to Cursor so you can use features like **Cloud Agents** and **Bugbot**.

Think of this as the **bridge between Cursor and your code** – without this connection, Cursor can't read your code, create branches, or open pull requests.

Let me break this down for a beginner.

---

## What Is the GitHub Integration? (The 10-Second Summary)

**The Cursor GitHub app connects your repositories so you can use features like Cloud Agents and Bugbot.**

| Without GitHub Integration | With GitHub Integration |
|---------------------------|------------------------|
| Cursor can't access your code | Cursor can clone, branch, and create PRs |
| No automatic PR reviews | Bugbot can review code |
| No Cloud Agents on your repos | Agents can work autonomously |

---

## Setup

### Requirements:

| Requirement | Details |
|-------------|---------|
| **Cursor admin access** | You need to be a Cursor admin |
| **GitHub org admin access** | You need admin access to the GitHub organization |

### Supported GitHub Versions:

| Version | Support |
|---------|---------|
| **GitHub.com** | ✅ Yes |
| **GitHub Enterprise Server** | ✅ Yes |

### Installation Steps:

| Step | Action |
|------|--------|
| **1** | Go to **Integrations** in the Cursor dashboard |
| **2** | Click **Connect** next to GitHub (or **Manage Connections** if already connected) |
| **3** | Choose **All repositories** or **Selected repositories** |
| **4** | Return to the dashboard to configure features on your repositories |

### To Disconnect:

Return to the integrations dashboard and click **Disconnect Account**.

---

## IP Allow List Configuration (For Organizations with IP Restrictions)

If your organization uses GitHub's **IP allow list** feature to restrict access to your repositories, Cursor can use a hosted egress proxy with a narrow set of IPs.

### Important First Step:

> *"Before configuring IP allowlists, contact hi@cursor.com to enable this feature for your team. This is required for either configuration method below."*

---

### Method 1: Enable for Installed GitHub Apps (Recommended)

The Cursor GitHub app has the IP list already pre-configured. You can enable the allowlist for installed apps to automatically inherit this list.

**This is the recommended approach** – it allows Cursor to update the list, and your organization receives updates automatically.

#### To enable:

1. Go to your organization's **Security settings**
2. Navigate to **IP allow list settings**
3. Check **"Allow access by GitHub Apps"**

For detailed instructions, see GitHub's documentation.

---

### Method 2: Add IPs Directly to Your Allowlist

If your organization uses IdP-defined allowlists in GitHub or otherwise cannot use the pre-configured allowlist, add the proxy IPs listed in **Git egress proxy and IP allow list** documentation.

---

## Advanced Networking (For Self-Hosted Instances)

Self-hosted instances support multiple connection methods beyond IP whitelisting:

| Method | Description |
|--------|-------------|
| **PrivateLink (AWS) or Private Service Connect (GCP)** | Secure private connection between Cursor and your self-hosted GitHub |
| **Reverse Proxy Tunnel** | Tunnel-based connection for self-hosted instances |

---

## Permissions (What the GitHub App Needs)

The GitHub app requests the following permissions to support Cursor features:

| Permission | Purpose |
|------------|---------|
| **Repository access** | Clone your code and create working branches |
| **Pull requests** | Create PRs and leave review comments |
| **Issues** | Track bugs and tasks discovered during reviews |
| **Checks and statuses** | Report on code quality and test results |
| **Actions and workflows** | Monitor CI/CD pipelines and deployment status |

> *"All permissions follow the principle of least privilege."* (Only the minimum necessary permissions are requested.)

---

## Troubleshooting

Common issues:

| Issue | What to check |
|-------|---------------|
| **Agent can't access repository** | Verify GitHub integration is connected and has access to the repo |
| **Permission denied for pull requests** | Check that the GitHub app has PR creation permissions |
| **App not visible in GitHub settings** | Verify installation completed successfully, or reinstall |

---

## Next Steps (What You Can Do After Connecting)

Once your GitHub integration is connected, configure the features that use it:

| Feature | What it does |
|---------|--------------|
| **Bugbot** | Automated PR reviews that catch bugs and security issues |
| **Cloud Agents** | AI agents that run in the cloud on your repositories |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Connects GitHub repos to Cursor |
| **Requirements** | Cursor admin + GitHub org admin |
| **Setup location** | Dashboard → Integrations |
| **Repository access** | All repos or selected repos |
| **IP allow list** | Contact hi@cursor.com to enable |
| **Supported GitHub** | GitHub.com + GitHub Enterprise Server |
| **Key permissions** | Read/write repos, create PRs, read issues |

---

## Common Beginner Questions

### Q: Do I need admin access to set this up?
**A:** Yes – you need both Cursor admin and GitHub organization admin access.

### Q: Can I choose which repositories Cursor can access?
**A:** Yes – during setup, choose **All repositories** or **Selected repositories**.

### Q: What if my organization uses IP allow lists?
**A:** Contact hi@cursor.com to enable the feature, then either enable for GitHub Apps (recommended) or add proxy IPs manually.

### Q: Does Cursor support GitHub Enterprise Server?
**A:** Yes – both GitHub.com and GitHub Enterprise Server are supported.

### Q: Can I disconnect the integration?
**A:** Yes – return to Integrations dashboard and click **Disconnect Account**.

### Q: What features require GitHub integration?
**A:** Bugbot (PR reviews) and Cloud Agents (autonomous agents) both require GitHub integration.

---

## The Bottom Line

**The GitHub integration is the foundation for most of Cursor's advanced features – without it, Cloud Agents and Bugbot cannot work on your repositories.**

**Think of it as:**
- **Without GitHub integration** = Cursor can't touch your code 🚫
- **With GitHub integration** = Cursor can clone, branch, review, and create PRs ✅

**For teams:** This is a one-time setup by an admin. After that, your whole team can use Cloud Agents and Bugbot on your repositories.

**Key points:**
1. Requires **Cursor admin + GitHub org admin** to set up
2. Choose which repos to grant access to
3. Permissions follow **least privilege** principle
4. IP allow list support available (contact hi@cursor.com)
5. Once connected, enable Bugbot and Cloud Agents

