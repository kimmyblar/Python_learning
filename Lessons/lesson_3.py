a = 1, 2, 3
b = [15, 20, 9, 1, 2, 3]
# print(id(a))
# print(id(b))
# a = a+a
# print(id(a))
# print(b)
# print(b.append(4))
# print(b)
# # b = b.append(4)
# print(b)
#
# c = b.count(1)
# print(c)
#
# print(b.sort())
# print(b.sort())
#
# b.extend(b)
# print(b)
#
# b.reverse()
# print(b)
# print(id(b))
# print(b)
#
# print(a.__sizeof__())
# print(b.__sizeof__())
# a = [1,2,3]
# b = sum(a.copy()[:])
# # a = 'hello'
# print(sum(a))
# print(b)
# # b.append(4)
# print(a)
# print(b)

c = [1, 1, 5, 7, 20, 7]
print(list(set(c)))

d = {1, 2, 3, 3, 7, 'hello', 60, 'hello', 2, 'a'}
print(d)

a = 10
if a in d:
    print("a есть в нашем списке")

с = {1, 5, 7, 10, 'a'}
print(d.intersection(c))

e = frozenset({1,5})
