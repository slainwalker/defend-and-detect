# Phishing Response SOP

Phishing remains one of the most common and effective techniques used by attackers to gain unauthorized access to systems, steal credentials, or scam individuals. Proper analysis is critical to mitigate such threats quickly and effectively. This SOP outlines the standard steps to triage and respond to suspected phishing emails.

---

## Step 1: Triage

- Determine whether the email was reported by a user or flagged by a system.
- Check for red flags in the **subject line**, **sender address**, and **email body**.
- Inspect all **attachments** and **embedded URLs**.
- Analyze the tone of the message — is it urgent, manipulative, or out of context?
- Based on this initial review, classify the email as **phish**, **spam**, **scam**, or a **false positive**.

---

## Step 2: Header Analysis

- Review email headers to validate:
  - **SPF**, **DKIM**, and **DMARC** results
  - **Reply-to** address mismatches
  - Suspicious or **unusual sending domains**
  - Uncommon email clients or forged fields like **X-Mailer**
- Check for **lookalike domain names** (e.g., `rnicrosoft.com` instead of `microsoft.com`).

---

## Step 3: IronPort Analysis

- Search for the message using **Message ID** or **sender address** in IronPort.
- Review:
  - **Delivery status**
  - **Attachment analysis**
  - **Threat score or verdict** (if available)

---

## Step 4: Attachments and URLs

- Analyze all attachments and URLs in a **sandboxed environment**.

### For URLs:
- Check domain age and WHOIS information.
- Evaluate the risk score (using tools like URLScan, VirusTotal, etc.).
- Inspect if the link redirects to:
  - Lookalike or typo-squatted domains
  - Insecure HTTP sites
  - Malware downloads or data exfiltration pages

### For Attachments:
- Review threat level and scan results
- Detect any malware signatures
- Monitor behavior like system file or registry changes

---

## Step 5: Remediation

- Block the **sender domain/IP** across security systems.
- Notify affected users and recommend **password resets** if credentials were exposed.
- Remove any **downloaded files or registry entries** related to the phishing attempt.
- In severe cases, **isolate or reimage the system** to prevent further compromise.

---
