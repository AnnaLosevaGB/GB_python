def int_func(some_str):
    return some_str.capitalize()


not_some_result = True
while not_some_result:
    new_list = list(input('Введите строку слов из маленьких латинских букв: ').split())
    result = ''
    for i in new_list:
        if i.isalpha() and i.lower() == i:
            result = result + int_func(i) + ' '
            not_some_result = False
    print(result)
