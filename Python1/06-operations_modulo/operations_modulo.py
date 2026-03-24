"""
Une fonction qui retourne vraie su le nombre est paire
faux si il ne l'est pas
"""


__author__ = "benoui_m"


def is_even(n: int) -> bool:
    """
    Fonction qui retourne un etat de verité çelon
    que le int soit pair ou non
    """
    return (True if (n % 2) == 0 else False)
