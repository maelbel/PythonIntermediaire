import sqlite3

# Connexion à la base de données SQLite
def create_connection():
    return sqlite3.connect('library.db')

# Initialisation de la base de données (création des tables)
def initialize_db():
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_available INTEGER DEFAULT 1
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS loans (
                user_id INTEGER,
                book_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(book_id) REFERENCES books(id),
                PRIMARY KEY (user_id, book_id)
            )
        ''')

# Ajouter un livre à la base de données
def add_book(title, author):
    conn = create_connection()
    with conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    print(f"Livre ajouté : {title} par {author}")

# Ajouter un utilisateur à la base de données
def add_user(name):
    conn = create_connection()
    with conn:
        conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    print(f"Utilisateur ajouté : {name}")

# Trouver un livre par son titre dans la base de données
def find_book(title):
    conn = create_connection()
    book = conn.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchone()
    return book

# Trouver un utilisateur par son nom dans la base de données
def find_user(name):
    conn = create_connection()
    user = conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchone()
    return user

# Emprunter un livre
def loan_book(user_name, book_title):
    user = find_user(user_name)
    book = find_book(book_title)
    
    if user and book and book[3]:  # Vérifie que le livre est disponible
        conn = create_connection()
        with conn:
            conn.execute("INSERT INTO loans (user_id, book_id) VALUES (?, ?)", (user[0], book[0]))
            conn.execute("UPDATE books SET is_available = 0 WHERE id = ?", (book[0],))
        print(f"{user_name} a emprunté {book_title}")
    else:
        print(f"Erreur : utilisateur ou livre introuvable, ou le livre est déjà emprunté.")

# Rendre un livre
def return_book(user_name, book_title):
    user = find_user(user_name)
    book = find_book(book_title)
    
    if user and book:
        conn = create_connection()
        with conn:
            conn.execute("DELETE FROM loans WHERE user_id = ? AND book_id = ?", (user[0], book[0]))
            conn.execute("UPDATE books SET is_available = 1 WHERE id = ?", (book[0],))
        print(f"{user_name} a rendu {book_title}")
    else:
        print("Erreur : utilisateur ou livre introuvable.")

# Lister les livres disponibles
def list_available_books():
    conn = create_connection()
    available_books = conn.execute("SELECT title, author FROM books WHERE is_available = 1").fetchall()
    
    if available_books:
        print("Livres disponibles :")
        for book in available_books:
            print(f"- {book[0]} par {book[1]}")
    else:
        print("Aucun livre disponible.")

# Lister les emprunts d'un utilisateur
def list_user_loans(user_name):
    user = find_user(user_name)
    
    if user:
        conn = create_connection()
        borrowed_books = conn.execute('''
            SELECT books.title, books.author 
            FROM books 
            JOIN loans ON books.id = loans.book_id 
            WHERE loans.user_id = ?
        ''', (user[0],)).fetchall()
        
        if borrowed_books:
            print(f"Livres empruntés par {user_name} :")
            for book in borrowed_books:
                print(f"- {book[0]} par {book[1]}")
        else:
            print(f"{user_name} n'a emprunté aucun livre.")
    else:
        print("Utilisateur introuvable.")

# Fonction principale pour l'interface en ligne de commande
def main():
    initialize_db()
    
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
