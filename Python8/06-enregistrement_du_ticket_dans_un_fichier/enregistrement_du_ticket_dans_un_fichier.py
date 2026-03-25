"""
Sauvegarder le ticket dans
un fichier ticket.txt.
"""


__author__ = "benoui_m"


def save_receipt(filename: str, content: str):
    """
    Sauvegarder le ticket dans
    un fichier ticket.txt.
    """
    with open(filename, 'w') as f:
        f.write(f"{content}")
