"""
Retourner l'élément à l'index
donné d'une liste.
"""


__author__ = "benoui_m"


def get_element(lst: list, index: int):
    """
    Retourner l'élément à
    l'index donné d'une liste.
    """
    if index in range(len(lst)):
        return (lst[index])
