#!/usr/bin/python3
"""Defines a JSON sring function"""


import json


def from_json_string(my_str):
    """Return a Python object representation from a JSON string"""
    return json.loads(my_str)
