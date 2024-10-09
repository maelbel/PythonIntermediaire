import sqlite3

from library_management.database.database import DATABASE_PATH
from library_management.books.classes import Book

def add_book(book:Book) -> None:
    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        cursor = cnx.cursor()

        sql = "INSERT INTO books VALUES (NULL, :title, :author)"
        param = {
            "title": book.title,
            "author": book.author,
        }
        cursor.execute(sql, param)

        cnx.commit()

        print("Livre créé...")

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

def list_available_books() -> list[Book]:

    data = []

    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM loans)")

        data = cursor.fetchall()

        print("Livre disponible récupéré...")

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

    return data