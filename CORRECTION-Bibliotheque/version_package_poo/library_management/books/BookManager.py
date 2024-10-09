from books.Book import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Livre ajouté : {book}")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_book_available()]
        if available_books:
            print("Livres disponibles :")
            for book in available_books:
                print(f"- {book}")
        else:
            print("Aucun livre disponible.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
