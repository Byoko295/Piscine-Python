"""
Appliquer une fonction de mise
en majuscule à une liste de mots.
"""


__author__ = "benoui_m"


def to_upper(words: list) -> list:
    """
    Appliquer une fonction de mise en
    majuscule à une liste de mots.
    """
    for x in range(len(words)):
        words[x] = words[x].upper()
    return (words)
