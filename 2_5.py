rating_list = [10, 7, 5, 1]
new_number = int(input('Введите новый элемент: '))
index = len(rating_list)
for i in range(len(rating_list)):
    if rating_list[i] < new_number:
        index = i
        break
rating_list.insert(index, new_number)
print(rating_list)
