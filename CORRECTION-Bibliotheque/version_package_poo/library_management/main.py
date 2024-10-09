from books.BookManager import BookManager
from users.UserManager import UserManager
from loans.LoanManager import LoanManager

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    loan_manager = LoanManager(book_manager, user_manager)

    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un livre")
        print("2. Ajouter un utilisateur")
        print("3. Emprunter un livre")
        print("4. Rendre un livre")
        print("5. Lister les livres disponibles")
        print("6. Lister les emprunts d'un utilisateur")
        print("7. Quitter")

        choice = input("Choisissez une option: ")

        if choice == "1":
            title = input("Titre du livre: ")
            author = input("Auteur: ")
            book_manager.add_book(title, author)
        elif choice == "2":
            name = input("Nom de l'utilisateur: ")
            user_manager.add_user(name)
        elif choice == "3":
            user_name = input("Nom de l'utilisateur: ")
            book_title = input("Titre du livre: ")
            loan_manager.loan_book(user_name, book_title)
        elif choice == "4":
            user_name = input("Nom de l'utilisateur: ")
            book_title = input("Titre du livre: ")
            loan_manager.return_book(user_name, book_title)
        elif choice == "5":
            book_manager.list_available_books()
        elif choice == "6":
            user_name = input("Nom de l'utilisateur: ")
            user = user_manager.find_user(user_name)
            if user:
                user.list_borrowed_books()
            else:
                print("Utilisateur introuvable.")
        elif choice == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
