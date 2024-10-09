import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__))) # c:\...\library_management

from library_management.database.database import create_db

from library_management.users.classes import User
from library_management.users.user_manager import add_user, get_users

from library_management.books.classes import Book
from library_management.books.book_manager import add_book, list_available_books

from library_management.loans.classes import Loan
from library_management.loans.loan_manager import loan_book, return_book, list_user_loans

def main() -> None:
    # create_db()
    while True:
        choice = input("""

--- Menu ---
1 - Ajouter un livre
2 - Ajouter un utilisateur
3 - Emprunter un livre
4 - Rendre un livre
5 - Lister les livres disponibles
6 - Lister les emprunts d'un utilisateur
7 - Quitter

""")    
        if choice == "7":
            print("Fin du programme...")
            break
        
        match choice:
            case "1":
                add_book(Book(0, input("Title: "), input("Author: ")))
            case "2":
                add_user(User(0, input("Nom: "), input("Prénom: ")))
            case "3":
                user = User(int(input("ID de l'utilisateur: ")), " ", " ")
                book = Book(int(input("ID du livre: ")), " ", " ")
                loan_book(user, book)
            case "4":
                user = User(int(input("ID de l'utilisateur: ")), " ", " ")
                book = Book(int(input("ID du livre: ")), " ", " ")
                return_book(user, book)
            case "5":
                available_books = list_available_books()

                if available_books:
                    print(f"{len(available_books)} livres trouvés")
                    print(available_books)
                else:
                    print("Aucun livre disponible...")
            case "6":

                users = get_users()

                if users:
                    print(f"{len(users)} utilisateurs trouvés")
                    print(users)
                else:
                    print("Aucun utilisateur trouvé...")
                    continue

                user_loans = list_user_loans(int(input("ID: ")))

                if user_loans:
                    print(f"{len(user_loans)} livres empruntés trouvés")
                    print(user_loans)
                else:
                    print("Aucun livre emprunté...")
            case other:
                print("Commande invalide...")
                continue


if __name__ == "__main__":
    main()