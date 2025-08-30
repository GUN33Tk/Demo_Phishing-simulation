import xml.etree.ElementTree as ET

# Loading the file
tree = ET.parse('report.xml')
root = tree.getroot()

# Preparing summary
report = []
report.append("# Phishing Simulation Report\n")

# Extracting data
for url in root.findall('.//url'):
    uname = None
    password = None
    for param in url.findall('param'):
        text = param.text.strip()
        if text.startswith("uname="):
            uname = text.split("=", 1)[1]
        elif text.startswith("pass="):
            password = text.split("=", 1)[1]
    if uname or password:
        report.append(f"- Username: {uname if uname else 'N/A'}")
        report.append(f"  - Password: {password if password else 'N/A'}\n")

# Saving summary
with open("analysis_report.md", "w") as f:
    f.write("\n".join(report))

print("✅ Analysis complete. Report saved as analysis_report.md")
