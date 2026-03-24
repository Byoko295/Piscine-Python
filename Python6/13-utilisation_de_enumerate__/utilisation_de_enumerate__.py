"""
Retourner une liste de tuples
contenant index et élément.
"""


__author__ = "benoui_m"


def enumerate_list(lst: list) -> list:
    """
    Retourner une liste de tuples
    contenant index et élément.
    """
    output = []
    for x in range(len(lst)):
        output.append((x, lst[x]))
    return (output)
