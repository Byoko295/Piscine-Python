"""
Appliquer un pourcentage de
remise sur le total.
"""


__author__ = "benoui_m"


def apply_discount(cart: list, discount: float) -> float:
    """
    Appliquer un pourcentage
    de remise sur le total.
    """
    somme = 0
    for x in range(len(cart)):
        somme += cart[x][1] * cart[x][2]
    return (round(somme - somme * discount / 100, 2))
