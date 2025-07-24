# ai_git/commands/issue.py

from ai_git.utils.github_api import create_issue

def run(args):
    print("📦 Creating GitHub issue...")
    create_issue(args.repo, args.title, args.body)

def add_subparser(subparsers):
    parser = subparsers.add_parser(
        "issue", help="Create a GitHub issue"
    )
    parser.add_argument("repo", help="GitHub repository (e.g. user/repo)")
    parser.add_argument("title", help="Issue title")
    parser.add_argument("body", help="Issue description")
    parser.set_defaults(func=run)
