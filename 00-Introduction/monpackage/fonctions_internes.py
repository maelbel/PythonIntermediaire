# Fonctions internes au package
# Elles ne pourront pas être importées dans un fichier externe au package "monpackage"

# Exemple:

def fragile():
    print("Cette fonction est fragile")

def delete():
    print("Cette fonction supprime tout")