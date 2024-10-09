import sqlite3

class Database:
    
    def __init__(self, path:str) -> None:
        self.path = path
        self.connection = None

    def connect(self):
        """Se connecter à la base de données."""
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def create_table(self, query):
        """Créer une table en fonction de la requête SQL donnée."""
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, query, values):
        """Insérer des données dans une table."""
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_all(self, query, params = {}):
        """Récupérer toutes les données d'une table."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def fetch_one(self, query, params = {}):
        """Récupérer la première donnée trouvée d'une table."""
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def update(self, query, values):
        """Mettre à jour des données."""
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, query, values):
        """Supprimer des données."""
        self.cursor.execute(query, values)
        self.connection.commit()

    def rollback(self):
        """Annuler les requêtes"""
        self.connection.rollback()

    def close(self):
        """Fermer la connexion à la base de données."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()