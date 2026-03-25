"""
Permettre aux clients de payer
avec leurs points fidélité.
"""


__author__ = "benoui_m"


def redeem_loyalty_points(cart: list, points: int) -> float:
    """
    Permettre aux clients de payer
    avec leurs points fidélité.
    """
    somme = 0
    for x in cart:
        somme += x[1] * x[2]
        somme = round(somme, 2)
    return (somme - points if points <= somme else 0)
