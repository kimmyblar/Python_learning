import random
# Словари

k = "Victory"
v = 8963000000
a = {"Ivan":840, k:v}
# print(a)
#
# print(a["Victory"])
# # print(a["Tom"])
#
# print(a.get("Tom", 000))
# print(a.keys())
# print(a.values())
# print(a.items())
# print(list(a.keys())[0])
# print(list(a.items())[0][0])

a["Tom"] = 100
a.update({'Ivan': 111})


# Циклы
#
# for i in a.keys():
#     print(i)
# Для каждого элемента в нашей переменной
# b = ((1,2,3), (4,5,6))
#
# for k, v in a.items():
#     print(k, v)
# # Для каждого элемента в нашей переменной
#
# for first, second, third in b:
#     print(first, second, third)

spisok = ['Olga', 'Kira', 'Lena']
for name in spisok:
    a[name] = random.randint(10000, 100000)
for k, v in a.items():
    a[k] = random.randint(10000, 100000)

for k, v in a.items():
    print(k, v)
