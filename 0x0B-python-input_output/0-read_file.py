#!/usr/bin/python3
"""Define read file"""


def read_file(filename=""):
    """Use 'with' and print content"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
