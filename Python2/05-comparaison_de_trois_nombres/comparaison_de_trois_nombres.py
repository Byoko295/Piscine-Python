"""
Retourner le plus grand de trois nombres donnés.
"""


__author__ = "benoui_m"


def max_of_three(a: int, b: int, c: int) -> int:
    """
    Retourner le plus grand de trois nombres donnés.
    """
    return (max(max(a, b), max(b, c)))
