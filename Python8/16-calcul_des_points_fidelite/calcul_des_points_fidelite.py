"""
Générer des points fidélité
en fonction du total.
"""


__author__ = "benoui_m"


def calculate_loyalty_points(cart: list) -> int:
    """
    Générer des points fidélité
    en fonction du total.
    """
    somme = 0
    for x in cart:
        somme += x[1] * x[2]
    return int(somme)
