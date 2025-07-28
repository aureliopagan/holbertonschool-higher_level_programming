def multiply_list_map(my_list, number):
    return list(map(lambda x: x * number, my_list))


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    multiplier = 2
    result = multiply_list_map(test_list, multiplier)
    print(f"Original list: {test_list}")
    print(f"Multiplied by {multiplier}: {result}")