# user = input('Please, enter your name: ')
# print('Hello, ' + user)
# print(f'Hello, {user}')
# print('Hello, {}'.format(user))

# number = int(input('Please, enter any number: '))
# print(number**2)

def sum_arrays(arrays, shift):
    res = []
    for i in range(len(arrays[0])+shift * (len(arrays) - 1)):
        res.append(0)
        for j in range(len(arrays)):
            if len(arrays[0]) + j * shift > i >= j * shift:
                res[i] += arrays[j][i-j*shift]
    return res


print(sum_arrays([[1, 2, 3, 4, 5, 6], [7, 7, 7, -7, 7, 7], [1, 1, 1, 1, 1, 1]], 3))
