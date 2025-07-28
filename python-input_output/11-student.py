#!/usr/bin/python3
"""Student class module."""

class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary of attributes."""
        return self.__dict__

    def reload_from_json(self, json):
        """Update attributes from dictionary."""
        for key in json:
            setattr(self, key, json[key])

    def __str__(self):
        """Return string representation."""
        return "[Student] {} {} {}".format(
            self.first_name, self.last_name, self.age
        )
