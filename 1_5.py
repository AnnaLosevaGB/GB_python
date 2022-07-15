rev = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if rev > costs:
    print('Финансовый результат - прибыль')
    rent = (rev - costs) * 100 / costs
    print(f'Рентабельность - {rent:.1f} %')
    count = int(input('Введите численность сотрудников: '))
    print(f'Прибыль на одного сотрудника - {(rev - costs) / count :.2f} рублей')
elif rev < costs:
    print('Финансовый результат - убыток')
else:
    print('Финансовый результат - нулевой')
