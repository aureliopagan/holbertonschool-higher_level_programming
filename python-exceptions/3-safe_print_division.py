#!/usr/bin/python3
def safe_print_division(dividend, divisor):
    quotient = None
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
