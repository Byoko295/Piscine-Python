"""
Écrire une fonction qui retourne une
liste contenant les nombres de 1 à n.
"""


__author__ = "benoui_m"


def create_list(n: int) -> list:
    """
    Écrire une fonction qui retourne
    une liste contenant les nombres de 1 à n.
    """
    lst = [x for x in range(1, n + 1)]
    return (lst)
