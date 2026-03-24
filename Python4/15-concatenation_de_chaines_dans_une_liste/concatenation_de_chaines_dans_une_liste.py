"""
Retourner une seule chaîne contenant
toutes les valeurs d'une liste de chaînes.
"""


__author__ = "benoui_m"


def join_strings(lst: list) -> str:
    """
    Retourner une seule chaîne contenant
    toutes les valeurs d'une liste de chaînes.
    """
    strr = ""
    for x in range(len(lst)):
        if x == 0:
            strr += lst[x]
        else:
            strr += " " + lst[x]
    return strr
