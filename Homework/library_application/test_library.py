from fileinput import filename
from itertools import count

import pytest

from Python_learning.Homework.library_application.library import Library, Book


@pytest.mark.parametrize('attributes, expected_value, index', [
    ('author', 'Тестовый автор', 0),
    ('title', 'Идиот', 0),
    ('author', 'Тургенев', 1),
    ('title', 'Муму', 1)
])
def test_add_book(attributes, expected_value, index, created_library):
    book=created_library.book_list[index]
    assert getattr(book, attributes)==expected_value

def test_search_book(created_library):
    result=created_library.search_book(title='Идиот')
    assert result[0].title=='Идиот'


@pytest.mark.parametrize('attributes, deleted_value', [
    ('author', 'Тургенев'),
    ('title', 'Идиот')
])
def test_delete_book(attributes, deleted_value, created_library):
    kwargs = {attributes:deleted_value}
    created_library.delete_book(**kwargs)
    assert deleted_value not in created_library

def test_load_library(created_empty_library):
    created_empty_library.load_library('test_library.txt')
    assert len(created_empty_library.book_list) > 0
    assert isinstance(created_empty_library.book_list[0], Book)

def test_save_library(created_library):
    file_name = 'test_save_library.txt'
    expected_result = 'Идиот|Тестовый автор|2025\n'\
                      'Муму|Тургенев|1889\n' \
                      'Солярис|Станислав Лем|1990\n'
    created_library.save_library(file_name)
    with open(file_name, 'r') as f:
        saved_file =  f.read()
    assert saved_file == expected_result

def test_library_context_manager():
    library2 = Library('Библиотека_2', 'test_library.txt')
    book3 = Book('Идиот', 'Тестовый автор', 2025)
    with library2 as lib:
        assert len(lib) == 3
        lib.add_book(book3)
    with open('test_library.txt') as f:
        count = 0
        for _ in f:
            count = count+1
        assert count == 4


