#!/usr/bin/python3
"""Code that does something with squares"""


class Square:
    """ Initialise empty square class"""
    def __init__(self, size=0):
        """ Initialize size 
        Args:
            size (int, optional): The side length of the square. Defaults to 0.

        Raises:
            ValueError: If the side length is negative.
            TypeError: If the side length is not an integer."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
