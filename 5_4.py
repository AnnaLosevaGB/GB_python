my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('text_4.txt', 'r', encoding='utf-8') as file_4_1:
    with open('text_4_out.txt', 'w', encoding='utf-8') as file_4_2:
        for line in file_4_1:
            now_list = list(line.split())
            now_list[0] = my_dict[now_list[0]]
            now_line = ''
            for i in now_list:
                now_line = now_line + ' ' + i
            now_line = now_line[1:] + '\n'
            file_4_2.write(now_line)
