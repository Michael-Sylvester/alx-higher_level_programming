#!/usr/bin/python3
"""Module for add_atrtibute Function"""


def add_attribute(obj, attr, value):
    """Checks if valid stribut is being set"""
    if not isinstance(attr, str):
        raise TypeError("can't add new attribute")

    if not isinstance(obj, object):
        raise TypeError("can't add new attribute")

    if hasattr(obj, '__slots__') and attr not in obj.__slots__:
        raise TypeError("can't add new attribute")

    builtin_types = [int, str, list, dict, tuple, set,co
                     float, bool, complex, bytes]
    if type(obj) in builtin_types:
        raise TypeError("can't add new attribute")

    status = setattr(obj, attr, value)

if __name__ == "__main__":
    pass