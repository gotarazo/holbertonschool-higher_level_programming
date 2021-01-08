#!/usr/bin/python3
"""Defines my name is printing function"""


def say_my_name(first_name, last_name=""):
    """Prints a string for a names"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
