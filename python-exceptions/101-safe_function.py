#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Execute a function safely with error handling.

    Args:
        fct: Function to execute
        *args: Arguments to pass to the function

    Returns:
        Result of the function if successful, None if an exception occurs
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
