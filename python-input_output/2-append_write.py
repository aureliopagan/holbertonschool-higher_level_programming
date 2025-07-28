#!/usr/bin/python3
"""Handles appending text to files."""


def append_write(filename="", text=""):
    """Adds text to end of file and returns character count."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
