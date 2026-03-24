"""
carrés des nombres donnés.
"""


__author__ = "benoui_m"


def squares(lst: list) -> list:
    """
    carrés des nombres donnés.s.
    """
    for x in range(len(lst)):
        lst[x] *= lst[x]
    return (lst)
