import pytest
from Python_learning.Homework.pytest_example.lesson_11 import debug_books_list
from Python_learning.Homework.pytest_example import calculator

@pytest.fixture
def generate_book_list():
    return [
    ("Мы", "Замятин", '1968'),
    ("Преступление и наказание", "Фёдор Достоевский", "1866")
]

@pytest.fixture(scope='session', autouse=True)
def prepare_test_envierement():
    print('НАЧАЛО ТЕСТИРОВАНИЯ')
    debug_books_list = []
    yield
    print('ТЕСТИРОВАНИЕ ЗАВЕРШЕНО')