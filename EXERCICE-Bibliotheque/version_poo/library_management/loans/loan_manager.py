from database.database import Database
from medias.book import Book
from users.user import User
from loans.load import Loan

class LoanManager:

    def __init__(self) -> None:
        self.db = Database()

    def loan_book(self, user_id:int, book_id:int) -> None:

        try:
            
            self.db.connect()

            book = self.db.fetch_one("SELECT * FROM books WHERE id = ?", (book_id,))

            if not book:
                print(f"ID du livre introuvable...")
                return
            
            user = self.db.fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))

            if not user:
                print(f"ID de l'utilisateur introuvable...")
                return

            self.db.insert("INSERT INTO loans VALUES (NULL, :user_id, :book_id)", {"user_id": user_id, "book_id": book_id})

            print(f"Le livre {book[1]} de {book[2]} est emprunté par {user[1]} {user[2]}...")

        except Exception as e:
            print(f"Une erreur de type {e} est survenue")
            self.db.rollback()

        finally:
            self.db.close()

    def return_book(self, user_id:int, book_id:int) -> None:
        try:
            self.db.connect()

            book = self.db.fetch_one("SELECT * FROM books WHERE id = ?", (book_id,))

            if not book:
                print(f"ID du livre introuvable...")
                return
            
            user = self.db.fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))

            if not user:
                print(f"ID de l'utilisateur introuvable...")
                return
            
            loan = self.db.fetch_one("SELECT * FROM loans WHERE user_id = :user_id and book_id = :book_id", {"user_id": user_id, "book_id": book_id})

            if not loan:
                print(f"Aucune emprunt trouvé...")
                return

            self.db.delete("DELETE FROM loans WHERE user_id = :user_id and book_id = :book_id", {"user_id": user_id, "book_id": book_id})

            print(f"L'utilisateur {user[1]} {user[2]} a retourné le livre {book[1]} de {book[2]}")

        except Exception as e:
            print(f"Une erreur de type {e} est survenue")
            self.db.rollback()

        finally:
            self.db.close()

    def list_user_loans(self, user_id:int) -> list[Loan]:
        data = []

        try:
            self.db.connect()

            data = self.db.fetch_all("""SELECT books.*, users.* FROM loans 
                        INNER JOIN books ON books.id = loans.book_id
                        INNER JOIN users ON users.id = loans.user_id
                        WHERE user_id = :user_id""", {"user_id": user_id})

            print("Livre emprunté récupéré...")

        except Exception as e:
            print(f"Une erreur de type {e} est survenue")
            self.db.rollback()

        finally:
            self.db.close()

        return data