#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random as rm

numbers = [rm.randint(-20, 20) for _ in range(1, 30)]
print(numbers)
max_negat_number = -21
for i in numbers:
    if i > max_negat_number and i < 0:
        max_negat_number = i

print(max_negat_number)

