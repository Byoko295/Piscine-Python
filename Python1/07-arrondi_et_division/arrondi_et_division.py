"""
Une fonction qui retourne vraie su le nombre est paire
faux si il ne l'est pas
"""


__author__ = "benoui_m"


def division_details(a: int, b: int) -> tuple:
    """
    retourne le quotient et le reste
    de la division
    """
    return ((a // b, a % b) if b != 0 else (None, None))
