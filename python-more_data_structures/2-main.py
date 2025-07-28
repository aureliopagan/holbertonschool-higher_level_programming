def uniq_add(my_list):
    """Adds all unique integers in a list."""
    return sum(set(my_list))

if __name__ == "__main__":
    # Example test case
    print(uniq_add([1, 2, 3, 2, 1]))  # Output: 6
    print(uniq_add([1, 1, 1, 1]))     # Output: 1
    print(uniq_add([]))                # Output: 0