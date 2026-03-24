"""
Retourner la table de multiplication d’un nombre sous forme de liste.
"""


__author__ = "benoui_m"


def multiplication_table(n: int) -> list:
    """
    Retourner la table de multiplication
    dun nombre sous forme de liste.
    """
    i = 1
    table = []
    while i < 11:
        table.append(i * n)
        i += 1
    return (table)
