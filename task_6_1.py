#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
#первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#b. написать 3 варианта кода (один у вас уже есть);
#проанализировать 3 варианта и выбрать оптимальный;

#c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
#d. написать общий вывод: какой из трёх вариантов лучше и почему.

#Выбрана задача:
#Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
#как массив, элементы которого — цифры числа.

from collections import OrderedDict
import sys

def show_size(my_obj):
    print(f'type: {my_obj.__class__}, size: {sys.getsizeof(my_obj)}, object: {my_obj}')


class NewNumb:

    def __init__(self, numb):
        self.numb = numb

    def get_numb_10(self):
        my_table = OrderedDict()
        letters = '0123456789ABCDEF'
        for i in range(16):
            my_table[letters[i]] = i

        show_size(my_table)

        num_10 = 0
        for i in range(0, len(self.numb)):
            n = len(self.numb) - i - 1
            #print(f"{my_table.get(self.numb[n])} * (16 ** {i})")
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
show_size(numb_1)
numb_2 = NewNumb(list(input("Введите второе в шестадцатеричной системе счисления: ")))

print("Результат сложения чисел:", numb_1 + numb_2)
print("Результат умножения чисел:", numb_1 * numb_2)
print(sys.version, sys.platform)

# Версия python и ОС:
# 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] win32

#В данной реализации цифры шестнадцатиричной системы счисления хранятся в виде словаря OrderedDict.
#Числа в шестнадцатиричной системе счисления хранятся в виде объектов класса NewNumb

#Размер словаря, в котором хранились пары цифр в десятиричной и шестнадцатиричной системах счисления:
# type: <class 'collections.OrderedDict'>, size: 1472, object: OrderedDict([('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15)])
#Размер объекта класса NewNumb, представляющего собой числа в шестнадцатиричной системе счисления:
#type: <class '__main__.NewNumb'>, size: 48, object: A 2




