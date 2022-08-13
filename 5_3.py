with open('text_3.txt', 'r', encoding='utf-8') as file_3:
    count_people = 0
    all_sum = 0
    sad_people = []
    for line in file_3:
        now_list = list(line.split())
        now_list[1] = float(now_list[1])
        count_people += 1
        all_sum += now_list[1]
        if now_list[1] < 20000:
            sad_people.append(now_list[0])
    print('Доход менее 20000 рублей имеют следующие сотрудники:', *sad_people, sep='\n')
    print(f'\nСредняя величина дохода сотрудников: {all_sum / count_people:.2f}')
