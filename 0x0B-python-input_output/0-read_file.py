#!/usr/bin/python3
"""Module for reading from files"""


def read_file(filename=""):
    """File to read all info from a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")


if __name__ == "__main__":
    pass
