"""
Afficher les articles les plus vendus.
"""


__author__ = "benoui_m"
import json


def sales_statistics(sales_data: list) -> dict:
    """
    Afficher les articles les plus vendus.
    """
    sales_f = {}
    for x in sales_data:
        sales_f[x[0]] = sales_f.get(x[0], 0) + x[1]
    return sales_f
