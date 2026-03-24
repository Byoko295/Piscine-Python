"""
Classifier une personne selon son âge (enfant, ado, adulte, senior).
"""


__author__ = "benoui_m"


def age_category(age: int) -> str:
    """
    Classifier une personne selon son âge (enfant, ado, adulte, senior).
    """
    if (age < 12):
        return "enfant"
    elif (age >= 12 and age < 18):
        return "ado"
    elif (age >= 18 and age < 70):
        return "adulte"
    else:
        return "senior"
