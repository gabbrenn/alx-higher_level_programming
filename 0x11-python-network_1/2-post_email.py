#!/usr/bin/python3
"""
A script that performs the following tasks:
- Takes in a URL as a command-line argument.
- Sends a POST request to the provided URL.
- Takes an email as a parameter.
- Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
