#4. Определить, какое число в массиве встречается чаще всего.

import random as rm

numbers = [rm.randint(0, 10) for _ in range(0, 30)]
print(numbers)
frequencies = {numbers[0]: 1, }
for i in range(1, 30):

    if frequencies.get(numbers[i]) is not None:
        frequencies[numbers[i]] += 1
    else:
        frequencies[numbers[i]] = 1

print(frequencies)
key_of_max_val = numbers[0]
max_val = frequencies[key_of_max_val]
for (k, v) in frequencies.items():
    if v > max_val:
        max_fr = v
        key_of_max_val = k


print(f"Число {max_val} встречается в массиве наибольшее количество раз: {max_val} раз(а)")





