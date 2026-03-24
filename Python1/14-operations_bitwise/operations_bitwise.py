"""
application les operations bitwise ou et et or xor
en binaire retourne un tuple contenant les 3 resultats
"""


__author__ = "benoui_m"


def bitwise_operations(a: int, b: int) -> tuple:
    """
    fonction qui applique les operations
    bitwise et ou et or
    """
    return (a & b, a | b, a ^ b)
