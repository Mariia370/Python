# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

def prime_numbers(n):

    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result

# n=20
# 1000 loops, best of 5: 4.67 usec per loop
# n=50
#1000 loops, best of 5: 11.1 usec per loop
# n=100
# 1000 loops, best of 5: 22.6 usec per loop
