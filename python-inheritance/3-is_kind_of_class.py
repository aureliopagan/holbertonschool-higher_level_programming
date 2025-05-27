#!/usr/bin/python3
"""
Module for is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or
    an instance of a subclass of a_class; otherwise False.
    """
    return isinstance(obj, a_class)
