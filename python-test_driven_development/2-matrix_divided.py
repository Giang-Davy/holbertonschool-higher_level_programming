#!/usr/bin/python3
"""Fonction de division de matrice"""


def matrix_divided(matrix, div):
    """Divise chaque élément à 2 décimales"""
    if not (isinstance(matrix, list) or all(isinstance(x, (int, float)) for row in matrix for x in row)):
        er = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(er)
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
