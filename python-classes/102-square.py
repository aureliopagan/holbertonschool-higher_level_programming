#!/usr/bin/python3
"""Square class with size attribute and comparison operators."""


class Square:
    """Square class with size attribute and comparison operators."""

    def __init__(self, size=0):
        """Initialize a Square instance with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality operator (==) based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality operator (!=) based on area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than operator (>) based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal operator (>=) based on area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than operator (<) based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal operator (<=) based on area."""
        return self.area() <= other.area()
