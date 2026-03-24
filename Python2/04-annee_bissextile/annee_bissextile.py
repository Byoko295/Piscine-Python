"""
return vraie si c'est une année bissextile
"""


__author__ = "benoui_m"


def is_leap_year(year: int) -> bool:
    """
    retourne vrai si c'est une année bissextile
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return (True)
    else:
        return (False)
