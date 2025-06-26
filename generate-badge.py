# generate-badge.py
import re

def get_progress():
    with open("README.md", "r") as file:
        content = file.read()
    
    total = len(re.findall(r"- ( |x) ", content))
    done = len(re.findall(r"- x ", content))
    percent = int((done / total) * 100) if total else 0

    color = (
        "red" if percent < 25 else
        "yellow" if percent < 50 else
        "orange" if percent < 75 else
        "brightgreen"
    )

    badge_url = f"https://img.shields.io/badge/CSRF%20Study-{percent}%25-{color}"

    updated = re.sub(
        r"!Progress.*?",
        f"![Progress]({badge_url})",
        content
    )

    with open("README.md", "w") as file:
        file.write(updated)

if __name__ == "__main__":
    get_progress()