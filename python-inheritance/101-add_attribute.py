#!/usr/bin/python3
"""Module that defines add_attribute function"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible"""
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    
    if hasattr(obj, '__slots__') and name not in obj.__slots__:
        raise TypeError("can't add new attribute")
    
    setattr(obj, name, value)
