"""
Retourner une liste
sans doublons.
"""


__author__ = "benoui_m"


def remove_duplicates(lst: list) -> list:
    """
    Retourner une liste
    sans doublons.
    """
    lst = list(dict.fromkeys(lst))
    return (lst)
