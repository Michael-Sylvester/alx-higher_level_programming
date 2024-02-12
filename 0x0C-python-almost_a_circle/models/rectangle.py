#!/usr/bin/python3
"""Rectangle Class inherites from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """Return Class attributes as a dictionary"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def display(self):
        """Display the obj as a group of #"""
        symbol = '#'
        value = ""
        for num in range(self.__y):
            value += "\n"
        for h in range(self.__height):
            for num in range(self.__x):
                value += " "
            value += (str(symbol) * self.__width)
            if h < self.__height - 1:
                value += "\n"
        print(value)

    def __str__(self):
        """determin how the class is represented as a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """update the attributes of the obj"""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError as e:
                return
        elif kwargs and len(kwargs) > 0:
            for key, item in kwargs.items():
                if key == "id":
                    super().__init__(item)
                elif key == "width":
                    self.width = item
                elif key == "height":
                    self.height = item
                elif key == "x":
                    self.x = item
                elif key == "y":
                    self.y = item

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of rectangle"""
        return self.__height * self.__width
