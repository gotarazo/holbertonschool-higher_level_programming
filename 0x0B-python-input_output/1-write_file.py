#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """Write string to text file and returns number characters written"""
    with open(filename, "w", encoding="utf-8") as _file:
        return _file.write(text)
