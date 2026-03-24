"""
Filtrer les nombres pairs dune liste.
"""


__author__ = "benoui_m"


def filter_even(numbers: list) -> list:
    """
    Filtrer les nombres pairs dune liste.
    """
    pairs = []
    for x in range(len(numbers)):
        if (not numbers[x] & 1):
            pairs.append(numbers[x])
    return (pairs)
