#!/usr/bin/python3
"""Define reaf file"""

def read_file(filename=""):
	"""use of with and print content"""
	with open(filename,encoding='utf-8') as file:
		print(file.read(),end="")
