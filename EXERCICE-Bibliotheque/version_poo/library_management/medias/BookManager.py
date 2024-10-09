from database.Database import Database
from medias.Book import Book

class BookManager:

    def __init__(self) -> None:
        self.db = Database()
    
    def add_book(self, title:str, author:str) -> None:

        book = Book(0, title, author)

        self.db.insert("INSERT INTO books VALUES (NULL, :title, :author)", {"title": book.title, "author": book.author})

        print("Livre créé...")

    def list_available_books(self) -> list[Book]:

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

