#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        Representing the Rectangle class
        Inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Returning private attribute
        """
        return self.__width

    @property
    def height(self):
        """
        Returning private attribute
        """
        return self.__height

    @property
    def x(self):
        """
        Return the value for x
        """
        return self.__x

    @property
    def y(self):
        """
        Return the value for y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
            Setting private attribute
        """
        self.setter_validation("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """
            Setting private attribute
        """
        self.setter_validation("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setting private attributes
        """
        self.setter_validation("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """
            Setting private attribute
        """
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """
            Returns the area of the rectangle
        """
        return (self.height * self.width)

    def display(self):
        """
            Prints to stdout the representation of the rectangle
        """
        # We handled for x and y here
        # self.x handles the horizontal position of the rectangle
        # self.y handles the vertical position of the rectangle
        # The default values for x and y are zero (in __init__ method)

        # Create an empty string
        rectangle = ""

        # Printing the empty space for y
        print("\n" * self.y, end="")

        for i in range(self.height):
            # Printing the empty space in front of '#' for x
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"

        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """
            Updates the arguments in the class
        """
        """
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                # setattr(self, key, value)
                self.__setattr__(key, value)
        else:
            # If args is not empty
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                    a += 1
                elif kwargs and len(kwargs) != 0:
                    for k, v in kwargs.items():
                        if k == "id":
                            if v is None:
                                self.__init__(self.width, self.height, self.x,
                                              self.y)
                            else:
                                self.id = v
                        elif k == "width":
                            self.width = v
                        elif k == "height":
                            self.height = v
                        elif k == "x":
                            self.x = v
                        elif k == "y":
                            self.y = v

    def to_dictionary(self):
        """
            Returns a dictionary representation of this class
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}

    @staticmethod
    def setter_validation(attribute, value):
        """ The setter_validation function """
        # Checking if value is an integer
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))

        # Checking if attribute == x or attribute == y
        # and if value is greater than 0
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        """
            Overwritting the str method
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)
