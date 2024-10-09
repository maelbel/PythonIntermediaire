import sqlite3


from library_management.database.database import DATABASE_PATH

from library_management.books.classes import Book
from library_management.users.classes import User
from library_management.loans.classes import Loan

def loan_book(user:User, book:Book) -> None:

    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        cursor = cnx.cursor()
        print(user.id, book.id)
        cursor.execute("SELECT * FROM books WHERE id = ?", (book.id,))

        result_book = cursor.fetchone()

        cursor.execute("SELECT * FROM users WHERE id = ?", (user.id,))

        result_user = cursor.fetchone()

        if result_book and result_user:
            sql = "INSERT INTO loans VALUES (NULL, :user_id, :book_id)"
            param = {
                "user_id": result_user[0],
                "book_id": result_book[0]
            }
            cursor.execute(sql, param)

            print(f"Le livre {result_book[1]} de {result_book[2]} est emprunté par {result_user[1]} {result_user[2]}...")

        else:
            print("Aucun utilisateur ou livre trouvé...")

        cnx.commit()

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

def return_book(user:User, book:Book) -> None:
    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM books WHERE id = ?", (book.id,))

        result_book = cursor.fetchone()

        cursor.execute("SELECT * FROM users WHERE id = ?", (user.id,))

        result_user = cursor.fetchone()

        if result_book and result_user:
            sql = "DELETE FROM loans WHERE user_id = :user_id and book_id = :book_id"
            param = {"user_id": result_user[0], "book_id": result_book[0]}
            cursor.execute(sql, param)
            print(f"L'utilisateur {result_user[1]} {result_user[2]} a retourné le livre {result_book[1]} de {result_book[2]}")
        else:
            print("Aucun utilisateur ou livre trouvé...")

        cnx.commit()

        

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

def list_user_loans(user_id:int) -> list[Loan]:
    data = []

    try:
        cnx = sqlite3.connect(DATABASE_PATH)
        cursor = cnx.cursor()

        cursor.execute("""SELECT books.*, users.* FROM loans 
                       INNER JOIN books ON books.id = loans.book_id
                       INNER JOIN users ON users.id = loans.user_id
                       WHERE user_id = ?""", (user_id,))

        data = cursor.fetchall()

        print("Livre emprunté récupéré...")

    except Exception as e:
        print(f"Une erreur de type {e} est survenue")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

    return data