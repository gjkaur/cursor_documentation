This is the **CLI Authentication** reference documentation – it explains how to authenticate the Cursor CLI using either **browser-based login** (recommended for humans) or **API keys** (for automation and CI/CD).

Think of this as the **login guide** for the `agent` command – how to prove who you are to use Cursor from the terminal.

Let me break this down.

---

## Two Authentication Methods

| Method | Best for | How it works |
|--------|----------|--------------|
| **Browser authentication** | Interactive use (humans) | Opens browser, you log in once |
| **API key authentication** | Automation, scripts, CI/CD | Use API key from dashboard |

---

## Method 1: Browser Authentication (Recommended)

This is the easiest way for interactive use.

### Commands:

```bash
# Log in using browser flow
agent login

# Check authentication status
agent status

# Log out and clear stored authentication
agent logout
```

### How It Works:

1. Run `agent login`
2. Your default browser opens
3. You authenticate with your Cursor account
4. Credentials are **securely stored locally**
5. You're ready to use the CLI

> *"The login command will open your default browser and prompt you to authenticate with your Cursor account. Once completed, your credentials are securely stored locally."*

---

## Method 2: API Key Authentication

Best for automation, scripts, and CI/CD environments where you can't use a browser.

### Step 1: Generate an API Key

Generate a **user API key** from:
- Cursor Dashboard → Integrations → API Keys

### Step 2: Use the API Key

You can provide the API key in two ways:

#### Option 1: Environment Variable (Recommended)

```bash
export CURSOR_API_KEY=your_api_key_here
agent "implement user authentication"
```

#### Option 2: Command Line Flag

```bash
agent --api-key your_api_key_here "implement user authentication"
```

---

## Authentication Status

Check your current authentication status:

```bash
agent status
```

This command displays:
- Whether you're authenticated
- Your account information
- Current endpoint configuration

---

## Logout

To clear stored authentication:

```bash
agent logout
```

This logs you out and removes locally stored credentials.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **"Not authenticated" errors** | Run `agent login` or ensure your API key is correctly set |
| **SSL certificate errors** | Use `--insecure` flag for development environments |
| **Endpoint issues** | Use `--endpoint` flag to specify a custom API endpoint |

---

## Quick Reference Card

| Command | Purpose |
|---------|---------|
| `agent login` | Browser-based login |
| `agent status` | Check authentication status |
| `agent logout` | Clear stored authentication |
| `export CURSOR_API_KEY=...` | Set API key as env var |
| `agent --api-key <key>` | Pass API key as CLI flag |

### API Key Generation:

| Location | Action |
|----------|--------|
| Cursor Dashboard → Integrations → API Keys | Generate user API key |

---

## Common Beginner Questions

### Q: Do I need to log in every time I use the CLI?
**A:** No – once you run `agent login`, credentials are stored locally. You stay logged in until you run `agent logout`.

### Q: Can I use both authentication methods?
**A:** Yes, but the last one used will be active.

### Q: Is the API key secure?
**A:** Store it as an environment variable, never hardcode it in scripts. Use `export CURSOR_API_KEY=...` in your CI/CD secrets.

### Q: What's the difference between user API key and service account?
**A:** User API key is tied to your account. Service account keys are for team automation (see Service Accounts documentation).

### Q: How do I check if I'm logged in?
**A:** Run `agent status`.

### Q: What does `agent logout` do?
**A:** Clears stored credentials – you'll need to `agent login` again.

---

## The Bottom Line

**Authentication is simple: `agent login` for interactive use, or `CURSOR_API_KEY` env var for scripts.**

**For most users:** Just run `agent login` once and you're done.

**For automation:** Generate an API key from the dashboard and set `CURSOR_API_KEY` in your environment.

**Remember:** Keep your API key secret – never commit it to version control.

