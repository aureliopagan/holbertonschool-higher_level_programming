#!/usr/bin/python3
"""This script adds all command-line integers and prints the sum."""


def calculate_sum():
    """Calculates the sum of all integer arguments."""
    from sys import argv
    result = 0
    for number in argv[1:]:
        result += int(number)
    return result


if __name__ == "__main__":
    print(calculate_sum())
