from books.BookManager import BookManager
from users.UserManager import UserManager

class LoanManager:
    def __init__(self, book_manager: BookManager, user_manager: UserManager):
        self.book_manager = book_manager
        self.user_manager = user_manager

    def loan_book(self, user_name, book_title):
        user = self.user_manager.find_user(user_name)
        book = self.book_manager.find_book(book_title)

        if user and book and book.is_book_available():
            user.borrow_book(book)
            book.set_available(False)
            print(f"{user_name} a emprunté {book_title}")
        else:
            print(f"Erreur : utilisateur ou livre introuvable, ou le livre est déjà emprunté.")

    def return_book(self, user_name, book_title):
        user = self.user_manager.find_user(user_name)
        book = self.book_manager.find_book(book_title)

        if user and book and book in user.borrowed_books:
            user.return_book(book)
            book.set_available(True)
            print(f"{user_name} a rendu {book_title}")
        else:
            print("Erreur : utilisateur ou livre introuvable.")
