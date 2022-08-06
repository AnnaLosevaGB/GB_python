def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


while True:
    try:
        a, b, c = map(float, input('Введите три числа через пробел: ').split())
    except ValueError:
        print('Введите корректный тип данных! (число)')
    else:
        break
print(my_func(a, b, c))
