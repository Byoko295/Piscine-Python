"""
Convertir la liste triée en une
chaîne de texte lisible.
"""


__author__ = "benoui_m"


def list_to_string(lst: list) -> str:
    """
    Convertir la liste triée en
    une chaîne de texte lisible.
    """
    str = ""
    jump = "\\n"
    for x in range(len(lst)):
        if x == len(lst) - 1:
            jump = ""
        str += f"{x + 1}. {lst[x][0]}: {lst[x][1]}{jump}"
    return (str)




lst = [("cherry", 8), ("apple", 5), ("banana", 2)]
print(list_to_string(lst))