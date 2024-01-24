#!/usr/bin/python3
"""Code that does something with squares"""


class Square:
    """ Initialise empty square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize size
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        # validation for position tuple
        pos = position
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(pos[0], int) or not isinstance(pos[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter or the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with #s"""
        if (self.__size == 0):
            print("")
        else:
            num = self.__size
            for posH in range(self.__position[1]):
                print("\n")
            for hash in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size + '\n')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """For setting new values to position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """ String representation of the square for printing. """
        result = ""
        if self.__size == 0:
            return result

        for hieght in range(self.__position[1]):
            result += '\n'

        for breath in range(self.__size):
            result += (' ' * self.__position[0]) + ('#' * self.__size + '\n')

        return result
