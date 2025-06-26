import re

def get_progress():
    with open("README.md", "r") as file:
        content = file.read()

    all_checkboxes = re.findall(r"- \[( |x)\]", content)
    checked = re.findall(r"- \[x\]", content)

    print(f"🔍 Total checkboxes found: {len(all_checkboxes)}", flush=True)
    print(f"✅ Boxes checked: {len(checked)}", flush=True)
    print(f"⛳ Matches found: {checked}", flush=True)

    total = len(all_checkboxes)
    done = len(checked)
    percent = int((done / total) * 100) if total else 0

    color = (
        "red" if percent < 25 else
        "yellow" if percent < 50 else
        "orange" if percent < 75 else
        "brightgreen"
    )

    badge_url = f"https://img.shields.io/badge/CSRF%20Study-{percent}%25-{color}"
    print(f"📊 New badge URL: {badge_url}", flush=True)

    updated = re.sub(
        r"!\[Progress\]\(.*?\)",
        f"![Progress]({badge_url})",
        content
    )

    with open("README.md", "w") as file:
        file.writ
