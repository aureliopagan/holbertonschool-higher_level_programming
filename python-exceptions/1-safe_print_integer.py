#!/usr/bin/python3
def safe_print_integer(val):
    is_integer = True
    try:
        print("{:d}".format(val))
    except (ValueError, TypeError):
        is_integer = False
    return is_integer
