# Task 2.1

# try:
#     health = int(input('Enter health level: '))
# except ValueError:
#     print('You entered not a number!')
#
# if health <= 0:
#     print(False)
# else:
#     print(True)

# Task 2.2

# if not int(input('Введите число: ')) % 2:
#     print("Четное")
# else:
#     print("Нечетное")

# Task 2.3

# try:
#     year = int(input('Введите год: '))
# except ValueError:
#     print('Вы ввели не число!')
# if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#     print('Год високосный')
# else:
#     print('Год не високосный')

# Task 2.4

# text = input('Введите текст: ')
# try:
#     num = int(input('Введите количество повторений: '))
# except ValueError:
#     print('Вы ввели не число!')
# for i in range(num):
#     print(text)

# Task 2.5

# import sys
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
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# elif operator == '*':
#     result = num1 * num2
# elif operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# else:
#     result = ''
#     print(f'{operator} не является допустимым оператором')
# if result != '':
#     print(f'{num1} {operator} {num2} = {result}')
