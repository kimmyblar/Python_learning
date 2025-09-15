import time
#
#
# def decorator(func):
#     def wrapper():
#         print('Подготовлена тестовая среда')
#         func()
#         print('Очистка тестовой среды')
#     return wrapper
#
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Ваша функция выполнилась за {round(end - start,2)}')
#     return wrapper
#
# @decorator
# @timer
# def say_hello():
#     time.sleep(3)
#     print('Привет')
#
# say_hello = decorator(say_hello)
#
#
# @decorator
# @timer
# def say_goodbye():
#     time.sleep(2)
#     print('Пока')
#
#
# say_hello()
# say_goodbye()

#
# def sqare(x):
#     return x*x
# print(sqare(3))
#
# square = lambda x: x*x
# print(square(5))
#
# numbers = [1,4,7,6]
#
# print(list(map(sqare, numbers)))
# print(sorted(numbers))

list_of_numbers = []
numbers = range(11)
for i in numbers:
    if i%2 == 0:
        list_of_numbers.append(i**3)


print(list_of_numbers)

print([i**3 for i in range(1000) if i%2 == 0])