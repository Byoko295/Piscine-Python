"""
Retourner lélément dun
tuple à lindex donné.
"""


__author__ = "benoui_m"


def get_tuple_element(tpl: tuple, index: int):
    """
    Retourner lélément dun
    tuple à lindex donné.
    """
    if (index not in range(len(tpl))):
        return None
    else:
        return tpl[index]
