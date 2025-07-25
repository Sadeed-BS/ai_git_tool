# ai_git/utils/github_api.py

import os
import requests
from subprocess import run, PIPE
from ai_git.utils.ai_utils import generate_pr_message


def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ Error: GITHUB_TOKEN not found in environment (.env)")
        return None
    return token


def create_pull_request(repo: str, head_branch: str, base_branch: str, use_ai: bool = False):
    token = get_github_token()
    if not token:
        return

    # Default title/body
    title = f"Merge `{head_branch}` into `{base_branch}`"
    body = ""

    # Use AI for title/body generation if requested
    if use_ai:
        try:
            diff = run(["git", "diff", f"{base_branch}...{head_branch}"], stdout=PIPE, text=True, check=True).stdout
            title, body = generate_pr_message(diff)
        except Exception as e:
            print(f"❌ Error generating PR message using AI: {e}")
            return

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
        pr_url = response.json().get("html_url")
        print("✅ Pull Request created successfully!")
        print(f"🔗 {pr_url}")
    else:
        print(f"❌ Failed to create Pull Request ({response.status_code})")
        print(response.json().get("message", "Unknown error"))
        if response.text:
            print(response.text)


def create_issue(repo: str, title: str, body: str):
    token = get_github_token()
    if not token:
        return

    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        issue_url = response.json().get("html_url")
        print("✅ Issue created successfully!")
        print(f"🔗 {issue_url}")
    else:
        print(f"❌ Failed to create issue ({response.status_code})")
        print(response.json().get("message", "Unknown error"))
        if response.text:
            print(response.text)
