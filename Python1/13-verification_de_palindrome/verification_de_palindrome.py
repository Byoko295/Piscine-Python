"""
Fonction qui retourne vraie ou faux celon si
linput est un palindrom ou pas
"""


__author__ = "benoui_m"


def is_palindrome(s: str) -> bool:
    """
    fonction qui verifie un palindrome
    """
    is_palindrome = 1
    for x in range(len(s) // 2):
        if (s[x].upper() != s[len(s) - x - 1].upper()):
            return (False)
    return (True)
