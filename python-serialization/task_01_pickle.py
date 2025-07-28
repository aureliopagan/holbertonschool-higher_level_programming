#!/usr/bin/python3
"""Module for custom object serialization using pickle."""

import pickle

class CustomObject:
    """A custom class that supports serialization with pickle."""
    
    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.
        
        Args:
            name: The object's name (str)
            age: The object's age (int)
            is_student: Student status (bool)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle.
        
        Args:
            filename: Path to save the serialized object
            
        Returns:
            None if serialization fails
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.
        
        Args:
            filename: Path to the serialized object
            
        Returns:
            CustomObject instance or None if deserialization fails
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (IOError, pickle.UnpicklingError, AttributeError, EOFError):
            return None
        return None
