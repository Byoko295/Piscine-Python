"""
Écrire une fonction qui prend une liste de paires en paramètre
"""


__author__ = "benoui_m"


def list_to_dict(pairs: list[tuple]) -> dict[int, str]:
    """
    Écrire une fonction qui prend une liste de paires en paramètre
    """
    lst = {x: y for x, y in pairs}
    return (lst)
