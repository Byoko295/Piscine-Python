"""
retourne le signe d'un int
"""


__author__ = "benoui_m"


def sign(n: int) -> int:
    """
    retourne le signe d'un int
    """
    if (n > 0):
        return (+1)
    elif (n == 0):
        return (0)
    else:
        return (-1)
