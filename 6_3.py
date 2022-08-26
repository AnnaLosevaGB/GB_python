class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}'


pos_1 = Position('Alfred', 'Molina', 'accountant', 20000, 7000)
pos_2 = Position('James', 'Franko', 'secretary', 16000, 3000)

print(pos_1.get_full_name())
print(pos_1.get_total_income())
print(pos_2.get_full_name())
print(pos_2.get_total_income())
