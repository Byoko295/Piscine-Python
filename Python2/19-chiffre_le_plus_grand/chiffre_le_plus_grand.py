"""
Retourner la somme des
chiffres dun entier.
"""


__author__ = "benoui_m"


def max_digit(n: int) -> int:
    """
    retourne la somme des chiffres d'un nombre
    """
    if (n < 0):
        n = -n
    stringed = str(n)
    sizer = len(stringed)
    maxi = int(stringed[0])
    for x in range(1, sizer):
        if (max(maxi, int(stringed[x])) > maxi):
            maxi = int(stringed[x])
    return (maxi)
