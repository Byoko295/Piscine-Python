"""
Retourner une liste contenant
les nombres de 1 à n.
"""


__author__ = "benoui_m"


def create_list(n: int) -> list:
    """
    Retourner une liste contenant
    les nombres de 1 à n.
    """
    lst = []
    for x in range(1, n + 1):
        lst.append(x)
    return lst
