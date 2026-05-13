This is the **Search Tools** documentation – it explains how the Agent finds code in your codebase. The Agent has multiple ways to search, and it automatically picks the right strategy based on what you ask.

Think of this as the Agent having **super-powered search** – it can find code by exact name OR by meaning, even when you don't know the exact words.

Let me break this down for a complete beginner.

---

## What Are Search Tools? (The 10-Second Summary)

**Agent combines multiple search tools to find relevant code across your codebase.** You describe what you're looking for in natural language, and Agent picks the right strategy.

| Without Search Tools | With Search Tools |
|---------------------|-------------------|
| You manually browse folders | Agent finds code instantly |
| You guess where things are | Agent searches by meaning |
| You miss relevant files | Agent finds everything related |

---

## Two Main Search Methods

The Agent has two fundamental ways to search:

| Search Type | What it does | Best for |
|-------------|--------------|----------|
| **Grep (Instant Grep)** | Exact text matching | When you know the exact name (function, variable, error string) |
| **Semantic Search** | Search by meaning | When you don't know exact names, just describe what it does |

---

## 1. Instant Grep (Exact Matching) 🔍

**The fastest way to find code is an exact match:** a function name, variable, error string, or regex pattern.

Agent uses **grep** automatically when you reference specific symbols.

### What is grep?

Grep is a command-line tool that searches for exact text patterns. Think of it like `Ctrl+F` (Find) but across your entire codebase.

### Cursor's Custom Engine: Instant Grep

Cursor ships with **Instant Grep**, a custom search engine that outperforms traditional grep on large codebases.

**Key features:**
- Runs automatically – no configuration needed
- Supports **full regex** (powerful pattern matching)
- Supports **word-boundary matching**

### Regex Examples:

| Pattern | What it finds |
|---------|---------------|
| `import .*PaymentService` | Any import statement that includes PaymentService |
| `PaymentFailedError` | Exact error name |
| `\buser\b` | The word "user" as a whole word (not "username" or "userData") |

**Why this matters:** Agent can construct precise patterns to trace references across files.

---

## 2. Semantic Search (Search by Meaning) 🧠

**When you don't know the exact name, semantic search finds code by meaning.**

### The Magic:

Ask: *"Where do we handle authentication?"*

Agent can find `middleware/auth.ts` even though the word "authentication" never appears in the file!

**How?** The file contains code about login, sessions, tokens, and user verification – which is semantically related to "authentication."

### Why This Is Powerful:

| Traditional Search | Semantic Search |
|-------------------|-----------------|
| Must match exact words | Finds related concepts |
| Returns nothing if words don't match | Returns relevant files even with different terminology |
| "Find payment code" finds files with "payment" | "Find checkout code" finds payment files too |

### The Research:

> *"Research on Cursor's semantic search shows that combining it with grep produces 12.5% higher accuracy answering codebase questions compared to grep alone. The improvement is largest on codebases with 1000+ files."*

**For large projects:** Semantic search is a game-changer.

---

## How Semantic Search Indexing Works 📚

Cursor builds a **search index** of your codebase. Here's how:

### Step 1: Chunking
Cursor breaks your code into meaningful chunks:
- Functions
- Classes
- Logical blocks

### Step 2: Vector Embedding
Each chunk is converted into a **vector embedding** – a mathematical representation that captures its meaning.

Think of it as a "fingerprint" of what the code DOES, not just what it says.

### Step 3: Storage
Embeddings are stored in a vector database.

### Step 4: Searching
When you search, your query is converted into a vector using the same model and matched against the stored embeddings.

### Indexing Timeline:

| Event | What happens |
|-------|--------------|
| **Workspace opened** | Indexing begins automatically |
| **80% complete** | Semantic search becomes available |
| **100% complete** | Full search capability |

### Keeping the Index Current:

| Change | Action |
|--------|--------|
| **New files** | Added to index automatically |
| **Modified files** | Old embeddings removed, new ones created |
| **Deleted files** | Removed from index |

**Sync happens automatically every 5 minutes** (only changed files).

---

## Configuration and Privacy

### Check Indexing Status:

Go to **Cursor Settings > Indexing**

### What Gets Indexed:

Cursor indexes all files **except** those in ignore files:
- `.gitignore`
- `.cursorIgnore`

**Pro tip:** Ignoring large generated files or logs improves search accuracy.

### View Included Files:

**Cursor Settings > Indexing & Docs > View included files**

---

## Privacy and Security 🔒

This is important for people worried about their code being sent to the cloud.

| What happens | Security measure |
|--------------|------------------|
| **File paths** | Encrypted before sending to Cursor's servers |
| **Code content** | Never stored in plaintext – held in memory during indexing, then discarded |
| **Embeddings** | Created without storing filenames or source code |
| **Searching** | Cursor retrieves embeddings, decrypts chunks on YOUR client side |

**Your code is not stored on Cursor's servers in readable form.**

---

## How Agent Combines Search Tools

Agent picks the right tool based on your prompt – **you don't choose**. Just describe what you need.

| Prompt Style | Tools Used | Example |
|--------------|------------|---------|
| **Specific symbol or string** | Grep | "Find all files that import PaymentService" |
| **Concept or behavior** | Semantic search, then grep to fill details | "How does our app handle failed payments?" |
| **Complex exploration** | Multiple searches, file reads, reference following | "Map the data flow from checkout to confirmation email" |

### Complex Task Example:

For a complex query like *"Map the data flow from checkout to confirmation email,"* Agent might:

1. **Semantic search** to find entry points (checkout-related code)
2. **Grep** to trace specific function references
3. **File reads** to build full context
4. **Reference following** to see how data moves between files

---

## Tips for Better Search Results

### 1. Start Specific, Then Go Broad

| If you know... | Do this |
|----------------|---------|
| **The exact function name** | Say it! "Find all callers of `processOrder`" |
| **You're exploring unfamiliar code** | Describe the behavior "How does payment processing work?" |

### 2. Explore Before Changing

Ask Agent to **show existing patterns** before asking it to add new ones.

**Why this matters:** Prevents Agent from creating duplicates or breaking existing conventions.

**Example:** Instead of "Add a new API endpoint," first ask "How are existing API endpoints structured?"

### 3. Reference Concrete Code

| Good prompt (specific) | Bad prompt (vague) |
|------------------------|---------------------|
| "Find all callers of `processOrder`" | "Find the order code" |
| "Where is `PaymentFailedError` used?" | "Find payment errors" |

> *"Prompts like 'find all callers of processOrder' give Agent an exact target. Prompts like 'find the order code' force Agent to guess what you mean."*

---

## Real-World Examples

### Example 1: Finding a Specific Function

**You ask:** "Where is `calculateTotal` defined?"

**Agent uses:** Grep (exact match)

**Finds:** `src/utils/cart.js` line 42

### Example 2: Understanding a Concept

**You ask:** "How does the app handle user authentication?"

**Agent uses:** Semantic search first, then grep

**Finds:** 
- `src/middleware/auth.js` (even though "authentication" isn't in the file)
- `src/utils/jwt.js`
- `src/routes/login.js`

### Example 3: Tracing a Bug

**You ask:** "What files touch the `userSession` variable?"

**Agent uses:** Grep for exact variable name

**Finds:** All 12 files where `userSession` appears

### Example 4: Large Codebase Exploration

**You ask (new to project):** "Where should I start to understand the payment flow?"

**Agent uses:** Semantic search to find payment-related concepts, then reads key files

**Shows you:** 
- `src/payment/checkout.js` (entry point)
- `src/payment/processor.js` (core logic)
- `src/payment/webhooks.js` (external integrations)

---

## FAQ (From Documentation)

The documentation lists these FAQs (though answers aren't shown in your file):

1. Is my source code stored on Cursor servers?
2. How long are indexed codebases retained?
3. Can I customize path encryption?
4. How does team sharing work?
5. Does Cursor support multi-root workspaces?

**For beginners:** The privacy section above answers #1 (no, code isn't stored in readable form).

---

## Common Beginner Questions

### Q: Do I need to choose between grep and semantic search?
**A:** No. Agent chooses automatically based on your prompt.

### Q: How long does indexing take?
**A:** Depends on codebase size. You can search at 80% completion.

### Q: Can I see what's indexed?
**A:** Yes – Settings > Indexing & Docs > View included files

### Q: Does semantic search work offline?
**A:** No, it uses Cursor's servers for embedding generation.

### Q: What if Agent can't find something?
**A:** Try being more specific, or use `@` mentions to point to relevant files.

### Q: Can I exclude files from indexing?
**A:** Yes – add them to `.gitignore` or `.cursorIgnore`.

---

## Quick Reference Card

| Search Type | What it does | Best for |
|-------------|--------------|----------|
| **Instant Grep** | Exact text matching | Known function/variable names |
| **Semantic Search** | Search by meaning | Unknown exact names, concepts |
| **Combined** | Both strategies | Complex exploration |

| Feature | Details |
|---------|---------|
| **Indexing start** | Automatic when workspace opens |
| **Search available** | At 80% indexing completion |
| **Sync frequency** | Every 5 minutes (changed files only) |
| **Privacy** | Code never stored in plaintext |
| **Ignore files** | `.gitignore`, `.cursorIgnore` |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Search Tools?** | Ways Agent finds code in your codebase |
| **What's grep?** | Exact text matching (like `Ctrl+F` across all files) |
| **What's semantic search?** | Finds code by meaning, even without exact words |
| **Do I choose the tool?** | No – Agent picks automatically |
| **Is my code stored?** | No – encrypted, never stored in readable form |
| **When is search available?** | After 80% indexing (automatic) |

---

## The Bottom Line

**Search tools are how Agent navigates your codebase without you pointing to every file.**

**Think of it as:**
- **Grep** = `Ctrl+F` on steroids (find exact text) 🔍
- **Semantic search** = "I know what it does, not what it's called" 🧠

**For beginners:** Just describe what you want in plain English. Agent will figure out the right search method. The more specific you are, the better the results.

**The most powerful insight:** You don't need to know where things are. Just ask Agent to find them. It will search by exact name OR meaning and show you what's relevant.

Would you like me to explain regex patterns for Instant Grep, or move on to another document?