"""
Retourner la somme des éléments
dune liste de nombres.
"""


__author__ = "benoui_m"


def sum_list(numbers: list) -> int:
    """
    Retourner la somme des éléments
    dune liste de nombres.
    """
    count = 0
    for x in range(len(numbers)):
        count += numbers[x]
    return (count)
