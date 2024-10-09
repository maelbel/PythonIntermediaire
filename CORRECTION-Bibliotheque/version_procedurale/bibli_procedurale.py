# Liste globale des livres
books = []
# Liste globale des utilisateurs
users = []

# Fonction pour ajouter un livre
def add_book(title, author):
    book = {"title": title, "author": author, "is_available": True}
    books.append(book)
    print(f"Livre ajouté: {title} par {author}")

# Fonction pour ajouter un utilisateur
def add_user(name):
    user = {"name": name, "borrowed_books": []}
    users.append(user)
    print(f"Utilisateur ajouté: {name}")

# Fonction pour trouver un livre par titre
def find_book(title):
    return next((book for book in books if book["title"] == title), None)

# Fonction pour trouver un utilisateur par nom
def find_user(name):
    return next((user for user in users if user["name"] == name), None)

# Fonction pour emprunter un livre
def loan_book(user_name, book_title):
    user = find_user(user_name)
    book = find_book(book_title)
    
    if user and book and book["is_available"]:
        user["borrowed_books"].append(book)
        book["is_available"] = False
        print(f"{user_name} a emprunté {book_title}")
    else:
        print(f"Erreur : soit l'utilisateur, soit le livre est introuvable, ou le livre est déjà emprunté.")

# Fonction pour rendre un livre
def return_book(user_name, book_title):
    user = find_user(user_name)
    book = find_book(book_title)
    
    if user and book and book in user["borrowed_books"]:
        user["borrowed_books"].remove(book)
        book["is_available"] = True
        print(f"{user_name} a rendu {book_title}")
    else:
        print("Erreur : utilisateur ou livre introuvable.")

# Fonction pour lister les livres disponibles
def list_available_books():
    available_books = [book for book in books if book["is_available"]]
    if available_books:
        print("Livres disponibles :")
        for book in available_books:
            print(f"- {book['title']} par {book['author']}")
    else:
        print("Aucun livre disponible.")

# Fonction pour lister les emprunts d'un utilisateur
def list_user_loans(user_name):
    user = find_user(user_name)
    
    if user and user["borrowed_books"]:
        print(f"Livres empruntés par {user_name} :")
        for book in user["borrowed_books"]:
            print(f"- {book['title']} par {book['author']}")
    elif user:
        print(f"{user_name} n'a emprunté aucun livre.")
    else:
        print("Utilisateur introuvable.")

# Fonction principale pour l'interface en ligne de commande
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

# Exécution du programme principal
if __name__ == "__main__":
    main()

