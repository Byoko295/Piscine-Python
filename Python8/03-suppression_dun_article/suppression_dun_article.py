"""
Retirer un article du panier
par son nom.
"""


__author__ = "benoui_m"


def remove_item(cart: list, name: str) -> list:
    """
    Retirer un article du
    panier par son nom.
    """
    for item in cart:
        if item[0] == name:
            cart.remove(name)
    return (cart)
