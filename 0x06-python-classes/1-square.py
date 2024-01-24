#!/usr/bin/python3
"""Code that does something """


class Square:
    """ Initialise empty square class"""
    __size = None
    def __init__(self, size):
        """Initialize Non to a vlaue """
        if size is not None:
            self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)