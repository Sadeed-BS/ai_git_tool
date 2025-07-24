# ai_git/core/git_ops.py

import subprocess
from ai_git.utils.ai_utils import generate_commit_message

def ai_commit(repo_path):
    try:
        # Get staged changes
        result = subprocess.run(
            ['git', '-C', repo_path, 'diff', '--cached'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        diff = result.stdout.strip()

        if not diff:
            print("No staged changes found. Stage files with `git add` first.")
            return

        # Get AI-generated commit message
        commit_message = generate_commit_message(diff)
        print(f"AI-generated commit message:\n{commit_message}")

        # Run git commit
        subprocess.run(['git', '-C', repo_path, 'commit', '-m', commit_message])

    except Exception as e:
        print(f"Error in AI commit: {e}")


def clone_repo(url):
    import os
    import git
    repo_name = url.split("/")[-1].replace(".git", "")
    print(f"Cloning {url} into ./{repo_name}")
    git.Repo.clone_from(url, repo_name)
    print("Clone complete.")

def analyze_repo(path):
    print(f"Analyzing repo at {path}")
    # Add LangGraph or AI logic here
