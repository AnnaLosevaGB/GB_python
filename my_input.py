def int_input(name='Введите целое число: '):
    """Проверка и преобразование входных данных в целое число (добьет, пока пользователь не введет правильно)"""
    while True:
        try:
            x = int(input(name))
        except ValueError:
            print('Введите корректный тип данных! (число)')
        else:
            return x


def int_pos_input(name='Введите целое положительное число: '):
    """Проверка и преобразование входных данных в целое число (ПОЛОЖИТЕЛЬНОЕ)
    (добьет, пока пользователь не введет правильно)"""
    while True:
        try:
            x = int(input(name))
        except ValueError:
            print('Введите корректный тип данных! (число)')
        else:
            if x > 0:
                return x
            else:
                print('Введите положительное число!')


def float_input(name='Введите действительное число: '):
    """Проверка и преобразование входных данных в действительное число
    (добьет, пока пользователь не введет правильно)"""
    while True:
        try:
            x = float(input(name))
        except ValueError:
            print('Введите корректный тип данных! (число)')
        else:
            return x


def int_test(x):
    """Проверка и преобразование входных данных в целое число (одноразовая штука)"""
    while True:
        try:
            x = int(x)
        except ValueError:
            return 'Error!'
        else:
            return x


def float_test(x):
    """Проверка и преобразование входных данных в действительное число (одноразовая штука)"""
    while True:
        try:
            x = float(x)
        except ValueError:
            return 'Error!'
        else:
            return x

