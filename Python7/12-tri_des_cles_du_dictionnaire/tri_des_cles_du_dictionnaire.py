"""
Trier le dictionnaire par ordre croissant des clés.
"""


__author__ = "benoui_m"


def sort_dict_by_keys(d: dict) -> dict:
    """
    Trier le dictionnaire par ordre
    croissant des clés.
    """
    return (dict(sorted(d.items())))
