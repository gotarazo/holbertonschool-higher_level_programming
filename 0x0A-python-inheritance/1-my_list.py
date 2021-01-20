#!/usr/bin/python
"""Defines the extended version of list"""


class MyList(list):
    """Represent a extended version of MyList"""

    def print_sorted(self):
        """Print the list but sorted (ascending sort)"""
        print(sorted(self))
