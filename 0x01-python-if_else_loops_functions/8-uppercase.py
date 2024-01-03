#!/usr/bin/python3
def uppercase(input_str):
    """
    Prints the uppercase version of a string followed by a new line.

    Parameters:
    - input_str (str): The input string.

    Returns:
    - None
    """
    for char in input_str:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase_char), end="")
        print()
