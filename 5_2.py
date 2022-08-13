file_2 = open('text_2.txt', 'r', encoding='utf-8')
for index, line in enumerate(file_2, 1):
    count = len(list(line.split()))
    print(f'Строка {index}, слов в строке {count}')
file_2.close()
