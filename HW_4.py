# # Task 4.1
# def square(a):
#     return a * 4, a * a, a * 2 ** 0.5
#
#
# b = square(5)
# print(b)
# print(type(b))

# # Task 4.2
# def func_out(**data):
#     for key, value in data.items():
#         print(f'{key}: {value}')
#
#
# func_out(name='John', last_name='Smith', age=35, position='web developer')

# # Task 4.3
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x >= 0, my_list)))

# # Task 4.4
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# print(reduce(lambda x, y: x * y, my_list))

# Task 4.5
# import time
#
# def perf_f(func):
#     def wrapper(arg):
#         time_start = time.perf_counter()
#         a = func(arg)
#         print(f'Время выполнения: {time.perf_counter() - time_start} сек')
#         return a
#     return wrapper
#
# @perf_f
# def func_sleep(n):
#     time.sleep(n)
#     return f'Задержка: {n} сек.'
#
# print(func_sleep(1.5))

# Task 4.6
# import my_calc as mc
# a = 5
# b = 2
# print(mc.addition(a, b))
# print(mc.subtraction(a, b))
# print(mc.multiplication(a, b))
# print(mc.division(a, b))
