
"""
Vérifier si un fichier existe avant de le lire.
"""


__author__ = "benoui_m"
import os


def file_exists(filename: str) -> bool:
    """
    Vérifier si un fichier existe avant de le lire.
    """
    if os.path.exists(filename):
        return (True)
    else:
        return (False)
