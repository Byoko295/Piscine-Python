"""
Retourner la fusion
de deux dictionnaires.
"""


__author__ = "benoui_m"


def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Retourner la fusion
    de deux dictionnaires.
    """
    return (d1 | d2)
