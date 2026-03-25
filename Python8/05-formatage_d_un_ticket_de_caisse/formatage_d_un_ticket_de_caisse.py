"""
Générer un texte formaté affichant*
les articles et le total.
"""


__author__ = "benoui_m"


def format_receipt(cart: list) -> str:
    """
    Générer un texte formaté
    affichant les articles et le total.
    """

    str = ""
    j = "\n"
    somme = 0
    c = cart
    for x in range(len(c)):
        if x == len(c) - 1:
            j = ""
        somme_p = c[x][1] * c[x][2]
        somme += c[x][1] * c[x][2]
        str += f"{c[x][0]} (x{round(c[x][2], 2)}) - {round(somme_p, 2)}€{j}"
    str += f"Total : {round(somme, 2)}€"
    return (str)
