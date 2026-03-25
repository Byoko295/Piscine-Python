"""
Retourner le total du panier
en tenant compte des quantités.
"""


__author__ = "benoui_m"


def calculate_total(cart: list) -> float:
    """
    Retourner le total du panier
    en tenant compte des quantités.
    """
    somme = 0.0
    for x in range(len(cart)):
        somme += cart[x][1] * cart[x][2]
    return somme
