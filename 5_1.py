file_1 = open('text_1.txt', 'w', encoding='utf-8')
now_string = None
print('Введите данные построчно. Прекращение - пустая строка.')
while now_string != '':
    now_string = input()
    file_1.write(now_string + '\n')
file_1.close()
