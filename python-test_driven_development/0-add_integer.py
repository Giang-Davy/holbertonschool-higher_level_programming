#!/usr/bin/python3
"""Definir la fonction"""
def add_integer(a, b=98):
    """Erreur pour si != int et float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """si float => int"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
