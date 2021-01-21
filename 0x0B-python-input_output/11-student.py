#!/usr/bin/python3
"""Defines the class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the Student"""
        if (type(attrs) == list and
                all(type(a) == str for a in attrs)):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for a, b in json.items():
            setattr(self, a, b)
