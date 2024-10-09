from users.user import User
from database.database_manager import Database

class UserManager():

    def __init__(self) -> None:
        self.db = Database()

    def add_user(self, nom, prenom) -> None:
        try:

            self.db.connect()

            user = User(0, nom, prenom)

            self.db.insert("INSERT INTO users VALUES (NULL, :nom, :prenom)", {"nom": user.nom, "prenom": user.prenom})

            print("Utilisateur créé...")

        except Exception as e:
            print(f"Une erreur de type {e} est survenue")
            self.db.rollback()

        finally:
            self.db.close()

    def get_users(self)-> None:
        data = []

        try:
            self.db.connect()

            data = self.db.fetch_all("SELECT * FROM users")

            print("Utilisateurs récupérés...")

        except Exception as e:
            print(f"Une erreur de type {e} est survenue")
            self.db.rollback()

        finally:
            self.db.close()

        return data