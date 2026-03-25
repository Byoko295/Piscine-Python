"""
Appliquer une réduction automatique
sur certains articles.
"""


__author__ = "benoui_m"


def apply_promotion(cart: list, promotions: dict) -> list:
    """
    Appliquer une réduction
    automatique sur certains articles.
    """
    end = []
    for x in cart:
        if x[0] in promotions.keys():
            new_price = x[1] - x[1] * promotions[x[0]] / 100
            end.append((x[0], round(new_price, 2), x[2]))
        else:
            end.append((x[0], x[1], x[2]))
    return end
