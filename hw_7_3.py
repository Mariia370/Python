# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

import random


def search_median(arr):
    if len(arr) % 2 == 1:
        n = len(arr) // 2
    else:
        n = len(arr) // 2 - 1

    for i in range(len(arr)):
        count_less = 0
        count_more = 0
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                count_less += 1

            elif arr[i] < arr[j]:
                count_more += 1

        if (count_less == n) and (count_more == n):
            return arr[i]


new_arr = [random.randint(0, 49) for _ in range(15)]
print(new_arr)
print("Найдена медиана:", search_median(new_arr))

new_arr.sort()
print(f"Проверка. Медиана в массиве {new_arr}-это {new_arr[7]}")
