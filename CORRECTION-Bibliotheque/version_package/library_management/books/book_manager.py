# Liste globale des livres en mémoire
books = []

def add_book(title, author):
    book = {"title": title, "author": author, "is_available": True}
    books.append(book)
    print(f"Livre ajouté : {title} par {author}")

def list_available_books():
    available_books = [book for book in books if book["is_available"]]
    
    if available_books:
        print("Livres disponibles :")
        for book in available_books:
            print(f"- {book['title']} par {book['author']}")
    else:
        print("Aucun livre disponible.")

def find_book(title):
    return next((book for book in books if book["title"] == title), None)
