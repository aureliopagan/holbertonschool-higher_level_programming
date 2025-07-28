#!/usr/bin/python3
"""Basic JSON serialization/deserialization module."""

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save to file.
    
    Args:
        data: Dictionary to serialize
        filename: Path to save JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """Load and deserialize JSON file to dictionary.
    
    Args:
        filename: Path to JSON file
        
    Returns:
        Deserialized dictionary data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
