"""
Une fonction qui fait les operations de base
sur deux int et retour le tout dans un tuple
"""


__author__ = "benoui_m"


def basic_operations(a: int, b: int) -> tuple:
    """
    Fonction qui fait des operations sur 2 int
    :param a: premier int
    :type a: int
    :param b: deuxiemme int
    :type b: int
    :return: tuple contenant les resultat des op
    """
    return (a + b, a - b, a * b, None if b == 0 else a / b)
