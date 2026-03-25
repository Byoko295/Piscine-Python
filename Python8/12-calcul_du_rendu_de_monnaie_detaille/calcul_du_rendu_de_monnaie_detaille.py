"""
Donner le nombre de billets/pièces à rendre.
"""


__author__ = "benoui_m"


def calculate_detailed_change(change: float) -> dict:
    """
    Donner le nombre de
    billets/pièces à rendre.
    """
    monnaie = [500, 200, 100, 50, 20, 10, 5, 2,
               1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    caisse_en = {}
    while change > 0.00:
        sub_change = max(x for x in monnaie if x <= change)
        change -= sub_change
        change = round(change, 2)
        caisse_en[sub_change] = caisse_en.get(sub_change, 0) + 1
    return caisse_en
