"""
Transformer un tuple en liste.
"""


__author__ = "benoui_m"


def tuple_to_list(tpl: tuple) -> list:
    """
    Transformer un tuple en liste.
    """
    lst = []
    for x in range(len(tpl)):
        lst.append(tpl[x])
    return lst
