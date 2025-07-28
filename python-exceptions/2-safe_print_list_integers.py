#!/usr/bin/python3
def safe_print_list_integers(collection=None, elements=0):
    if collection is None:
        collection = []
    printed_ints = 0
    for index in range(elements):
        try:
            print("{:d}".format(collection[index]), end="")
            printed_ints += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print("")
    return printed_ints
