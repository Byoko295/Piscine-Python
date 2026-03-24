"""
Une fonction qui fait les operations de base
sur deux int et retour le tout dans un tuple
"""


__author__ = "benoui_m"


def get_type(value) -> str:
    """
    print the type of the argument fed to the function by
    calling type(X).__name__ method to del first part
    """
    return (type(value).__name__)
