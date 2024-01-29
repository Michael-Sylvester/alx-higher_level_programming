#!/usr/bin/python3
"""Module for printing multiple blank lines"""


def text_indentation(text):
    """prints 2 new lines when special characer is read """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = 0
    text = text.lstrip()
    while ch < len(text):
        if text[ch] in ['.', '?', ':']:
            print(text[ch] + "\n")

            while (ch + 1) < len(text) and text[ch + 1] == ' ':
                ch += 1
        else:
            print(text[ch], end="")
        ch += 1
