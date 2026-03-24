
"""
Supprimer le fichier texte si son contenu contient
un mot spécifique.
"""


__author__ = "benoui_m"
import os


def delete_file_if_contains(filename: str, word: str):
    """
    Supprimer le fichier texte si son contenu
    contient un mot spécifique.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if word in content:
        os.remove(filename)
