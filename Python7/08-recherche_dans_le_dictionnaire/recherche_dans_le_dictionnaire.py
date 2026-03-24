"""
Vérifier si une clé est présente dans le dictionnaire et retourner sa valeur.
"""


__author__ = "benoui_m"


def get_value_from_dict(d: dict, key: int) -> str:
    """
    Vérifier si une clé est présente dans
    le dictionnaireet retourner sa valeur.
    """
    if (key in d.keys()):
        return (str(d[key]))
    else:
        return "Key not found in dictionary"
