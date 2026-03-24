"""
    Retourner le signe du produit de deux nombres.
"""


__author__ = "benoui_m"


def product_sign(a: int, b: int) -> str:
    """
    Retourner le signe du produit de deux nombres.
    """
    if ((a < 0 and b < 0) or (a > 0 and b > 0)):
        return "positif"
    elif ((a < 0 and b > 0) or (a > 0 and b < 0)):
        return "négatif"
    else:
        return "nul"
