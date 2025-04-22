# Header_Script.py — Email Header & Threat Analyzer

`Header_Script.py` is a lightweight web application built using Flask. It is designed for Blue Team analysts, SOC operators, and cybersecurity learners to analyze email headers, extract embedded URLs and domains, and interactively scan selected elements using VirusTotal.

---

## 🔐 Step 1: Getting a VirusTotal API Key

To enable URL and domain scanning, this tool uses the public **VirusTotal API**.

### How to get your API key:

1. Go to [https://www.virustotal.com](https://www.virustotal.com)
2. Create or log in to your account
3. Navigate to your API key page:  
   [https://www.virustotal.com/gui/user/apikey](https://www.virustotal.com/gui/user/apikey)
4. Copy the **Public API Key**

---

## ⚙️ Step 2: Adding the API Key to the Script

Once you have the API key:

1. Open `Header_Script.py` in any text editor
2. Locate this line near the top:
   ```python
   VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"
   ```
3. Replace the placeholder with your real key:
   ```python
   VT_API_KEY = "your-actual-api-key"
   ```

---

## 🚀 Step 3: Running the Tool

### System Requirements:
- Python 3.6 or higher
- Packages: `Flask`, `requests`

### Installation:
```bash
pip install flask requests
```

### Running the app:
```bash
python Header_Script.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🛠️ Key Features

| Feature                               | Description                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------|
| 📥 Upload `.eml` files                | Analyze real emails exported from Outlook, Thunderbird, etc.               |
| 📋 Extract full email headers         | Displayed in a scrollable, readable format                                 |
| 🔗 URL Extraction                     | Detects all embedded HTTP/HTTPS links in headers                           |
| 🌐 Domain Extraction                  | Uses `urlparse()` to precisely extract domains                             |
| ✅ VirusTotal Scanning (selective)    | Scan only the URLs/domains you check                                       |
| 🔘 Select All / Deselect All buttons  | Easily control what to send to VirusTotal                                  |
| 🧪 Auto-cleans VirusTotal links       | Fixes invalid IDs for GUI link usability                                   |
| 🧭 Tools Integration                  | Links to [Google MHA](https://toolbox.googleapps.com/apps/messageheader/), [urlscan.io](https://urlscan.io/), and VT file upload

---

## 🧪 Sample Workflow

1. Upload a `.eml` email file
2. Review the full extracted headers
3. Scroll through the list of embedded **URLs** and **domains**
4. Select the elements you want to scan
5. Click **Run VirusTotal Scan**
6. Review the VT links and threat verdicts

---

## 📤 VirusTotal File Upload

To scan suspicious attachments (e.g. `.exe`, `.zip`, `.docm`), manually upload them here:

🔗 [https://www.virustotal.com/gui/home/upload](https://www.virustotal.com/gui/home/upload)

---

## 🧠 Good To Know

- The tool does **not store any email data**. All parsing is local and only selected items are submitted to VT.
- The script safely cleans VT scan IDs so they open in the GUI.
- URL/domain logic uses `urlparse()` instead of regex for domain accuracy.

---

## 📫 Requesting Features or Submitting Updates

### Found a bug or want a new feature?

Submit a GitHub **Issue** with the following format:

**Title:**  
`[Feature] Integrate AbuseIPDB for domain IP rep check`

**Description:**  
"This would help with high-fidelity triage by checking malicious IPs related to domains."

**Optional Add-ons:**  
- Suggested UI changes  
- Links to APIs or references

Or fork the repo and submit a **Pull Request** — your contribution is welcome!

---

## 📄 License

This tool is licensed under the **MIT License** and can be used or modified freely for educational, research, or internal SOC usage.

---

## 👨‍💻 Maintainer

**Bhrigu Sharma**  
Cybersecurity Analyst
🔗 [LinkedIn](www.linkedin.com/in/bhrigu-sharma-74b5431b4)

---

> Last Updated: April 2025
