"""
Déterminer si trois longueurs peuvent former un triangle.
"""


__author__ = "benoui_m"


def is_triangle(a: int, b: int, c: int) -> bool:
    """
    Déterminer si trois longueurs
    peuvent former un triangle.
    """
    if (a >= b and a >= c):
        if (b + c > a):
            return (True)
        else:
            return (False)
    elif (b >= a and b >= c):
        if (a + c > b):
            return (True)
        else:
            return (False)
    elif (c >= b and c >= a):
        if (a + b > c):
            return (True)
        else:
            return (False)
    else:
        return (False)
