# ai_git/commands/pr.py

from ai_git.utils.github_api import create_pull_request

def run(args):
    print("🔃 Creating Pull Request...")
    create_pull_request(
        repo=args.repo,
        head_branch=args.head,
        base_branch=args.base,
        use_ai=args.ai
    )

def add_subparser(subparsers):
    parser = subparsers.add_parser(
        "pr", help="Create a pull request"
    )
    parser.add_argument("repo", help="GitHub repository (e.g. user/repo)")
    parser.add_argument("head", help="Source branch (e.g. feature-branch)")
    parser.add_argument("base", help="Target branch (e.g. main)")
    parser.add_argument("--ai", action="store_true", help="Use AI to generate PR title/description")
    parser.set_defaults(func=run)
