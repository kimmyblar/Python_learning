import random

# 1)Создай словарь, где ключи — имена студентов, а значения — их оценки (числа).
# Выведи имена студентов, у которых оценка выше 75.
Students = {'Ivan':100, 'Maria':90, 'Stepan':55, 'Sergei':74}
for name, score in Students.items():
    if score >=75:
        print(name)

# 2) Дан список кортежей, каждый из которых содержит название товара и его цену.
# Выведи все товары с ценой выше 100.
Goods = [('apple', 89), ('carrot', 54), ('milk', 105), ('butter', 215)]
for name, price in Goods:
    if price > 100:
        print(name)

# 3) Дан словарь с названиями городов и их населением.
# Посчитай общее население всех городов.
Cities = {'Moscow':0, 'Da nang':0, 'Seoul':0, 'Minsk':0, 'Bangkok':0 }
for city in Cities:
    Cities[city] = random.randint(10000,5000000)
population = 0
for v in Cities.values():
   # print(v)
    population = v + population
#    Читала, что можно +=, но не совсем привыкла к такому

print(f'Общее население всех городов {population}')
