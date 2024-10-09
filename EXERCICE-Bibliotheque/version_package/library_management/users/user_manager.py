import sqlite3

from library_management.database.database import DATABASE_PATH
from library_management.users.classes import User

def add_user(user:User) -> None:
    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        curseur = cnx.cursor()

        sql = "INSERT INTO users VALUES (NULL, :nom, :prenom)"
        param = {
            "nom": user.nom,
            "prenom": user.prenom,
        }
        curseur.execute(sql, param)

        cnx.commit()

        print("Utilisateur créé...")

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        curseur.close()
        cnx.close()

def get_users()-> None:
    data = []

    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM users")

        data = cursor.fetchall()

        print("Utilisateurs récupérés...")

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

    return data