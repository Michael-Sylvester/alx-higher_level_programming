#!/usr/bin/python3
"""Square Class inherites from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """CLass sqaure is a child of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(size, size, x, y, id)

    def __str__(self):
        """determin how the class is represented as a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """getter for width"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for width"""
        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes of the obj"""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError as e:
                return
        elif kwargs and len(kwargs) > 0:
            for key, item in kwargs.items():
                if key == "id":
                    super().__init__(self.size,
                                     self.size,
                                     self.x,
                                     self.y,
                                     item)
                elif key == "size":
                    self.size = item
                elif key == "x":
                    self.x = item
                elif key == "y":
                    self.y = item

    def to_dictionary(self):
        """Return Class attributes as a dictionary"""
        return {key: getattr(self, key) for key in ['x', 'y', 'id', 'size']}
