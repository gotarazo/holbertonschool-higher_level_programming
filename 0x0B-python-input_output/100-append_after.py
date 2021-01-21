#!/usr/bin/python3
"""Defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts line of text to file line containing specific string after"""
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
