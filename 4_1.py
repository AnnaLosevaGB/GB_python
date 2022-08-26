from sys import argv
import my_input

try:
    name, production, rate, premium = argv
except ValueError:
    print('Неоходимо ввести три аргумента! (выработка, ставка, премия)')
else:
    production = my_input.float_test(production)
    rate = my_input.float_test(rate)
    premium = my_input.float_test(premium)
    if production == 'Error!' or rate == 'Error!' or premium == 'Error!':
        print('Некорректный тип данных, необходимо ввести числа')
    else:
        print(production * rate + premium)
