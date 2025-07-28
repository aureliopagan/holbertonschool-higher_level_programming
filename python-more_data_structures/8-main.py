def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# Example usage
if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Before deletion:", my_dict)
    simple_delete(my_dict, 'b')
    print("After deletion:", my_dict)