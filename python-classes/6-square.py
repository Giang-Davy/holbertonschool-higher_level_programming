#!/usr/bin/python3


"""Initialisation d'une classe représentant un carré."""
class Square:
    """BLABLA"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise la taille et la position du carré."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré en vérifiant les conditions."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retourne la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré avec une vérification."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l'aire du carre"""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré dans la console en tenant compte de la position."""
        if self.size == 0:
            print("")
            return
        for _ in range(self.position[1]):
            print("")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)