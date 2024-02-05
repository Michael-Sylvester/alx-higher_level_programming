#!/usr/bin/python3
"""module for lookup function"""

def lookup(obj):
    """function to look up attributes"""
    attributes = list(dir(obj))
    return attributes

if __name__ == "__main__":
    pass
