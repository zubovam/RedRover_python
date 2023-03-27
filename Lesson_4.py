# def calc(a, b=1):
#     return a * b
#
# print(calc(b=5, a=4))

# def person(age, f_name, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} years old'
#
# print(person(25, 'Anna', 'Smith'))
# print(person(f_name='Anna', l_name='Smith', age=20))

# print(sum([5, 6, 7, 4]))
# print(min([5, 6, 7, 4]))
# print(max([5, 6, 7, 4]))

# def pattern(lenght, char2, char1='*'):
#     return (char1 + char2) * lenght + char1
#
# print(pattern(8, '-'))
# print(pattern(8, '-', '#'))
# print(pattern(8, '/', char1='='))

# mult = lambda x, y: x*y
# print(mult(5, 6))

# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and not x % 2, l))
# print(*filtered)
# power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
# print(power)

# l1 = [20, 15, 8, 7, 6]
# power = list(map(lambda x: x**2, l1))
# print(power)

# from functools import reduce
#
# result = reduce(lambda x, y: x - y, l1)
# print(result)

# def say_hello(name):
#     print(f'Hello, {name}')

# def my_decorator(func):
#     def wrapper(arg):
#         print('Я - обертка!')
#         func(arg)
#         print('Звернули')
#     return wrapper
#
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
#
# say_hello('Sam')

# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#     return wrapper
#
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
#
# @milk
# @sugar
# def coffee():
#     print('Coffee')
#     return '12345'
#
# coffee()
# print(coffee)

# import datetime
# print(datetime.date.today())
# print(datetime.date.today().month)
# bdate = 1980
# current_date = datetime.date.today()
# age = current_date.year - bdate
# print(age)
#
# import math as m
# print(m.pi)
# l1 = [20, 15, 8, 7, 6]
# print(m.prod(l1))

# import modul
# print(modul.hello('Sam'))

# from modul import hello, sum
# from modul import *
# print(hello('Sam'))
# print(sum(5, 28))

# print(dir(__builtins__))
# print(f'Globals: {globals()}')
# print(f'Locals: {locals()}')

# def my_func(**keywords):
#   pass


# Lesson 4 Review Review Review Review Review Review Review Review Review Review Review Review

# def fun(*args):
#     print(args)
#
# *a, b, c = [1, 'Hello', 3.5, True, 89]
# fun(a, b, c)

# def return_dict(*args, **kwargs):
#     print(f'Return kwargs: {kwargs}')
#     print(f'Return args: {args}')
#
# return_dict(a=2, b=5, c=9)
# return_dict(1, 5, 8, 'Hello')
# return_dict(1, 5, 8, 'Hello', a=2, b=5, c=9)
# my_dict = {
#     'a': 'A',
#     'b': 'B',
#     'c': 'CCC'
# }
# return_dict(my_dict)

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# for i in range(15):
#     print(fibonacci(i+1), end=' ')
