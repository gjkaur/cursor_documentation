This is the **Billing Groups** documentation – it explains how Enterprise admins can understand and manage spend across groups of users.

Think of this as the **cost allocation tool** for enterprises – useful for reporting, internal chargebacks, and budgeting across teams.

Let me break this down.

---

## What Are Billing Groups?

**Billing groups allow Enterprise admins to understand and manage spend across groups of users.** This functionality is useful for reporting, internal chargebacks, and budgeting.

> *"Billing groups are available on the Enterprise plan."*

---

## Billing Group Architecture

| Rule | Description |
|------|-------------|
| **One group per member** | Members can only be in one billing group at a time |
| **Unassigned group** | Members not actively assigned to any group are placed in a reserved "Unassigned" group |
| **Time-based attribution** | All usage is attributed to the user's group at the time it occurs |
| **Historical data** | Does not change when users move between groups |
| **Group deletion** | When a group is deleted, all its usage is moved to the Unassigned group |

---

## View Billing Groups

Enterprise admins can view billing groups in the web dashboard under the **Members & Groups** tab.

The table shows:
| Column | Description |
|--------|-------------|
| Group Name | Name of the billing group |
| Members | Number of members in the group |
| Unassigned | Number of unassigned users |
| Spend | Spend for the period |
| Actions | Edit/Delete options |

---

## Create and Add Members to a Billing Group

Admins can create billing groups by clicking **Create Group**. After naming the group, there are **four ways** to assign members:

| Method | Description |
|--------|-------------|
| **SCIM** | Sync the billing group with an existing SCIM group |
| **API** | Create groups and add members programmatically via the Admin API |
| **CSV** | Upload a CSV with group names and email addresses of members |
| **Manual** | Click Add Members and manually select Unassigned members |

> *"Billing groups synced with SCIM cannot be edited via CSV, API, or manual UI changes. All member assignment for SCIM-synced groups must be handled via SCIM."*

---

## Move Members Between Billing Groups

| Method | How it works |
|--------|--------------|
| **Manual groups** | Click on billing group and select Move |
| **SCIM** | When members are moved between SCIM groups in your identity provider, the billing group follows automatically |
| **API** | Use add members and remove members endpoints to move programmatically |

---

## Rename a Billing Group

| Method | Action |
|--------|--------|
| **UI** | Click the gear button on main menu, or click Rename on the group page |
| **API** | Use the update group endpoint |

---

## Delete a Billing Group

| Method | Action |
|--------|--------|
| **UI** | Click the gear button on main menu, or click Delete on the group page |
| **API** | Use the delete group endpoint |

> *"Deleting a billing group is a destructive operation; data cannot be recovered. All historic usage for deleted groups is assigned retroactively to the Unassigned group."*

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Reporting** | See spend by department, team, or project |
| **Internal chargebacks** | Allocate costs back to business units |
| **Budgeting** | Track spend against budgets for different teams |

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **Availability** | Enterprise plan only |
| **Location** | Dashboard → Members & Groups tab |
| **Assignment methods** | SCIM, API, CSV, Manual |
| **Members per group** | One group at a time |
| **Unassigned** | Auto-created group for unassigned members |
| **Historical attribution** | Time-based, doesn't change on moves |
| **SCIM-synced groups** | Cannot be edited via UI/API/CSV |

---

## Common Beginner Questions

### Q: Are billing groups available on Teams plans?
**A:** No – billing groups are only available on Enterprise plans.

### Q: Can a member be in multiple billing groups?
**A:** No – members can only be in one billing group at a time.

### Q: What happens to unassigned members?
**A:** They are placed in a reserved "Unassigned" group automatically.

### Q: Can I edit a SCIM-synced billing group manually?
**A:** No – SCIM-synced groups must be managed via SCIM. Manual changes are not allowed.

### Q: What happens to historical usage when I delete a group?
**A:** All historic usage for the deleted group is moved to the Unassigned group. This cannot be undone.

### Q: How do I see spend by group?
**A:** View the billing groups table in the dashboard under Members & Groups tab.

---

## The Bottom Line

**Billing groups give Enterprise admins the ability to track and manage spend across teams – essential for reporting, chargebacks, and budgeting.**

**Key features:**
- **One group per member** – clear attribution
- **Four assignment methods** – SCIM, API, CSV, Manual
- **Time-based attribution** – usage tracked to group at time of use
- **SCIM integration** – automatic sync with identity provider groups
- **Unassigned group** – catch-all for members without a group

**For enterprise finance and IT teams:** Billing groups enable:
- Cost allocation by department or team
- Chargebacks to business units
- Budget tracking across projects
- Programmatic management via Admin API

Would you like me to explain any specific billing group feature in more detail?