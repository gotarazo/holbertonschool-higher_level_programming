#!/usr/bin/python3
"""Defines the class-checking function"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of specified class"""

    if type(obj) == a_class:
        return True
    return False
