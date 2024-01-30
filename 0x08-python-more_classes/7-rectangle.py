#!/usr/bin/python3
""" Module for work on More_Python_Classes"""


class Rectangle:
    """ Class for rectangle reaction"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates the perimiter of the rectangle"""
        perim = (2 * self.__height) + (2 * self.__width)

        if self.__width == 0 or self.__height == 0:
            perim = 0
        return perim

    def __str__(self):
        """ String representation of the rectangle for printing. """

        value = ""
        if self.__width == 0 or self.__height == 0:
            return value
        else:
            symbol = self.print_symbol
            for h in range(self.__height):
                value += (str(symbol) * self.__width)
                if h < self.__height - 1:
                    value += "\n"
        return value

    def __repr__(self):
        """Returns the official representation of the class instance"""
        rep = ("Rectangle({}, {})".format(self.__width, self.__height))
        return rep

    def __del__(self):
        """Prints this message before instance deletion"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
