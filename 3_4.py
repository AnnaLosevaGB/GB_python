def my_pow(arg1, agr2):
    res = 1
    for i in range(1, abs(agr2) + 1):
        res *= arg1
    if agr2 < 0:
        res = 1 / res
    return res


def my_pow_2(arg1, arg2):
    return arg1 ** arg2


while True:
    try:
        x = float(input('Введите действительное положительное число: '))
        y = int(input('Введите целое отрицательное число: '))
    except ValueError:
        print('Введите корректный тип данных')
    else:
        if x > 0 and y < 0:
            break
        else:
            print('Проверьте знаки, x - положительное, у - отрицательное!')

print(my_pow(x, y))
