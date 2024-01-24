#!/usr/bin/python3
"""Code that does something with squares"""


class Square:
    """ Initialise empty square class"""
    def __init__(self, size=0):
        """ Initialize size 
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def size(self):
        return self.size

    def size(self, value):
        """ setter or the size value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value