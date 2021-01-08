#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after '.', '?', and ':"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    specials = ['.', '?', ':']
    for ch in text:
        string += ch
        if ch in specials:
            string += "\n\n"
    print(string, end='')
