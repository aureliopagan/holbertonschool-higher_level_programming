#!/usr/bin/python3

"""
0-add_integer.py
"""


def add_integer(a, b=98):
    """ add two integers or two floats """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return a + b
