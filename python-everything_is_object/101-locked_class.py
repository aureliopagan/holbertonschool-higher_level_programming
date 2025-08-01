#!/usr/bin/python3
"""Module that defines a LockedClass"""


class LockedClass:
    """Class that prevents dynamic attribute creation except first_name"""
    __slots__ = ['first_name']
