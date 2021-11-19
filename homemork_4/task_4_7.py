def my_fact(n):
    if n > 0:
        res = 1
        for i in range(1, n+1):
            res = res * i
            yield res
    elif n == 0:
        yield 1
    else:
        StopIteration


for elem in my_fact(5):
    print(elem)
