class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' par {self.author}"

    def set_available(self, available):
        self.is_available = available

    def is_book_available(self):
        return self.is_available
