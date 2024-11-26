#!/usr/bin/python3
"""Representation d'un carre"""


class Square:
    """d√©finition de la classe Squar"""

    def __init__(self, size=0):
        """initialisation de size"""
        self.size = size

    def area(self):
        """Retourne l'aire du carr√"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter pour r√©cup√©rer la taille du car"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour modifier la taille du carr√"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
