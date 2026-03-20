#!/usr/bin/python3
"""Module for adding two integers"""


def add_integer(a, b=98):
    """Adds two integers and returns the result"""

    if not isinstance(a, (int, float)) or a != a:  
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)) or b != b:  
        raise TypeError("b must be an integer")

    return int(a) + int(b)
