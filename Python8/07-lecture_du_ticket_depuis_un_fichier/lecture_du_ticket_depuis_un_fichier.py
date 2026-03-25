"""
Lire et afficher un ticket précédemment sauvegardé.
"""


__author__ = "benoui_m"


def load_receipt(filename: str) -> str:
    """
    Lire et afficher un ticket précédemment sauvegardé.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return (f.read())
