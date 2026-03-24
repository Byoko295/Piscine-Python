"""
retourne le signe d'un int en str
"""


__author__ = "benoui_m"


def number_sign(n: int) -> str:
    """
    retourne le signe d'un int en str
    """
    if (n > 0):
        return ("positif")
    elif (n == 0):
        return ("nul")
    else:
        return ("négatif")
