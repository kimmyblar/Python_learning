# class Genre():
#     def __init__(self, genre):
#         self.genres = ['sci-fi', 'detective', 'poem']
#         self.genre = genre
#         self.check_genre()
#
#     def check_genre(self):
#         if self.genre not in self.genres:
#             raise ValueError(f'Такого жанра нет в списке {self.genres}')
from operator import ifloordiv


class Book():
    def __init__(self, title, author, year=None):
        # super().__init__(genre)
        self.title = title
        self.author = author
        self.year = year


    def __repr__(self):
        return f'{self.title} {self.author} {self.year}'


    def __str__(self):
        return f'{self.title} {self.author} {self.year}'

class Library():
    def __init__(self, name, filename='library.txt'):
        self.book_list = []
        self.list_of_book = []
        self.name = name
        self.filename = filename


    def __len__(self):
        return len(self.book_list)

    # def __getitem__(self, item):
    #     return self.book_list[item]

    def __contains__(self, value):
        return any(
            value == book.title or value == book.author
            for book in self.book_list
        )

    def __enter__(self):
        print('Мы вошли в библиотеку')
        self.load_library(self.filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_library(self.filename)
        print('Мы вышли из библиотеки')

    # def __iter__(self):
    #     return iter(self.book_list)

    def load_library(self, filename=None):
        try:
            filename = filename if filename else self.filename
            with open(filename, 'r') as books:
                for line in books:
                    line = line.strip('\n')
                    parts = line.split('|')
                    title, author, year = parts[0], parts[1], parts[2]
                    new_book = Book(title, author, year)
                    self.book_list.append(new_book)

        except FileNotFoundError:
            print('Файл с библиотекой не найден, создаем пустую библиотеку ')

    def add_book(self, book: Book):
        if isinstance(book,Book):
            self.book_list.append(book)
        else:
            raise ValueError('В библиотеку можно добавить только экземпляры класса Book')

    def show_books(self, books=None):
        books = books if books else self.book_list
        for book in books:
            print(book)

    def check_input(self, title=None, author=None, message=None):
        if title is None and author is None:
            user_input = input(message).lower()
        else:
            if title and author:
                raise ValueError('Необходимо ввести только один из искомых параметров')
            elif title:
                if title.isalpha():
                    user_input = title.lower()
                else:
                    raise ValueError('Название книги может содержать только буквенные и цифровые значения')
            else:
                if author.isalpha():
                    user_input = author.lower()
                else:
                    raise ValueError('Имя автора книги может содержать только буквенные значения')
        return user_input

    def search_book(self, title=None, author=None):
        search = self.check_input(title, author, 'Введите автора или название книги, которую хотите найти: ')
        result = []
        for book in self.book_list:
            if search in book.title.lower() or search in book.author.lower():
                result.append(book)
        if result:
            print('Найденные книги:')
            self.show_books(result)
        else:
            print('Книги не найдено или она не существует')
        return result

    def delete_book(self, title=None, author=None):
        user_delete = self.check_input(title, author, 'Введите название или автора книги, которую хотите удалить')
        list_after_deleting = []
        list_of_deleted_books = []
        for book in self.book_list:
            if user_delete in book.title.lower() or user_delete in book.author.lower():
                list_of_deleted_books.append(book)
                print(f'Вы удалили книгу: ')
            else:
                list_after_deleting.append(book)
        self.show_books(list_of_deleted_books)
        if not list_of_deleted_books:
            print('Книга не найдена')
        # return list_after_deleting
        self.book_list = list_after_deleting

    def save_library(self, filename):
        with open(filename, 'w') as books:
            for book in self.book_list:
                if book.year:
                    books.write(f'{book.title}|{book.author}|{book.year}')
                else:
                    books.write(f'{book.title}|{book.author}|')
                books.write('\n')
        print('Список книг сохранён. До свидания!')




library1 = Library('Библиотека')

with library1 as lb:
    print('Я нахожусь в библиотеке')
#в ent засунуть лоад, в ex засунуть save_library, написать тест, который покажет что менеджер работает корректно
#
# book1 = Book('Идиот','Тестовый автор',  2025)
#
# library1.add_book(book1)
# print(library1.book_list[0].author)
#
# library1.show_books()
#
# library1.search_book('Идиот')
# library1.search_book('Книгакоторойнет')
#
# print(len(library1))
#
# print(library1)
#
# print('Идиот' in library1)
#
# for book in library1:
#     print(book)