def int_func(some_str):
    return some_str.capitalize()


while True:
    new_srt = input('Введите строку из маленьких латинских букв: ')
    if new_srt.isalpha() and new_srt.lower() == new_srt:
        print(int_func(new_srt))
        break
