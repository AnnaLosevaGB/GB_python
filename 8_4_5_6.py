class TestNumber(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'{self.text} должны быть числом!'


class Warehouse:
    def __init__(self, length, width, height):
        if (isinstance(length, int) or isinstance(length, float)) and (
                isinstance(width, int) or isinstance(width, float)) and (
                isinstance(height, int) or isinstance(height, float)):
            self.length = length
            self.width = width
            self.height = height
            self.volume = self.length * self.width * self.height
            self.stock = []
        else:
            raise TestNumber('Длина, ширина и высота хранилища')

    def put_in(self, equip):
        eq_volume = equip.dict['length'] * equip.dict['width'] * equip.dict['height']
        if eq_volume <= self.volume:
            eq_type = ''
            if type(equip) is Printer:
                eq_type = 'Printer'
            elif type(equip) is Copier:
                eq_type = 'Copier'
            elif type(equip) is Scanner:
                eq_type = 'Scanner'
            else:
                eq_type = 'Err'
            self.stock.append((eq_type, equip.dict))
            self.volume -= eq_volume
        else:
            print('The warehouse is full!')

    def put_out(self, equip):
        for i in self.stock:
            if i[0] == equip:
                print('Equipment transferred to the customer')
                eq_volume = i[1]['length'] * i[1]['width'] * i[1]['height']
                self.stock.remove(i)
                self.volume += eq_volume
                break
            else:
                print('This equipment is not in the warehouse')


class OfficeEquipment:
    def __init__(self, name, length, width, height):
        if (isinstance(length, int) or isinstance(length, float)) and (
                isinstance(width, int) or isinstance(width, float)) and (
                isinstance(height, int) or isinstance(height, float)):
            self.dict = {
                'name': name,
                'length': length,
                'width': width,
                'height': height
            }
        else:
            raise TestNumber('Длина, ширина и высота принтера')


class Printer(OfficeEquipment):
    def __init__(self, name, length, width, height, color=False, paper_size='A4'):
        super().__init__(name, length, width, height)
        self.dict['color'] = color
        self.dict['paper_size'] = paper_size


class Scanner(OfficeEquipment):
    def __init__(self, name, length, width, height, wifi=False, email=True):
        super().__init__(name, length, width, height)
        self.dict['wifi'] = wifi
        self.dict['email'] = email


class Copier(OfficeEquipment):
    def __init__(self, name, length, width, height, paper_size='A4', scanner=True):
        super().__init__(name, length, width, height)
        self.dict['paper_size'] = paper_size
        self.dict['scanner'] = scanner


try:
    equip_1 = Printer('1', 1, 2, 1)
    equip_2 = Scanner('2', 1, 1, 4)
    equip_3 = Copier('3', 2, 3, 1)
    warehouse_1 = Warehouse(5, 8, 3)
except TestNumber as err:
    print(err)
else:
    print(warehouse_1.volume)
    warehouse_1.put_in(equip_1)
    warehouse_1.put_in(equip_2)
    warehouse_1.put_in(equip_3)
    print(*warehouse_1.stock, sep='\n')
    print(warehouse_1.volume)
    warehouse_1.put_out('Printer')
    print(*warehouse_1.stock, sep='\n')
    print(warehouse_1.volume)
