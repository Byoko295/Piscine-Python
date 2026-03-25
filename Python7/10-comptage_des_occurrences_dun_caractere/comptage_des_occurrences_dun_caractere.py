"""
Compter le nombre d'occurrences d'un
caractère donné dans toutes les valeurs d'un dictionnaire.
"""


__author__ = "benoui_m"


def count_char_occurrences(d: dict, char: str) -> int:
    """
    Compter le nombre d'occurrences d'un caractère
    donné dans toutes les valeurs d'un dictionnaire.
    """
    return (sum(str(c).count(char) for c in d.values()))
