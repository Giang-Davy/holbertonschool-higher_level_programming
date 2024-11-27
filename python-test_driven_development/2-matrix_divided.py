#!/usr/bin/python3
"""Fonction de division de matrice"""


def matrix_divided(matrix, div):
    """Divise chaque élément de la matrice par décimales"""  
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
