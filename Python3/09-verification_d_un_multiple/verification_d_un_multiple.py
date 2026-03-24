"""
Vérifier si un nombre est un
multiple dun autre.
"""


__author__ = "benoui_m"


def is_multiple(n: int, m: int) -> bool:
    """
    Vérifier si un nombre est un
    multiple dun autre.
    """
    if (m == 0):
        return "Error dividing by 0"
    return (True if (n % m == 0) else False)
