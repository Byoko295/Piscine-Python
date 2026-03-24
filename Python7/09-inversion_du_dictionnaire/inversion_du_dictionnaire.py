"""
Inverser les clés et les valeurs d'un dictionnaire.
"""


__author__ = "benoui_m"


def invert_dict(d: dict) -> dict:
    """
    Inverser les clés et les valeurs d'un dictionnaire.
    """
    return ({v: k for k, v in d.items()})
