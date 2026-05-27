# Exercise 10.2: Bulk Export via CSV Streaming

**Module 10:** AI Code Tracking and Reporting  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 10, Lesson 10.2)  
**Time:** 7 min  
**Difficulty:** Beginner

**Objective:** Stream large CSV exports for BI tools.

---

## API basics (read this first)

**Demonstration (Windows):** Use **PowerShell** in Cursor's terminal (``Ctrl+` ``).

1. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

2. Use **`curl.exe`** (not the `curl` alias) or Python `requests`.
3. Install **jq** for JSON parsing: `winget install jqlang.jq` or use Python instead.
4. Bash `curl` examples below each have a **PowerShell** equivalent — use those on Windows.
5. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps from the training slides

**Environment:** Windows 10/11 · **PowerShell** · use **`curl.exe`** (not the `curl` alias)

**Before API calls:** set your key (replace with your real key):

```powershell
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"
# Admin exercises use:
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"
```

Follow each step in order. Confirm the **Expected result** before moving on.

### Step 1 — Stream CSV download

```powershell
$end = Get-Date -Format "yyyy-MM-dd"
$start = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
curl.exe -s -u "$($env:CURSOR_ADMIN_API_KEY):" `
  "https://api.cursor.com/v1/analytics/ai-code/commits.csv?startDate=$start&endDate=$end" `
  -o cursor_commits_export.csv
```

**Expected result:** File `cursor_commits_export.csv` created in current directory.

---

### Step 2 — Preview rows

```powershell
Get-Content .\cursor_commits_export.csv -Head 10
```

**Expected result:** Header row + data rows visible in PowerShell.

---

### Step 3 — Open in Excel

**Do this:** Double-click CSV or **Open with** Excel.

**Expected result:** Columns sortable; suitable for pivot tables.

**Success criteria:** CSV downloaded · previewed · opened in spreadsheet tool
---

## Success criteria

- [ ] Streamed CSV · loaded into DataFrame · created BI-ready files

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] Admin API key from Exercise 1
- [ ] Cursor Enterprise plan
- [ ] `curl` installed
- [ ] Python 3.8+ with pandas (optional, for analysis)

---

## Step-by-Step Instructions

### Step 1: Download CSV from Command Line (2 minutes)

Download commit metrics as CSV for the last 30 days.

**Command:**
```bash
curl -L -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=30d&endDate=now" \
  -o ai_commits_30d.csv

# Preview the first few lines
head -5 ai_commits_30d.csv
```

**Expected output:**
```csv
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,commit_source,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4e5f6,user_abc123,alice@company.com,main-app,main,true,ide,120,30,50,10,40,5,30,15,"Add new feature",2025-01-15T14:12:03Z,2025-01-15T14:12:30Z
e5f6g7h8i9j0,user_abc123,alice@company.com,main-app,feature/auth,false,ide,85,15,30,5,25,3,30,7,"Add auth",2025-01-14T10:30:00Z,2025-01-14T10:30:45Z
```

---

### Step 2: Download by Date Range (2 minutes)

Download data for a specific date range.

**Command:**
```bash
curl -L -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-01-01&endDate=2025-01-31" \
  -o ai_commits_january.csv

# Count lines (minus header)
wc -l ai_commits_january.csv
```

---

### Step 3: Filter by Specific User (2 minutes)

Download AI commit data for a single developer.

**Command:**
```bash
curl -L -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=90d&endDate=now&user=alice@company.com" \
  -o alice_commits.csv

# Check how many commits
tail -n +2 alice_commits.csv | wc -l
```

---

### Step 4: Analyze CSV with Python/pandas (2 minutes)

**Create `analyze_commits.py`:**
```python
#!/usr/bin/env python3
"""
Analyze AI commit CSV data with pandas
"""

import pandas as pd
import os
import sys

def analyze_csv(filename):
    """Load and analyze AI commit CSV."""
    
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        print("   Run: python analyze_commits.py ai_commits_30d.csv")
        return
    
    print(f"📊 Analyzing {filename}")
    print("=" * 50)
    
    # Load CSV
    df = pd.read_csv(filename)
    
    print(f"\n📈 Basic Statistics")
    print("-" * 30)
    print(f"   Total commits: {len(df):,}")
    print(f"   Date range: {df['commit_ts'].min()} to {df['commit_ts'].max()}")
    print(f"   Unique users: {df['user_email'].nunique()}")
    print(f"   Unique repos: {df['repo_name'].nunique()}")
    
    # AI contribution
    total_lines = df['total_lines_added'].sum()
    ai_lines = df['tab_lines_added'].sum() + df['composer_lines_added'].sum()
    ai_percentage = (ai_lines / total_lines * 100) if total_lines > 0 else 0
    
    print(f"\n🤖 AI Contribution")
    print("-" * 30)
    print(f"   Total lines added: {total_lines:,}")
    print(f"   AI-generated lines: {ai_lines:,}")
    print(f"   AI percentage: {ai_percentage:.1f}%")
    
    # Breakdown by source
    tab_lines = df['tab_lines_added'].sum()
    composer_lines = df['composer_lines_added'].sum()
    
    print(f"\n   Tab completions: {tab_lines:,} ({tab_lines/total_lines*100:.1f}%)")
    print(f"   Agent edits: {composer_lines:,} ({composer_lines/total_lines*100:.1f}%)")
    
    # By user
    print(f"\n👥 Top Users by AI Percentage")
    print("-" * 35)
    
    user_stats = df.groupby('user_email').agg({
        'total_lines_added': 'sum',
        'tab_lines_added': 'sum',
        'composer_lines_added': 'sum',
        'commit_hash': 'count'
    }).rename(columns={'commit_hash': 'commit_count'})
    
    user_stats['ai_lines'] = user_stats['tab_lines_added'] + user_stats['composer_lines_added']
    user_stats['ai_percentage'] = (user_stats['ai_lines'] / user_stats['total_lines_added'] * 100).fillna(0)
    
    top_users = user_stats.nlargest(10, 'ai_percentage')[['ai_percentage', 'commit_count', 'total_lines_added']]
    
    for email, row in top_users.iterrows():
        print(f"   {email[:25]:<25} {row['ai_percentage']:>5.1f}% ({row['commit_count']} commits)")
    
    # By repo
    print(f"\n📁 Top Repositories by AI Lines")
    print("-" * 35)
    
    repo_stats = df.groupby('repo_name').agg({
        'total_lines_added': 'sum',
        'tab_lines_added': 'sum',
        'composer_lines_added': 'sum'
    })
    
    repo_stats['ai_lines'] = repo_stats['tab_lines_added'] + repo_stats['composer_lines_added']
    repo_stats['ai_percentage'] = (repo_stats['ai_lines'] / repo_stats['total_lines_added'] * 100).fillna(0)
    
    top_repos = repo_stats.nlargest(5, 'ai_lines')[['ai_lines', 'ai_percentage', 'total_lines_added']]
    
    for repo, row in top_repos.iterrows():
        print(f"   {repo[:30]:<30} {row['ai_lines']:>8,} lines ({row['ai_percentage']:.0f}% AI)")
    
    # Daily trend
    print(f"\n📅 Daily AI Percentage Trend (Last 7 days)")
    print("-" * 40)
    
    df['date'] = pd.to_datetime(df['commit_ts']).dt.date
    daily = df.groupby('date').agg({
        'total_lines_added': 'sum',
        'tab_lines_added': 'sum',
        'composer_lines_added': 'sum'
    })
    daily['ai_percentage'] = (daily['tab_lines_added'] + daily['composer_lines_added']) / daily['total_lines_added'] * 100
    
    for date, row in daily.sort_index().tail(7).iterrows():
        pct = row['ai_percentage']
        bar = "█" * int(pct / 4)
        print(f"   {date} {bar} {pct:.0f}%")

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_commits.py <csv_file>")
        print("Example: python analyze_commits.py ai_commits_30d.csv")
        sys.exit(1)
    
    analyze_csv(sys.argv[1])

if __name__ == "__main__":
    main()
```

**Run the analysis:**
```bash
python analyze_commits.py ai_commits_30d.csv
```

---

### Step 5: Download Large Dataset with Progress (2 minutes)

Create a script for downloading large datasets with progress indication.

**Create `download_large_dataset.py`:**
```python
#!/usr/bin/env python3
"""
Download large AI commit dataset with progress bar
"""

import requests
import os
import sys
from tqdm import tqdm

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

def download_with_progress(url, output_file, auth):
    """Download file with progress bar."""
    response = requests.get(url, auth=auth, stream=True)
    
    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        return False
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(output_file, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=output_file) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))
    
    print(f"✅ Downloaded to {output_file}")
    return True

def download_commits(start_date, end_date, output_file, user=None):
    """Download commit metrics CSV."""
    url = "https://api.cursor.com/analytics/ai-code/commits.csv"
    params = {
        "startDate": start_date,
        "endDate": end_date
    }
    
    if user:
        params["user"] = user
    
    auth = (API_KEY, "")
    
    print(f"📥 Downloading commits from {start_date} to {end_date}")
    
    # Build URL with params
    param_str = '&'.join([f"{k}={v}" for k, v in params.items()])
    full_url = f"{url}?{param_str}"
    
    return download_with_progress(full_url, output_file, auth)

def main():
    print("🚀 Large Dataset Downloader")
    print("=" * 40)
    
    # Download last 90 days
    download_commits("90d", "now", "ai_commits_90d.csv")
    
    # Download for specific user
    download_commits("180d", "now", "alice_commits_180d.csv", user="alice@company.com")
    
    print("\n✅ Downloads complete!")
    print("\n💡 To analyze:")
    print("   python analyze_commits.py ai_commits_90d.csv")

if __name__ == "__main__":
    main()
```

**Install tqdm if needed:**
```bash
pip install tqdm pandas
```

---

## Expected Output

### Step 4 Output:
```
📊 Analyzing ai_commits_30d.csv
==================================================

📈 Basic Statistics
------------------------------
   Total commits: 1,234
   Date range: 2025-01-01 to 2025-01-31
   Unique users: 25
   Unique repos: 8

🤖 AI Contribution
------------------------------
   Total lines added: 45,678
   AI-generated lines: 29,876
   AI percentage: 65.4%

   Tab completions: 12,345 (27.0%)
   Agent edits: 17,531 (38.4%)

👥 Top Users by AI Percentage
-----------------------------------
   alice@company.com           78.2% (45 commits)
   bob@company.com             71.4% (38 commits)
   carol@company.com           65.3% (32 commits)

📁 Top Repositories by AI Lines
-----------------------------------
   main-app                     15,234 lines (68% AI)
   backend-api                  8,456 lines (72% AI)
   mobile-app                   6,123 lines (55% AI)

📅 Daily AI Percentage Trend (Last 7 days)
-------------------------------------------
   2025-01-25 ████████████████████ 78%
   2025-01-26 ██████████████████ 72%
   2025-01-27 ████████████████████ 76%
   2025-01-28 █████████████████ 68%
   2025-01-29 ████████████████████ 80%
   2025-01-30 ██████████████████ 74%
   2025-01-31 ████████████████████ 79%
```

---

## CSV Columns Reference

| Column | Description |
|--------|-------------|
| `commit_hash` | Git commit hash |
| `user_id` | Encoded user ID |
| `user_email` | User's email address |
| `repo_name` | Repository name |
| `branch_name` | Branch name |
| `is_primary_branch` | Whether this is the primary branch |
| `commit_source` | Where commit originated (`ide`, `cli`, `cloud`) |
| `total_lines_added` | Total lines added in commit |
| `total_lines_deleted` | Total lines deleted in commit |
| `tab_lines_added` | Lines added via Tab completions |
| `tab_lines_deleted` | Lines deleted via Tab completions |
| `composer_lines_added` | Lines added via Agent edits |
| `composer_lines_deleted` | Lines deleted via Agent edits |
| `non_ai_lines_added` | Human-written lines added |
| `non_ai_lines_deleted` | Human-written lines deleted |
| `message` | Commit message |
| `commit_ts` | Commit timestamp |
| `created_at` | Ingestion timestamp |

---

## Success Criteria

- [ ] Downloaded CSV using curl
- [ ] Downloaded by date range
- [ ] Filtered by specific user
- [ ] Analyzed CSV with pandas
- [ ] Created download script with progress bar
- [ ] Generated summary statistics

---

## Important Notes

| Note | Description |
|------|-------------|
| **CSV streaming** | Streams in pages of 10,000 records |
| **No pagination params** | Use `startDate` and `endDate` only |
| **Large exports** | CSV is more efficient than JSON for large datasets |
| **Filtering** | Only `startDate`, `endDate`, and `user` parameters |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Empty CSV | No data in date range; try longer range |
| Partial download | Use `-L` flag with curl to follow redirects |
| Memory issues | CSV streams; shouldn't cause memory problems |
| Unicode errors | CSV is UTF-8 encoded |

---

## Exercise Complete ✓

Check off when done:
- [ ] Downloaded CSV with curl
- [ ] Downloaded by date range
- [ ] Filtered by specific user
- [ ] Analyzed CSV with pandas
- [ ] Created download script with progress bar
- [ ] Generated summary statistics

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project

