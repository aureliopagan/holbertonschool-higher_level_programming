#!/usr/bin/python3

"""
Write a function that prints My name is <first name> <last name>
Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a
TypeError exception with the message first_name must be a string or
last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first name and last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if not first_name:
        raise TypeError("say_my_name() missing 1 required \
                positional argument: 'first_name'")
    print("My name is {} {}".format(first_name, last_name))
