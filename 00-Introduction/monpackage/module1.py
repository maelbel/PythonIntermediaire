# Fonctions importables à l'extérieur du package "monpackage"

from fonctions_internes import fragile

def warn():
    fragile()
    return input("Êtes-vous sûr de vouloir faire cela? (y/n)")