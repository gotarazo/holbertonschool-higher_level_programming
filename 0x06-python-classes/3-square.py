#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square with size"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
