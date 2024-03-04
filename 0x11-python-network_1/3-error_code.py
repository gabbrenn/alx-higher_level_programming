#!/usr/bin/python3
"""
A script that performs the following tasks:
- Takes in a URL as a command-line argument.
- Sends a request to the URL.
- Displays the body of the response, decoded in UTF-8.
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
