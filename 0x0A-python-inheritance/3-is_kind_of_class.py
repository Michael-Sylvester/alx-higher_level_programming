#!/usr/bin/python3
"""module for checking obj class"""


def is_kind_of_class(obj, a_class):
    """function to check objects against a class and its children"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
