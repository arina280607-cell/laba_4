from typing import List, Union, Iterator, Optional
from collections import defaultdict
from .book import Book


class BookCollection:
    """
        списковая коллекция, реализована через композицию (содержит список книг внутри)
    """
    def __init__(self):# композиция: коллекция содержит список книг
        self.books: List[Book] = []

    def __getitem__(self, index: Union[int, slice]) -> Union[Book, 'BookCollection']: #доступ по индексу или срезу.
        if isinstance(index, slice):
            slised = BookCollection()
            slised.books = self.books[index]
            return slised
        else:
            return self.books[index]

    def __iter__(self) -> Iterator[Book]:
        return iter(self.books)
    def __len__(self) -> int:
        return len(self.books)
    def __repr__(self) -> str :
        return f'BookCollection({len(self)} книг)'

    def insert(self, index: int, book: Book): # вставляет книгу на определённое место
        self.books.insert(index, book)
    def remove(self, book: Book): # удаляет книгу из коллекции
        self.books.remove(book)
    def append(self, book: Book): # добавляет книгу в коллекцию
        self.books.append(book)
    # что еще может быть полезно
    def contains(self, book: Book) -> bool: # проверим, есть ли книга в коллекции
        return book in self.books
    def get_by_title(self, title: str) -> Optional[Book]:# найти книгу по названию
        for book in self.books:
            if book.title == title:
                return book
        return None



class IndexDict:
    """
        словарная коллекция
    """
    def __init__(self):
        self.index_isbn = {} # isbn -> книга
        self.index_author = defaultdict(list) #список книг данного автора
        self.index_year = defaultdict(list) #список книг по году
    def __getitem__(self, isbn) -> Book:
        if isbn not in self.index_isbn:
            raise IndexError(f'книга с индексом {isbn} не найдена')
        return self.index_isbn[isbn]
    def __setitem__(self, isbn, book: Book):
        if isbn in self.index_isbn:
            old_book = self.index_isbn[isbn]
            if old_book.author in self.index_author:
                if old_book in self.index_author[old_book.author]:
                    self.index_author[old_book.author].remove(old_book)
            if old_book.year in self.index_year:
                if old_book in self.index_year[old_book.year]:
                    self.index_year[old_book.year].remove(old_book)
        self.index_isbn[isbn] = book
        self.index_author[book.author].append(book)
        self.index_year[book.year].append(book)

    def __delitem__(self, isbn):
        if isbn not in self.index_isbn:
            raise KeyError(f"книга не найдена")
        book = self.index_isbn[isbn]
        del self.index_isbn[isbn]
        if book.year in self.index_year:
            self.index_year[book.year].remove(book)
        if book.author in self.index_author:
            self.index_author[book.author].remove(book)

    def __iter__(self):
        return iter(self.index_isbn)
    def __len__(self):
        return len(self.index_isbn)
    def __repr__(self):
        return f'IndexDict({self.index_isbn})'
    def __contains__(self, isbn):
        return isbn in self.index_isbn










