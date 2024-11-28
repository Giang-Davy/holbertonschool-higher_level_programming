#!/usr/bin/python3
"""Fonction de division de matrice"""


def text_indentation(text):
    """Fonction pour ajouter des stion ou des deux-points."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for i in text:
        if i == " " and skip_space:
            continue
        result += i
        if i in ".:?":
            result += "\n\n"
            skip_space = True
        else:
            skip_space = False
    print(result.strip(), end="")
