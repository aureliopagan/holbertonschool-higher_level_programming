#!/usr/bin/python3
"""Handles saving Python objects to JSON files."""

def save_to_json_file(my_obj, filename):
    """Save a Python object to a file as JSON.
    
    Args:
        my_obj: The Python object to save
        filename: Where to save the JSON data
    """
    with open(filename, 'w') as f:
        import json
        f.write(json.dumps(my_obj))
