"""
Ajouter un élément à une liste
(en gérant la mutabilité).
"""


__author__ = "benoui_m"


def add_to_list(item, lst=None) -> list:
    """
    Ajouter un élément à une
    liste (en gérant la mutabilité).
    """
    if lst is None:
        lst = []
    lst.append(item)
    return (lst)
