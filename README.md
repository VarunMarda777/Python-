# Ads_Blocker — GitHub-Native Python Automation

![GitHub Actions](https://github.com/VarunMarda777/Ads_Blocker/actions/workflows/run.yml/badge.svg)  

**Block ads & distracting domains entirely in GitHub — no local setup needed.**  
- Runs **automatically** or manually via GitHub Actions  
- Downloads **70k+ domains** from public ad-block lists  
- Outputs results as a **downloadable artifact**  
- Clean, interview-ready Python + CI pipeline  

**⚡ Quick start:** Go to **Actions → Run workflow → main → Run**

---

## One-Line Summary

A GitHub-only Python project that fetches a real ad-block list, extracts blocked domains, and publishes results as downloadable artifacts — no local setup required.

---

## TL;DR (Quick Readers)

* ▶ Runs **entirely in GitHub Actions**
* ❌ No local Python / installs
* 📦 Output downloadable as an **Artifact**
* 🧱 Clean `src/` structure
* 🌐 Uses real open-source ad-block data

---

## How It Works (Architecture)

Trigger (push / manual)
↓
GitHub Actions Runner (Ubuntu)
↓
Setup Python (3.11)
↓
Execute src/main.py
↓
Download public hosts list
↓
Parse & extract domains
↓
Generate blocked_domains.txt
↓
Upload artifact (downloadable)

**Key point:** The entire execution lifecycle happens inside GitHub’s infrastructure.

---

## Project Structure

Ads_Blocker/
├── .github/
│ └── workflows/
│ └── run.yml # CI pipeline
├── src/
│ └── main.py # Core logic
├── blocked_domains.txt # Generated during workflow
└── README.md

---

## What the Project Does

Boost productivity by restricting access to time-wasting sites—runs entirely within GitHub.

1. Downloads a **public ad‑block hosts list**
2. Extracts domain names mapped to `0.0.0.0`
3. Counts total blocked domains
4. Saves a **sample of 100 domains**
5. Uploads the output as a **GitHub Actions artifact**

---

## Data Source

* **StevenBlack Hosts List**
* Widely used by Pi‑hole, firewalls, and ad-blocking tools
* Contains **70,000+ known ad, tracking, and malicious domains**

---

## Running the Project (GitHub-Only)

### Manual Run (Recommended)

1. Go to **Actions**
2. Select **Run Python Project**
3. Click **Run workflow**
4. Choose branch: `main`
5. Click **Run**

### Automatic Run

* Any push to `main` triggers the workflow

---

## Output

After completion:

1. Open the workflow run
2. Scroll to **Artifacts**
3. Download `blocked-domains-output`

### Sample Output

ads.facebook.com
doubleclick.net
tracking.google.com

---

## Resume / LinkedIn Version

**Ads Blocker Automation (GitHub Actions)**

* Built a GitHub‑native Python automation pipeline using GitHub Actions
* Processed real‑world ad-blocking datasets (70k+ domains)
* Implemented CI execution, artifact publishing, and manual triggers
* Designed with clean project structure and production-style logging

---

## Technical / Interview Talking Points

* Why GitHub Actions over local execution
* Artifact handling in CI/CD pipelines
* Safe network calls inside CI runners
* Separation of logic (`src/`) and orchestration (workflow)
* Deterministic builds via pinned Python version

---

## Requirements

* A GitHub account  
* Nothing else

---

## Possible Enhancements

* CSV export option
* Workflow inputs (domain count)
* Scheduled execution (cron)
* Test & lint stages

---

## Author

**Varun Marda**  
Technology Consultant | Python | GitHub Actions

⭐ Star the repository if you find it useful
