from database.Database import Database
from database.database_manager import DBManager
from users.user_manager import UserManager
from medias.BookManager import BookManager
from loans.loan_manager import LoanManager

DATABASE_PATH = 'Cas_pratique_bibliotheque/version_poo/library_management/database/db.sqlite3'

class Menu:

    def __init__(self) -> None:
        self.db_manager = DBManager(Database(DATABASE_PATH))
        self.user_manager = UserManager()
        self.book_manager = BookManager()
        self.loan_manager = LoanManager()

    def afficher_menu(self):
        print("""

--- Menu ---
1 - Ajouter un livre
2 - Ajouter un utilisateur
3 - Emprunter un livre
4 - Rendre un livre
5 - Lister les livres disponibles
6 - Lister les emprunts d'un utilisateur
7 - Quitter

""")

    def main(self) -> None:
        # self.db_manager.create_db()

        while True:

            self.afficher_menu()

            choice = input()

            if choice == "7":
                print("Fin du programme...")
                break
            
            match choice:

                case "1":
                    self.book_manager.add_book(input("Title: "), input("Author: "))

                case "2":
                    self.user_manager.add_user(input("Nom: "), input("Prénom: "))

                case "3":
                    self.loan_manager.loan_book(int(input("ID de l'utilisateur: ")), int(input("ID du livre: ")))

                case "4":
                    self.loan_manager.return_book(int(input("ID de l'utilisateur: ")), int(input("ID du livre: ")))

                case "5":

                    available_books = self.book_manager.list_available_books()

                    if available_books:
                        print(f"{len(available_books)} livres trouvés")
                        print(available_books)
                    else:
                        print("Aucun livre disponible...")

                case "6":

                    users = self.user_manager.get_users()

                    if users:
                        print(f"{len(users)} utilisateurs trouvés")
                        print(users)
                    else:
                        print("Aucun utilisateur trouvé...")
                        continue

                    user_loans = self.loan_manager.list_user_loans(int(input("ID: ")))

                    if user_loans:
                        print(f"{len(user_loans)} livres empruntés trouvés")
                        print(user_loans)
                    else:
                        print("Aucun livre emprunté...")
                case other:
                    print("Commande invalide...")
                    continue


if __name__ == "__main__":
    main = Menu()
    main.main()