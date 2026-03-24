"""
Modifier un dictionnaire pour supprimer toutes
les entrées dont la clé commence par une voyelles.
"""


__author__ = "benoui_m"


def remove_vowels_from_dict(d: dict) -> dict:
    """
    Modifier un dictionnaire pour supprimer toutes
    les entrées dont la clé commence par une voyelles.
    """
    return ({k: v for k, v in d.items() if k[0].lower() not in 'aeiou'})
