#!/usr/bin/python3
"""Student class with filtered JSON conversion."""


class Student:
    """Represents a student with filtered JSON serialization."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: Student's first name
            last_name: Student's last name
            age: Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary representation with optional filtering.

        Args:
            attrs: List of attributes to include (None for all)

        Returns:
            Dictionary containing requested student attributes
        """
        if attrs is None:
            return self.__dict__

        return {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }