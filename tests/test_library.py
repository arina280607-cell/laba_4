from src.book import Book
from src.my_collections import BookCollection, IndexDict
from src.library import Library

def test_book_creation():
    """
    тесты создания объекта Book
    """
    b = Book("Название", "Автор", 2000, "Жанр", "12345")
    assert b.title == "Название"
    assert b.author == "Автор"
    assert b.year == 2000
    assert b.genre == "Жанр"
    assert b.isbn == "12345"

class TestBookCollection:

    def setup_method(self):
        self.collection = BookCollection()
        self.book1 = Book("t1", "a1", 2000, "g1", "1")
        self.book2 = Book("t2", "a2", 2000, "g2", "2")

    def test_len(self):# тесты длины коллекции
        assert len(self.collection) == 0
        self.collection.append(self.book1)
        assert len(self.collection) == 1
        self.collection.append(self.book2)
        assert len(self.collection) == 2

    def test_add_iter(self):# тесты добавления и итерации
        self.collection.append(self.book1)
        self.collection.append(self.book2)
        collection = list(self.collection)
        assert len(self.collection) == 2
        assert self.book1 in collection
        assert self.book2 in collection

    def test_getitem(self):# тесты доступа по индексу
        self.collection.append(self.book1)
        self.collection.append(self.book2)
        assert self.collection[0] == self.book1
        assert self.collection[1] == self.book2

    def test_slice(self):# тесты доступа по срезу
        self.collection.append(self.book1)
        self.collection.append(self.book2)
        sliced = self.collection[0:1]
        assert isinstance(sliced, BookCollection)
        assert len(sliced) == 1
        assert sliced[0] == self.book1

    def test_add_rm(self):# тесты добавления и удаления
        self.collection.append(self.book1)
        assert self.book1 in self.collection
        assert len(self.collection) == 1
        self.collection.remove(self.book1)
        assert len(self.collection) == 0


class TestIndexDict:

    def setup_method(self):
        self.index = IndexDict()
        self.book1 = Book("t1", "a1", 2001, "g1", "1")
        self.book2 = Book("t2", "a1", 2000, "g2", "2")
        self.book3 = Book("t3", "a3", 2000, "g3", "3")

    def test_set_get(self):# получение по ключу
        self.index[self.book1.isbn] = self.book1
        retrieved = self.index[self.book1.isbn]
        assert retrieved == self.book1

    def test_index_add(self):# тесты обновления индексов
        self.index[self.book1.isbn] = self.book1
        assert self.book1.isbn in self.index.index_isbn
        assert self.book1 in self.index.index_author[self.book1.author]
        assert self.book1 in self.index.index_year[self.book1.year]

    def test_update(self): # изменение индексов
        self.index[self.book1.isbn] = self.book1
        self.index[self.book2.isbn] = self.book2

        assert len(self.index.index_author["a1"]) == 2
        assert self.book1 in self.index.index_author["a1"]
        assert self.book2 in self.index.index_author["a1"]

        assert len(self.index.index_year[2001]) == 1
        update_book1 = Book("t11", "a1", 2002, "g2", "1")
        self.index[update_book1.isbn] = update_book1

        assert self.book1 not in self.index.index_year[2001]
        assert update_book1 in self.index.index_year[2002]
        assert update_book1 in self.index.index_author["a1"]

    def test_delete(self): # тестирование удаления индексов и обновления
        self.index[self.book1.isbn] = self.book1
        initial_len = len(self.index)
        del self.index[self.book1.isbn]
        assert len(self.index) == initial_len - 1
        assert self.book1.isbn not in self.index.index_isbn
        assert self.book1 not in self.index.index_author[self.book1.author]
        assert self.book1 not in self.index.index_year[self.book1.year]

class TestLibrary:

    def setup_method(self):
        self.library = Library()
        self.book1 = Book("t1", "a1", 2000, "g1", "1")
        self.book2 = Book("t2", "a1", 2000, "g2", "2")

    def test_add(self):
        self.library.add_book(self.book1)
        assert len(self.library.books) == 1
        assert len(self.library.indexes) == 1
        assert self.book1.isbn in self.library.indexes.index_isbn

    def test_remove(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        success = self.library.remove_book("1")
        assert success == True
        assert len(self.library.books) == 1
        assert len(self.library.indexes) == 1
        assert "1" not in self.library.indexes

        success2 = self.library.remove_book("3")
        assert success2 == False

    def test_find_author(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        result = self.library.find_by_author("a1")
        assert len(result) == 2
        assert self.book1 in result
        assert self.book2 in result

    def test_find_year(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        result = self.library.find_by_year(2000)
        assert len(result) == 2
        assert self.book1 in result
        assert self.book2 in result

    def test_contains(self):
        self.library.add_book(self.book1)
        assert "1" in self.library
        assert "3" not in self.library














