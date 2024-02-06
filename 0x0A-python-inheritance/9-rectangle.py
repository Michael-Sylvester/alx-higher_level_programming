#!/usr/bin/python3
"""module for child class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize starting values"""
        self.integer_validator("Rectangle", width)
        self.integer_validator("Rectangle", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        msg = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return msg
