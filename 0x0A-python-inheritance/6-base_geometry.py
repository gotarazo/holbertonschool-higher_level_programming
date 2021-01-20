#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Calculate area of shape"""
        raise Exception("area() is not implemented")
