class User():
    
    def __init__(self, id:int, nom:str, prenom:str) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def __str__(self) -> str:
        return f"ID : {self.id} - Nom: {self.nom} - Prénom: {self.prenom}"

    def get_user(self):
        return self
    
    def set_user(self, id = -1, nom = "", prenom = ""):
        if id >=0:
            self.id = id
        if nom:
            self.nom = nom
        if prenom:
            self.prenom = prenom