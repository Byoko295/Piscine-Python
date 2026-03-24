"""
Convertir une note sur 100 en une lettre
(A >= 90, B >= 80, C >= 70, D >= 60, F le reste).
"""


__author__ = "benoui_m"


def grade_conversion(score: int) -> str:
    """
    Convertir une note sur 100 en une lettre
    """
    if (score >= 60 and score < 70):
        return "D"
    elif (score >= 70 and score < 80):
        return "C"
    elif (score >= 80 and score < 90):
        return "B"
    elif (score >= 90):
        return "A"
    else:
        return "F"
