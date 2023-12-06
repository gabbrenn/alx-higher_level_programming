#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """Append to the end of the file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)

