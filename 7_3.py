class Cell:
    def __init__(self, count):
        while True:
            try:
                self.count = int(count)
                break
            except ValueError:
                print('Количество клеток должно быть целым числом!')
                count = input('Введите количество клеток: ')

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            return Cell(self.count - other.count)
        else:
            print('Количество ячеек первой клетки меньше, чем второй')

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, row):
        if isinstance(row, int):
            i = 0
            end_string = ''
            for j in range(row, self.count, row):
                end_string = end_string + '*' * row + '\n'
                i += row
            end_string = end_string + '*' * (self.count - i)
            return end_string
        else:
            print('Количество ячеек в ряду должно быть целым числом')

    def __str__(self):
        return '*' * self.count


cell_1 = Cell(16)
print(cell_1.make_order(5))
cell_2 = Cell(4)
cell_3 = cell_1 + cell_2
print(cell_3.count)
cell_4 = cell_1 - cell_2
print(cell_4.count)
print(cell_4)
cell_5 = cell_2 - cell_1
cell_6 = cell_1 * cell_2
print(cell_6.count)
cell_7 = cell_1 / cell_2
print(cell_7.count)
print(cell_6.make_order(10))
