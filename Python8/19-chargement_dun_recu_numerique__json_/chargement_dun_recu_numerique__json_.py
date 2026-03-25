"""
Charger et afficher un ticket depuis un fichier JSON.
"""


__author__ = "benoui_m"
import json


def load_receipt_json(filename: str) -> list:
    """
    Sauvegarder le ticket en JSON pour usage digital.
    """
    tickets = []
    with open("test.json", "r") as f:
        tickets = json.load(f)
    return tickets
