#!/usr/bin/python3
"""
A script that retrieves the X-Request-Id headeri
variable from a request to a specified URL.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
