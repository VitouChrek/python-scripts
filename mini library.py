class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
class library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        return [str(book) for book in self.books]
    def find_books_by_author(self, author):
        return [str(book) for book in self.books if book.author == author]
