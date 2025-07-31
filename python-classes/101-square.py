#!/usr/bin/python3
"""Square class with size and position attributes."""


class Square:
    """Square class with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the Square."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2

    def my_print(self):
        """Print the Square using the '#' character, considering the position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the Square for printing."""
        result = []
        if self.__size == 0:
            return ""

        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result)
