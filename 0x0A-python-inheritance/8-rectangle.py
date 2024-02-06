#!/usr/bin/python3
"""module for child class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize starting values"""
        self.__width = self.integer_validator("Rectangle", width)
        self.__height = self.integer_validator("Rectangle", height)
