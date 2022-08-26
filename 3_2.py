def one_line(first_name, last_name, birth_year, now_city, email, phone):
    return f'{first_name} {last_name}, {birth_year} года рождения, проживает в {now_city};' \
           f' контактные данные: {email}, {phone}'


name_1 = input('Введите имя: ')
name_2 = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
tel = input('Введите телефон: ')
em = input('Введите email: ')

print(one_line(first_name=name_1, last_name=name_2, email=em, phone=tel, birth_year=year, now_city=city))
