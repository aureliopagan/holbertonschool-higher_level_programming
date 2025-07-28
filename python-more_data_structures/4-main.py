# 4-main.py

#!/usr/bin/python3
"""
Main file for testing the function only_diff_elements.
"""

from 4-only_diff_elements import only_diff_elements

# Test cases
if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]
    print(only_diff_elements(list_1, list_2))  # Expected output: [1, 2, 3, 6, 7, 8]

    list_1 = ["apple", "banana", "cherry"]
    list_2 = ["banana", "kiwi", "mango"]
    print(only_diff_elements(list_1, list_2))  # Expected output: ['apple', 'cherry', 'kiwi', 'mango']