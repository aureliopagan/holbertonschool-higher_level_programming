#!/usr/bin/python3
"""JSON string deserialization module."""

import json

def from_json_string(my_str):
    """Convert a JSON formatted string to a Python object."""
    return json.loads(my_str)
