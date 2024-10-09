# Fonctions importables à l'extérieur du package "monpackage"

from fonctions_internes import delete
from module1 import warn

def delete_all():
    res = warn()

    if res == "y":
        delete()

delete_all()