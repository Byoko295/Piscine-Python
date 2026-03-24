"""
Retourner uniquement les nombres
pairs d'une liste.
"""


__author__ = "benoui_m"


def even_numbers(lst: list) -> list:
    """
    Retourner uniquement les
    nombres pairs d'une liste.
    """
    res = [i for i in lst if i % 2 == 0]
    return (res)
