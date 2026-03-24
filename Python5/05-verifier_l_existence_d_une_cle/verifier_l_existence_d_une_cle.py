"""
Vérifier si une clé existe
dans un dictionnaire.
"""


__author__ = "benoui_m"


def key_exists(d: dict, key) -> bool:
    """
    Vérifier si une clé
    existe dans un dictionnaire.
    """
    if key in d:
        return True
    return False
