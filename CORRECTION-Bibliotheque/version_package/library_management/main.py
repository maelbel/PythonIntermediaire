from books.book_manager import add_book, list_available_books
from users.user_manager import add_user, list_user_loans
from loans.loan_manager import loan_book, return_book

def main():
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
            add_book(title, author)
        elif choice == "2":
            name = input("Nom de l'utilisateur: ")
            add_user(name)
        elif choice == "3":
            user_name = input("Nom de l'utilisateur: ")
            book_title = input("Titre du livre: ")
            loan_book(user_name, book_title)
        elif choice == "4":
            user_name = input("Nom de l'utilisateur: ")
            book_title = input("Titre du livre: ")
            return_book(user_name, book_title)
        elif choice == "5":
            list_available_books()
        elif choice == "6":
            user_name = input("Nom de l'utilisateur: ")
            list_user_loans(user_name)
        elif choice == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
