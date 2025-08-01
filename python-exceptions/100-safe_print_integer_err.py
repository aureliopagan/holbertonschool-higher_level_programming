#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Safely print an integer with error handling.

    Args:
        value: Value of any type to attempt to print as integer

    Returns:
        True if value was successfully printed as integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
