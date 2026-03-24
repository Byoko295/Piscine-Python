"""
Retourner une fonction qui ajoute
un nombre donné à son paramètre.
"""


__author__ = "benoui_m"


def make_adder(x: int):
    """
    Retourner une fonction qui ajoute
    un nombre donné à son paramètre.
    """
    def adder(n):
        return x + n
    return adder
