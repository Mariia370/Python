# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


def bubble_sort(arr):
    print(arr)
    count = 0  # число проходов по циклу
    k = len(arr) - 2
    while k > 0:

        for j in range(k):
            count += 1
            if arr[j + 1] < arr[j + 2]:
                arr[j + 2], arr[j + 1] = arr[j + 1], arr[j + 2]

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        k -= 2

    print(count)



#классическая реализация пузырька - число проходов по циклу получается больше, чем в 2 раза
# def bubble_sort(arr):
#     print(arr)
#     count = 0
#     for i in range(1, len(arr)):
#         for j in range(len(arr) - i):
#             count += 1
#
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
#     print(count)
#     print(arr)


new_arr = [random.randint(-100, 99) for _ in range(15)]
bubble_sort(new_arr)
print(new_arr)
