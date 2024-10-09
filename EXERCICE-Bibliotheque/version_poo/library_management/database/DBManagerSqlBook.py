from medias.Book import Book
from database.Database import Database
from database.IDBManager import IDBManager

class DBManagerSqlBook(IDBManager):
    
    def __init__(self, db: Database):
        self.db = db

    def create(self, book: Book):
        try:

            self.db.connect()

            self.db.insert("INSERT INTO books VALUES (NULL, :title, :author)", {"title": book.title, "author": book.author})

        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.db.close()
    
    def select(self):
        data = []

        try:
            self.db.connect()

            data = self.db.fetch_all("SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM loans)")

            print("Livre disponible récupéré...")

        except Exception as e:
            print(f"Une erreur de type {e} est survenue")

        finally:
            self.db.close()

        return data
    
    def update(self):
        return super().update()
    
    def delete(self):
        return super().delete()