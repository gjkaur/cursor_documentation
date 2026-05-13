This is the **Canvases** documentation – it explains how Cursor can create **interactive visual artifacts** that render next to your chat. Instead of scrolling through long markdown tables or code blocks, you get a beautiful, standalone view.

Think of Canvases as Cursor's way of **showing you data visually** – like dashboards, reports, and analyses – rather than just dumping raw text.

Let me break this down for a complete beginner.

---

## What Are Canvases? (The 10-Second Summary)

**Canvases let Cursor create interactive artifacts that render next to the chat.** Instead of scrolling through a long markdown table or code block, you get a standalone view with sections, stats, and tables.

| Without Canvases | With Canvases |
|------------------|---------------|
| Agent dumps raw data as text | Data appears in a beautiful dashboard |
| You scroll through long tables | You see organized sections and stats |
| Hard to understand at a glance | Easy to read and interact with |
| Can't easily revisit | Saved in your workspace |

---

## When Does Cursor Use Canvases?

Cursor automatically creates a canvas when:
1. Your task benefits from a **visual or interactive view**
2. You **ask for one directly**

**Examples of when Cursor might use a canvas:**
- "Show me a dashboard of my API usage"
- "Analyze our test coverage"
- "Create a dependency audit report"
- "Give me a quarterly revenue report"

Instead of giving you raw numbers in chat, Cursor builds a **beautiful, organized view**.

---

## How Canvases Work (4 Steps)

| Step | What happens |
|------|--------------|
| **1** | Cursor decides a canvas would help (or you ask for one) |
| **2** | Cursor builds the canvas and inserts a reference in your chat |
| **3** | You review the rendered view, tweak it, or ask Cursor to change it |
| **4** | Cursor saves the canvas so you can reopen it later with fresh data |

### Step 1: Triggering a Canvas

**Automatic:** Cursor detects that your task would benefit from a visual view.

**Manual:** You ask directly – "Create a canvas showing..." or "Visualize this as a dashboard..."

### Step 2: Building the Canvas

Cursor creates the canvas and puts a **card** at the end of its response. Click it to open.

### Step 3: Review and Refine

You can:
- Review the rendered view
- Switch to the source code to tweak it manually
- Ask Cursor to change it ("Make the chart show weekly instead of daily")

### Step 4: Saving

**Each canvas appears in your workspace's canvas list**, so you can jump back to past ones without rerunning them.

---

## Opening a Canvas

| Method | How to do it |
|--------|--------------|
| **From Cursor** | Click the card at the end of the response |
| **Command Palette** | Run "Open Canvas" (listed under View) |
| **Agents Window** | Open a canvas tab from the new tab menu |

---

## Iterating on a Canvas (Making Changes)

Canvases are designed to be **easy to refine**:

| Problem | Solution |
|---------|----------|
| **Layout isn't right** | Tell Cursor what to change instead of editing by hand |
| **Numbers look stale/off** | Ask Cursor to rerun the underlying query or show its work |
| **Large rework needed** | Revert and prompt Cursor again with more details (faster than small follow-ups) |
| **Small tweaks** | Manually edit the source code |

> *"For larger reworks, revert and prompt Cursor again with more details. This is usually faster than nudging through small followups."*

**This is a key insight:** Instead of making 10 tiny requests to fix a canvas, just start over with a better description. It's faster.

---

## Packaging Canvases as Skills (Advanced)

Common canvas workflows can be packaged as **skills** so Cursor produces a consistent layout every time you ask.

### What a Canvas Skill Includes:

| Component | What it defines | Example |
|-----------|-----------------|---------|
| **Trigger description** | When Cursor should use this skill | "quarterly revenue report" or "dependency audit" |
| **Layout instructions** | Sections, stats, tables the canvas should contain | Header with KPI cards, then line chart, then data table |
| **Data sources and queries** | How to populate the view | SQL query, API call, or shell command |
| **Formatting rules** | Units, date ranges, sort order | "$" for currency, "MM/DD/YYYY" for dates |

### Once a skill is in place:

- A **short prompt** is enough to regenerate the canvas with fresh data
- **Every teammate** using the skill gets the same output shape

**For beginners:** You don't need to create skills initially. Just know they exist for power users and teams.

---

## Real-World Examples

### Example 1: API Usage Dashboard

**You ask:**
> "Show me a dashboard of my API usage for the last 30 days"

**Without Canvas:** Agent dumps a table of numbers in chat:
```
Day 1: 1,234 requests
Day 2: 1,456 requests
Day 3: 1,201 requests
...
```

**With Canvas:** Agent creates a beautiful dashboard with:
- KPI cards (Total requests, Average latency, Error rate)
- Line chart showing trends
- Table of daily breakdowns
- Filters to change date range

### Example 2: Dependency Audit

**You ask:**
> "Audit our package dependencies for security vulnerabilities"

**Canvas shows:**
- Summary cards (Total packages, Vulnerable count, Critical issues)
- Color-coded table of vulnerable packages
- Links to remediation steps
- Charts showing risk levels

### Example 3: Test Coverage Report

**You ask:**
> "Analyze our test coverage"

**Canvas shows:**
- Overall coverage percentage
- Breakdown by file/folder
- Chart of coverage over time
- List of uncovered functions

### Example 4: Quarterly Revenue Report

**You ask:**
> "Create a quarterly revenue report"

**Canvas shows:**
- Revenue by month (bar chart)
- Growth percentage
- Comparison to previous quarter
- Breakdown by product/service

---

## Canvas vs. Regular Chat Response

| Feature | Regular Chat | Canvas |
|---------|--------------|--------|
| **Format** | Text/markdown | Visual dashboard |
| **Interactivity** | None | Can click, filter, explore |
| **Reusability** | Scroll back in chat | Saved in workspace list |
| **Refreshing data** | Ask again | Rerun query |
| **Editing** | Tell Agent to regenerate | Tell Agent OR edit source |
| **Best for** | Simple answers | Complex data, reports, dashboards |

---

## Common Beginner Questions

### Q: Do I need to request a canvas, or does Cursor decide?
**A:** Both. Cursor automatically uses canvases when helpful, but you can also ask directly.

### Q: Can I edit a canvas manually?
**A:** Yes, for small tweaks you can edit the source code directly.

### Q: Are canvases saved forever?
**A:** They appear in your workspace's canvas list. You can reopen them anytime.

### Q: Can I refresh a canvas with new data?
**A:** Yes – ask Cursor to rerun the underlying query.

### Q: Can I share canvases with my team?
**A:** If you package them as skills, yes – teammates get the same output shape.

### Q: What kinds of things work well in canvases?
**A:** Dashboards, reports, audits, analyses, anything with data that benefits from visualization.

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **What they are** | Interactive visual artifacts rendered next to chat |
| **When used** | When a visual view is better than text |
| **How to open** | Click card, Command Palette, or Agents Window |
| **Saving** | Automatically saved to workspace canvas list |
| **Iteration** | Tell Cursor changes, or edit source manually |
| **Skills** | Package common canvases for consistent output |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Canvases?** | Visual dashboards and reports created by Cursor |
| **When do they appear?** | When a visual view is better than text |
| **How do I open one?** | Click the card at the end of the response |
| **Can I change it?** | Yes – tell Cursor or edit the source |
| **Are they saved?** | Yes – in your workspace's canvas list |
| **Can I refresh data?** | Yes – ask Cursor to rerun the query |

---

## The Bottom Line

**Canvases transform raw data into beautiful, readable dashboards.**

**Think of it as:**
- **Without Canvases** = Getting a spreadsheet dumped in an email 📊📧
- **With Canvases** = Getting an interactive dashboard 📊✨

**For beginners:** When you ask Cursor for data analysis, reports, or audits, expect to see a canvas. Click the card, explore the visual view, and if something isn't right, just tell Cursor what to change.

**The most exciting features:**
1. **Automatic visualization** – Cursor decides when a canvas would help
2. **Saved canvases** – Reopen past reports anytime
3. **Iteration** – Tell Cursor to fix the layout instead of editing by hand
4. **Skills** – Create reusable canvas templates for your team

Would you like me to explain how to create custom canvas skills, or move on to another document?