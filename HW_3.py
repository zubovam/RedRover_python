# # Task 3.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(str(my_list[2]))
# for i in my_list[2]:
#     print(i)

# # Task 3.2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# s = 0
# for i in list_1:
#     if type(i) == int:
#         s += i
#     elif type(i) == str and 'a' in i:
#         print(i)
# print(f'Сумма всех чисел списка: {s}')

# # Task 3.3
# my_list = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(my_list)
# print(my_tuple, type(my_tuple))

# # Task 3.4
# family_1 = input('Перечислите членов семьи family_1 через запятую:')
# family_2 = input('Перечислите членов семьи family_2 через запятую:')
# f1 = family_1.split(',')
# f2 = family_2.split(',')
# f = []
# if len(f1) > len(f2):
#     f = f1
# elif len(f1) < len(f2):
#     f = f2
# else:
#     print('Equal')
# if f:
#     k = False
#     for i in f:
#         if k:
#             print(', ', end='')
#         print(f'{i.strip()}', end='')
#         k = True

# # Task 3.5
# film = {
#     'title': 'Best movie',
#     'director': 'Petr Petrov',
#     'year': 2024,
#     'budget': 1000000000,
#     'main_actor': 'Vasiliy Pupkin',
#     'slogan': "It's the best movie"
# }
#
# print(film.keys())
# print(film.values())
# print(film)

# # Task 3.6
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# s = 0
# for i in my_dictionary:
#     if type(my_dictionary[i]) == int:
#         s += int(my_dictionary[i])
# print(f'Сумма всех чисел списка: {s}')

# # Task 3.7
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# my_list = list(set(my_list))
# print(my_list)

# # Task 3.8
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set2.symmetric_difference(set1))
# print(set2.issubset(set1))
# print(set1.issubset(set2))
