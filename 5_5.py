with open('text_5.txt', 'w+', encoding='utf-8') as file_5:
    new_list = [n for n in range(1, 200, 7)]
    new_line = ''
    for i in new_list:
        new_line = new_line + ' ' + str(i)
    new_line = new_line[1:] + '\n'
    file_5.write(new_line)
    file_5.seek(0)
    read_list = list(map(int, file_5.read().split()))
    my_sum = 0
    for i in read_list:
        my_sum += i
    print(my_sum)
