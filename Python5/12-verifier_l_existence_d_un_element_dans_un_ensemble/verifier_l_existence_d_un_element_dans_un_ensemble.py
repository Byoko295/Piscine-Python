"""
Vérifier si un élément est
présent dans un ensemble.
"""


__author__ = "benoui_m"


def element_in_set(s: set, elem) -> bool:
    """
    Vérifier si un élément
    est présent dans un ensemble.
    """
    if elem in s:
        return (True)
    return False
