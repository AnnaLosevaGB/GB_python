number = int(input('Введите число: '))
max_num = 0
while number > 0:
    new_num = number % 10
    number = number // 10
    if new_num > max_num:
        max_num = new_num
print(max_num)
