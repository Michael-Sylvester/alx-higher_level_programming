#!/usr/bin/python3
"""Code that does something with squares

Attributes:
        size (int): Size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        area(self): Calculates and returns the area of the square.
"""


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
        """Return the current area of the square.
        Returns: 
        int: the calculated square of the __size property
        """
        return self.__size ** 2
