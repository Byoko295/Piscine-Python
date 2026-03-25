"""
Transformer un dictionnaire en liste de
tuples triée par valeurs décroissantes.
"""


__author__ = "benoui_m"


def dict_to_sorted_list(d: dict) -> list:
    """
    Transformer un dictionnaire en liste de
    tuples triée par valeurs décroissantes.
    """

    lst = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return lst
