#!/usr/bin/python3
"""module for child class Myint"""


class MyInt(int):
    """CLass for custom int Class"""
    def __eq__(self, __value: object) -> bool:
        """Runs the not equal to when called"""
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """Runs the equal to built-in when called"""
        return super().__eq__(__value)
