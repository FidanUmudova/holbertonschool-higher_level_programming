#!/usr/bin/python3
"""Module that defines Animal abstract class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
