from collections import OrderedDict


class NewNumb:

    def __init__(self, numb):
        self.numb = numb

    def get_numb_10(self):
        my_table = OrderedDict()
        letters = '0123456789ABCDEF'
        for i in range(16):
            my_table[letters[i]] = i

        num_10 = 0
        for i in range(0, len(self.numb)):
            n = len(self.numb) - i - 1
            print(f"{my_table.get(self.numb[n])} * (16 ** {i})")
            num_10 += my_table.get(self.numb[n]) * (16 ** i)
            print(num_10)

        return num_10

    @staticmethod
    def get_numb_16(num_10):
        my_table = OrderedDict()
        letters = '0123456789ABCDEF'
        for i in range(16):
            my_table[i] = letters[i]
        #print(my_table)
        num_16 = []

        while num_10 > 15:
            num_16.append(my_table.get(num_10 % 16))
            num_10 = num_10 // 16
        num_16.append(my_table.get(num_10))

        return NewNumb(num_16[::-1])

    def __add__(self, other):

        return NewNumb.get_numb_16((self.get_numb_10() + other.get_numb_10()))

    def __mul__(self, other):
        return NewNumb.get_numb_16((self.get_numb_10() * other.get_numb_10()))

    def __str__(self):
        return " ".join(self.numb)

numb_1 = NewNumb(list(input("Введите первое число в шестадцатеричной системе счисления: ")))

numb_2 = NewNumb(list(input("Введите второе в шестадцатеричной системе счисления: ")))

print("Результат сложения чисел:", numb_1 + numb_2)
print("Результат умножения чисел:", numb_1 * numb_2)
