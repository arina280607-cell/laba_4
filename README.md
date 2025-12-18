# Лабораторная работа №5

### Отладĸа ĸодовой базы проеĸта на Python с помощью средств отладĸи

### Ошибка 1 — ошибка границы цикла (off-by-one)
Место: simulation.py, строка 17

Симптом:
Цикл выполняется на 1 шаг меньше, 
чем указано в параметре steps

Как воспроизвести:
Запустить симуляцию с steps=10. 
Будет выполнено только 9 итераций

Отладка:
Установлен breakpoint на условие if.
В отладчике видно, что выражение всегда True.

Причина:
Неверно указан конец диапазона в range

Исправление:
- Заменено (for i in range(1, steps))
- На (for i in range(1, steps + 1)

Проверка:
Поведение симуляции соответствует ожидаемому.

Доказательства:

### Ошибка 2 — неверное логическое условие
Место: simulation.py, строка 22

Симптом:
Книги добавляются даже при других событиях, если первое условие ложно.

Как воспроизвести:
Запустить симуляцию с seed=30. 
В некоторых шагах будет печататься "добавили книгу",
хотя событие не "add_book".

Отладка:
Breakpoint на if event == "add_book" or "remove_book". 
Видно, что "remove_book" всегда True

Причина:
Использовано неверное составное условие с or

Исправление:
- Заменено (if event == "add_book" or "remove_book":)
- На (if event == "add_book":)

Проверка:
Книги добавляются только при событии "add_book"

Доказательства:

### Ошибка 3 —  использование изменяемого значения по умолчанию
Место: library.py, строка 29

Симптом:
При повторном вызове find_by_genre 
без аргумента возвращается предыдущий 
результат.

Как воспроизвести:
Запустить симуляцию и наблюдать за поиском по жанру.

Отладка:
Breakpoint в методе find_by_genre. 
Видно, что параметр genre=None 
сохраняется между вызовами.

Причина:
Использование изменяемого объекта (списка)
как значения по умолчанию.

Исправление:
- Заменено (def find_by_genre(self, genre=None):
    if genre is None:
        genre = []
    return [book for book in self.books if book.genre == genre])
- На (def find_by_genre(self, genre):
    return [book for book in self.books if book.genre == genre])

Проверка:
Книги добавляются только при событии "add_book"

Доказательства:

### Ошибка 4 — перепутанные аргументы или поля объекта
Место: simulation.py, строка 17

Симптом:
Год публикации и жанр книги перепутаны местами.

Как воспроизвести:
При добавлении книги жанр записывается в год и наоборот.

Отладка:
Breakpoint в конструкторе Book.

Причина:
Аргументы переданы в неправильном порядке.

Исправление:
- Заменено (new_book = Book(
    title=random.choice(titles),
    author=random.choice(authors),
    genre=random.choice(genres),
    year=random.choice(range(1833, 1997)),
    isbn=f"ISBN:{random.randint(111111, 999999)}"
))
- На (new_book = Book(
    title=random.choice(titles),
    author=random.choice(authors),
    year=random.choice(range(1833, 1997)),
    genre=random.choice(genres),
    isbn=f"ISBN:{random.randint(111111, 999999)}"
))

Проверка:
Теперь поля книги заполняются правильно.

Доказательства:


### Ошибка 5 — сравнение через is вместо ==
Место:library.py, строка 27

Симптом:
Проверка на None может работать некорректно.

Как воспроизвести:
Искать несуществующий ISBN.

Отладка:
Установить breakpoint на возвращаемом значении.

Причина:
если где-то возвращается не None, а False или 0, сравнение is может дать неожиданный результат.

Исправление:
- Заменено (def find_by_isbn(self, isbn: str) -> Optional[Book]:
    result = self.indexes.index_isbn.get(isbn)
    if result is False: 
        return None
    return result)
- На (def find_by_isbn(self, isbn: str) -> Optional[Book]:
    result = self.indexes.index_isbn.get(isbn)
    if not result: 
        return None
    return result)

Проверка:
Теперь сравнение работает корректно

Доказательства:

