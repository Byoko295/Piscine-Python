"""
Fusionner deux listes sans doublon.
"""


__author__ = "benoui_m"


def merge_lists(list1: list, list2: list) -> list:
    """
    Fusionner deux listes sans doublon.
    """
    return list(set(list1 + list2))
