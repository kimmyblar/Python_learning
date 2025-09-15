
# 1) Попробуй добавить в функцию add_book возможность не только передавать книги через ввод с клавиатуры,
# но и как параметры функции, то есть вызывать функцию указывая название, автора и год издания.
# 2) Попробуй переработать программу так, чтобы год издания книги был необязательным параметром,
# обрати внимание что это может повлиять на работу и со списком, и на чтение и на запись в файл.
# 3) Добавь в итоговую функцию скрытый вызов еще одного режима,
# который назовём 'debug' т.е elif answer == 'debug', то...
# И здесь реализуй добавления нескольких книг из словаря при помощи именованных аргументов,
# и из списка используя позиционные аргументы.
# Словарь и список с книгами создай сама как глобальные переменные)

debug_books_list = [
    ("1984", "Джордж Оруэлл", '1968'),
    ("Преступление и наказание", "Фёдор Достоевский", "1866")
]

debug_books_dict = [
    {'title':"Война и мир", "author":"Лев Толстой", "year": "1869"},
{'title':'Мастер и Маргарита','author': "Михаил Булгаков"}
]

def load_books(filename):
    try:
        with open(filename, 'r') as books:
            book_list = []
            for line in books:
                parts = line.split('|')
                title, author, year = parts[0], parts[1], parts[2]
                book_list.append((title, author, year))
            return book_list
    except FileNotFoundError:
        print('Файл не найден, продолжаем работу с пустым файлом')
        return []

def print_books(book_list):
    list_of_book = []
    for book in book_list:
        try:
            print(f'{book[0]}, {book[1]}, {book[2]}')
            list_of_book.append(book)
        except IndexError:
            print(f'{book[0]}, {book[1]}')
            list_of_book.append(book)
    return list_of_book


def add_book(book_list, title=None, author=None, year=None):
    if title and author:
        if year is not None:
            book_list.append((title, author, year))
        else:
            book_list.append((title, author))
    else:
        title = input('Введите название книги: ')
        author = input('Введите автора: ')
        year = input('Введите год издания (можно оставить пустым): ')
        book_list.append((title, author, year))
    print(f'Добавлена новая книга: {title}, {author}, {year}')


def search_book(book_list, title=None, author=None):
    if title is None and author is None:
        search = input('Введите автора или название книги, которую хотите найти: ').lower()
    else:
        if title and author:
            raise ValueError('Необходимо ввести только один из искомых параметров')
        elif title:
            if title.isalpha():
                search = title.lower()
            else:
                raise ValueError('Название книги может содержать только буквенные и цифровые значения')
        else:
            if author.isalpha():
                search = author.lower()
            else:
                raise ValueError('Имя автора книги может содержать только буквенные значения')
    result = []
    for book in book_list:
        if search in book[0].lower() or search in book[1].lower():
            result.append(book)
    if result:
        print('Найденные книги:')
        print_books(result)
    else:
        print('Книги не найдено или она не существует')
    return result

def delete_book(book_list):
    user_delete = input('Введите автора или название книги, которую хотите удалить: ').lower()
    list_after_deleting = []
    list_of_deleted_books = []
    for book in book_list:
        if user_delete in book[0].lower() or user_delete in book[1].lower():
            list_of_deleted_books.append(book)
        else:
            list_after_deleting.append(book)
    print(f'Вы удалили книгу: ')
    print_books(list_of_deleted_books)
    if not list_of_deleted_books:
        print('Книга не найдена')
    return list_after_deleting


def show_books(book_list):
    if not book_list:
        print('В списке нет книг')
    else:
        print('Ваш список книг:')
        print_books(book_list)

def break_program(book_list, filename):
    with open(filename, 'w') as books:
        for book in book_list:
            if len(book) == 3:
                books.write(f'{book[0]}|{book[1]}|{book[2]} \n ')
            else:
                books.write(f'{book[0]}|{book[1]}| \n')
    print('Список книг сохранён. До свидания!')


def we_work_with():
    filename = '../library_application/test_library.txt'
    book_list = load_books(filename)
    while True:
        print('\nМеню:')
        print('1 - Добавить книгу')
        print('2 - Найти книгу')
        print('3 - Удалить книгу')
        print('4 - Отобразить все книги')
        print('5 - Завершить программу')

        answer = input('Выберите действие: ')
        if answer == '1':
            add_book(book_list)
        elif answer == '2':
            search_book(book_list)
        elif answer == '3':
            book_list = delete_book(book_list)
        elif answer == '4':
            show_books(book_list)
        elif answer == '5':
            break_program(book_list, filename)
            break
        elif answer.lower() == 'debug':
            for book in debug_books_list:
                add_book(book_list,*book)
            for book in debug_books_dict:
                add_book(book_list, **book)

        else:
            print('Неверный ввод. Пожалуйста, выберите действие из списка.')

# we_work_with()


