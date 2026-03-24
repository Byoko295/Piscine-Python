"""
Retourner le jour de la semaine correspondant
à un nombre (1 = lundi, 7 = dimanche).
"""


__author__ = "benoui_m"


def day_of_week(n: int) -> str:
    """
    Retourner le jour de la semaine correspondant
    à un nombre (1 = lundi, 7 = dimanche).
    """
    if n == 1:
        return "lundi"
    elif n == 2:
        return "mardi"
    elif n == 3:
        return "mercredi"
    elif n == 4:
        return "jeudi"
    elif n == 5:
        return "vendredi"
    elif n == 6:
        return "samedi"
    elif n == 7:
        return "dimanche"
    else:
        return "Erreur, nombre invalide"
