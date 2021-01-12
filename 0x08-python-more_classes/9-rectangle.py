#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""

        Rectangle.number_of_instances += 1
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

        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                rectangle += str(self.print_symbol)
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

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle with by the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle of width = height = size"""
        return cls(size, size)
