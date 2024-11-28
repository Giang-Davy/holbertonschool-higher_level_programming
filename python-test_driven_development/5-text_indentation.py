#!/usr/bin/python3
"""Fonction de division de matrice"""


def text_indentation(text):
    """def"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    result = ""
    skip_space = False
    for i in text:
        if skip_space and i == " ":
            continue
        result += i
        if i in ".:?":
            result += "\n\n"
            skip_space = True
        else:
            skip_space = False
    print(result.strip(), end="")
