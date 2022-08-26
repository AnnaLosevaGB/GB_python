from itertools import count, cycle
import my_input

start_num = my_input.int_input('Введите начальное значение: ')
finish_num = my_input.int_input('Введите конечное значение: ')
first_list = []
for i in count(start_num):
    if i > finish_num:
        break
    else:
        first_list.append(i)
print(first_list)

print('-' * 100)

input_list = list(input('Введите изначальный список элементов через пробел: ').split())
count_num = my_input.int_input('Введите количество элементов конечного списка: ')
n = 1
second_list = []
for i in cycle(input_list):
    if n > count_num:
        break
    else:
        second_list.append(i)
        n += 1
print(second_list)
