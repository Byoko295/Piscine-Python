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

    reversed_d = dict(reversed(sorted(d.items())))
    lst = []
    for x in reversed_d.keys():
        lst.append((x, d[x]))
    return (lst)
