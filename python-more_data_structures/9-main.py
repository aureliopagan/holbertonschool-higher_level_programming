def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}

if __name__ == "__main__":
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = multiply_by_2(sample_dict)
    print(result)  # Expected output: {'a': 2, 'b': 4, 'c': 6}