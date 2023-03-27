# import sys
# compare = 3 == 4
# print(compare)

# x = 3
# print(x > 3 and not x < 8)
# print(x > 3 and not x > 8)

# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More than five')
# else:
#     print('Less than five')

# age = int(input('Please, enter your age: '))
# if age >= 18:
#     print('Welcome')
# else:
#     print('Go home, baby!')

# try:
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
# except ValueError:
#     print('Вы ввели не число!')
#     sys.exit()
# operator = input('Operator: ')
# if operator == '/':
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# massage = 'Hello'
# i = 1
# while i < 6:
#     if i == 3:
#         i += 1
#         continue
#     print(f'{massage} {i}')
#     i += 1

# for i in range(6):
#     print(i)
#
# for i in 'Hello':
#     print(i, end = ' ')
#
# def num(a, b):
#     return int(a * b)
#
# for i in range(2, num(3, 6), 3):
#     print(i)

# Lesson 2 Review

# s = 'Hello world'
# print(s.replace(' ', '_'))
# print(s.count('l'))

# w= 'Денисов Денис Денисович'
# print(w.split())
# w1 = '1, 2, 3, 4, 5'
# # print(w1.split(',', maxsplit=3))
# w2 = w1.split(',', maxsplit=3)
# print('?'.join(w1))

# w3  = '     123hello123      '
# print(w3)
# print(w3.strip().strip('123'))

# w4 = 'hello world'
# print(w4.find('e'))
# print(w4.index('o'))

# w5 = 'Name woRld tiTlE'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = '1234'
# w88 = '1234asd'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())
# print(w88.islower())

# w6 = 'QWERTy'
# w7 = 'QWERTY'
# w8 = '1234'
# w88 = '1234ASD'
# print(w6.isupper())
# print(w7.isupper())
# print(w8.isupper())
# print(w88.isupper())

# w6 = '01234'
# w7 = '0,1'
# w8 = '1234E'
# w88 = '1234ASD'
# print(w6.isdigit())
# print(w7.isdigit())
# print(w8.isdigit())
# print(w88.isdigit())

# w6 = '01234'
# w7 = 'QWErty'
# w8 = '1234E'
# w88 = '1234asd'
# print(w6.isalpha())
# print(w7.isalpha())
# print(w8.isalpha())
# print(w88.isalpha())

# if 10 < 20:
#     pass
# print(6)

# x, y = 55, 60
# s = x if x > y else y
# print(s)

# value = 6
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print('Такой цифры нет')

