#!/usr/bin/python3
"""Module for reading from files"""


def read_file(filename=""):
    """File to read all info from a file"""
    with open(filename, 'r') as file:
        line = file.read()
    return line


if __name__ == "__main__":
    pass
