# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rm

numbers = [rm.randint(0, 100) for _ in range(0, 20)]
print(numbers)
index_min = 0
max_numb = numbers[0]
index_max = 0
min_numb = numbers[0]
i=1

while i < len(numbers):
    if numbers[i] > max_numb:
        max_numb = numbers[i]
        index_max = i
    elif numbers[i] < min_numb:
        min_numb = numbers[i]
        index_min = i
    i += 1
numbers[index_min] = max_numb
numbers[index_max] = min_numb
print(numbers)
