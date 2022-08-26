a = float(input('Введите a: '))
b = float(input('Введите b: '))
day = 1
while a < b:
    print(f'{day}-й день: {a:.2f} км')
    a = a * 1.1
    day += 1
print(f'{day}-й день: {a:.2f} км')
print(f'Ответ: на {day} день')
