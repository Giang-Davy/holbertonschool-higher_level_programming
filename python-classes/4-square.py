#!/usr/bin/python3

"""Representation d'un carré"""


class Square:
    """Définition de la classe Square"""

    def __init__(self, size=0):
        """Initialisation de size"""
        self.size = size

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter pour récupérer la taille du carré"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour modifier la taille du carré"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
