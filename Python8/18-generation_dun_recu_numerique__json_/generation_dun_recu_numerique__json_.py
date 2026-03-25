"""
Sauvegarder le ticket en JSON pour usage digital.
"""


__author__ = "benoui_m"
import json


def save_receipt_json(filename: str, cart: list):
    """
    Sauvegarder le ticket en JSON pour usage digital.
    """
    dicter = []
    for x in cart:
        d_sub_lst = {"name": x[0], "price": x[1], "quantity": x[2]}
        dicter.append(d_sub_lst)
    print(dicter)
    with open(filename, "w") as f:
        json.dump(dicter, f, indent=4)

cart = [
    ("Pomme", 1.5, 3),
    ("Banane", 2.0, 2),
    ("Orange", 1.8, 4),
    ("Kiwi", 2.5, 1),
    ("Fraise", 3.0, 5)
]
save_receipt_json("test.json", cart)
