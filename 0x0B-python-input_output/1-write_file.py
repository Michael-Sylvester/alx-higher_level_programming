#!/usr/bin/python3
"""Module for writing to files"""


def write_file(filename="", text=""):
    """File to write text to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        num = file.write(text)
    return num


if __name__ == "__main__":
    pass
