"""
retourne la somme des chiffre contenue dans
nombre
"""


__author__ = "benoui_m"


def sum_of_digits(n: int) -> int:
    """
    retourne la somme des chiffres d'un nombre
    """
    somme = 0
    if n < 0:
        ne = -n
    else:
        ne = n
    size = len(str(ne))
    for x in range(size):
        somme += int(str(ne)[x])
    return (somme)
