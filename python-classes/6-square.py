#!/usr/bin/python3

"""Representation d'un carré"""


class Square:
    """Définition de la classe Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialisation de size et position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter pour récupérer la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour modifier la taille du carré."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter pour récupérer la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter pour modifier la position du carré."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère # en tenant compte de la position."""
        if self.size == 0:
            print("")
            return

        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
