"""
Vérifier si un ensemble est
inclus dans un autre.
"""


__author__ = "benoui_m"


def is_subset(s1: set, s2: set) -> bool:
    """
    Vérifier si un ensemble est
    inclus dans un autre.
    """
    return (set.issubset(s1, s2))
