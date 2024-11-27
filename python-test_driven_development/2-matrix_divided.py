#!/usr/bin/python3
"""Fonction"""


def matrix_divided(matrix, div):
    """Divise chaque élément de la matdeux décimales"""
    # Vérifier si chaque ligne a la même taille
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
