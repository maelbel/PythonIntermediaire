from database.database import Database

class DBManager:
    def __init__(self) -> None:
        self.db = Database()

    def create_users(self) -> None:
        try:

            self.db.connect()
            
            self.db.create_table("""
        CREATE TABLE IF NOT EXISTS users(
            id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
            nom VARCHAR(30) NOT NULL,
            prenom varchar(30) NOT NULL
        )
        """)
            
            self.db.insert("INSERT INTO users values(NULL, :nom, :prenom)", {"nom": "Berger", "prenom": "Michel"})
            self.db.insert("INSERT INTO users values(NULL, :nom, :prenom)", {"nom": "Belliard", "prenom": "Mael"})

        except Exception as e:
            print(e)
            self.db.rollback()

        finally:
            self.db.close()

    def create_books(self) -> None:
        try:

            self.db.connect()

            self.db.create_table("""
        CREATE TABLE IF NOT EXISTS books(
            id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
            title VARCHAR(30) NOT NULL,
            author varchar(30) NOT NULL
        )
        """)
            
            self.db.insert("INSERT INTO books values(NULL, :title, :author)", {"title": "Pensées pour moi-même", "author": "Marc-Aurèle"})
            self.db.insert("INSERT INTO books values(NULL, :title, :author)", {"title": "Le Cid", "author": "Corneille"})

        except Exception as e:
            print(e)
            self.db.rollback()

        finally:
            self.db.close()

    def create_loans(self) -> None:
        try:

            self.db.connect()
            
            self.db.create_table("""
        CREATE TABLE IF NOT EXISTS loans(
            id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_id int NOT NULL,
            book_id int NOT NULL
        )
        """)
            
        except Exception as e:
            print(e)
            self.db.rollback()

        finally:
            self.db.close()

    def create_db(self) -> None:
        try:

            self.create_users()
            self.create_books()
            self.create_loans()

        except Exception as e:
            print(e)

        finally:
            print("Database created...")
