class Zero(Exception):
    def __str__(self):
        return 'Деление на 0!'


try:
    num_1 = float(input('Введите делимое: '))
    num_2 = float(input('Введите делитель: '))
    if num_2 == 0:
        raise Zero
    else:
        print(num_1 / num_2)
except ValueError:
    print('Введен некорректный тип данных!')
except Zero as err:
    print(err)
