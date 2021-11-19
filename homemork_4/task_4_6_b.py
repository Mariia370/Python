from itertools import cycle


def my_cycle(my_list, num_of_iter):
    curr_num_of_iter = 0
    if num_of_iter > 0:
        for elem in cycle(my_list):
            if curr_num_of_iter // 3 == num_of_iter:
                break
            else:
                curr_num_of_iter += 1
                yield elem

    else:
        StopIteration


for i in my_cycle([1, 2, 3], 4):
    print(i)
