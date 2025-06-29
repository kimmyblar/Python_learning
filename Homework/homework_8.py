def load_books(filename):
    try:
        with open('homework_7.txt', 'r') as books:
            book_list = []
            for line in books:
                parts = line.split('|')
                title, author, year = parts[0], parts[1], parts[2]
                book_list.append((title, author, year))
            return book_list
    except FileNotFoundError:
        print('Файл не найден, продолжаем работу с пустым файлом')
        return []

def add_book(book_list):
    title = input('Введите название книги: ')
    author = input('Введите автора: ')
    year = input('Введите год издания: ')
    book_list.append((title, author, year))

def search_book(book_list):
    search = input('Введите автора или название книги, которую хотите найти: ').lower()
    result = []
    for book in book_list:
        if search in book[0].lower() or search in book[1].lower():
            result.append(book)
    if result:
        print('Найденные книги:')
        for book in result:
            print(f'{book[0]}, {book[1]}, {book[2]}')
    else:
        print('Книги не найдено или она не существует')

def delete_book(book_list):
    user_delete = input('Введите автора или название книги, которую хотите удалить: ').lower()
    list_after_deleting = []
    list_of_deleted_books = []
    for book in book_list:
        if user_delete in book[0].lower() or user_delete in book[1].lower():
            list_of_deleted_books.append(book)
        else:
            list_after_deleting.append(book)
    for book in list_of_deleted_books:
        print(f'Вы удалили книгу: {book[0]}, {book[1]}, {book[2]}')
    if not list_of_deleted_books:
        print('Книга не найдена')
    return list_after_deleting


def show_books(book_list):
    if not book_list:
        print('В списке нет книг')
    else:
        print('Ваш список книг:')
        for book in book_list:
            print(f'{book[0]}, {book[1]}, {book[2]}')

def break_program(book_list, filename):
    with open(filename, 'w') as books:
        for book in book_list:
            books.write(f'{book[0]}|{book[1]}|{book[2]}\n')
    print('Список книг сохранён. До свидания!')

def we_work_with():
    filename = 'homework_7.txt'
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
        else:
            print('Неверный ввод. Пожалуйста, выберите действие из списка.')


we_work_with()

