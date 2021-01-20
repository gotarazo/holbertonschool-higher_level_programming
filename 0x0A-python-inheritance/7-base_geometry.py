#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Represent the base geometry"""

    def area(self):
        """Calculate area of shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a parameter is an integer"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
