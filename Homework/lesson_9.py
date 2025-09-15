
from Modules.helper import divide_num

divide_num(1,2)



#
# # args* это позиционные аргументы (какая позиция, такой и порядковый аргумент)
#
# divide_num(1, 2)
# a = [1, 2]
# divide_num(*a)
#
# # kwargs** это именованные аргументы (какой ключ, такой и аргумент функции)
#
# divide_num(num1=1, num2=2)
# divide_num(num2=2, num1=1)
# b = {'num1':5, 'num2':6}
# divide_num(**b)
#
# divide_num(5)
# divide_num(1, 2, twice=True)