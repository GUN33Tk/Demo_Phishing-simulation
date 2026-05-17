# 🎯 Phishing Simulation & Awareness Project

This repository contains a **phishing simulation project** developed purely for **educational and learning purposes**.  
It demonstrates how phishing attacks can capture sensitive information (like usernames and passwords) through cloned web pages and how those credentials may be stored for analysis.

⚠️ **Disclaimer:**  
- This project is **not intended for malicious use**.  
- Performing phishing attacks **without consent** is **illegal and punishable under cyber laws**.  
- Everything here is created and shared **only for cybersecurity education, awareness, and research**.  
- I am highly precautionary and aware of the legal & ethical implications of such activities.  

---
# 🎣 Phishing Simulation Home Lab
---

## 📌 Overview

This project is a self-built phishing simulation home lab designed to replicate real-world social engineering attacks in a controlled environment. The goal was twofold: **understand how attackers craft and deliver phishing campaigns**, and **develop the defender skills to detect and respond to them**.

The lab modelled **5+ attack vectors** across **50+ simulated interactions**, produced actionable detection signatures, and mapped all observed techniques to the MITRE ATT&CK framework.

> ⚠️ **Disclaimer**: This project was built strictly for educational and research purposes in an isolated lab environment. Do not use any of these techniques against real systems or individuals without explicit authorisation.

---

## 🎯 Objectives

- Simulate realistic phishing campaigns to understand attacker methodology
- Develop and test defender detection rules and identification heuristics
- Map attack behaviours to industry-standard threat intelligence frameworks
- Improve blue team phishing identification accuracy through repeatable testing

---

## ⚙️ Tech Stack

| Component | Purpose |
|-----------|---------|
| **Python** | Payload generation, automation scripts, email templating |
| **HTML/CSS** | Credential harvesting page clones, lure landing pages |
| **Social Engineering Toolkit (SET)** | Campaign delivery, spear phishing modules, vector simulation |

---

## 🔬 Attack Vectors Simulated

| # | Vector | Description |
|---|--------|-------------|
| 1 | **Credential Harvesting** | Cloned login pages capturing victim credentials via form POST |
| 2 | **Spear Phishing** | Targeted emails with personalised lures and malicious links |
| 3 | **Pretexting** | Scenario-based social engineering simulating IT helpdesk and HR contexts |
| 4 | **Malicious Attachment** | Email-delivered payloads (macro-enabled document simulation) |
| 5 | **Link Redirection** | Multi-hop URL chains obscuring the final phishing destination |

---

## 📊 Key Results

- 🎯 **50+ simulated interactions** across 5+ attack vectors
- 🛡️ **~30% improvement** in phishing identification accuracy through developed detection signatures
- 🗺️ All observed TTPs mapped to **MITRE ATT&CK T1566 (Phishing) & T1059 (Command and Scripting Interpreter)**

---

## 🔍 Detection Signatures Developed

Through the simulation process, the following defender detection heuristics were identified and documented:

**Email-based IOCs:**
- Mismatched sender display name vs. actual email domain
- Use of third-party mail relay services (e.g., Elastic Email, SendGrid) for spoofed domains
- Suspicious `Reply-To` headers differing from the `From` address
- DKIM/SPF/DMARC failures on impersonated domains

**URL/Link IOCs:**
- Lookalike domains using typosquatting (e.g., `bpakcaging.xyz` vs `bpackaging.com`)
- Newly registered domains (< 30 days) used as phishing infrastructure
- Redirect chains with multiple hops before reaching harvest page

**Payload IOCs:**
- LNK files with embedded PowerShell commands in the Command Line Arguments field
- Macro-enabled Office documents with `AutoOpen` or `Document_Open` triggers
- Base64-encoded PowerShell download cradles

---

## 🗺️ MITRE ATT&CK Mapping

| Technique ID | Technique Name | Sub-technique |
|-------------|---------------|---------------|
| **T1566** | Phishing | T1566.001 — Spear Phishing with Attachment |
| **T1566** | Phishing | T1566.002 — Spear Phishing Link |
| **T1059** | Command and Scripting Interpreter | T1059.001 — PowerShell |
| **T1204** | User Execution | T1204.002 — Malicious File |
| **T1598** | Phishing for Information | Credential Harvesting |

---

## 🏗️ Lab Architecture

```
Phishing Simulation Lab
│
├── attacker/
│   ├── email_templates/        # HTML phishing email templates
│   ├── harvest_pages/          # Cloned credential capture pages (HTML/CSS)
│   ├── payloads/               # Python-generated payloads and stagers
│   └── set_configs/            # Social Engineering Toolkit config files
│
├── defender/
│   ├── detection_signatures/   # IOC lists and detection rules
│   ├── analysis_reports/       # Per-simulation analysis writeups
│   └── mitre_mapping/          # ATT&CK technique documentation
│
└── docs/
    └── simulation_log.md       # Record of all 50+ simulated interactions
```

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.x
python3 --version

# Social Engineering Toolkit
sudo apt install set

# Clone the repository
git clone https://github.com/GUN33Tk/Demo_Phishing-simulation.git
cd Demo_Phishing-simulation
```

### Running a Simulation

```bash
# Launch SET
sudo setoolkit

# Or run the Python email templating script
python3 attacker/generate_email.py --template invoice --target simulation@lab.local
```

> All simulations must be run in an **isolated lab environment** (e.g., local VM network). Never target external systems.

---

## 📚 References & Learning Resources

- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
- [MITRE ATT&CK — T1059 Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
- [TrustedSec — Social Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)
- [PhishTank — Phishing URL Database](https://phishtank.org)
- [Any.run Sandbox — Payload Analysis](https://any.run)

---


*Built for educational purposes as part of a personal cybersecurity portfolio.*
