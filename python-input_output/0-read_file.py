#!/usr/bin/python3
"""Contains function to display file contents."""


def read_file(filename=""):
    """Prints contents of UTF-8 text file to screen.

    Uses context manager for automatic file handling.
    Reads entire file at once for small files.
    """
    with open(filename, mode='r', encoding='utf-8') as file_obj:
        print(file_obj.read(), end='')
