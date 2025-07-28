#!/usr/bin/python3
"""Handles loading JSON data from files."""

import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file.

    Args:
        filename: Path to the JSON file to read

    Returns:
        The Python object represented by the JSON data
    """
    with open(filename, 'r') as f:
        return json.load(f)
