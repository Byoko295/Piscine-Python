"""
Vérifier si un nombre est pair ou multiple de 3.
"""


__author__ = "benoui_m"


def check_number(n: int) -> str:
    """
    Vérifier si un nombre est pair ou multiple de 3.
    """
    if (n % 3 == 0):
        return "multiple de 3"
    elif (n % 2 == 0):
        return "pair"
    else:
        return "rien de spécial"
