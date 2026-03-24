"""
Une fonction qui fait les operations de base
sur deux int et retour le tout dans un tuple
"""


__author__ = "benoui_m"


def convert_type(value):
    """
    Returns an "str" when input is int
    Returns int when input is str
    """
    if (type(value) is int):
        return (str(value))
    elif (type(value) is str):
        return (int(value))
