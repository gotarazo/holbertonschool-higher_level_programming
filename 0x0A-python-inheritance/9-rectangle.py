#!/usr/bin/python3
"""Defines the class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle shape, inheirts from basegeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Method for str and print representation"""
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string

    def area(self):
        """Return the area for use rectangle"""
        return (self.__width * self.__height)
