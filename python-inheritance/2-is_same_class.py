#!/usr/bin/python3
"""
This module contains a function that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, else False.

    Args:
        obj: The object to check.
        a_class: The class to compare the type against.

    Returns:
        True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) == a_class
