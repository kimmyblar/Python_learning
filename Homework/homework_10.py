import time
#
# 1) Дан список чисел от 10 до 100.
# Верни новый список, где если число делится на 3 — оставляем его как есть, иначе — заменяем на None.
# Реализуй при помощи лямбда выражений и map
# (там где мы писали x*x дальше можно спокойно дописывать различные условия с if и else )

list_of_numbers = list(range(10, 101))
final_list = list(map(lambda x: x if x % 3 == 0 else None, list_of_numbers))
print(final_list)

list_of_numbers = list(range(10, 101))
print([x if x % 3 == 0 else None for x in list_of_numbers ])
#
#
# # 2) Дан список слов и строка с гласными.
# words = ["яблоко", "банан", "апельсин", "слива", "арбуз"]
# vowels = "аеёиоуыэюя"
# result = [word.upper() for word in words if word[0].lower() in vowels]
# print(result)
# При помощи list comprehension оставь только слова,
# начинающиеся с гласной, и переведи их в верхний регистр.

# 3) Напиши декоратор count_calls,
# который считает, сколько раз была вызвана обёрнутая функция.
# Подсказка: тебе нужно объявить словарь counter = {"count": 0}
# до того как мы попадём внутрь wrapperа, и внутри wrapper его увеличивать.
# Почему именно словарь, а не просто счётчик типа int?
# В Python переменные, такие как int, внутри замыканий (функции внутри функции) — нельзя изменять напрямую,
# если они не объявлены как nonlocal. Если есть желание, можешь попробовать через nonlocal,
# тогда тебе надо будет объявить counter как обычный int
# а потом внутри wrapper сделать вот такой хинт nonlocal counter,
# и дальше уже сможешь его спокойно увеличивать) Это не частый кейс, но неплохо знать что и такое бывает)

# def count_calls(func):
#     counter = {'count': 0}
#     def wrapper():
#         counter['count'] += 1
#         func()
#         print(f"Функция была вызвана {counter['count']} раз(а)")
#     return wrapper
#
# @count_calls
# def say_hello():
#     time.sleep(3)
#     print('Привет')
#
# say_hello()
# say_hello()
# say_hello()
