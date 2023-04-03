import random

a, b = 1, 100
A = random.randint(a, b)

while True:
    s = input(f'Введите целое число от {a} до {b}: ')
    if s.strip().isdigit():
        x = int(s.strip())
        if x == A:
            print('Вы угадали, поздравляем!')
            break
        elif x > A:
            print('Слишком много, попробуйте еще раз')
        else:
            print('Слишком мало, попробуйте еще раз')
    else:
        print('Вы ввели не число')
    ans = input('Для продолжения нажмите ENTER. Для выхода из программы введите "N": ')
    if ans in 'NnТт' and ans != '':
        break


