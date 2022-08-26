word_list = list(input('Введите строку: ').split())
for i, value in enumerate(word_list, 1):
    if len(value) > 10:
        value = value[:10]
    print(f'{i}. {value}')
