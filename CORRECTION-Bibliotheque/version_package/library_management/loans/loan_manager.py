from users.user_manager import find_user
from books.book_manager import find_book

def loan_book(user_name, book_title):
    user = find_user(user_name)
    book = find_book(book_title)
    
    if user and book and book["is_available"]:
        user["borrowed_books"].append(book)
        book["is_available"] = False
        print(f"{user_name} a emprunté {book_title}")
    else:
        print(f"Erreur : utilisateur ou livre introuvable, ou le livre est déjà emprunté.")

def return_book(user_name, book_title):
    user = find_user(user_name)
    book = find_book(book_title)
    
    if user and book and book in user["borrowed_books"]:
        user["borrowed_books"].remove(book)
        book["is_available"] = True
        print(f"{user_name} a rendu {book_title}")
    else:
        print("Erreur : utilisateur ou livre introuvable.")
