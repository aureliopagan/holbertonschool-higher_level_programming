#!/usr/bin/python3
def list_division(list1, list2, length):
    division_results = []
    for index in range(length):
        current_result = 0
        try:
            # Check if elements are numbers
            if not isinstance(list1[index], (int, float)) or not isinstance(list2[index], (int, float)):
                raise TypeError
            current_result = list1[index] / list2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            division_results.append(current_result)
    return division_results
