#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """Create and write in file"""
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(text)
    return len(text)
