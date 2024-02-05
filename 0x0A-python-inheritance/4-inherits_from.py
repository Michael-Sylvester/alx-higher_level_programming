#!/usr/bin/python3
"""module for checking obj class"""


def inherits_from(obj, a_class):
    """function to check objects against a class and its children"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
if __name__ == "__main__":
    pass