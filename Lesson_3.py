# my_list = [1, 'hello', 2.0, True, None, 1, 1]
#
# sentence = 'Python is awesome!'
#
# # print(sentence.split(' '))
# # print(sentence.split(' ', maxsplit=1))
# # print(my_list[-1])
#
# print(my_list)
# my_list[0] = 25
# print(my_list)

# my_list.append(sentence)
# print(my_list)
# print(len(my_list))

# my_list.insert(-2, sentence)
# print(my_list)

# print(my_list.count(1))
# print(my_list.index(None))

# my_list1 = [1, 2, 3, 4, 5]
# print(sum(my_list1))
# print(min(my_list1))
# print(max(my_list1))

# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
# print(my_list1[-1])
# print(my_list1[-1][1])

# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [11, 22]]]
# print(my_list1[-1])
# print(my_list1[-1][1])
# print(my_list1[-1][-1][0])
# my_list1.reverse()
# print(my_list1)

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num**2)
#
# print(numbers)
# print([x*x for x in numbers if x % 2])
# print([x for x in numbers if x % 2])

# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))
#
# my_tuple1 = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple1)
# print(type(my_tuple))
#
# name = 'Mark',
# print(name)
# print(type(name))
#
# name = ('Mark',)
# print(name)
# print(type(name))

# my_tuple2 = ('apple', 'banana', 'cat')
# a, b, c = my_tuple2
# print(a)
# print(b)
# print(c)
#
# my_tuple2[0] = 'ananas'
# print(my_tuple2)
#
# my_list2 = list(my_tuple2)
# my_list2[0] = 'ananas'
# print(my_list2)

# my_tuple1 = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple1.index('name'))
# print(my_tuple1.count('name'))

# my_tuple = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tuple if isinstance(item, int)])
# print(result)
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of my_tuple is: {len(my_tuple)}')
# print(f'Length of result is: {len(result)}')

# my_tuple = (1, 'name', None, 'name', 'name', 25)
# for (index, item) in enumerate(my_tuple):
#     print(index, item)

# a = 'banan'
# fruits = ('apple', ['ananas', 'mango'], 'melon', a)
# print(fruits)
# fruits[1][0] = 'cherry'
# print(fruits)
# a = 'orange'
# print(fruits)

# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')

# def sum_it(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))
# print(sum_it(4, 5, 10, 6, 20, 4, 5, 10, 6, 20))

# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append((item * item))
#     return l
#
# print(func(2, 5, 6, 8, 10))

# my_dict = {
#     'name': 'Alex',
#     'last_name': 'Zubov',
#     'age': 39,
#     'de[atament': 'IT'
# }
#
# print(my_dict)
# print(type(my_dict))
# print(id(my_dict))
# print(my_dict['last_name'])
# print(len(my_dict))
# my_dict['salary'] = 5000
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('salary', 'Not Found'))

# keys = ['name', 'salary', 'department']
# values = ['Alex', 50000, 'IT']
# employee = dict(zip(keys, values))
# print(employee)
#
# employee1 = dict(name='John', position='developer', salary=20000, department='IT', city='NY')
# print(employee1)

# my_list = [2, 1, 8, 2, 1, 5, 8, 9]
# print(set(my_list))

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
#
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))
# print(set1)
# print(id(set1))
# set1.remove(1)
# print(id(set1))
# set1.add(8)
# print(id(set1))
# print(set1)

# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# fs.add(4)
