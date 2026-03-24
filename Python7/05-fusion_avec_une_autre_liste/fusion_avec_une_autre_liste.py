"""
list fusionnant deux listes de mêmes dimensions
"""


__author__ = "benoui_m"


def merge_lists(list1: list, list2: list) -> list:
    """
    list fusionnant deux listes de mêmes dimensions
    """
    output = []
    for x in range(len(list1)):
        output.append((list1[x], list2[x]))
    return (output)
