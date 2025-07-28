#!/usr/bin/python3
"""Defines a student class with JSON conversion capability."""


class Student:
    """Represents a student with basic info and JSON conversion."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student.

        Returns:
            dict: The student's attributes as key/value pairs
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
