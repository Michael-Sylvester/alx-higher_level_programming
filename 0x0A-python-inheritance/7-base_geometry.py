#!/usr/bin/python3
"""module for base BaseGeometry"""


class BaseGeometry:
    """base class for further tasks"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer", format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
