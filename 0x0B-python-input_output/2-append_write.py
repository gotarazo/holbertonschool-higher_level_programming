#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """Appends string at end of text file and return number of chars"""
    with open(filename, "a", encoding="utf-8") as _file:
        return _file.write(text)
