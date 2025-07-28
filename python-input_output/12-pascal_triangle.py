#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        new_row = [1]
        for i in range(1, len(triangle[-1])):
            new_row.append(triangle[-1][i - 1] + triangle[-1][i])
        new_row.append(1)
        triangle.append(new_row)
    return triangle