#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON"""


class Student:
    """Class that defines a student with filtered to_json method"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation with optional filter"""
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
