def my_division(n_1, n_2):
    try:
        res = n_1 / n_2
    except ZeroDivisionError:
        res = 'Деление на 0!'
    return res


while True:
    try:
        num_1 = float(input('Введите делимое: '))
        num_2 = float(input('Введите делитель: '))
    except ValueError:
        print('Введите корректный тип (числа)!')
    else:
        break
print(my_division(num_1, num_2))
