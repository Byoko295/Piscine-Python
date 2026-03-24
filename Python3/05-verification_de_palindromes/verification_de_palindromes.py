"""
Fonction qui retourne vraie ou faux celon si
linput est un palindrom ou pas
"""


__author__ = "benoui_m"


def is_palindrome(word: str) -> bool:
    """
    fonction qui verifie un palindrome
    """
    for x in range(len(word)):
        if ((word[x]).upper() != (word[len(word) - x - 1]).upper()):
            return (False)
    return (True)
