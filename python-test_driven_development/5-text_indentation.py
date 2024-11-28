#!/usr/bin/python3
"""Fonction de division de matrice"""


def text_indentation(text):
    """Fonction pour ajouter des sauts dation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    skip_space = False
    for i in text:
        if i == " " and skip_space:
            continue
        result += i
        if i in ".:?":
            result += "\n"
            skip_space = True
        else:
            skip_space = False
    print(result.strip(), end="")
