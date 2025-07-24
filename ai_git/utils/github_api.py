# ai_git/utils/github_api.py

import requests
import os
from ai_git.utils.ai_utils import generate_pr_message

def create_pull_request(repo, head_branch, base_branch, use_ai=False):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not found in .env")
        return

    title = f"Merge `{head_branch}` into `{base_branch}`"
    body = ""

    if use_ai:
        from subprocess import run, PIPE
        diff = run(["git", "diff", f"{base_branch}...{head_branch}"], stdout=PIPE, text=True).stdout
        title, body = generate_pr_message(diff)

    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "head": head_branch,
        "base": base_branch,
        "body": body
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("✅ Pull Request created successfully.")
        print("🔗", response.json().get("html_url"))
    else:
        print("❌ Failed to create PR:", response.status_code)
        print(response.text)


def create_issue(repo, title, body):
    import requests
    import os

    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        return

    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"title": title, "body": body}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Issue created successfully")
    else:
        print(f"Failed to create issue: {response.status_code}")
        print(response.text)
