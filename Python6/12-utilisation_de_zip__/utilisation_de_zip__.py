"""
Associer deux listes élément par
élément sous forme de tuples.
"""


__author__ = "benoui_m"


def pair_lists(list1: list, list2: list) -> list:
    """
    Associer deux listes élément par
    élément sous forme de tuples.
    en supposant que les deux font la meme taille
    """
    output = []
    for x in range(len(list1)):
        output.append((list1[x], list2[x]))
    return (output)
