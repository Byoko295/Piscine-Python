"""
Vérifier si un nombre est premier.
"""


__author__ = "benoui_m"


def is_prime_optimized(n: int) -> bool:
    """
    Vérifier si un nombre est premier.
    """
    count = 0
    if (n < 2):
        return (False)
    for x in range(1, n + 1):
        if (n % x == 0):
            count += 1
    if (count != 2):
        return (False)
    else:
        return (True)
