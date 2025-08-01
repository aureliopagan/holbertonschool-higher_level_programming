#!/usr/bin/python3
"""Module for calculating weighted average."""


def weight_average(my_list=[]):
    """
    Calculate the weighted average of tuples containing (score, weight).

    Args:
        my_list: List of tuples where each tuple is (score, weight)

    Returns:
        Float representing the weighted average, or 0 if list is empty
    """
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weight += weight

    return total_weighted_sum / total_weight
