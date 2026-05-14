This is the **Privacy and Data Governance** documentation – it explains how data flows through Cursor, what guarantees you have, and where data lives.

Think of this as the **security deep dive** for compliance teams – covering everything from indexing to LLM requests to Cloud Agents, with details on Privacy Mode, encryption, and data retention.

Let me break this down.

---

## Three Data Flows

There are **three ways data leaves your local environment** when using Cursor:

| Flow | What it does |
|------|--------------|
| **1. Indexing process** | Creates embeddings for semantic search |
| **2. LLM requests** | Sends prompts and code context to AI providers |
| **3. Cloud Agents** | Runs agents in isolated VMs (optional) |

---

## 1. The Indexing Process (Semantic Search)

When you open a project in Cursor, we create **embeddings** (mathematical representations) that power semantic search.

### What Gets Sent:

| Item | Status |
|------|--------|
| Your code | Temporarily, to create embeddings |
| Storage | **Nothing is stored** – embeddings generated, original code discarded |

### What Gets Stored:

| Item | Description |
|------|-------------|
| **One-way mathematical embeddings** | Vectors that represent code semantics (cannot be reverse-engineered) |
| **Obfuscated file paths** | Paths are obscured |
| **Line numbers** | For code location |

### How It Works:

1. You ask a question or use Cmd+K
2. Cursor creates an embedding from your request
3. Searches for similar embeddings in the vector database
4. Returns obfuscated file paths and line numbers
5. Cursor looks up actual code on your **local machine** using those coordinates

> *"The vector database never sees your raw code. It only stores mathematical representations that can't be reverse-engineered back to source code."*

---

## 2. LLM Requests (AI Features)

When you use AI features, we send prompts and code context to language model providers like OpenAI, Anthropic, and Google.

### With Privacy Mode Enabled:

| Guarantee | Status |
|-----------|--------|
| Code stored by model providers | ❌ Never |
| Code used for training | ❌ Never |
| Zero Data Retention (ZDR) agreements | ✅ In place |

### Zero Data Retention Agreements:

Cursor has **contractual ZDR policies** with:

| Provider | ZDR Agreement |
|----------|---------------|
| OpenAI | ✅ |
| Anthropic | ✅ |
| Google Vertex AI | ✅ |
| xAI Grok | ✅ |

> *"These agreements legally prevent providers from storing inputs or outputs or using your data for training."*

### Privacy Mode Default:

> *"Privacy Mode is on by default for Enterprise teams."*

---

## 3. Cloud Agents (Optional)

**Cloud Agents are the only feature that requires Cursor to store code.** Unlike indexing or LLM requests, Cloud Agents need access to your repository over time to make changes.

### Architecture:

| Feature | Description |
|---------|-------------|
| **Isolated VMs** | Agents run in isolated virtual machines |
| **Dedicated environment** | Each agent has its own environment |
| **Isolation** | Separated from other agents and users |

### What Gets Stored:

| Item | Status |
|------|--------|
| Encrypted copies of repositories | ✅ Stored temporarily while agent runs |
| Retention | Deleted after agent completes |

### Optional Feature:

> *"Cloud Agents are optional. If your security policy prohibits code storage, don't enable Cloud Agents. You can still use all other Cursor features."*

---

## Privacy Mode Enforcement

Privacy Mode can be enabled at the **team level** to ensure all team members benefit from ZDR guarantees.

### Team-Level Enforcement:

| Step | Action |
|------|--------|
| 1 | Go to your team dashboard |
| 2 | Navigate to Settings |
| 3 | Enable Privacy Mode for the team |
| 4 | Optionally enforce it so members can't disable it |

### MDM Enforcement (Additional Assurance):

Use the **Allowed Team IDs** policy to prevent users from logging into personal accounts (which might not have Privacy Mode enabled) on corporate devices.

> *"See Identity and Access Management for policy details and Deployment Patterns for MDM configuration."*

---

## Compliance and Contracts

| Feature | Description |
|---------|-------------|
| **DPA** | Comprehensive data protection commitments including data minimization, access control, and secure processing |
| **Sub-processors** | All covered by appropriate data processing agreements |

---

## Data Encryption

Cursor encrypts data for all infrastructure:

| Encryption Type | Standard |
|-----------------|----------|
| **In transit** | TLS 1.2+ |
| **At rest** | AES-256 |

### Customer Managed Encryption Keys (CMEK) – Enterprise

For enhanced security control, enterprise customers can use **Customer Managed Encryption Keys (CMEK)**.

| Feature | Description |
|---------|-------------|
| **Embeddings** | Encrypted using your customer encryption key |
| **Cloud Agent data** | Encrypted using your customer encryption key |
| **Key control** | You control key rotation and access |
| **Security** | Provides additional layer beyond standard encryption |

> *"Contact sales to enable CMEK for your organization."*

---

## Summary of Data Flows

| Feature | Code sent? | Code stored? | Encryption | Optional? |
|---------|------------|--------------|------------|-----------|
| **Indexing** | Temporarily | No (embeddings only, not reverse-engineerable) | TLS 1.2+/AES-256 | No |
| **LLM requests (Privacy Mode)** | Yes | No (ZDR agreements) | TLS 1.2+ | No |
| **Cloud Agents** | Yes | Yes (temporary, encrypted) | AES-256 + optional CMEK | ✅ Yes |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Indexing** | One-way embeddings only – no reverse engineering |
| **Privacy Mode** | Zero Data Retention with all AI providers – on by default for Enterprise |
| **Cloud Agents** | Only feature that stores code – optional |
| **Encryption** | TLS 1.2+ in transit, AES-256 at rest |
| **CMEK** | Enterprise – you control encryption keys |
| **Enforcement** | Team-level Privacy Mode + MDM Allowed Team IDs |

---

## Common Beginner Questions

### Q: Can my code be reverse-engineered from embeddings?
**A:** No – embeddings are one-way mathematical representations that cannot be reverse-engineered back to source code.

### Q: What Zero Data Retention agreements does Cursor have?
**A:** Contractual ZDR policies with OpenAI, Anthropic, Google Vertex AI, and xAI Grok – legally preventing storage or training.

### Q: Is Privacy Mode on by default for Enterprise teams?
**A:** Yes – Privacy Mode is on by default for Enterprise teams.

### Q: Are Cloud Agents required to use Cursor?
**A:** No – Cloud Agents are optional. If your security policy prohibits code storage, don't enable them.

### Q: Can I use my own encryption keys?
**A:** Yes – Customer Managed Encryption Keys (CMEK) are available for Enterprise customers.

### Q: How can I enforce Privacy Mode across my team?
**A:** Enable Privacy Mode in team dashboard and optionally enforce it. Use MDM Allowed Team IDs to prevent personal account logins.

---

## The Bottom Line

**Cursor's privacy and data governance model has three data flows, each with different guarantees.**

| Flow | Key Guarantee |
|------|---------------|
| **Indexing** | Only one-way embeddings (no reverse engineering) |
| **LLM requests** | Zero Data Retention with all providers (Privacy Mode) |
| **Cloud Agents** | Optional – temporary encrypted storage only |

**For security-conscious organizations:**
- Privacy Mode is **on by default** for Enterprise
- **ZDR agreements** legally prevent LLM providers from storing data
- **CMEK** gives you control over encryption keys
- **MDM policies** enforce team IDs to prevent personal account usage

**The bottom line:** Your code is protected at every stage – through one-way embeddings, ZDR agreements, encryption, and optional controls.

