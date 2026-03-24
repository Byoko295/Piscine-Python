"""
Supprimer un élément spécifique
d'une liste (s'il existe).
"""


__author__ = "benoui_m"


def remove_element(lst: list, elem) -> list:
    """
    Supprimer un élément spécifique
    d'une liste (s'il existe).
    """
    res = [i for i in lst if i != elem]
    return (res)
