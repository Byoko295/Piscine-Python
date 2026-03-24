"""
Fusionner deux dictionnaires en combinant leurs valeurs
si les clés sont identiques.
"""


__author__ = "benoui_m"


def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Fusionner deux dictionnaires en combinant leurs valeurs
    si les clés sont identiques.
    """
    return ({k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)})
