#!/usr/bin/python3
"""Code that does something with squares"""


class Square:
    """ Initialise empty square class"""
    def __init__(self, size=0):
        """ Initialize size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Public func for calculating area"""
        return self.__size ** 2
