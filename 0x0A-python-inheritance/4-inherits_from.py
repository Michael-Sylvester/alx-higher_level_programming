#!/usr/bin/python3
"""module for checking obj class"""


def inherits_from(obj, a_class):
    """function to check objects against a class and its children"""
    allclasses = type(obj).__mro__
    for cls in allclasses:
        if cls is a_class:
            return False
        if issubclass(cls, a_class):
            return True
    else:
        return False
if __name__ == "__main__":
    pass