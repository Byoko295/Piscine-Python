"""
retourne une liste ne contenant que les paires
dont le premier élément
"""


__author__ = "benoui_m"


def extract_valid_pairs(pairs: list) -> list:
    """
    dont le premier élément est entier
    """
    lst = [x for x in pairs if isinstance(x[0], int)]
    return (lst)
