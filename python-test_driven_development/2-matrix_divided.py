#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divise chaque élément de la matrice par div, arrondi à deux décimales"""

    # Vérifier si chaque ligne a la même taille
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Faire les calculs ensuite
    return [[round(elem / div, 2) for elem in row] for row in matrix]
