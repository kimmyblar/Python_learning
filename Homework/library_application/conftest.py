from os import linesep
from tarfile import TruncatedHeaderError

import pytest
import os

from pygments.lexers import find_lexer_class_by_name

from Python_learning.Homework.library_application.library import *

@pytest.fixture
def created_library():

    library1 = Library('Библиотека')


    book1 = Book('Идиот','Тестовый автор',  2025)
    book2 = Book('Муму','Тургенев',  1889)
    book3 = Book('Солярис', 'Станислав Лем', 1990)

    library1.add_book(book1)
    library1.add_book(book2)
    library1.add_book(book3)

    return library1

@pytest.fixture
def created_empty_library():

    library2 = Library('Пустая библиотека')

    return library2

@pytest.fixture(scope="session", autouse=True)
def prepare_test_envierement():
    file_name = 'test_save_library.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
    yield
    file_name = 'test_library.txt'
    if os.path.exists(file_name):
       with open(file_name, 'r+') as f:
           lines = f.readlines()
           f.seek(0)
           f.writelines(lines[:-1])
           f.truncate()



