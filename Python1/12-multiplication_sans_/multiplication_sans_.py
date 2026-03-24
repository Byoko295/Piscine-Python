"""
fait une operation de mmultiplication en utilisant
une loop
"""


__author__ = "benoui_m"


def multiply(a: int, b: int) -> int:
    """
    fonction qui multiplie par iteration
    """
    res = 0
    signe = 1
    for x in range(abs(b)):
        res += a
    if (b < 0):
        signe = -1
    if (signe == 1):
        return (res)
    else:
        return (-res)
