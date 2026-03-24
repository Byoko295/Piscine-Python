"""
Supprimer un élément
spécifique d'un ensemble.
"""


__author__ = "benoui_m"


def remove_from_set(s: set, elem) -> set:
    """
    Supprimer un élément
    spécifique d'un ensemble.
    """
    s.remove(elem)
    return s
