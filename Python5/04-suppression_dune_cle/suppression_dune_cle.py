"""
Supprimer une clé
spécifique d'un dictionnaire.
"""


__author__ = "benoui_m"


def remove_key(d: dict, key) -> dict:
    """
    Ajouter une paire clé-valeur
    à un dictionnaire existant.
    """
    if key in d.keys():
        del d[key]
    return (d)
