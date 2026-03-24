"""
Convertir la liste triée en une
chaîne de texte lisible.
"""


__author__ = "benoui_m"


def write_to_file(filename: str, content: str):
    """
    Convertir la liste triée en
    une chaîne de texte lisible.
    """
    with open(filename, 'w') as f:
        f.write(f"{content}")
