#!/usr/bin/python3
"""module for child class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Initialize starting values"""
        self.integer_validator("Square", size)
        self.__size = size

    def area(self):
        """Function for calculating area based on private attributes"""
        return self.__size ** 2

    def __str__(self):
        """Function for determining what class looks like as string"""
        msg = "[Square] {}/{}".format(self.__size, self.__size)
        return msg
