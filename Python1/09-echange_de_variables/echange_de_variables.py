"""
Une fonction qui swap des variables
"""


__author__ = "benoui_m"


def swap(a: int, b: int) -> tuple:
    """
    fonction qui swap les deux variables a et b
    """
    c = a
    a = b
    b = c
    return (a, b)
