class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self):
        return f"book(title = '{self.title}', author = '{self.author}', year = '{self.year}', genge = '{self.genre}', isbn = '{self.isbn}')"
    def __str__(self):
        return f"'{self.title}'written by {self.author} ISBN: {self.isbn}'"