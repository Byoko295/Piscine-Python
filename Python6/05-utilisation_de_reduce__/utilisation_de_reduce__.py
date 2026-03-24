"""
Calculer le produit de tous
les éléments dune liste.
"""
from functools import reduce


__author__ = "benoui_m"


def product(numbers: list) -> int:
    """
    Calculer le produit de tous
    les éléments dune liste.
    """
    if len(numbers) == 0:
        return 0
    else:
        return (reduce(lambda a, b: a * b, numbers))
