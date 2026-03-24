"""
Retirer tous les éléments
None d'une liste.
"""


__author__ = "benoui_m"


def remove_none(lst: list) -> list:
    """
    Retirer tous les éléments
    None d'une liste.
    """
    res = [i for i in lst if i is not None]
    return (res)
