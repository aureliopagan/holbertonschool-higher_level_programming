#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for letter in str:
        ascii_val = ord(letter)
        if 97 <= ascii_val <= 122:  # Check if lowercase
            uppercase_str += chr(ascii_val - 32)
        else:
            uppercase_str += letter
    print("{}".format(uppercase_str), end="")
    print()
    