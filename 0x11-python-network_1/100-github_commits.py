#!/usr/bin/python3
"""
A script that:
- fetches and lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    # Extract repository owner and name from command-line arguments
    repo_owner = sys.argv[2]
    repo_name = sys.argv[1]

    # Construct URL for GitHub API endpoint
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    # Send GET request to GitHub API to retrieve commit data
    response = requests.get(url)

    # Parse JSON response to obtain commit information
    commits = response.json()

    # Print information for the 10 most recent commits
    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
