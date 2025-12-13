import random
from .library import Library
from .book import Book


def simulate(steps: int = 10, seed=20):
    random.seed(seed)
    library = Library()
    authors = ["Агата Кристи", "Уильям Шекспир", "Джоан Роулинг", "Михаил Булгаков", "Фёдор Достоевский", "Лев Толстой",
               "Александр Пушкин", "Стивен Кинг"]
    titles = ["Убийство в Восточном экспрессе", "Гамлет", "Гарри Поттер и философский камень", "Мастер и Маргарита",
              "Преступление и наказание", "Война и мир", "Евгений Онегин", "Сияние"]
    genres = ["детектив", "драма", "фэнтези", "роман", "психологический роман", "роман-эпопея", "роман в стихах",
              "ужасы"]

    print(f"начинается симуляция в {steps} шагов...")
    for i in range(1, steps + 1):
        event = random.choice(["add_book", "remove_book", "search_author",
                               "search_genre", "search_year", "get_book_by_isbn", "get_nonexistent"])
        print(f"шаг {i}:  событие {event}")
        if event == "add_book":
            new_book = Book(
                title=random.choice(titles),
                author=random.choice(authors),
                genre=random.choice(genres),
                year=random.choice(range(1833, 1997)),
                isbn=f"ISBN:{random.randint(111111, 999999)}"
            )
            library.add_book(new_book)
            print(f"добавили книгу {new_book}")
            print(f"всего стало книг: {len(library.books)}")

        elif event == "remove_book" and len(library.books) >= 1:
            remove_book = random.choice(library.books)
            isbn_removed = remove_book.isbn
            success = library.remove_book(isbn_removed)
            if success:
                print(f"удалена книга {remove_book}")
                print(f"всего стало книг: {len(library.books)}")
            else:
                print(f"случилась ошибка с удалением книги {remove_book}")

        elif event == "search_author":
            search_author = random.choice(authors)
            result = library.find_by_author(search_author)
            if result:
                print(f"найдены книги автора {search_author} в количестве {len(result)} штук")
            else:
                print(f"не найдены книги автора {search_author}")

        elif event == "search_genre":
            search_genre = random.choice(genres)
            result = library.find_by_genre(search_genre)
            if result:
                print(f"найдены книги жанра {search_genre} в количестве {len(result)} штук")
            else:
                print(f"не найдены книги автора {search_genre}")
        elif event == "search_year":
            search_year = random.randint(1883, 1997)
            result = library.find_by_year(search_year)
            if result:
                print(f"найдены книги, изданные в {search_year} году в количестве {len(result)} штук")
            else:
                print(f"не найдены книги изданные в  {search_year} году")
        elif event == "get_book_by_isbn" and len(library.books) >= 1:
            ibsn_to_book = random.choice(list(library.indexes.keys()))
            result = library.find_by_isbn(ibsn_to_book)
            if result:
                print(f"найдена книга с isbn {ibsn_to_book}: {result}")
            else:
                print(f"не найдена книга с isbn {ibsn_to_book}")

        elif event == "get_nonexistent":
            nonexistent = "ISBN: 99999999"
            result = library.find_by_isbn(nonexistent)
            if result is None:
                print(f"не найдена книга с isbn {nonexistent}, так и должно быть!")
            else:
                print(f"как-то нашлась книга с isbn {nonexistent}")

    print("ИТОГ")
    if len(library.books) == 0:
        print("библиотека пуста(")
    else:
        print(f"всего книг в библиотеке: {len(library.books)}")
    print("конец!")
