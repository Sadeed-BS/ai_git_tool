# ai_git/core/git_ops.py

import subprocess
import os
import git
from ai_git.utils.ai_utils import generate_commit_message


def ai_commit(repo_path: str):
    """
    Commit staged changes using an AI-generated commit message.
    """
    try:
        if not os.path.exists(os.path.join(repo_path, ".git")):
            print("❌ Not a git repository. Please provide a valid repo path.")
            return

        # Get staged diff
        result = subprocess.run(
            ['git', '-C', repo_path, 'diff', '--cached'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(f"❌ Error running git diff: {result.stderr.strip()}")
            return

        diff = result.stdout.strip()
        if not diff:
            print("⚠️ No staged changes found. Use `git add` to stage files.")
            return

        # Generate commit message
        commit_message = generate_commit_message(diff)
        print(f"\n🤖 AI-generated commit message:\n» {commit_message}\n")

        # Commit
        commit_result = subprocess.run(
            ['git', '-C', repo_path, 'commit', '-m', commit_message],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if commit_result.returncode == 0:
            print("✅ Commit successful.")
        else:
            print(f"❌ Commit failed:\n{commit_result.stderr.strip()}")

    except Exception as e:
        print(f"❌ Exception during AI commit: {e}")


def clone_repo(url: str):
    """
    Clone a GitHub repository to the local directory.
    """
    try:
        repo_name = url.split("/")[-1].replace(".git", "")
        print(f"📥 Cloning {url} into ./{repo_name} ...")
        git.Repo.clone_from(url, repo_name)
        print("✅ Clone complete.")
    except Exception as e:
        print(f"❌ Failed to clone repository: {e}")


def analyze_repo(path: str):
    """
    Analyze the given repo (placeholder for future AI analysis).
    """
    try:
        if not os.path.exists(os.path.join(path, ".git")):
            print("❌ Not a valid Git repository.")
            return

        print(f"🔍 Analyzing repository at: {path}")
        print("🚧 Analysis logic is under construction (LangGraph or LLM can be used here).")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
