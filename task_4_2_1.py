# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

def prime_numbers(n):
    numbers = set()
    result = []
    for i in range(2, n // 2):
        for j in range(2, n // 2):
            numbers.add(i*j)
    for i in range(2, n):
        if not i in numbers:
            result.append(i)

    return result
#print(prime_numbers(20))

# n=20
# 1000 loops, best of 5: 9.16 usec per loop
# n=50
#1000 loops, best of 5: 54.2 usec per loop
# n=100
# 1000 loops, best of 5: 237 usec per loop
