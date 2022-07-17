list_of_goods = []
while True:
    print('-' * 130)
    operation = input('Введите запрос: \n'
                      'Для ввода нового товара - new, '
                      'для просмотра списка товаров - goods, '
                      'для просмотра аналитики - analysis, '
                      'для выхода - exit: ')
    if operation == 'new':
        new_good = {
            'наименование': input('Введите наименование товара: '),
            'цена': float(input('Введите цену товара: ')),
            'количество': float(input('Введите количество товара: ')),
            'ед': input('Введите единицу измерения товара: ')
        }
        number = len(list_of_goods) + 1
        list_of_goods.append((number, new_good))
    elif operation == 'goods':
        for i in list_of_goods:
            print(i)
    elif operation == 'analysis':
        name = []
        for i in list_of_goods:
            name.append(i[1]['наименование'])
        price = []
        for i in list_of_goods:
            price.append(i[1]['цена'])
        quantity = []
        for i in list_of_goods:
            quantity.append(i[1]['количество'])
        unit = []
        for i in list_of_goods:
            unit.append(i[1]['ед'])
        analysis = {
            'наименование': set(name),
            'цена': set(price),
            'количество': set(quantity),
            'ед': set(unit)
        }
        print(analysis)
    elif operation == 'exit':
        break
    else:
        print('Введен не верный запрос')
