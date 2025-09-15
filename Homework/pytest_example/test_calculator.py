import pytest
from Python_learning.Homework.pytest_example import calculator
import allure

@pytest.fixture
def number_set():
    return 10, 5

@allure.title('Тренируем написание шагов')
@allure.description('Тестовое описание просто посмотреть отобразится ли оно на этот раз')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
def test_add_with_fixture(number_set):
    with allure.step('Шаг 1: Определяем список чисел'):
        a, b = number_set
    with allure.step('Шаг 2: Сравниваем ожидаемый результат с фактическим'):
        assert calculator.add(a, b) == 15

@allure.title('Тестируем сложение')
@allure.description('Тестовое описание просто посмотреть отобразится ли оно на этот раз')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-1, -1, -2),
    (0, 5, 5),
])
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected

@allure.title('Тестируем вычитание')
@allure.description('Тестовое описание просто посмотреть отобразится ли оно на этот раз')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (5, 10, -5),
    (0, 0, 0),
])
def test_subtract(a, b, expected):
    assert calculator.subtract(a, b) == expected

@allure.title('Тестируем умножение')
@allure.description('Тестовое описание просто посмотреть отобразится ли оно на этот раз')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (-1, 3, -3),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert calculator.multiply(a, b) == expected

@allure.title('Тестируем деление')
@allure.description('Тестовое описание просто посмотреть отобразится ли оно на этот раз')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (9, 3, 3),
])
def test_divide(a, b, expected):
    assert calculator.divide(a, b) == expected

@allure.title('Тестируем деление на 0')
@allure.description('Тестовое описание просто посмотреть отобразится ли оно на этот раз')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Viktoriia')
@allure.link('http://ya.ru', name='Тестируемый сайт')
@allure.issue('TEST-123')
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="ноль"):
        calculator.divide(10, 0)
