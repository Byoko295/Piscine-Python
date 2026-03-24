
"""
Lire un fichier en capturant les erreurs potentielles."
"""


__author__ = "benoui_m"
import os


def safe_read_file(filename: str) -> str:
    """
    Lire un fichier en capturant les erreurs potentielles.
    """
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return (f.read())
    else:
        return "Erreur : fichier introuvable"
