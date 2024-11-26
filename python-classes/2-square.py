#!/usr/bin/python3
"""Representation d'un carre"""


class Square:
    """définition de la classe Square"""

    def __init__(self, size=0):
        """initialisation de size"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
    
