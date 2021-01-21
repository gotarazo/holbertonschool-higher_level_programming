#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n (returns list of lists of integers)"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        a = triangle[-1]
        b = [1]
        for i in range(len(a) - 1):
            b.append(tri[i] + a[i + 1])
        b.append(1)
        triangle.append(tmp)
    return triangle
