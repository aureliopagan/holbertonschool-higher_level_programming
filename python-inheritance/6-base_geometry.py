#!/usr/bin/python3
"""
Module containing the BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """
        Public instance method that raises an Exception
        indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")
