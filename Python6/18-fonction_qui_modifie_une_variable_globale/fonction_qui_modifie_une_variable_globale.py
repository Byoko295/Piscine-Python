"""
Modifier une variable
globale dans une fonction.
"""


__author__ = "benoui_m"
global_var = 0


def modify_global():
    """
    Modifier une variable
    globale dans une fonction.
    """
    global global_var
    global_var = 10
    return (global_var)
