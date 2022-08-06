def my_sum(num_list):
    res = 0
    for i in num_list:
        if i == 'q':
            break
        else:
            try:
                res += float(i)
            except ValueError:
                pass
    return res


result = 0
test = True
while test:
    print('Введите числа через пробел. Для завершения работы введите "q".')
    num = list(input().split())
    if 'q' in num:
        test = False
    result += my_sum(num)
    print(result)
