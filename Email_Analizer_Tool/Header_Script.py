import os
import re
import email
import requests
from urllib.parse import urlparse
from flask import Flask, render_template_string, request

app = Flask(__name__)

VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"

HTML_TEMPLATE = """
<!doctype html>
<title>Email Header & Threat Analyzer</title>
<script>
  function toggleCheckboxes(group, check) {
    const boxes = document.querySelectorAll(`input[name="${group}"]`);
    boxes.forEach(box => box.checked = check);
  }
</script>

<h2>Upload an Email (.eml) File</h2>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="email_file" required>
  <input type="submit" value="Analyze">
</form>

{% if header_text %}
<hr>
<h3>Email Header (Extracted)</h3>
<textarea rows="20" cols="100">{{ header_text }}</textarea><br>
<a href="https://toolbox.googleapps.com/apps/messageheader/" target="_blank">Open Google MHA Tool</a>
{% endif %}

{% if urls or domains %}
<hr>
<h3>Scan Options</h3>
<form method="post">
  <input type="hidden" name="header_text" value="{{ header_text }}">

  {% if urls %}
  <h4>Detected URLs</h4>
  <a href="#" onclick="toggleCheckboxes('selected_urls', true); return false;">Select All</a> |
  <a href="#" onclick="toggleCheckboxes('selected_urls', false); return false;">Deselect All</a><br><br>
  {% for url in urls %}
    <input type="checkbox" name="selected_urls" value="{{ url }}" checked> {{ url }}<br>
  {% endfor %}
  <br>
  {% endif %}

  {% if domains %}
  <h4>Extracted Domains</h4>
  <a href="#" onclick="toggleCheckboxes('selected_domains', true); return false;">Select All</a> |
  <a href="#" onclick="toggleCheckboxes('selected_domains', false); return false;">Deselect All</a><br><br>
  {% for domain in domains %}
    <input type="checkbox" name="selected_domains" value="{{ domain }}" checked> {{ domain }}<br>
  {% endfor %}
  <br>
  {% endif %}

  <input type="submit" name="vt_scan" value="Run VirusTotal Scan">
</form>
{% endif %}

{% if vt_results %}
<hr>
<h3>VirusTotal Scan Results</h3>
<ul>
  {% for item in vt_results %}
  <li>
    <strong>Type:</strong> {{ item.type }}<br>
    <strong>Item:</strong> {{ item.original }}<br>
    <strong>VirusTotal:</strong> <a href="{{ item.vt_link }}" target="_blank">{{ item.vt_link }}</a> - {{ item.status }}
  </li>
  {% endfor %}
</ul>
{% endif %}

<hr>
<h3>Other Tools</h3>
<ul>
  <li><a href="https://urlscan.io/" target="_blank">Open URLScan.io</a></li>
  <li><a href="https://www.virustotal.com/gui/home/upload" target="_blank">Upload File to VirusTotal</a></li>
</ul>
"""

def extract_email_parts(file_data):
    msg = email.message_from_bytes(file_data)
    headers = str(msg)

    urls = set(re.findall(r'https?://[^\s\'"<>]+', headers))

    domains = set()
    for url in urls:
        try:
            parsed = urlparse(url)
            if parsed.netloc:
                domains.add(parsed.netloc.lower())
        except Exception as e:
            print(f"Failed to parse URL: {url} -> {e}")

    return headers, sorted(urls), sorted(domains)

def check_virustotal_url(url_or_domain):
    headers = {"x-apikey": VT_API_KEY}
    data = {"url": url_or_domain}
    response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=data)

    if response.status_code == 200:
        scan_id = response.json()["data"]["id"]
        # Remove 'u-' prefix and split off timestamp if present
        clean_id = scan_id.replace("u-", "").split("-")[0]
        gui_link = f"https://www.virustotal.com/gui/url/{clean_id}"
        return gui_link, "Submitted"
    else:
        return url_or_domain, "Failed to submit"

@app.route("/", methods=["GET", "POST"])
def index():
    header_text = None
    urls = []
    domains = []
    vt_results = []

    if request.method == "POST":
        if "email_file" in request.files:
            file = request.files["email_file"]
            if file:
                file_data = file.read()
                header_text, urls, domains = extract_email_parts(file_data)

        elif "vt_scan" in request.form:
            header_text = request.form.get("header_text")
            selected_urls = request.form.getlist("selected_urls")
            selected_domains = request.form.getlist("selected_domains")

            for url in selected_urls:
                vt_link, status = check_virustotal_url(url)
                vt_results.append({
                    "type": "URL",
                    "original": url,
                    "vt_link": vt_link,
                    "status": status
                })

            for domain in selected_domains:
                vt_link, status = check_virustotal_url(domain)
                vt_results.append({
                    "type": "Domain",
                    "original": domain,
                    "vt_link": vt_link,
                    "status": status
                })

    return render_template_string(
        HTML_TEMPLATE,
        header_text=header_text,
        urls=urls,
        domains=domains,
        vt_results=vt_results
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
