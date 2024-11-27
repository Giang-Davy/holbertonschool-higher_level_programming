#!/usr/bin/python3
"""Fonction"""


def add_integer(a, b=98):
    """Ajoute deux entiers ou flottants"""
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = a + b
    if result > 1e308:
        return float('inf')
    return result
