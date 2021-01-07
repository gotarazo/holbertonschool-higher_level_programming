#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all integers or floats of a matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix
    len_row = -1
    list_resul = []
    for row in matrix:
        if (len_row != len(row) and len_row != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                list_resul.append(round(ele / div, 2))
        len_row = len(row)
    return list_resul
