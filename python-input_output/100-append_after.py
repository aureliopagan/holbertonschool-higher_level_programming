#!/usr/bin/python3
"""Module for appending text after lines containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.

    Args:
        filename: Name of the file to modify
        search_string: String to search for in each line
        new_string: String to insert after matching lines
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
