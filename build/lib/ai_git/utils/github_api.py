# ai_git/utils/github_api.py

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
