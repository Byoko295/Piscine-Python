"""
Retourner un message formaté
avec des arguments nommés.
"""


__author__ = "benoui_m"


def greet(**kwargs) -> str:
    """
    Retourner un message formaté
    avec des arguments nommés.
    """
    iterator = iter(kwargs)
    fkey = kwargs[next(iterator)]
    skey = kwargs[next(iterator)]
    return (f"{fkey} a {skey} ans.")
