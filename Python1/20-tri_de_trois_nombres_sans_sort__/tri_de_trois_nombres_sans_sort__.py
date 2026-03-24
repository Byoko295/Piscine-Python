"""
tri entre trois nombre
"""


__author__ = "benoui_m"


def sort_three_numbers(a: int, b: int, c: int) -> tuple:
    """
    retourne les int dans l'ordre
    """
    smallest = min(a, b, c)
    largest = max(a, b, c)
    middle = a + b + c - smallest - largest
    return (smallest, middle, largest)
