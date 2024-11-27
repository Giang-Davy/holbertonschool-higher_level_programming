#!/usr/bin/python3
"""Fonction de division de matrice"""


def print_square(size):
    """alo"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
