# 3-main.py

from common_elements import common_elements

# Test cases for common_elements function
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print("Common elements:", common_elements(list1, list2))

    list1 = ["apple", "banana", "cherry"]
    list2 = ["banana", "kiwi", "cherry"]
    print("Common elements:", common_elements(list1, list2))

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("Common elements:", common_elements(list1, list2))