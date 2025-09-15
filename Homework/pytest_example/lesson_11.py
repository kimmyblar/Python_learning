from Python_learning.Homework.pytest_example.homework_9 import *
import pytest
import allure



debug_books_list = [
    ("Мы", "Замятин", '1968'),
    ("Преступление и наказание", "Фёдор Достоевский", "1866")
]

negative_books_list = [
    ("Мы", "Замятин"),
    ("Преступление и наказание", "Фёдор Достоевский", "1866")
]

@pytest.mark.xfail
@pytest.mark.parametrize('books_for_search, title', [(debug_books_list, 'Мы'),
                                                     (negative_books_list, 'ПРЕСТУПЛЕНИЕ И НАКАЗАНИЕ'),
                                                     (negative_books_list, 'ПРЕСТУПЛЕНИЕ')])
def test_search_book_by_title_found(books_for_search, title):
   result = search_book(books_for_search, title=title)
   assert len(result) > 0, 'Не найдено ни одного результата'

@allure.title('Тест поиска отсутствующей книги')
@allure.description('Отправляем все некорректные книги и ожидаем что поиск не будет произведен')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
@pytest.mark.parametrize('books_for_search, title', [(debug_books_list, 'Собаканасене')])
def test_search_book_by_title_not_found(books_for_search, title):
   result = search_book(books_for_search, title=title)
   assert len(result) == 0, 'Мы нашли книгу по вашему запросу'


@pytest.mark.parametrize('books_for_search, title, author, error_message', [(debug_books_list, '?',None, 'Название книги может содержать только буквенные и цифровые значения'),
                                                                            (debug_books_list, None, '1', 'Имя автора книги может содержать только буквенные значения'),
                                                                            (debug_books_list, None, '%', 'Имя автора книги может содержать только буквенные значения')])
def test_search_book_wrong_data(books_for_search, title, author, error_message):
   with pytest.raises(ValueError, match=error_message):
       result = search_book(books_for_search, title=title, author=author)



@pytest.mark.parametrize('list_of_books', [debug_books_list, negative_books_list])
def test_print_books(list_of_books):
    list_of_book = print_books(list_of_books)
    assert list_of_book == list_of_books

# @allure.title('Тест вывода книг на экран')
@allure.description('Отправляем все некорректные книги и ожидаем что поиск не будет произведен')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
def test_print_books_fixture(generate_book_list):
    with allure.step('Шаг1: Вызываем функцию печати книг'):
        list_of_book = print_books(generate_book_list)
    with allure.step('Шаг2: Проверяем данные'):
        assert list_of_book == generate_book_list



