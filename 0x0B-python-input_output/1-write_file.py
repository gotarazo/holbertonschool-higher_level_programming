#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """Write a string to a text file and returns the number characters written"""
    with open(filename, "w", encoding="utf-8") as _file:
        return _file.write(text)
