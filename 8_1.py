class Data:
    def __init__(self, data):
        self.data = Data.convert(data)

    @staticmethod
    def control(year, month, date):
        return (year.isdigit() and month.isdigit() and date.isdigit() and 1000 <= int(year) <= 2022
                and ((int(month) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(date) <= 31) or
                     (int(month) in [4, 6, 9, 11] and 1 <= int(date) <= 30) or
                     (int(month) == 2 and 1 <= int(date) <= 29)))

    @classmethod
    def convert(cls, data):
        date, month, year = data.split('-')
        if Data.control(year, month, date):
            year = int(year)
            month = int(month)
            date = int(date)
            return date, month, year
        else:
            print('Incorrect data')


data_1 = Data('02-03-2020')
print(data_1.data)
data_1 = Data('31-04-2020')
