"""
retourne une liste constituée
uniquement des nombres pairs
"""


__author__ = "benoui_m"


def filter_even_numbers(numbers: list[int]) -> list:
    """
    retourne une liste constituée
    uniquement des nombres pairs
    """
    lst = list(filter(lambda x: x % 2 == 0, numbers))
    return (lst)
