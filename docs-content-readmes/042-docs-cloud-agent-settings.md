This is the **Cloud Agents Settings** documentation – it explains how workspace admins can configure Cloud Agent behavior from the dashboard.

Think of these settings as the **control panel** for how Cloud Agents work across your team – setting defaults, controlling network access, managing security, and enabling features.

Let me break this down.

---

## Where to Find Settings

Workspace admins can configure settings from the **Cloud Agents tab** on the dashboard.

---

## Defaults Settings

| Setting | What it does |
|---------|--------------|
| **Default model** | Model used when a run doesn't specify one. Pick any model that supports Max Mode. |
| **Default repository** | When empty, agents ask user to choose a repo. Supplying a repo lets users skip that step. |
| **Base branch** | Branch agents fork from when creating pull requests. Leave blank to use repository's default branch. |

---

## Network Access Settings

Control which network resources Cloud Agents can reach.

### Three Modes:

| Mode | Behavior |
|------|----------|
| **Allow all network access** | No domain restrictions |
| **Default + allowlist** | Default domains + any domains you add |
| **Allowlist only** | Only domains you explicitly add |

### Precedence:

| If... | Then... |
|-------|---------|
| User has their own setting | User setting takes precedence |
| User has no setting | Team default applies |
| Admin has locked the setting | Team setting applies to everyone |

> *"See Network Access for full details."*

---

## Security Settings

**All security options require admin privileges.**

| Setting | What it does |
|---------|--------------|
| **Display agent summary** | Controls whether Cursor shows agent's file-diff images and code snippets. Disable if you don't want to expose file paths or code in sidebar. |
| **Display agent summary in external channels** | Extends previous toggle to Slack or any connected external channel |
| **Team follow-ups** | Controls whether team members can send follow-up messages to cloud agents created by other users |

---

## Team Feature Settings

Team admins can enable or disable these features for their team:

| Feature | Description |
|---------|-------------|
| **Long running agents** | Controls whether team members can run agents for extended durations |
| **Computer use** | Controls whether agents can use computer interaction capabilities (Enterprise teams only) |

> *"Changes save instantly and affect new agents immediately."*

---

## Team Follow-ups (Important Security Consideration)

Team members can send follow-up messages to cloud agents created by other users on the same team.

### Why This Is Useful:

| Scenario | Benefit |
|----------|---------|
| Teammate starts an agent and is unavailable | You can course-correct |
| Need to add context | Add missing information |
| Continue work | Move the task forward |

### Three Settings:

| Setting | Behavior |
|---------|----------|
| **Disabled** | Only original creator can send follow-ups. No team follow-ups allowed. |
| **Service accounts only** | Team members can follow up on agents created by service accounts, NOT by other human users |
| **All** | Any team member can follow up on any agent, regardless of creator |

---

## ⚠️ Security Warning: Lateral Movement and Secret Exposure

This is a **critical security consideration**:

> *"Enabling team follow-ups means a user can influence the execution of a cloud agent that runs with another user's secrets and credentials."*

### The Risk:

| What Could Happen | Example |
|-------------------|---------|
| Read environment variables | "Print all env vars" |
| Print secrets to logs | "Echo the API key" |
| Push credentials externally | "Send .env file to webhook" |
| Perform actions with other user's tokens | "Use my access token to delete repos" |

> *"A team member with limited permissions could escalate their access by directing an agent that holds a more privileged user's secrets."*

### Recommendation:

> *"Treat this setting with the same care you would give shared SSH keys or service credentials."*

---

## Complete Settings Summary

| Category | Setting | Options |
|----------|---------|---------|
| **Defaults** | Default model | Any Max Mode model |
| | Default repository | Any repo or blank |
| | Base branch | Any branch or blank (uses default) |
| **Network** | Access mode | Allow all / Default+allowlist / Allowlist only |
| **Security** | Display agent summary | On/Off |
| | Display in external channels | On/Off |
| | Team follow-ups | Disabled / Service accounts only / All |
| **Features** | Long running agents | On/Off |
| | Computer use (Enterprise) | On/Off |

---

## Common Beginner Questions

### Q: Who can change these settings?
**A:** Workspace admins (team admins) can configure them from the Cloud Agents tab.

### Q: Do settings apply to existing agents or only new ones?
**A:** "Changes save instantly and affect new agents immediately." (Existing running agents may not be affected.)

### Q: What's the most secure network setting?
**A:** **Allowlist only** – agents can only reach domains you explicitly add.

### Q: Should I enable team follow-ups?
**A:** Only if you understand the security risks (lateral movement, secret exposure). Consider starting with "Disabled" or "Service accounts only."

### Q: What's "computer use"?
**A:** Agents controlling desktop and browser – Enterprise only.

---

## Quick Reference Card

| Category | Key Settings |
|----------|--------------|
| **Defaults** | Model, repository, base branch |
| **Network** | Allow all / Default+allowlist / Allowlist only |
| **Security** | Display summaries, team follow-ups |
| **Features** | Long-running agents, computer use (Enterprise) |

---

## The Bottom Line

**Cloud Agent Settings give admins control over defaults, network access, security, and features for their entire team.**

**Think of it as:**
- **Defaults** = Setting up the team's standard tools 🛠️
- **Network access** = Controlling where agents can go 🌐
- **Team follow-ups** = Allowing collaboration (with security risks) 👥
- **Features** = Enabling/disabling capabilities ⚙️

**For admins:**
1. Set reasonable **defaults** (model, repo, branch) to streamline user experience
2. Choose **network access mode** based on your security requirements
3. Be **very careful** with team follow-ups – understand the lateral movement risk
4. Enable **computer use** only if your team needs it (Enterprise)

**Most important warning:** Team follow-ups create security risks. A less privileged user could direct a more privileged user's agent to expose secrets or perform unauthorized actions.

Would you like me to explain any specific setting in more detail?