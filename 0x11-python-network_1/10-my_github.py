#!/usr/bin/python3
"""
A script that:
- accepts GitHub credentials (username and password) as command-line arguments
- retrieves your GitHub user ID using the GitHub API
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # Retrieve GitHub credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Authenticate using HTTP basic authentication
    auth = HTTPBasicAuth(username, password)

    # Send GET request to GitHub API to fetch user information
    response = requests.get("https://api.github.com/user", auth=auth)

    # Extract and print user ID from response JSON
    user_id = response.json().get("id")
    print(user_id)
