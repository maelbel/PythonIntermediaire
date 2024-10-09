class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        return f"Utilisateur : {self.name}"

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"Livres empruntés par {self.name} :")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{self.name} n'a emprunté aucun livre.")
