"""
Calculer la factorielle dun
nombre en utilisant la récursivité.
"""


__author__ = "benoui_m"


def recursive_factorial(n: int) -> int:
    """
    Calculer la factorielle dun
    nombre en utilisant la récursivité.
    """
    if (n <= 1):
        return (1)
    return (n * recursive_factorial(n - 1))
