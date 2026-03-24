"""
paramètre une liste et retourne une liste
en remplaçant chaque multiple de 3 par "Fizz".
"""


__author__ = "benoui_m"


def replace_multiples_of_3(numbers: list) -> list:
    """
    paramètre une liste et retourne une liste
    en remplaçant chaque de 3 par "Fizz".
    """
    numbers = ["Fizz." if x % 3 == 0 else x for x in numbers]
    return (numbers)
