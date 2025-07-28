#!/usr/bin/python3
def safe_print_list(a_list=None, num_elements=0):
    if a_list is None:
        a_list = []
    elements_printed = 0
    for index in range(num_elements):
        try:
            print(f"{a_list[index]}", end="")
            elements_printed += 1
        except IndexError:
            break
    print("")
    return elements_printed
