"""
Ajouter une paire clé-valeur
à un dictionnaire existant.
"""


__author__ = "benoui_m"


def add_entry(d: dict, key, value) -> dict:
    """
    Ajouter une paire clé-valeur
    à un dictionnaire existant.
    """
    d[key] = value
    return d
