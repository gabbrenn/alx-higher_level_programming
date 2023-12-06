#!/usr/bin/python3
"""Define write_file function"""


def append_write(filename="", text=""):
    """Will append to the end of file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)

