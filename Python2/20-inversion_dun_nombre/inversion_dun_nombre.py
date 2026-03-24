"""
Retourner linverse dun nombre
entier sous forme de string.
"""


__author__ = "benoui_m"


def reverse_number(n: int) -> str:
    """
    Retourner linverse dun nombre
    entier sous forme de string.
    """
    signe = 0
    if n < 0:
        signe = 1
        n = -n
    stringed = str(n)
    if (signe == 1):
        return ('-' + stringed[::-1])
    return (stringed[::-1])
