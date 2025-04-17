# Free Tools for Phishing Analysis 🧰

This document lists free and reliable tools that can assist in analyzing phishing emails, including sandbox environments, header parsers, email verification tools, and URL checkers. These are helpful for Blue Teamers during triage and investigation.

---

## 🧪 Sandbox Environments

Used for safely detonating suspicious attachments or URLs:

- [ANY.RUN](https://any.run) – Interactive malware sandbox, great for real-time analysis
- [Joe Sandbox Cloud](https://www.joesandbox.com/) – Advanced behavior analysis (limited free runs)
- [Hybrid Analysis](https://www.hybrid-analysis.com/) – Public malware sandbox by CrowdStrike
- [Intezer Analyze](https://analyze.intezer.com/) – Behavioral and genetic malware analysis
- [ThreatBook](https://x.threatbook.cn/) (China-based, UI in English) – Fast and visual sandboxing

---

## ✉️ Email Header Analysis

Parse and analyze full email headers for SPF/DKIM/DMARC and routing issues:

- [MXToolbox Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx)
- [Google Admin Toolbox - MessageHeader](https://toolbox.googleapps.com/apps/messageheader/)
- [Mailheader.org](https://mailheader.org/) – Quick and simple parsing
- [Dmarcian Header Analyzer](https://dmarcian.com/header-analyzer/) – Specialized in DMARC/SPF breakdown

---

## 🔎 Email Checker & Intelligence

Tools to check sender reputation, domain age, blacklist status, etc.

- [EmailRep.io](https://emailrep.io/) – Provides risk reputation for email addresses
- [EmailVerifier.io](https://emailverifier.io/) – Checks deliverability, MX records, DNS info
- [Whois Lookup](https://whois.domaintools.com/) – Check domain registration details
- [Talos Intelligence](https://talosintelligence.com/) – Sender IP/domain reputation

---

## 🌐 URL and Domain Analysis

Check URLs for malicious behavior, domain reputation, and redirection:

- [VirusTotal](https://www.virustotal.com/gui/home/url) – Aggregated threat detection from dozens of sources
- [URLScan.io](https://urlscan.io/) – Visual scan of webpage behavior and redirects
- [PhishTool](https://www.phishtool.com/) – Helps analyze phishing indicators (limited free version)
- [AbuseIPDB](https://www.abuseipdb.com/) – IP reputation lookup and reporting
- [URLVoid](https://www.urlvoid.com/) – Domain reputation and threat detection
- [OpenPhish](https://openphish.com/) – Public phishing feed for known malicious domains

---

## 🧠 Honorable Mentions / Bonus

- [HaveIBeenPwned](https://haveibeenpwned.com/) – Check if an email address has been compromised in a breach
- [MalwareBazaar](https://bazaar.abuse.ch/) – Repository of malware samples (for research/sandboxing)

---

> ✅ Most of these tools are free or freemium. Always review results from multiple sources for better confidence during triage or incident analysis.

