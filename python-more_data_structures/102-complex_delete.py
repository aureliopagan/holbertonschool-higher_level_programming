#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Delete all keys from dictionary that have a specific value.
    
    Args:
        a_dictionary: The dictionary to modify
        value: The value to search for and delete keys that have it
        
    Returns:
        The modified dictionary
    """
    keys_to_delete = []
    
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_delete.append(key)
    
    for key in keys_to_delete:
        del a_dictionary[key]
    
    return a_dictionary
