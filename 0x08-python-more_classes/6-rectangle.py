#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""
        type(self).instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the rectangle"""
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
        """Set the height of the rectangle"""
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
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Prints the representation of the rectangle"""

        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(0, self.height):
            for j in range(0, self.width):
                rectangle += '#'
            if i != self.height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """Prints the string representation of the rectangle"""

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Print a message for every deletion of the rectangle"""
        type(self).instances -= 1
        print("Bye rectangle...")
