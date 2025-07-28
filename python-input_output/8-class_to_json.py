#!/usr/bin/python3
"""Converts class attributes to JSON-serializable dictionary."""

def class_to_json(obj):
    """Returns object's attributes as a dictionary.
    
    Gets all attributes that can be serialized to JSON.
    """
    return obj.__dict__
