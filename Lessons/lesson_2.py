#
a = 'John'
b = 'Doe'
print(a +' ' + b)

print('Hello, my name is {name} {lastname}'.format(name = a, lastname = b))
print(f'hello, my name is {a} {b}' )
print('I worked \n in "Rebrain"')
c = ('hello my name is haha '
     'hi my name is hoho')
print(c)

d = '''test text 
test test '''
print(d)
print('I worked \\ in "Rebrain"')
print(r'\Users\kimmyblar\PycharmProjects\PythonProject\lesson_1.py')

print(a*3)

print(a[0])

k = a+b
print(k[0])
print(k[-2])

print(k[:2])

print(k[2:])
print(k[: :-1])
print(len(k))
print(k.find('n'))
print(k.replace('o', 'a'))
print(c.split(' '))

e = '5'
if e.isdigit():
    print('Это число')
else :
    print(e.upper())

print(e.count('l'))

a = (1,2,3, 'hello', True, (1,2,3))
print(a[0::2])

print(a.count(2))