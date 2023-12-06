#!/usr/bin/python3
"""Define Write_file function"""


def write_file(filename="", text=""):
    """Create and Write in file"""
    with open(filename,'w+',encoding='utf-8') as file:
        file.write(text)
    return len(text)
