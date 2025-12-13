from .my_collections import BookCollection, IndexDict
from .book import Book
from typing import List, Optional

class Library:
    def __init__(self):
        self.books = BookCollection()
        self.indexes = IndexDict()

    def add_book(self, book: Book): # добавляет книгу в библиотеку
        self.books.append(book)
        self.indexes[book.isbn] = book

    def remove_book(self, isbn): # удаляет книгу из библиотеки по индексу
        if isbn not in self.indexes:
            print(f"книги с индексом {isbn} уже нет")
            return False
        remove_book = self.indexes[isbn]
        self.books.remove(remove_book)
        del self.indexes[isbn]
        return True
    def find_by_author(self, author: str) -> List[Book]: # ищем книгу по автору используя индекс
        return self.indexes.index_author.get(author, [])
    def find_by_year(self, year: int) -> List[Book]: # ищем книгу по году используя индекс
        return self.indexes.index_year.get(year, [])
    def find_by_isbn(self, isbn: str) -> Optional[Book]: # получаем книгу по isbn из индекса
        return self.indexes.index_isbn.get(isbn)
    def find_by_genre(self, genre):
        return list(book for book in self.books if book.genre == genre)
    def __contains__(self, isbn: str) -> bool:
        return isbn in self.indexes.index_isbn
    def __repr__(self):
        return f"Library(books={len(self.books)}, indexes={len(self.indexes)})"






