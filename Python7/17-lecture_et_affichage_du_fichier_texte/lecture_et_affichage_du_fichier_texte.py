"""
Lire le fichier texte et afficher son contenu.
"""


__author__ = "benoui_m"


def read_from_file(filename: str) -> str:
    """
    Lire le fichier texte et afficher son contenu.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return (f.read())
