"""
retourne le factoriel d'un nombre
"""


__author__ = "benoui_m"


def factorial(n: int) -> int:
    """
    retourne le factoriel d'un numbre
    """
    fact = 1
    if (n == 0):
        return (1)
    holder = n
    for x in range(n - 1):
        fact *= holder
        holder -= 1
    return (fact)
