#!/usr/bin/python


class MyList(list):
    """Defines a extended version of list"""

    def print_sorted(self):
        """Print the list but sorted (ascending sort)"""
        print(sorted(self))
