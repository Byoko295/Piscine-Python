"""
Retourner la somme des entiers de 1 à N.
"""


__author__ = "benoui_m"


def sum_up_to(n: int) -> int:
    """
    Retourner la somme des entiers de 1 à N.
    """
    count = 0
    for x in range(n + 1):
        count += x
    return (count)
