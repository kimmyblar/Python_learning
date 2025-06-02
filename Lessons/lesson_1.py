print("Hello world")
a = 5
print(type(a))
b = a ** 5
a = 5
b = 3
print(type(round(a / b, 2)))
print(a // b)
print(a % b)
print(type(1.67))
print(type(True))
c = True
c = 0
c = None
c = 3
if c == 1:
    print("1")
elif c > 2 and c <= 4:
    print("2 or 3")
else:
    print("not 1 or 2 or 3")

    # Если or (Одно из условий должно быть выполнено, значит True)
    # True or True = True
    # False or True = True
    # True or False = True
    # False or False = False

    # Если and (Если оба условия выполнены, значит True)
    # True and True = True
    # False and True = False
    # True and False = False
    # False and False = False

    number = int(input("Введите целое число: "))

    if number % 2 == 0:

        print("Число чётное.")
    else:
        print(f"Число нечётное.")