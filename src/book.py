class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self):
        return f"Book(title = '{self.title}', author = '{self.author}', year = '{self.year}', genre = '{self.genre}', isbn = '{self.isbn}')"
    def __str__(self):
        return f"Книга: {self.title} ({self.year}), автор: {self.author}"