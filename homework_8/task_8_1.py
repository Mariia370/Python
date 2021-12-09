class Data:
    # def __init__(self, data_str):
    #     self.data_str = data_str

    @classmethod
    def data_str_to_int(cls, data_str):
        return [int(i) for i in data_str.split('-')]

    @staticmethod
    def is_correct_data(data_str):
        [day, month, year] = Data.data_str_to_int(data_str)

        if month in [1, 3, 5, 7, 8, 10, 12] and day < 32:
            return True
        elif month in [4, 6, 9, 11] and day < 31:
            return True
        elif month == 2 and (year // 4 == 0 and day < 30 or year // 4 != 0 and day < 29):
            return True
        else:
            return False

print(Data.data_str_to_int('12-09-2021'))
print(Data.is_correct_data('13-10-1990'))
print(Data.is_correct_data('33-10-1990'))
print(Data.is_correct_data('31-04-1990'))
print(Data.is_correct_data('30-02-2000'))
print(Data.is_correct_data('28-02-2000'))
print(Data.is_correct_data('29-02-2001'))

