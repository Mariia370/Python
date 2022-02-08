# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random


def merge_arr(arr_1, arr_2):
    print(arr_1)
    print(arr_2)
    arr_3 = []
    while len(arr_1) > 0 and len(arr_2) > 0:
        if arr_1[0] < arr_2[0]:
            arr_3.append(arr_1.pop(0))
        else:
            arr_3.append(arr_2.pop(0))
        if len(arr_1) == 0 and len(arr_2) > 0:
            arr_3.extend(arr_2)
        if len(arr_2) == 0 and len(arr_1) > 0:
            arr_3.extend(arr_1)
    return arr_3


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    n = len(arr) // 2
    return merge_arr(merge_sort(arr[:n]), merge_sort(arr[n:]))


new_arr = [random.randint(0, 49) for _ in range(15)]
print(new_arr)
print(merge_sort(new_arr))
