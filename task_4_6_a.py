from itertools import count


def my_count(num_start, num_finish):
    if num_finish >= num_start:
        for elem in count(num_start):
            if elem <= num_finish:
                yield elem
            else:
                break
    else:
        print("Конечное значение превышает начальное")
        StopIteration


for i in my_count(-4, 0):
    print(i)
