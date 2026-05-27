This is the **GitLab Integration** documentation – it explains how to connect your GitLab repositories to Cursor so you can use features like **Cloud Agents** and **Bugbot**.

Think of this as the **GitLab version** of the GitHub integration – it bridges Cursor with your GitLab-hosted code.

Let me break this down for a beginner.

---

## What Is the GitLab Integration? (The 10-Second Summary)

**The GitLab integration connects your repositories so you can use features like Cloud Agents and Bugbot.**

| Without GitLab Integration | With GitLab Integration |
|---------------------------|------------------------|
| Cursor can't access your GitLab code | Cursor can clone, branch, and create merge requests |
| No automatic MR reviews | Bugbot can review code |
| No Cloud Agents on your repos | Agents can work autonomously |

---

## Important: Paid GitLab Plan Required

> *"GitLab integration requires a paid GitLab plan (Premium or Ultimate). Project access tokens, which are required for this integration, are not available on GitLab Free."*

**This is critical** – you cannot use this integration with GitLab's free tier.

---

## Requirements

| Requirement | Details |
|-------------|---------|
| **Cursor admin access** | You need to be a Cursor admin |
| **GitLab maintainer access** | You need maintainer access to the GitLab project/group |
| **GitLab plan** | **Premium or Ultimate** (required for project access tokens) |

### Supported GitLab Versions:

| Version | Support |
|---------|---------|
| **GitLab.com** | ✅ Yes |
| **GitLab Self-Hosted** | ✅ Yes |

---

## Setup (Installation Steps)

| Step | Action |
|------|--------|
| **1** | Go to **Integrations** in the Cursor dashboard |
| **2** | Click **Connect** next to GitLab (or **Manage Connections** if already connected) |
| **3** | Follow the **GitLab installation flow** |
| **4** | Back on the Integrations tab, click **Manage** next to your GitLab connection and select **Sync Repos** |
| **5** | Return to the dashboard to configure features on your repositories |

### To Disconnect:

Return to the Integrations dashboard and click **Disconnect Account**.

---

## Advanced Networking (For Self-Hosted Instances)

Self-hosted GitLab instances support multiple connection methods beyond IP whitelisting:

| Method | Description |
|--------|-------------|
| **PrivateLink (AWS) or Private Service Connect (GCP)** | Secure private connection between Cursor and your self-hosted GitLab |
| **Reverse Proxy Tunnel** | Tunnel-based connection for self-hosted instances |

---

## Next Steps (What You Can Do After Connecting)

Once your GitLab integration is connected, configure the features that use it:

| Feature | What it does |
|---------|--------------|
| **Bugbot** | Automated merge request reviews that catch bugs and security issues |
| **Cloud Agents** | AI agents that run in the cloud on your repositories |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Connects GitLab repos to Cursor |
| **Requirements** | Cursor admin + GitLab maintainer + GitLab Premium/Ultimate |
| **Setup location** | Dashboard → Integrations |
| **Sync repos** | Click Manage → Sync Repos after connecting |
| **Supported GitLab** | GitLab.com + GitLab Self-Hosted |
| **Key limitation** | Requires paid GitLab plan (Premium/Ultimate) |

---

## Common Beginner Questions

### Q: Can I use GitLab integration with the free GitLab plan?
**A:** No – you need **GitLab Premium or Ultimate**. Project access tokens are not available on GitLab Free.

### Q: Do I need admin access to set this up?
**A:** Yes – you need both Cursor admin and GitLab maintainer access.

### Q: Does Cursor support GitLab Self-Hosted?
**A:** Yes – both GitLab.com and GitLab Self-Hosted are supported.

### Q: What's the "Sync Repos" step for?
**A:** After connecting, you need to sync repositories so Cursor can see which repos to work with.

### Q: Can I disconnect the integration?
**A:** Yes – return to Integrations dashboard and click **Disconnect Account**.

### Q: What features require GitLab integration?
**A:** Bugbot (merge request reviews) and Cloud Agents both require GitLab integration.

---

## Comparison: GitHub vs. GitLab Integration

| Feature | GitHub | GitLab |
|---------|--------|--------|
| **Free tier support** | ✅ Yes | ❌ No (requires Premium/Ultimate) |
| **Setup time** | Simple | Requires sync step |
| **Self-hosted support** | ✅ Yes | ✅ Yes |
| **IP allow list** | ✅ Yes | Via advanced networking |
| **PrivateLink** | ✅ Yes | ✅ Yes |

---

## The Bottom Line

**The GitLab integration connects Cursor to your GitLab repositories, but requires a paid GitLab plan.**

**Think of it as:**
- **GitHub integration** = Works with free GitHub accounts 🆓
- **GitLab integration** = Requires Premium/Ultimate 💰

**For teams using GitLab Premium or Ultimate:** This integration works similarly to GitHub – connect once, then enable Bugbot and Cloud Agents on your repositories.

**Key steps to remember:**
1. Ensure you have **GitLab Premium or Ultimate**
2. Have **Cursor admin + GitLab maintainer** access
3. Connect → Install → **Sync Repos** → Configure features
4. Then enable Bugbot and/or Cloud Agents

