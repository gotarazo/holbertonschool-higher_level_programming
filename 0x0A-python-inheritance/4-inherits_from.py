#!/usr/bin/python3
"""Defines the inherited class-checking function"""


def inherits_from(obj, a_class):
    """Reurn True if an object is an inherited instance of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
