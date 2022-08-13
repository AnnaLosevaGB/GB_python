with open('text_6.txt', 'r', encoding='utf-8') as file_6:
    my_dict = {}
    for line in file_6:
        now_list = list(line.split())
        now_sum = 0
        for i in range(1, len(now_list)):
            if len(now_list[i]) == 1:
                now_list[i] = 0
            else:
                index = now_list[i].index('(')
                now_list[i] = now_list[i][:index]
            now_sum += int(now_list[i])
        my_dict[now_list[0]] = now_sum
print(my_dict)
