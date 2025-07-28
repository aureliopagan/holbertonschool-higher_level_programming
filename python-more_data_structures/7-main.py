def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] += value
    else:
        a_dictionary[key] = value
    return a_dictionary

# Example usage
if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2}
    print(update_dictionary(my_dict, 'a', 2))  # Should update 'a' to 3
    print(update_dictionary(my_dict, 'c', 3))  # Should add 'c' with value 3
    print(my_dict)  # Final dictionary should be {'a': 3, 'b': 2, 'c': 3}