"""
Ajouter un taux de
TVA au total.
"""


__author__ = "benoui_m"


def add_vat(cart: list, vat: float) -> float:
    """
    Ajouter un taux de
    TVA au total.
    """
    somme = 0
    for x in range(len(cart)):
        somme += cart[x][1] * cart[x][2]
    return (round(somme + somme * vat / 100, 2))
