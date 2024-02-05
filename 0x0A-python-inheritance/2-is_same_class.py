#!/usr/bin/python3
"""module for lookup function"""


def is_same_class(obj, a_class):
    """function to check objects against a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
