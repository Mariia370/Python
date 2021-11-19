
my_list = [int(elem) for elem in (input("Введите список целых чисел ").split())]
print([elem for elem in my_list if my_list.count(elem) == 1])
