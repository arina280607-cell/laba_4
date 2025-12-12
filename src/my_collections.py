from typing import List, Union, Iterator
from collections.abc import MutableMapping
from collections import defaultdict
from src.book import Book


class BookCollection(MutableMapping):
    """
        cписковая коллекция
    """
    def __init__(self):
        self.books: List[Book] = []
    def __getitem__(self, index: Union[int, slice]) -> Union[Book, 'BookCollection']:
        if isinstance(index, slice):
            sliced_books = self.books[index]
            new_books = BookCollection()
            new_books.books = sliced_books
            return new_books
        else:
            return self.books[index]
    def __iter__(self) -> Iterator[Book]:
        return iter(self.books)
    def __len__(self) -> int:
        return len(self.books)
    def __delitem__(self, index: int) -> None:
        del self.books[index]
    def __setitem__(self, index: int, value: Book) -> None:
        self.books[index] = value
    def __repr__(self) -> str :
        return f'BookCollection({self.books})'

    def insert(self, index: int, value: Book):
        self.books.insert(index, value)
    def remove(self, value: Book):
        self.books.remove(value)
    def append(self, value: Book):
        self.books.append(value)


class IndexDict(MutableMapping):
    """
        словарная коллекция
    """
    def __init__(self):
        self.store = {}
        self.index_isbn = {}
        self.index_author = defaultdict(list) #список книг данного автора
        self.index_year = defaultdict(list) #список книг по году
    def __getitem__(self, isbn):
        return self.store[isbn]
    def __setitem__(self, isbn, book):
        if isbn in self.store:
            return
        self.store[isbn] = book
        self.index_isbn[book.isbn] = book
        self.index_author[book.author].append(book)
        self.index_year[book.year].append(book)

    def __delitem__(self, isbn):
        if isbn not in self.store:
            return KeyError(f"book is not found")
        book_remove = self.store.pop(isbn)
        self.remove_book(book_remove)
    def remove_book(self, book: Book):
        if book.isbn in self.index_isbn:
            del self.index_isbn[book.isbn]
        if book.author in self.index_author and book in self.index_author[book.author]:
            self.index_author[book.author].remove(book)
        if book.year in self.index_year and book in self.index_year[book.year]:
            self.index_year[book.year].remove(book)

    def __iter__(self):
        return iter(self.store)
    def __len__(self):
        return len(self.store)
    def __repr__(self):
        return f'IndexDict({self.store})'









