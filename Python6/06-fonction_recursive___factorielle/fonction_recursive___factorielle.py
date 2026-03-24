"""
Implémenter une fonction récursive pour
calculer la factorielle dun nombre.
"""


__author__ = "benoui_m"


def factorial(n: int) -> int:
    """
    Implémenter une fonction récursive pour
    calculer la factorielle dun nombre.
    """
    if (n <= 1):
        return (1)
    return (n * factorial(n - 1))
