"""
retourne le solution d'une equation a une inconnue
"""


__author__ = "benoui_m"


def solve_equation(a: float, b: float) -> float:
    """
    retourne le solution d'une equation a une inconnue
    """
    if (a == 0):
        return (0)
    else:
        return (-b/a)
