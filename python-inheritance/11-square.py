#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle with str method"""

    def __init__(self, size):
        """Initialize square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

    def __str__(self):
        """Returns string description of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
