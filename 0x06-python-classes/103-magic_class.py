#!/usr/bin/python3
"""Define a Python class MagicClass that does the same as a Python bytecode"""


import math


class MagicClass:
    """Represent a Circle"""

    def __init__(self, radius=0):
        """Initialize the MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the Circle-MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the Circle-MagicClass"""
        return self.__radius * 2 * math.pi
