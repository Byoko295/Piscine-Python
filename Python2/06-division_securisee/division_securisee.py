"""
Diviser deux nombres avec gestion de l'erreur de division par zéro.
"""


__author__ = "benoui_m"


def safe_divide(a: int, b: int) -> float:
    """
    Diviser deux nombres avec gestion de l'erreur de division par zéro.
    """
    if (b == 0):
        return "Erreur : division par zéro"
    else:
        return (a / b)
