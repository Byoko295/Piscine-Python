"""
Ajouter un article sous forme de
tuple (nom, prix, quantité).
"""


__author__ = "benoui_m"


def add_item(cart: list, name: str, price: float, quantity: int) -> list:
    """
    Créer une liste vide qui
    représentera le panier.
    """
    cart.append((name, price, quantity))
    return (cart)
