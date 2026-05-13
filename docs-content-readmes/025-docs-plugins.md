This is the **Plugins** documentation – it explains how you can package and share rules, skills, agents, commands, MCP servers, and hooks into **distributable bundles**.

Think of plugins as **add-ons** or **extensions** for Cursor, similar to how VS Code has extensions. They let you share custom AI behaviors with your team or the community.

Let me break this down for a complete beginner.

---

## What Are Plugins? (The 10-Second Summary)

**Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles.**

Instead of manually configuring rules and skills for every project, you can bundle them into a **plugin** and share it.

| Without Plugins | With Plugins |
|-----------------|--------------|
| Manually copy rules to each project | Install a plugin once |
| Team members configure individually | Everyone gets same setup |
| Hard to share custom skills | One-click install from marketplace |

---

## Where to Find Plugins

| Source | What's there | URL |
|--------|--------------|-----|
| **Cursor Marketplace** | Official plugins (manually reviewed) | `cursor.com/marketplace` |
| **cursor.directory** | Community plugins and MCP servers | `cursor.directory` |

> *"Every plugin is manually reviewed before it's listed."*

**For beginners:** Start with the official marketplace. These plugins are vetted for security.

---

## What Plugins Can Contain

A plugin can bundle **any combination** of these components:

| Component | Description | Example |
|-----------|-------------|---------|
| **Rules** | Persistent AI guidance and coding standards | "Always use TypeScript", "Never use console.log" |
| **Skills** | Specialized agent capabilities for complex tasks | "Code reviewer skill", "Test generator skill" |
| **Agents** | Custom agent configurations and prompts | A pre-configured agent for API design |
| **Commands** | Agent-executable command files | `/review-my-code`, `/generate-tests` |
| **MCP Servers** | Model Context Protocol integrations | Connect to external databases or APIs |
| **Hooks** | Automation scripts triggered by events | Run tests after code changes |

---

## The Marketplace

### Official Marketplace:

- Plugins are distributed as **Git repositories**
- Submitted through the **Cursor team**
- **Every plugin is manually reviewed** before listing
- Browse at: `cursor.com/marketplace`

### Community Plugins:

- Browse at: **cursor.directory**
- Not manually reviewed by Cursor
- Use at your own risk

---

## Team Marketplaces (For Organizations)

Team marketplaces are available on **Teams and Enterprise plans**.

| Plan | Number of Team Marketplaces |
|------|----------------------------|
| **Teams plan** | Up to 1 |
| **Enterprise plan** | Unlimited |

### Where to Find Team Marketplace Settings:

- Dashboard → Settings → Plugins → Team Marketplaces
- On Enterprise plans, **only admins** can add team marketplaces

---

## Required vs. Optional Plugins

When you assign a plugin to a distribution group, you can set it as:

| Type | What it means |
|------|---------------|
| **Required** | Installed automatically for everyone in the distribution group |
| **Optional** | Available to everyone, but each developer chooses whether to install |

### Distribution Groups with SCIM:

If your organization uses **SCIM** (automated user provisioning):
- Manage group membership in your **identity provider** (Okta, Azure AD, etc.)
- Cursor syncs those group updates automatically

---

## Adding a Team Marketplace (Step by Step)

| Step | What to do |
|------|------------|
| **1** | Go to Dashboard → Settings → Plugins |
| **2** | In Team Marketplaces, click **Import** |
| **3** | Paste the GitHub repository URL |
| **4** | Review the parsed plugins (optionally set Team Access groups) |
| **5** | Set marketplace name and description, then save |

### Example Repository to Try:

`fieldsphere/cursor-team-marketplace-template`

---

## Where Developers Find Team Marketplaces

Developers can find team marketplaces in the **marketplace panel in Cursor**:

1. Open the marketplace panel in Cursor
2. Look for plugins from your team marketplace
3. Install optional plugins directly from the panel
4. Required plugins are **installed automatically**

---

## Installing Plugins

Install plugins from the marketplace. Plugins can be:

| Scope | What it means |
|-------|---------------|
| **Project level** | Only affects the current project |
| **User level** | Affects all your projects |

---

## MCP Apps Deeplinks

Share MCP server configurations using **install links**:

```
cursor://anysphere.cursor-deeplink/mcp/install?name=NAME&config=BASE64_ENCODED_CONFIG
```

**For beginners:** This is an advanced feature for sharing MCP setups with teammates.

---

## Managing Installed Plugins

### MCP Servers:

To toggle MCP servers on/off:

| Step | Action |
|------|--------|
| 1 | Open Settings (`Ctrl+Shift+J`) |
| 2 | Go to Features → Model Context Protocol |
| 3 | Click the toggle next to any server |

**Disabled servers won't load or appear in chat.**

### Rules and Skills:

Manage rules and skills from the **Rules section** of Cursor Settings.

**Modes for rules:**

| Mode | What it means |
|------|---------------|
| **Always** | Rule is always applied |
| **Agent Decides** | Agent chooses whether to use it |
| **Manual** | You must manually invoke it |

**Skills** appear in the Agent Decides section and can be invoked manually with `/skill-name` in chat.

---

## Using the Extension API (For Developers)

Extensions can register plugin directories programmatically.

**Use case:** Distributing plugins bundled inside VS Code extensions or automating plugin setup.

**API method:** `vscode.cursor.plugins.registerPath()`

**For beginners:** This is for advanced developers building VS Code extensions.

---

## Creating Plugins (For Developers)

A plugin is a **directory** with:
- `.cursor-plugin/plugin.json` (manifest)
- Your components (rules, skills, agents, commands, hooks, or MCP servers)

### File Structure:

```
my-plugin/
├── .cursor-plugin/
│   └── plugin.json
├── .rules/
│   └── coding-standards.mdc
├── .skills/
│   └── code-reviewer/
│       └── SKILL.md
└── .mcp.json
```

### Example `plugin.json`:

```json
{
  "name": "my-plugin",
  "description": "Custom development tools",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

### Start from Template:

Use the **plugin template repository** or create from scratch.

---

## Testing Plugins Locally

Before you publish, load your plugin from `~/.cursor/plugins/local`:

| Step | Action |
|------|--------|
| **1** | Create folder: `~/.cursor/plugins/local/my-plugin` |
| **2** | Copy your plugin files into that folder |
| **3** | Restart Cursor (or `Developer: Reload Window`) |
| **4** | Verify plugin components load in Cursor |

### For Faster Iteration (Symlink):

```bash
ln -s /path/to/my-plugin ~/.cursor/plugins/local/my-plugin
```

This lets you edit files in your source directory and see changes without copying.

---

## Publishing a Plugin

When your plugin is ready:

1. Submit it for review at: **`cursor.com/marketplace/publish`**
2. For multi-plugin repositories, add a marketplace manifest at `.cursor-plugin/marketplace.json`

### For Team/Enterprise Marketplaces:

- Contact Sales for private team marketplaces
- Organization-wide plugin distribution

---

## FAQ (From Documentation)

The documentation lists these FAQs:

1. **Are marketplace plugins reviewed for security?**
   - Official marketplace: ✅ Yes, manually reviewed
   - Community plugins (cursor.directory): ❌ Not reviewed by Cursor

2. **How do I create a plugin?**
   - Use the plugin template repository
   - Or create from scratch with `.cursor-plugin/plugin.json`

---

## Common Beginner Questions

### Q: Do I need plugins as a beginner?
**A:** Not necessarily. Start with built-in features. Plugins are for advanced customization.

### Q: Are plugins safe?
**A:** Official marketplace plugins are manually reviewed. Community plugins (cursor.directory) are not – use at your own risk.

### Q: Can I create my own plugin?
**A:** Yes! Anyone can create plugins. Submit to the marketplace for official listing.

### Q: What's the difference between a rule and a skill?
**A:** Rules are persistent guidelines ("always do X"). Skills are specialized capabilities for complex tasks.

### Q: Can teams have private plugins?
**A:** Yes – Team marketplaces let you distribute plugins privately to your organization.

### Q: How do I install a plugin?
**A:** From the marketplace panel in Cursor.

---

## Quick Reference Card

| Concept | Description |
|---------|-------------|
| **Plugins** | Bundles of rules, skills, agents, commands, MCP servers, hooks |
| **Marketplace** | Where to find official plugins (cursor.com/marketplace) |
| **cursor.directory** | Where to find community plugins (not reviewed) |
| **Team marketplace** | Private plugins for your organization |
| **Required plugin** | Auto-installed for everyone |
| **Optional plugin** | Available for individual install |
| **Plugin structure** | `.cursor-plugin/plugin.json` + components |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are plugins?** | Bundles of rules, skills, and agents for Cursor |
| **Where do I find them?** | Cursor Marketplace or cursor.directory |
| **Are they safe?** | Official ones are reviewed; community ones are not |
| **Do I need to make one?** | No – only if you want to share customizations |
| **Can teams have private plugins?** | Yes – Team marketplaces |
| **How do I install?** | From the marketplace panel in Cursor |

---

## The Bottom Line

**Plugins are how you package and share AI behaviors in Cursor.**

**Think of it as:**
- **Without plugins** = Cooking every meal from scratch 🍳
- **With plugins** = Using recipe books and meal kits 📚

**For beginners:** You don't need to worry about creating plugins. But you might enjoy **installing** plugins from the marketplace. Look for plugins that add rules or skills relevant to your work.

**For teams:** Team marketplaces are powerful. You can standardize coding standards (rules) and share specialized skills across your organization with one click.

**The plugin ecosystem is growing.** As more developers create plugins, Cursor becomes more powerful and customizable.

Would you like me to explain how to create a specific type of plugin (like a rule or skill), or move on to another document?