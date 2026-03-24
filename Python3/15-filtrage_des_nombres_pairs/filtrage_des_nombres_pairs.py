"""
Retourner une liste ne contenant que
les nombres pairs dune liste donnée.
"""


__author__ = "benoui_m"


def filter_even(numbers: list) -> list:
    """
    Retourner une liste ne contenant que
    les nombres pairs dune liste donnée.
    """
    final = []
    for x in range(len(numbers)):
        if (numbers[x] % 2 == 0):
            final.append(numbers[x])
    return (final)
