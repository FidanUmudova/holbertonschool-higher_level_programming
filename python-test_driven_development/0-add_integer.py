#!/usr/bin/python3
"""Module for adding two integers safely"""


def add_integer(a, b=98):
    """Adds two integers and returns the result"""

    # Type check
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN or Infinity
    for val, name in ((a, "a"), (b, "b")):
        if isinstance(val, float):
            if val != val or val == float('inf') or val == float('-inf'):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
