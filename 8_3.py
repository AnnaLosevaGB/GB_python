class TestInt(Exception):
    def __str__(self):
        return 'Это не число!'


my_list = []
while True:
    now_number = input('Введите число. Для остановки введите "stop". ')
    if now_number == 'stop':
        break
    point = False
    my_number = now_number[:]
    if now_number[0] == '-':
        my_number = now_number[1:]
    if my_number.find('.') != -1:
        my_number = my_number.replace('.', '', 1)
        point = True
    try:
        if my_number.isdigit():
            if point:
                my_list.append(float(now_number))
            else:
                my_list.append(int(now_number))
        else:
            raise TestInt
    except TestInt as err:
        print(err)
print(my_list)
