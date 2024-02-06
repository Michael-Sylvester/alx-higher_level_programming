#!/usr/bin/python3
"""Module for appending from files"""


def append_write(filename="", text=""):
    """Function to write text to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        num = file.write(text)
    return num


if __name__ == "__main__":
    pass
