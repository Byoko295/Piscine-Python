"""
Vérifier si deux mots sont des anagrammes.
"""


__author__ = "benoui_m"


def is_anagram(word1: str, word2: str) -> bool:
    """
    Vérifier si deux mots sont des anagrammes.
    """
    word1 = word1.upper()
    word2 = word2.upper()
    return (True if sorted(word1) == sorted(word2) else False)
