"""
Retourner le n-ième terme de la suite
de Fibonacci en utilisant la récursivité.
"""


__author__ = "benoui_m"


def fibonacci(n: int) -> int:
    """
    Retourner le n-ième terme de la
    suite de Fibonacci en utilisant la récursivité.
    """
    if (n == 1 or n == 2):
        return 1
    elif (n == 0):
        return (0)
    else:
        return (fibonacci(n - 2) + fibonacci(n - 1))
