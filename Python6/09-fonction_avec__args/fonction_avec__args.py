"""
Retourner la somme de plusieurs
nombres passés en paramètre.
"""


__author__ = "benoui_m"


def sum_all(*args) -> int:
    """
    Retourner la somme de plusieurs
    nombres passés en paramètre.
    """
    summ = 0
    for x in args:
        summ += x
    return summ
