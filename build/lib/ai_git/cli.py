import argparse
from ai_git.core.git_ops import clone_repo, analyze_repo, ai_commit
from ai_git.utils.github_api import create_issue

def main():
    parser = argparse.ArgumentParser(description="AI Git Assistant CLI")
    subparsers = parser.add_subparsers(dest='command')

    clone = subparsers.add_parser('clone', help='Clone a GitHub repo')
    clone.add_argument('url', help='GitHub repo URL')

    analyze = subparsers.add_parser('analyze', help='Analyze a repo')
    analyze.add_argument('path', help='Local repo path')

    issue = subparsers.add_parser('issue', help='Create GitHub issue')
    issue.add_argument('repo', help='Repo name')
    issue.add_argument('title', help='Issue title')
    issue.add_argument('body', help='Issue body')

    commit = subparsers.add_parser('commit', help='AI-powered Git commit')
    commit.add_argument('--repo', default='.', help='Path to local repo')

    args = parser.parse_args()

    if args.command == 'clone':
        clone_repo(args.url)
    elif args.command == 'analyze':
        analyze_repo(args.path)
    elif args.command == 'issue':
        create_issue(args.repo, args.title, args.body)
    elif args.command == 'commit':
        ai_commit(args.repo)
    else:
        parser.print_help()
