This is the **Cloud Agents** documentation – it explains how Cursor can run agents in **isolated cloud environments** instead of on your local machine.

Think of Cloud Agents as **hiring remote workers** who have their own computers, work 24/7, and don't require your laptop to be on. They can run in parallel, build and test code, and even let you remote into their desktop!

Let me break this down for a beginner.

---

## What Are Cloud Agents? (The 10-Second Summary)

**Cloud agents run in isolated environments in the cloud instead of on your local machine.** They leverage the same agent fundamentals but in the cloud.

| Local Agents | Cloud Agents |
|--------------|--------------|
| Run on YOUR computer | Run on Cursor's cloud computers |
| Stop when you close laptop | Run 24/7 |
| One at a time (typically) | Run as many as you want in parallel |
| Can't work while you sleep | Work while you're offline |

> *"You can run as many agents as you want in parallel, and they do not require your local machine to be connected to the internet."*

---

## Why Use Cloud Agents?

| Benefit | What it means |
|---------|---------------|
| **Parallel execution** | Run unlimited agents simultaneously |
| **No local resources** | Your laptop doesn't need to be on |
| **Build and test** | Cloud agents have their own virtual machines to build and test software |
| **Desktop control** | They can control desktops and browsers |
| **MCP support** | Access external tools, databases, APIs |
| **Work while you sleep** | Agents keep working even when you're offline |

---

## How to Access Cloud Agents

You can kick off cloud agents from **wherever you work**:

| Platform | How to use |
|----------|------------|
| **Cursor Web** | Start and manage agents from `cursor.com/agents` on any device |
| **Cursor Desktop** | Select "Cloud" in the dropdown under the agent input |
| **Slack** | Use the `@cursor` command to kick off an agent |
| **GitHub** | Comment `@cursor` on a PR or issue |
| **API** | Use the API to kick off an agent |

### Mobile Access (PWA)

For a native-feeling mobile experience, install Cursor as a **Progressive Web App (PWA)**:

| Platform | Instructions |
|----------|--------------|
| **iOS** | Open `cursor.com/agents` in Safari → Share button → "Add to Home Screen" |
| **Android** | Open URL in Chrome → Menu → "Install App" |

**You can manage cloud agents from your phone!**

---

## How Cloud Agents Work

### GitHub/GitLab Connection

Cloud agents:
1. **Clone** your repo from GitHub or GitLab
2. **Work on a separate branch**
3. **Push changes** to your repo for handoff

> *"You need read-write privileges to your repo and any dependent repos or submodules."*

**Support for other providers like Bitbucket is coming later.**

---

## Models

Cloud Agents use a **curated selection of models** that **always run in Max Mode**.

> *"There is no toggle to turn Max Mode off for Cloud Agents."*

**What this means:** Cloud agents always have the maximum context window available (1M tokens for most models).

---

## MCP Support

Cloud agents can use **MCP (Model Context Protocol) servers** configured for your team.

| Feature | Support |
|---------|---------|
| **Add/manage MCP** | Through MCP dropdown in `cursor.com/agents` |
| **Transports** | Both HTTP and stdio supported |
| **OAuth** | Supported for MCP servers that need it |

---

## Hooks Support

Cloud agents run **project hooks** from `.cursor/hooks.json`.

On **Enterprise plans**, they also run:
- Team hooks
- Enterprise-managed hooks

> *"This lets you keep formatters, audit scripts, and policy checks active when work runs in the cloud – whether you manage them in the repo or from the dashboard."*

---

## Artifacts and Remote Desktop Control 🖥️

Cloud agents produce **merge-ready PRs** with artifacts to demo their changes. You can also **control the agent's remote desktop**!

### Artifacts:

Agents produce:
| Artifact | What it shows |
|----------|---------------|
| **Screenshots** | Visual proof of changes |
| **Videos** | Recordings of the agent working |
| **Logs** | Detailed execution history |

> *"See exactly what changed and how the agent verified its work."*

### Remote Desktop Control:

> *"Take control of the agent's desktop to test the software yourself in a full development environment without checking out the branch locally. Release control back to the agent for it to keep working."*

**This is incredibly powerful:** You can remote into the cloud agent's computer, test the changes yourself, then let the agent continue working!

---

## Billing

Cloud Agents are charged at **API pricing for the selected model**.

> *"You'll be asked to set a spend limit when you first start using them."*

**For beginners:** Set a reasonable spend limit so you don't get surprised by bills.

---

## Related Pages (For More Info)

- Cloud Agent capabilities
- Cloud Agent security
- Cloud Agent settings

---

## Naming History

> *"Cloud Agents were formerly called Background Agents."*

So if you see "Background Agents" in older documentation, that's the same thing!

---

## Common Beginner Questions

### Q: Do I need Cloud Agents as a beginner?
**A:** Probably not. Local agents are fine for most tasks. Cloud agents are for heavy parallel workloads.

### Q: How much do Cloud Agents cost?
**A:** API pricing for the selected model + cloud compute (varies by usage). You set a spend limit.

### Q: Can I run Cloud Agents on my phone?
**A:** Yes! Through the PWA at `cursor.com/agents`.

### Q: Do Cloud Agents work while my computer is off?
**A:** Yes! That's the point. They run in the cloud.

### Q: Can I see what a Cloud Agent is doing?
**A:** Yes – artifacts (screenshots, videos, logs) show you everything.

### Q: Can I interrupt a Cloud Agent?
**A:** Yes – you can take control of its remote desktop or stop it from the dashboard.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What are they?** | Agents running in cloud environments, not on your machine |
| **Key benefit** | Run unlimited agents in parallel, work while you're offline |
| **Access methods** | Web, Desktop, Slack, GitHub, API, Mobile PWA |
| **Models** | Curated selection, always in Max Mode |
| **Artifacts** | Screenshots, videos, logs |
| **Remote desktop** | You can take control of the agent's computer |
| **Billing** | API pricing + spend limit |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Cloud Agents?** | Agents that run on Cursor's cloud computers, not your laptop |
| **Why use them?** | Run many at once, work 24/7, test in isolated environments |
| **How do I start one?** | Desktop (Cloud dropdown), Web, Slack, GitHub, API |
| **Can I use them on mobile?** | Yes – install as PWA |
| **Do they cost extra?** | Yes – API pricing, set a spend limit |
| **Can I see their work?** | Yes – screenshots, videos, logs, even remote desktop |

---

## The Bottom Line

**Cloud Agents are like having a team of remote developers who work 24/7 on their own computers.**

**Think of it as:**
- **Local Agent** = Employee working at your desk (only when you're there) 🪑
- **Cloud Agent** = Remote employee with their own computer (works 24/7) ☁️

**For beginners:** You probably don't need Cloud Agents yet. Start with local agents. When you need to run many tasks in parallel or want agents working while you sleep, that's when Cloud Agents shine.

**The coolest features:**
1. **Remote desktop control** – You can take over the agent's computer!
2. **Artifacts** – Screenshots and videos of the agent working
3. **Slack/GitHub integration** – Kick off agents from your workflow
4. **Mobile access** – Manage agents from your phone

**Security note:** Cloud agents run in isolated environments. Your code is processed in the cloud, so be mindful of sensitive data.

