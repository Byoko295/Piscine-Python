"""
Calculer la monnaie rendue selon un paiement donné.
"""


__author__ = "benoui_m"


def calculate_change(cart: list, amount_paid: float) -> float:
    """
    Calculer la monnaie rendue selon un paiement donné.
    """
    paid = 0.0
    somme = 0.0
    for x in range(len(cart)):
        somme += cart[x][1] * cart[x][2]
    return (amount_paid - somme if amount_paid >= somme else 0)
