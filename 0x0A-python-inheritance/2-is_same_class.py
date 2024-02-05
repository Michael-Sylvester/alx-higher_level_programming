#!/usr/bin/python3
"""module for checking obj class"""


def is_same_class(obj, a_class):
    """function to check objects against a specific class"""
    if type(obj) is a_class:
        return True
    else:
        return False
