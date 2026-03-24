"""
Transformer une liste en liste
de tuples (index, valeur).
"""


__author__ = "benoui_m"


def enumerate_list(lst: list) -> list:
    """
    Transformer une liste en
    liste de tuples (index, valeur).
    """
    res = []
    for x in range(len(lst)):
        res.append((x, lst[x]))
    return (res)
