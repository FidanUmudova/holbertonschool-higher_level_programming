#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """Class that defines a base geometry with area method"""

    def area(self):
        """Raises an Exception since area is not implemented"""
        raise Exception("area() is not implemented")
