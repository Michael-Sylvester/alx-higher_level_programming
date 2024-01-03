#!/usr/bin/python3
def remove_char_at(input_str, n):
    """
    Creates a copy of the string, removing the character at position n.

    Parameters:
    - input_str (str): The input string.
    - n (int): The position of the character to remove (C array index).

    Returns:
    - str: The modified string.
    """
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if n is out of range

    result = ""
    for i in range(len(input_str)):
        if i != n:
            result += input_str[i]

    return result
