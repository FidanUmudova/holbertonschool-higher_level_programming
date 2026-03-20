#!/usr/bin/python3
"""Module for adding two integers safely"""


def add_integer(a, b=98):
    """Adds two integers and returns the result"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        
    if isinstance(a, float) and (a != a or a in (float('inf'), float('-inf'))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b in (float('inf'), float('-inf'))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
