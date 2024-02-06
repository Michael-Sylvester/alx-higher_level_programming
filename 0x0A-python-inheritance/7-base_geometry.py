#!/usr/bin/python3
"""module for base BaseGeometry"""


class BaseGeometry:
    """base class for further tasks"""
    def area(self):
        """Always raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates  value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
