"""
Retourner une fonction qui
lève à une puissance donnée.
"""


__author__ = "benoui_m"


def make_power(n: int):
    """
    Retourner une fonction qui
    élève à une puissance donnée.
    """
    def power(x: int) -> int:
        """
        fonction qui retourne n puiss x
        """
        return x ** n
    return (power)
