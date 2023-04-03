# user = input('Please, enter your name: ')
# print('Hello, ' + user)
# print(f'Hello, {user}')
# print('Hello, {}'.format(user))
import random

# number = int(input('Please, enter any number: '))
# print(number**2)

# def sum_pairs(ints, s):
#     index = len(ints)
#     answer = []
#     set_ints = set(ints)
#     for ind_i in set_ints:
#         i = ints.index(ind_i)
#         if i >= index or i == len(ints) - 1:
#             continue
#         if ind_i * 2 == s and ind_i in ints[i+1:]:
#             j = ints.index(ind_i, i + 1)
#             if j < index:
#                 answer = [ind_i, ind_i]
#                 index = j
#                 continue
#         for ind_j in set_ints:
#             if ind_j == ind_i:
#                 continue
#             if ind_j not in ints[i+1:]:
#                 continue
#             j = ints.index(ind_j)
#             if j <= i:
#                 continue
#             if ind_i + ind_j == s and j < index:
#                 answer = [ind_i, ind_j]
#                 index = j
#     return answer if answer else None

# lst = []
# for i in range(10):
#     lst.append([random.randint(1, 5), i])
# print(lst)
#
# print((lst[:][:]))


def sum_pairs(ints, s):
    index = len(ints)
    answer = []
    list_i = [ints[0]]
    flag = False
    for j in range(1, len(ints)):
        if flag:
            break
        if ints[j] in list_i:
            if ints[j] * 2 == s:
                answer = [ints[j], ints[j]]
                break
            else:
                continue
        else:
            list_i.append(ints[j])
        for value_i in list_i[:-1]:
            if value_i + ints[j] == s:
                answer = [value_i, ints[j]]
                flag = True
                break
    return answer if answer else None

l9 = [1] * 1000000
l9[len(l9) // 2 - 1] = 6
l9[len(l9) // 2] = 7
l9[len(l9) - 2] = 8
l9[len(l9) - 1] = -3
l9[0] = 13
l9[1] = 3
print(l9)
print(sum_pairs(l9, 16))

l5 = [10, 5, 2, 3, 7, 5]
print(sum_pairs(l5, 10))

# l5 = [10, 5, 2, 3, 5, 10, 7, 5]
# print(sum_pairs(l5, 10))
